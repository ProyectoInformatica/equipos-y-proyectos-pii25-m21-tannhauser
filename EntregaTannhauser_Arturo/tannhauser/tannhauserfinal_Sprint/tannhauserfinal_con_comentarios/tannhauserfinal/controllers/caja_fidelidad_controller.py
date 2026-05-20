import json
import re
from mysql.connector import Error
from models.db import get_connection


class CajaFidelidadController:
    def extraer_user_id_desde_qr(self, texto_qr: str):
        if not texto_qr or not texto_qr.strip():
            return None

        texto_qr = texto_qr.strip()

        if texto_qr.isdigit():
            return int(texto_qr)

        try:
            data = json.loads(texto_qr)
            if isinstance(data, dict):
                if data.get("user_id"):
                    return int(data["user_id"])
                if data.get("id"):
                    return int(data["id"])
        except Exception:
            pass

        patrones = [
            r"user_id\s*[:=]\s*(\d+)",
            r"id\s*[:=]\s*(\d+)",
            r"cliente\s*[:=]\s*(\d+)",
            r"(\d+)"
        ]

        for patron in patrones:
            match = re.search(patron, texto_qr, re.IGNORECASE)
            if match:
                return int(match.group(1))

        return None

    def obtener_cliente_por_qr(self, texto_qr: str):
        user_id = self.extraer_user_id_desde_qr(texto_qr)
        if not user_id:
            return False, "No se pudo identificar al cliente desde el QR.", None

        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar a la base de datos.", None

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT
                    id,
                    nombre,
                    email,
                    is_active,
                    COALESCE(loyalty_points, 0) AS loyalty_points,
                    COALESCE(loyalty_total_spent, 0) AS loyalty_total_spent
                FROM users
                WHERE id = %s
                LIMIT 1
            """, (user_id,))
            row = cursor.fetchone()

            if not row:
                return False, "Cliente no encontrado.", None

            if int(row.get("is_active", 0)) != 1:
                return False, "El cliente existe pero está desactivado.", None

            return True, "Cliente validado correctamente.", row

        except Error as e:
            print(f"Error en obtener_cliente_por_qr: {e}")
            return False, f"Error de base de datos: {e}", None

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()

    def _calcular_puntos(self, importe: float):
        try:
            importe = float(importe)
        except Exception:
            return 0

        if importe <= 0:
            return 0

        puntos = int(importe // 10)
        if puntos <= 0:
            puntos = 1
        return puntos

    def registrar_compra(self, user_id: int, importe: float, referencia: str = ""):
        try:
            importe = float(str(importe).replace(",", "."))
        except Exception:
            return False, "El importe no es válido.", None

        if importe <= 0:
            return False, "El importe debe ser mayor que 0.", None

        puntos = self._calcular_puntos(importe)

        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar a la base de datos.", None

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)

            cursor.execute("""
                SELECT id, nombre, email, is_active,
                       COALESCE(loyalty_points, 0) AS loyalty_points,
                       COALESCE(loyalty_total_spent, 0) AS loyalty_total_spent
                FROM users
                WHERE id = %s
                LIMIT 1
            """, (user_id,))
            user = cursor.fetchone()

            if not user:
                return False, "Cliente no encontrado.", None

            if int(user.get("is_active", 0)) != 1:
                return False, "El cliente está desactivado.", None

            cursor.execute("""
                UPDATE users
                SET
                    loyalty_points = COALESCE(loyalty_points, 0) + %s,
                    loyalty_total_spent = COALESCE(loyalty_total_spent, 0) + %s,
                    updated_at = NOW()
                WHERE id = %s
            """, (puntos, importe, user_id))

            cursor.execute("""
                INSERT INTO loyalty_transactions (
                    user_id,
                    transaction_type,
                    purchase_amount,
                    points_delta,
                    description,
                    reference_code,
                    created_at
                ) VALUES (
                    %s, 'purchase', %s, %s, %s, %s, NOW()
                )
            """, (
                user_id,
                importe,
                puntos,
                "Compra registrada en caja por empleado",
                referencia or None
            ))

            conn.commit()

            cursor.execute("""
                SELECT
                    id,
                    nombre,
                    email,
                    COALESCE(loyalty_points, 0) AS loyalty_points,
                    COALESCE(loyalty_total_spent, 0) AS loyalty_total_spent
                FROM users
                WHERE id = %s
                LIMIT 1
            """, (user_id,))
            actualizado = cursor.fetchone()

            return True, f"Compra registrada. Se han sumado {puntos} puntos.", actualizado

        except Error as e:
            if conn:
                conn.rollback()
            print(f"Error en registrar_compra: {e}")
            return False, f"Error al registrar la compra: {e}", None

        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None and conn.is_connected():
                conn.close()