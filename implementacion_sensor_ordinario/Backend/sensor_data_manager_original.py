import json
import statistics
from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Optional, Tuple

from models.db import get_connection


class SensorDataManager:
    def __init__(self):
        self.sensor_catalog = {
            "sensor_temperatura": {
                "type_code": "temperatura",
                "type_name": "Temperatura",
                "unit": "C",
                "category": "ambiental",
                "description": "Sensor de temperatura ambiental",
                "device_code": "DEV-TEMP-001",
                "device_name": "Sensor Temperatura",
                "location_name": "Supermercado",
            },
            "sensor_humedad": {
                "type_code": "humedad",
                "type_name": "Humedad",
                "unit": "%",
                "category": "ambiental",
                "description": "Sensor de humedad ambiental",
                "device_code": "DEV-HUM-001",
                "device_name": "Sensor Humedad",
                "location_name": "Supermercado",
            },
            "sensor_luz": {
                "type_code": "luz",
                "type_name": "Luz",
                "unit": "%",
                "category": "ambiental",
                "description": "Sensor de luz",
                "device_code": "DEV-LUZ-001",
                "device_name": "Sensor Luz",
                "location_name": "Supermercado",
            },
            "sensor_nevera": {
                "type_code": "nevera",
                "type_name": "Nevera",
                "unit": "C",
                "category": "consumo",
                "description": "Sensor de temperatura de nevera",
                "device_code": "DEV-NEV-001",
                "device_name": "Sensor Nevera",
                "location_name": "Zona refrigerada",
            },
            "sensor_puerta": {
                "type_code": "puerta",
                "type_name": "Puerta",
                "unit": None,
                "category": "estado",
                "description": "Sensor de estado de puerta",
                "device_code": "DEV-PUE-001",
                "device_name": "Sensor Puerta",
                "location_name": "Entrada",
            },
        }

    def _is_numeric(self, value) -> bool:
        if isinstance(value, bool):
            return False
        if isinstance(value, (int, float, Decimal)):
            return True
        try:
            float(value)
            return True
        except (TypeError, ValueError):
            return False

    def _get_catalog_info(self, nombre_sensor: str) -> Dict:
        if nombre_sensor in self.sensor_catalog:
            return self.sensor_catalog[nombre_sensor]

        return {
            "type_code": nombre_sensor.lower(),
            "type_name": nombre_sensor.replace("_", " ").title(),
            "unit": None,
            "category": "otro",
            "description": f"Sensor {nombre_sensor}",
            "device_code": f"DEV-{nombre_sensor[:12].upper()}",
            "device_name": nombre_sensor.replace("_", " ").title(),
            "location_name": "No definida",
        }

    def _ensure_sensor_resources(self, nombre_sensor: str) -> Tuple[Optional[int], Optional[int], Optional[str]]:
        info = self._get_catalog_info(nombre_sensor)
        conn = get_connection()
        if not conn:
            return None, None, None

        cursor = conn.cursor(dictionary=True)

        # Sensor type
        cursor.execute(
            "SELECT id FROM sensor_types WHERE code = %s LIMIT 1",
            (info["type_code"],)
        )
        row = cursor.fetchone()

        if row:
            sensor_type_id = row["id"]
        else:
            cursor.execute(
                """
                INSERT INTO sensor_types (code, name, unit, category, description)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    info["type_code"],
                    info["type_name"],
                    info["unit"],
                    info["category"],
                    info["description"],
                )
            )
            conn.commit()
            sensor_type_id = cursor.lastrowid

        # Device
        cursor.execute(
            "SELECT id FROM devices WHERE device_code = %s LIMIT 1",
            (info["device_code"],)
        )
        row = cursor.fetchone()

        if row:
            device_id = row["id"]
        else:
            cursor.execute(
                """
                INSERT INTO devices (
                    device_code, device_name, sensor_type_id, location_name,
                    pin_or_channel, status, metadata, installed_at
                )
                VALUES (%s, %s, %s, %s, %s, 'activo', %s, %s)
                """,
                (
                    info["device_code"],
                    info["device_name"],
                    sensor_type_id,
                    info["location_name"],
                    None,
                    json.dumps({"sensor_name": nombre_sensor}, ensure_ascii=False),
                    datetime.now(),
                )
            )
            conn.commit()
            device_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return device_id, sensor_type_id, info["unit"]

    def _get_current_state_row(self, conn, device_id: int, state_code: str):
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT id, state_value, numeric_value
            FROM current_state
            WHERE device_id = %s AND state_code = %s
            ORDER BY id DESC
            LIMIT 1
            """,
            (device_id, state_code)
        )
        row = cursor.fetchone()
        cursor.close()
        return row

    def _upsert_current_state(
        self,
        conn,
        device_id: int,
        state_code: str,
        state_value: str,
        numeric_value,
        source: str = "simulado",
        payload: Optional[dict] = None,
    ):
        payload_json = json.dumps(payload or {}, ensure_ascii=False)

        existing = self._get_current_state_row(conn, device_id, state_code)
        cursor = conn.cursor()

        if existing:
            cursor.execute(
                """
                UPDATE current_state
                SET state_value = %s,
                    numeric_value = %s,
                    updated_at = NOW(6),
                    source = %s,
                    payload = %s
                WHERE id = %s
                """,
                (state_value, numeric_value, source, payload_json, existing["id"])
            )
        else:
            cursor.execute(
                """
                INSERT INTO current_state (
                    device_id, state_code, state_value, numeric_value, updated_at, source, payload
                )
                VALUES (%s, %s, %s, %s, NOW(6), %s, %s)
                """,
                (device_id, state_code, state_value, numeric_value, source, payload_json)
            )

        conn.commit()
        cursor.close()

    def _insert_state_history(
        self,
        conn,
        device_id: int,
        state_code: str,
        old_value,
        new_value,
        event_type: str,
        source: str = "simulado",
        payload: Optional[dict] = None,
    ):
        payload_json = json.dumps(payload or {}, ensure_ascii=False)
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO state_history (
                device_id, state_code, old_value, new_value, changed_at, event_type, source, payload
            )
            VALUES (%s, %s, %s, %s, NOW(6), %s, %s, %s)
            """,
            (device_id, state_code, old_value, new_value, event_type, source, payload_json)
        )
        conn.commit()
        cursor.close()

    def guardar_lectura_sensor(self, nombre_sensor: str, valor, source: str = "simulado"):
        device_id, sensor_type_id, unit = self._ensure_sensor_resources(nombre_sensor)
        if not device_id or not sensor_type_id:
            return

        conn = get_connection()
        if not conn:
            return

        payload = {"sensor_name": nombre_sensor}

        if self._is_numeric(valor):
            numeric_value = float(valor)
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO readings (
                    device_id, sensor_type_id, reading_value, normalized_value,
                    consumption_w, reading_unit, recorded_at, source, payload
                )
                VALUES (%s, %s, %s, %s, %s, %s, NOW(6), %s, %s)
                """,
                (
                    device_id,
                    sensor_type_id,
                    numeric_value,
                    numeric_value,
                    None,
                    unit,
                    source,
                    json.dumps(payload, ensure_ascii=False),
                )
            )
            conn.commit()
            cursor.close()

            self._upsert_current_state(
                conn,
                device_id,
                "lectura_actual",
                str(valor),
                numeric_value,
                source=source,
                payload=payload,
            )
        else:
            state_code = "estado"
            previous = self._get_current_state_row(conn, device_id, state_code)
            old_value = previous["state_value"] if previous else None
            new_value = str(valor)

            if old_value != new_value:
                self._insert_state_history(
                    conn,
                    device_id,
                    state_code,
                    old_value,
                    new_value,
                    "cambio_estado",
                    source=source,
                    payload=payload,
                )

            self._upsert_current_state(
                conn,
                device_id,
                state_code,
                new_value,
                None,
                source=source,
                payload=payload,
            )

        conn.close()

    def guardar_lecturas_lote(self, lecturas: List[Dict], source: str = "simulado"):
        if not lecturas:
            return
        for lectura in lecturas:
            self.guardar_lectura_sensor(
                lectura.get("sensor"),
                lectura.get("valor"),
                source=source,
            )

    def leer_lecturas_sensor(self, nombre_sensor: str) -> List[Dict]:
        info = self._get_catalog_info(nombre_sensor)

        conn = get_connection()
        if not conn:
            return []

        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT id FROM devices WHERE device_code = %s LIMIT 1",
            (info["device_code"],)
        )
        device = cursor.fetchone()

        if not device:
            cursor.close()
            conn.close()
            return []

        device_id = device["id"]

        if nombre_sensor == "sensor_puerta":
            cursor.execute(
                """
                SELECT new_value, changed_at
                FROM state_history
                WHERE device_id = %s AND state_code = 'estado'
                ORDER BY changed_at ASC, id ASC
                """,
                (device_id,)
            )
            rows = cursor.fetchall()

            if not rows:
                cursor.execute(
                    """
                    SELECT state_value, updated_at
                    FROM current_state
                    WHERE device_id = %s AND state_code = 'estado'
                    ORDER BY id DESC
                    LIMIT 1
                    """,
                    (device_id,)
                )
                current = cursor.fetchone()
                cursor.close()
                conn.close()

                if not current:
                    return []

                return [{
                    "timestamp": current["updated_at"].isoformat(),
                    "valor": current["state_value"]
                }]

            cursor.close()
            conn.close()

            return [
                {
                    "timestamp": row["changed_at"].isoformat(),
                    "valor": row["new_value"]
                }
                for row in rows
            ]

        cursor.execute(
            """
            SELECT reading_value, recorded_at
            FROM readings
            WHERE device_id = %s
            ORDER BY recorded_at ASC, id ASC
            """,
            (device_id,)
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return [
            {
                "timestamp": row["recorded_at"].isoformat(),
                "valor": float(row["reading_value"])
            }
            for row in rows
        ]

    def guardar_consumo_sensor(self, nombre_sensor: str, consumo_wh):
        device_id, _, _ = self._ensure_sensor_resources(nombre_sensor)
        if not device_id:
            return

        conn = get_connection()
        if not conn:
            return

        self._upsert_current_state(
            conn,
            device_id,
            "consumo_24h",
            str(consumo_wh),
            float(consumo_wh) if self._is_numeric(consumo_wh) else None,
            source="sistema",
            payload={"sensor_name": nombre_sensor, "tipo": "consumo_24h"},
        )
        conn.close()

    def obtener_estadisticas_sensores(self) -> Dict:
        estadisticas = {}
        for nombre_sensor in self.sensor_catalog.keys():
            estadisticas[nombre_sensor] = self.obtener_estadisticas_sensor_individual(nombre_sensor)
        return estadisticas

    def obtener_estadisticas_sensor_individual(self, nombre_sensor: str) -> Dict:
        lecturas = self.leer_lecturas_sensor(nombre_sensor)

        if not lecturas:
            return {
                "nombre": nombre_sensor,
                "estado": "sin_datos",
                "total_lecturas": 0,
                "mensaje": "No hay datos disponibles",
            }

        valores = []
        valores_no_numericos = []

        for lectura in lecturas:
            valor = lectura.get("valor")
            try:
                valores.append(float(valor))
            except (ValueError, TypeError):
                valores_no_numericos.append(valor)

        resultado = {
            "nombre": nombre_sensor,
            "estado": "operativo",
            "total_lecturas": len(lecturas),
            "ultima_lectura": lecturas[-1],
            "primera_lectura": lecturas[0],
        }

        if valores:
            resultado.update({
                "tipo_dato": "numerico",
                "valores_numericos": len(valores),
                "valores_no_numericos": len(valores_no_numericos),
                "minimo": round(min(valores), 2),
                "maximo": round(max(valores), 2),
                "promedio": round(sum(valores) / len(valores), 2),
                "mediana": round(statistics.median(valores), 2),
                "desviacion_estandar": round(statistics.stdev(valores), 2) if len(valores) > 1 else 0,
                "rango": round(max(valores) - min(valores), 2),
            })
        else:
            resultado.update({
                "tipo_dato": "texto",
                "valores_unicos": len(set(valores_no_numericos)),
                "valores": list(set(valores_no_numericos)),
            })

        return resultado