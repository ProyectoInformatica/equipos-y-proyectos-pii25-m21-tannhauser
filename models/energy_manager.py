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
        "esp32": 0.45,
        "microcontroller": 0.45,
        "dht": 0.01,
        "temperature": 0.01,
        "humidity": 0.01,
        "mq": 0.90,
        "mq2": 0.90,
        "mq135": 0.90,
        "air_quality": 0.90,
        "hc_sr04": 0.075,
        "ultrasonic": 0.075,
        "distance": 0.075,
        "ldr": 0.005,
        "light_sensor": 0.005,
        "led": 9.00,
        "light": 9.00,
        "esp32_cam": 1.30,
        "camera": 1.30,
        "fridge": 110.00,
        "freezer": 110.00,
        "door": 0.15,
        "generic": 0.25,
    }

    FALLBACK_DEVICES = [
        {"device_code": "esp32_main", "device_name": "ESP32 principal", "sensor_code": "esp32", "location_name": "Control"},
        {"device_code": "temp_01", "device_name": "DHT temperatura", "sensor_code": "temperature", "location_name": "Sala"},
        {"device_code": "hum_01", "device_name": "DHT humedad", "sensor_code": "humidity", "location_name": "Sala"},
        {"device_code": "mq135_01", "device_name": "MQ-135 aire", "sensor_code": "mq135", "location_name": "Sala"},
        {"device_code": "door_01", "device_name": "HC-SR04 puerta", "sensor_code": "distance", "location_name": "Entrada"},
        {"device_code": "ldr_01", "device_name": "LDR ambiente", "sensor_code": "ldr", "location_name": "Pasillo"},
        {"device_code": "light_01", "device_name": "Luces LED", "sensor_code": "light", "location_name": "Zona ventas"},
        {"device_code": "esp32_cam_01", "device_name": "ESP32-CAM", "sensor_code": "camera", "location_name": "Seguridad"},
        {"device_code": "fridge_01", "device_name": "Nevera simulada", "sensor_code": "fridge", "location_name": "Frio"},
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
            },
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
            "icon": self._icon_for_kind(kind),
            "power_w": round(power, 3),
            "daily_wh": round(power * 24, 2),
            "monthly_kwh": round(power * 24 * self.assumptions.days_per_month / 1000, 3),
            "source": row.get("source") or "estimado",
        }

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
            ("esp32_cam", ["esp32-cam", "esp32_cam", "camara", "camera", "videocam"]),
            ("fridge", ["fridge", "nevera", "freezer", "frio", "refriger"]),
            ("mq135", ["mq135", "mq-135", "mq2", "mq-2", "air_quality", "calidad"]),
            ("distance", ["hc-sr04", "hcsr04", "ultrasonic", "distance", "distancia"]),
            ("light", ["light_", "luces", "luz led", "led", "light"]),
            ("ldr", ["ldr"]),
            ("temperature", ["dht", "temp", "temperature", "temperatura"]),
            ("humidity", ["hum", "humidity", "humedad"]),
            ("door", ["door", "puerta"]),
            ("esp32", ["esp32", "microcontroller", "microcontrolador"]),
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
            "temperature": "thermostat",
            "humidity": "water_drop",
            "mq135": "air",
            "distance": "straighten",
            "door": "door",
            "ldr": "wb_sunny",
            "light": "lightbulb",
            "esp32_cam": "videocam",
            "camera": "videocam",
            "fridge": "kitchen",
            "esp32": "memory",
        }.get(kind, "sensors")

    def _recommendations(self, rows: list[dict[str, Any]], monthly_kwh: float, efficiency: float) -> list[str]:
        recs: list[str] = []
        top = max(rows, key=lambda item: item["power_w"], default=None)
        if top and top["power_w"] >= 10:
            recs.append(f"Revisar {top['device_name']}: concentra el mayor consumo estimado.")
        if any(row["kind"] == "light" for row in rows):
            recs.append("Programar las luces por franja horaria y mantener intensidad reducida fuera de horas punta.")
        if any(row["kind"] == "fridge" for row in rows):
            recs.append("Mantener la zona de frio cerrada y estable para reducir ciclos de compresor.")
        if any(row["kind"] in ["mq135", "esp32_cam"] for row in rows):
            recs.append("Usar muestreo inteligente en sensores de mayor consumo cuando la tienda este cerrada.")
        if efficiency < 70 or monthly_kwh > self.assumptions.target_monthly_kwh * 0.35:
            recs.append("Crear una rutina nocturna: luces al minimo, camara en modo captura y sensores en baja frecuencia.")
        if not recs:
            recs.append("Mantener la configuracion actual y revisar tendencias semanalmente.")
        return recs[:5]
