from mysql.connector import Error
from models.db import get_connection


class UmbralController:
    def obtener_umbrales(self):
        conn = get_connection()
        if not conn:
            return []

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT id, state_code, operator_type, threshold_value, severity, title, description_template, is_active, updated_at
                FROM alert_thresholds
                ORDER BY state_code, FIELD(severity, 'critical', 'warning', 'info'), threshold_value DESC, id ASC
            """)
            return cursor.fetchall()
        except Error as e:
            print(f"Error leyendo umbrales: {e}")
            return []
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

    def actualizar_umbral(self, row_id, operator_type, threshold_value, severity, title, description_template, is_active):
        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar a la base de datos."

        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE alert_thresholds
                SET operator_type=%s,
                    threshold_value=%s,
                    severity=%s,
                    title=%s,
                    description_template=%s,
                    is_active=%s
                WHERE id=%s
            """, (
                operator_type,
                threshold_value,
                severity,
                title,
                description_template,
                1 if is_active else 0,
                row_id
            ))
            conn.commit()
            return True, "Regla de umbral actualizada correctamente."
        except Error as e:
            print(f"Error actualizando umbral: {e}")
            return False, str(e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

    def crear_umbral(self, state_code, operator_type, threshold_value, severity, title, description_template, is_active):
        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar a la base de datos."

        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO alert_thresholds (
                    state_code,
                    operator_type,
                    threshold_value,
                    severity,
                    title,
                    description_template,
                    is_active
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (
                state_code,
                operator_type,
                threshold_value,
                severity,
                title,
                description_template,
                1 if is_active else 0
            ))
            conn.commit()
            return True, "Nueva regla creada correctamente."
        except Error as e:
            print(f"Error creando umbral: {e}")
            return False, str(e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

    def eliminar_umbral(self, row_id):
        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar a la base de datos."

        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM alert_thresholds WHERE id=%s", (row_id,))
            conn.commit()
            return True, "Regla eliminada correctamente."
        except Error as e:
            print(f"Error eliminando umbral: {e}")
            return False, str(e)
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()