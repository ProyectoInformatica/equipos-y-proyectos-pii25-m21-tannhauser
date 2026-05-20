import json
from mysql.connector import Error
from models.db import get_connection


class AlertaController:
    def obtener_eventos_nuevos(self, ultimo_id=0):
        conn = get_connection()
        if not conn:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT
                    e.id,
                    e.device_id,
                    e.event_type,
                    e.severity,
                    e.title,
                    e.description,
                    e.event_time,
                    e.payload,
                    e.is_resolved,
                    e.resolved_at,
                    d.device_code
                FROM events e
                LEFT JOIN devices d ON d.id = e.device_id
                WHERE e.id > %s
                  AND e.event_type = 'sensor_alert'
                  AND e.is_resolved = 0
                ORDER BY e.id ASC
            """, (ultimo_id,))
            rows = cursor.fetchall()

            for row in rows:
                payload = row.get("payload")
                if payload:
                    try:
                        row["payload_json"] = json.loads(payload)
                    except Exception:
                        row["payload_json"] = {}
                else:
                    row["payload_json"] = {}

            return rows

        except Error as e:
            print(f"Error leyendo eventos nuevos: {e}")
            return []

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

    def obtener_alertas_activas(self, limite=100):
        conn = get_connection()
        if not conn:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT
                    e.id,
                    e.device_id,
                    e.event_type,
                    e.severity,
                    e.title,
                    e.description,
                    e.event_time,
                    e.payload,
                    e.is_resolved,
                    e.resolved_at,
                    d.device_code
                FROM events e
                LEFT JOIN devices d ON d.id = e.device_id
                WHERE e.event_type = 'sensor_alert'
                  AND e.is_resolved = 0
                ORDER BY e.event_time DESC
                LIMIT %s
            """, (limite,))
            rows = cursor.fetchall()

            for row in rows:
                payload = row.get("payload")
                if payload:
                    try:
                        row["payload_json"] = json.loads(payload)
                    except Exception:
                        row["payload_json"] = {}
                else:
                    row["payload_json"] = {}

            return rows

        except Error as e:
            print(f"Error leyendo alertas activas: {e}")
            return []

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

    def obtener_historial_alertas(self, limite=100):
        conn = get_connection()
        if not conn:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT
                    e.id,
                    e.device_id,
                    e.event_type,
                    e.severity,
                    e.title,
                    e.description,
                    e.event_time,
                    e.payload,
                    e.is_resolved,
                    e.resolved_at,
                    d.device_code
                FROM events e
                LEFT JOIN devices d ON d.id = e.device_id
                WHERE e.event_type = 'sensor_alert'
                  AND e.is_resolved = 1
                ORDER BY e.resolved_at DESC, e.event_time DESC
                LIMIT %s
            """, (limite,))
            rows = cursor.fetchall()

            for row in rows:
                payload = row.get("payload")
                if payload:
                    try:
                        row["payload_json"] = json.loads(payload)
                    except Exception:
                        row["payload_json"] = {}
                else:
                    row["payload_json"] = {}

            return rows

        except Error as e:
            print(f"Error leyendo historial de alertas: {e}")
            return []

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

    def resolver_alerta(self, event_id, user_id=None):
        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar a la base de datos."

        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE events
                SET is_resolved = 1,
                    resolved_at = NOW(),
                    resolved_by_user_id = %s
                WHERE id = %s
            """, (user_id, event_id))
            conn.commit()
            return True, "Alerta resuelta correctamente."
        except Error as e:
            print(f"Error resolviendo alerta: {e}")
            return False, str(e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

    def ruta_para_evento(self, evento, rol_actual="superusuario"):
        payload = evento.get("payload_json", {}) or {}
        state_code = payload.get("state_code")
        device_code = payload.get("device_code")

        if rol_actual in ["superusuario", "administrador"]:
            return "/admin_mapa_sensores"

        if state_code in ["TEMP_AIR", "HUM_AIR", "MQ135_AIR"]:
            return "/sensores_aire"

        if state_code == "DISTANCE_CM" or device_code == "door_01":
            return "/sensores_puerta"

        return "/"