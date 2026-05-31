from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any

from mysql.connector import Error

from models.db import get_connection


@dataclass(frozen=True)
class EnergyAssumptions:
    electricity_price_eur_kwh: float = 0.22
    co2_kg_kwh: float = 0.231
    target_monthly_kwh: float = 120.0
    days_per_month: int = 30
    snapshot_min_interval_seconds: int = 60


class EnergyManager:
    """Energy estimator and history writer for the local smart-supermarket demo."""

    POWER_BY_KIND_W = {
        "dht11": 0.01,
        "dht": 0.01,
        "temperature": 0.01,
        "humidity": 0.01,
        "mq": 0.85,
        "mq135": 0.90,
        "air_quality": 0.90,
        "hc_sr04": 0.075,
        "ultrasonic": 0.075,
        "distance": 0.075,
        "lcd16x2": 0.35,
        "display": 0.35,
        "generic": 0.25,
    }

    REAL_SENSOR_KINDS = {"dht11", "mq135", "hc_sr04", "lcd16x2"}

    FALLBACK_DEVICES = [
        {"device_code": "dht11_01", "device_name": "DHT11 ambiente", "sensor_code": "dht11", "location_name": "Pasillo central"},
        {"device_code": "mq135_01", "device_name": "MQ135 calidad de aire", "sensor_code": "mq135", "location_name": "Entrada"},
        {"device_code": "hc_sr04_01", "device_name": "HC-SR04 acceso", "sensor_code": "hc_sr04", "location_name": "Puerta"},
        {"device_code": "lcd16x2_01", "device_name": "LCD 16x2 informacion", "sensor_code": "lcd16x2", "location_name": "Mostrador"},
    ]

    def __init__(self, assumptions: EnergyAssumptions | None = None):
        self.assumptions = assumptions or EnergyAssumptions()

    CREATE_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS energy_snapshots (
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
            created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
            total_watts DECIMAL(10,4) NOT NULL DEFAULT 0,
            daily_kwh DECIMAL(10,4) NOT NULL DEFAULT 0,
            monthly_kwh DECIMAL(10,4) NOT NULL DEFAULT 0,
            monthly_cost_eur DECIMAL(10,4) NOT NULL DEFAULT 0,
            monthly_co2_kg DECIMAL(10,4) NOT NULL DEFAULT 0,
            efficiency_percent DECIMAL(5,2) NOT NULL DEFAULT 0,
            highest_consumer VARCHAR(160) DEFAULT NULL,
            sustainability_status VARCHAR(60) DEFAULT NULL,
            source VARCHAR(40) NOT NULL DEFAULT 'estimated',
            breakdown_json JSON DEFAULT NULL,
            PRIMARY KEY (id),
            KEY idx_energy_snapshots_created_at (created_at)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
    """

    def resumen(self, persist: bool = True) -> dict[str, Any]:
        devices = self._read_devices()
        if not devices:
            devices = [dict(item, source="estimado") for item in self.FALLBACK_DEVICES]

        rows = [self._estimate_device(row) for row in devices]
        rows = self._canonical_real_rows(rows)

        total_w = round(sum(row["power_w"] for row in rows), 3)
        daily_wh = round(total_w * 24, 2)
        monthly_kwh = round(daily_wh * self.assumptions.days_per_month / 1000, 3)
        cost_month = round(monthly_kwh * self.assumptions.electricity_price_eur_kwh, 2)
        co2_month = round(monthly_kwh * self.assumptions.co2_kg_kwh, 2)
        target = self.assumptions.target_monthly_kwh
        efficiency = max(0, min(100, round(100 - (monthly_kwh / target * 100), 1)))
        top = max(rows, key=lambda item: item["power_w"], default=None)

        result = {
            "devices": rows,
            "totals": {
                "instant_w": total_w,
                "daily_wh": daily_wh,
                "daily_kwh": round(daily_wh / 1000, 3),
                "monthly_kwh": monthly_kwh,
                "cost_month_eur": cost_month,
                "co2_month_kg": co2_month,
                "efficiency_pct": efficiency,
                "device_count": len(rows),
                "top_device": top,
                "state": self._state(efficiency),
            },
            "recommendations": self._recommendations(rows, monthly_kwh, efficiency),
            "assumptions": {
                "price_eur_kwh": self.assumptions.electricity_price_eur_kwh,
                "co2_kg_kwh": self.assumptions.co2_kg_kwh,
                "target_monthly_kwh": self.assumptions.target_monthly_kwh,
                "scope": "DHT11, MQ135, HC-SR04 y LCD 16x2",
                "estimation_note": "Consumo estimado; usa readings.consumption_w cuando existe.",
            },
            "architecture": self._architecture_notes(),
            "history": self.obtener_historial(limit=18),
        }

        if persist:
            saved = self.guardar_snapshot(result)
            result["snapshot_saved"] = saved
            if saved:
                result["history"] = self.obtener_historial(limit=18)

        return result

    def _read_devices(self) -> list[dict[str, Any]]:
        conn = get_connection()
        if not conn:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                """
                SELECT
                    d.device_code,
                    d.device_name,
                    d.location_name,
                    d.status,
                    d.is_active,
                    st.code AS sensor_code,
                    st.name AS sensor_name,
                    cs.state_code,
                    cs.state_value,
                    cs.numeric_value,
                    (
                        SELECT r.consumption_w
                        FROM readings r
                        WHERE r.device_id = d.id
                          AND r.consumption_w IS NOT NULL
                        ORDER BY r.recorded_at DESC
                        LIMIT 1
                    ) AS latest_consumption_w
                FROM devices d
                LEFT JOIN sensor_types st ON st.id = d.sensor_type_id
                LEFT JOIN current_state cs ON cs.device_id = d.id
                WHERE COALESCE(d.is_active, 1) = 1
                ORDER BY d.device_code ASC
                """
            )
            raw_rows = cursor.fetchall() or []
        except Error:
            return []
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

        grouped: dict[str, dict[str, Any]] = {}
        for row in raw_rows:
            code = str(row.get("device_code") or "unknown")
            item = grouped.setdefault(
                code,
                {
                    "device_code": code,
                    "device_name": row.get("device_name") or code,
                    "location_name": row.get("location_name") or "Sin zona",
                    "sensor_code": row.get("sensor_code") or "",
                    "sensor_name": row.get("sensor_name") or "",
                    "states": {},
                    "latest_consumption_w": row.get("latest_consumption_w"),
                    "source": "base de datos",
                },
            )
            if item.get("latest_consumption_w") is None and row.get("latest_consumption_w") is not None:
                item["latest_consumption_w"] = row.get("latest_consumption_w")
            state_code = row.get("state_code")
            if state_code:
                item["states"][state_code] = {
                    "value": row.get("state_value"),
                    "numeric": row.get("numeric_value"),
                }

        return list(grouped.values())

    def _estimate_device(self, row: dict[str, Any]) -> dict[str, Any]:
        code = str(row.get("device_code") or "").lower()
        sensor_code = str(row.get("sensor_code") or "").lower()
        name = str(row.get("device_name") or code).lower()
        key = f"{code} {sensor_code} {name}"

        kind = self._detect_kind(key)
        power = self.POWER_BY_KIND_W.get(kind, self.POWER_BY_KIND_W["generic"])
        measured = row.get("latest_consumption_w")
        if measured is not None:
            try:
                power = max(0.0, float(measured))
            except Exception:
                pass

        if kind == "light":
            intensity = self._extract_intensity(row)
            power = round(max(0.8, self.POWER_BY_KIND_W["light"] * (intensity / 100)), 3)

        return {
            "device_code": row.get("device_code") or "unknown",
            "device_name": row.get("device_name") or row.get("device_code") or "Dispositivo",
            "location_name": row.get("location_name") or "Sin zona",
            "kind": kind,
            "kind_label": self._label_for_kind(kind),
            "icon": self._icon_for_kind(kind),
            "power_w": round(power, 3),
            "daily_wh": round(power * 24, 2),
            "monthly_kwh": round(power * 24 * self.assumptions.days_per_month / 1000, 3),
            "source": row.get("source") or "estimado",
            "raw_key": key,
            "measured": measured is not None,
        }

    def _canonical_real_rows(self, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
        canonical: list[dict[str, Any]] = []
        estimated_fallbacks = [self._estimate_device(dict(item, source="estimado")) for item in self.FALLBACK_DEVICES]
        by_kind = {row["kind"]: row for row in estimated_fallbacks}

        for kind in ["dht11", "mq135", "hc_sr04", "lcd16x2"]:
            candidates = [row for row in rows if row.get("kind") == kind]
            exact = [row for row in candidates if self._is_exact_real_device(kind, row.get("raw_key", ""))]
            chosen = exact[0] if exact else by_kind[kind]
            fallback = by_kind[kind]
            chosen = {
                **chosen,
                "device_code": fallback["device_code"],
                "device_name": fallback["device_name"],
                "location_name": fallback["location_name"],
                "source": "readings.consumption_w" if chosen.get("measured") and exact else "estimado",
            }
            if not exact:
                chosen["power_w"] = fallback["power_w"]
                chosen["daily_wh"] = fallback["daily_wh"]
                chosen["monthly_kwh"] = fallback["monthly_kwh"]
            canonical.append(chosen)
        return canonical

    def _is_exact_real_device(self, kind: str, text: str) -> bool:
        exact_tokens = {
            "dht11": ["dht11", "dht-11"],
            "mq135": ["mq135", "mq-135"],
            "hc_sr04": ["hc-sr04", "hcsr04", "hc_sr04"],
            "lcd16x2": ["lcd16x2", "lcd 16x2", "display 16x2"],
        }
        return any(token in text for token in exact_tokens.get(kind, []))

    def guardar_snapshot(self, data: dict[str, Any]) -> bool:
        conn = get_connection()
        if not conn:
            return False

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(self.CREATE_TABLE_SQL)
            conn.commit()

            cursor.execute("SELECT created_at FROM energy_snapshots ORDER BY created_at DESC LIMIT 1")
            last = cursor.fetchone()
            if last and last.get("created_at"):
                elapsed = datetime.now() - last["created_at"]
                if elapsed < timedelta(seconds=self.assumptions.snapshot_min_interval_seconds):
                    return False

            totals = data["totals"]
            top = totals.get("top_device") or {}
            cursor.execute(
                """
                INSERT INTO energy_snapshots (
                    total_watts,
                    daily_kwh,
                    monthly_kwh,
                    monthly_cost_eur,
                    monthly_co2_kg,
                    efficiency_percent,
                    highest_consumer,
                    sustainability_status,
                    source,
                    breakdown_json
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    totals["instant_w"],
                    totals["daily_kwh"],
                    totals["monthly_kwh"],
                    totals["cost_month_eur"],
                    totals["co2_month_kg"],
                    totals["efficiency_pct"],
                    top.get("device_name"),
                    (totals.get("state") or {}).get("label"),
                    "estimated_current_state",
                    json.dumps(data["devices"], ensure_ascii=False),
                ),
            )
            conn.commit()
            return True
        except Error:
            if conn:
                conn.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def obtener_historial(self, limit: int = 18) -> list[dict[str, Any]]:
        conn = get_connection()
        if not conn:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(self.CREATE_TABLE_SQL)
            conn.commit()
            cursor.execute(
                """
                SELECT
                    id,
                    created_at,
                    total_watts,
                    daily_kwh,
                    monthly_kwh,
                    monthly_cost_eur,
                    monthly_co2_kg,
                    efficiency_percent,
                    highest_consumer,
                    sustainability_status
                FROM energy_snapshots
                ORDER BY created_at DESC
                LIMIT %s
                """,
                (int(limit),),
            )
            rows = cursor.fetchall() or []
            return list(reversed(rows))
        except Error:
            return []
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def _detect_kind(self, text: str) -> str:
        checks = [
            ("mq135", ["mq135", "mq-135", "air_quality", "calidad", "aire"]),
            ("hc_sr04", ["hc-sr04", "hcsr04", "hc_sr04", "ultrasonic", "distance", "distancia", "puerta"]),
            ("lcd16x2", ["lcd16x2", "lcd 16x2", "display 16x2", "display", "pantalla"]),
            ("dht11", ["dht11", "dht-11", "dht", "temp", "temperature", "temperatura", "hum", "humidity", "humedad"]),
        ]
        for kind, needles in checks:
            if any(needle in text for needle in needles):
                return kind
        return "generic"

    def _extract_intensity(self, row: dict[str, Any]) -> float:
        states = row.get("states") or {}
        for key in ("LIGHT_INTENSITY", "intensity", "intensidad", "brightness"):
            value = states.get(key, {}).get("numeric")
            if value is not None:
                try:
                    return max(0.0, min(100.0, float(value)))
                except Exception:
                    pass
        return 70.0

    def _state(self, efficiency: float) -> dict[str, str]:
        if efficiency >= 80:
            return {"label": "Excelente", "tone": "green", "summary": "Operativa eficiente y sostenible."}
        if efficiency >= 60:
            return {"label": "Equilibrado", "tone": "gold", "summary": "Buen consumo, con margen de optimizacion."}
        return {"label": "Mejorable", "tone": "neutral", "summary": "Conviene revisar cargas de mayor consumo."}

    def _icon_for_kind(self, kind: str):
        return {
            "dht11": "thermostat",
            "mq135": "air",
            "hc_sr04": "sensors",
            "lcd16x2": "display_settings",
        }.get(kind, "sensors")

    def _label_for_kind(self, kind: str) -> str:
        return {
            "dht11": "DHT11",
            "mq135": "MQ135",
            "hc_sr04": "HC-SR04",
            "lcd16x2": "LCD 16x2",
        }.get(kind, "Sensor")

    def _recommendations(self, rows: list[dict[str, Any]], monthly_kwh: float, efficiency: float) -> list[str]:
        recs: list[str] = []
        top = max(rows, key=lambda item: item["power_w"], default=None)
        if top:
            recs.append(f"Vigilar {top['device_name']}: es el mayor consumidor estimado del conjunto real.")
        if any(row["kind"] == "mq135" for row in rows):
            recs.append("Aplicar muestreo adaptativo al MQ135 fuera de horario para reducir el calentador activo.")
        if any(row["kind"] == "lcd16x2" for row in rows):
            recs.append("Atenuar o apagar el backlight del LCD 16x2 cuando no haya operativa en mostrador.")
        if any(row["kind"] == "hc_sr04" for row in rows):
            recs.append("Mantener el HC-SR04 en lectura por intervalos; su consumo es bajo pero constante.")
        if efficiency < 70:
            recs.append("Revisar frecuencia de lectura y tiempos de pantalla para recuperar eficiencia.")
        if not recs:
            recs.append("Mantener la configuracion actual y revisar tendencias semanalmente.")
        return recs[:5]

    def _architecture_notes(self) -> list[dict[str, str]]:
        return [
            {"label": "Nucleo actual", "detail": "DHT11, MQ135, HC-SR04 y LCD 16x2", "icon": "sensors"},
            {"label": "Preparado para ampliar", "detail": "Camaras, luces, frio, caudalimetros o sensores de corriente", "icon": "hub"},
            {"label": "Historico estable", "detail": "Snapshots en MySQL con escritura limitada a una vez por minuto", "icon": "history"},
        ]
