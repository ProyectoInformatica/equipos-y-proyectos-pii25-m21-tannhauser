import json
from mysql.connector import Error
from models.db import get_connection


class LucesController:
    def listar_luces(self):
        conn = get_connection()
        if not conn:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT
                    d.id AS device_id,
                    d.device_code,
                    d.device_name,
                    d.location_name,
                    cs_state.state_value AS light_state_value,
                    cs_state.numeric_value AS light_state_numeric,
                    cs_state.updated_at AS light_state_updated_at,
                    cs_int.state_value AS intensity_state_value,
                    cs_int.numeric_value AS intensity_numeric,
                    cs_int.updated_at AS intensity_updated_at
                FROM devices d
                LEFT JOIN current_state cs_state
                    ON cs_state.device_id = d.id
                   AND cs_state.state_code = 'LIGHT_STATE'
                LEFT JOIN current_state cs_int
                    ON cs_int.device_id = d.id
                   AND cs_int.state_code = 'LIGHT_INTENSITY'
                WHERE LOWER(d.device_code) LIKE 'light%%'
                   OR LOWER(d.device_name) LIKE '%%luz%%'
                   OR LOWER(COALESCE(d.location_name, '')) LIKE '%%luz%%'
                ORDER BY d.id
            """)
            rows = cursor.fetchall()

            luces = []
            for row in rows:
                estado_raw = (row.get("light_state_value") or "").strip().lower()
                intensidad_raw = row.get("intensity_numeric")

                encendida = estado_raw in ["on", "encendida", "1", "true", "activo"]
                intensidad = 0
                if intensidad_raw is not None:
                    try:
                        intensidad = int(float(intensidad_raw))
                    except Exception:
                        intensidad = 0

                luces.append({
                    "device_id": row["device_id"],
                    "device_code": row["device_code"],
                    "device_name": row.get("device_name") or row["device_code"],
                    "location_name": row.get("location_name") or "Sin ubicación",
                    "encendida": encendida,
                    "intensidad": intensidad,
                    "updated_at": row.get("intensity_updated_at") or row.get("light_state_updated_at"),
                })

            return luces

        except Error as e:
            print(f"Error en listar_luces: {e}")
            return []

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

    def _upsert_current_state(self, cursor, device_id, state_code, state_value, numeric_value, payload_dict):
        payload = json.dumps(payload_dict, ensure_ascii=False)
        cursor.execute("""
            INSERT INTO current_state (
                device_id,
                state_code,
                state_value,
                numeric_value,
                updated_at,
                source,
                payload
            ) VALUES (
                %s, %s, %s, %s, NOW(), 'manual', %s
            )
            ON DUPLICATE KEY UPDATE
                state_value = VALUES(state_value),
                numeric_value = VALUES(numeric_value),
                updated_at = NOW(),
                source = 'manual',
                payload = VALUES(payload)
        """, (device_id, state_code, state_value, numeric_value, payload))

    def guardar_luz(self, device_id: int, encendida: bool, intensidad: int):
        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar a la base de datos."

        cursor = None
        try:
            intensidad = max(0, min(100, int(intensidad)))
            state_value = "ON" if encendida else "OFF"
            numeric_state = 1 if encendida else 0

            cursor = conn.cursor()

            self._upsert_current_state(
                cursor,
                device_id,
                "LIGHT_STATE",
                state_value,
                numeric_state,
                {
                    "origin": "panel_empleado",
                    "accion": "actualizacion_luz"
                }
            )

            self._upsert_current_state(
                cursor,
                device_id,
                "LIGHT_INTENSITY",
                str(intensidad),
                intensidad,
                {
                    "origin": "panel_empleado",
                    "accion": "actualizacion_intensidad"
                }
            )

            conn.commit()
            return True, "Configuración de luces actualizada correctamente."

        except Error as e:
            if conn:
                conn.rollback()
            print(f"Error en guardar_luz: {e}")
            return False, f"Error al guardar luces: {e}"

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()