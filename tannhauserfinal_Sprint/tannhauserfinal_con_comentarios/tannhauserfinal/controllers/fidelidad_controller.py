from typing import List, Dict, Tuple
from datetime import datetime, timedelta
from mysql.connector import Error
from models.db import get_connection
import random
import string


class FidelidadController:
    def __init__(self):
        self._offers = [
            {
                "id": "bebidas_10",
                "title": "10% en bebidas frías",
                "description": "Descuento directo en refrescos, agua y bebidas isotónicas.",
                "points_cost": 80,
                "badge": "10% DTO"
            },
            {
                "id": "snacks_2x1",
                "title": "2x1 en snacks seleccionados",
                "description": "Promoción aplicable en productos seleccionados de aperitivos.",
                "points_cost": 120,
                "badge": "2x1"
            },
            {
                "id": "lacteos_15",
                "title": "15% en lácteos",
                "description": "Descuento en leche, yogures, quesos y productos refrigerados.",
                "points_cost": 100,
                "badge": "15% DTO"
            },
            {
                "id": "cafe_gratis",
                "title": "Café gratis",
                "description": "Canjea esta recompensa por un café gratuito en caja.",
                "points_cost": 60,
                "badge": "GRATIS"
            },
            {
                "id": "descuento_5",
                "title": "5 € de descuento",
                "description": "Cupón descuento de 5 € para compras superiores a 30 €.",
                "points_cost": 150,
                "badge": "5€ DTO"
            },
        ]

    def _nivel_cliente(self, total_spent: float) -> str:
        if total_spent >= 500:
            return "Platino"
        if total_spent >= 250:
            return "Oro"
        if total_spent >= 100:
            return "Plata"
        return "Bronce"

    def _generar_codigo_cupon(self, user_id: int, offer_id: str) -> str:
        sufijo = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
        prefijo = offer_id[:6].upper()
        return f"TANN-{user_id}-{prefijo}-{sufijo}"

    def obtener_resumen(self, user_id: int) -> Dict:
        conn = get_connection()
        if not conn:
            return {
                "user_id": user_id,
                "nombre": "Cliente",
                "loyalty_points": 0,
                "total_spent": 0.0,
                "nivel": "Bronce"
            }

        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT
                    id,
                    nombre,
                    COALESCE(loyalty_points, 0) AS loyalty_points,
                    COALESCE(total_spent, 0) AS total_spent
                FROM users
                WHERE id = %s
                LIMIT 1
            """, (user_id,))
            row = cursor.fetchone()

            if not row:
                return {
                    "user_id": user_id,
                    "nombre": "Cliente",
                    "loyalty_points": 0,
                    "total_spent": 0.0,
                    "nivel": "Bronce"
                }

            row["nivel"] = self._nivel_cliente(float(row["total_spent"] or 0))
            return row
        finally:
            cursor.close()
            conn.close()

    def obtener_ofertas(self, user_id: int = None) -> List[Dict]:
        puntos_actuales = 0
        if user_id is not None:
            resumen = self.obtener_resumen(user_id)
            puntos_actuales = int(resumen.get("loyalty_points", 0) or 0)

        ofertas = []
        for item in self._offers:
            oferta = dict(item)
            oferta["can_redeem"] = puntos_actuales >= oferta["points_cost"]
            ofertas.append(oferta)
        return ofertas

    def obtener_historial(self, user_id: int, limit: int = 30) -> List[Dict]:
        conn = get_connection()
        if not conn:
            return []

        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT
                    id,
                    transaction_type,
                    purchase_amount,
                    points_delta,
                    description,
                    reference_code,
                    created_at
                FROM loyalty_transactions
                WHERE user_id = %s
                ORDER BY id DESC
                LIMIT %s
            """, (user_id, limit))
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    def obtener_cupones_activos(self, user_id: int) -> List[Dict]:
        conn = get_connection()
        if not conn:
            return []

        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT
                    id,
                    offer_id,
                    coupon_code,
                    title,
                    description,
                    points_cost,
                    status,
                    redeemed_at,
                    used_at,
                    expires_at
                FROM loyalty_coupons
                WHERE user_id = %s
                  AND status = 'active'
                ORDER BY id DESC
            """, (user_id,))
            return cursor.fetchall()
        finally:
            cursor.close()
            conn.close()

    def registrar_compra(self, user_id: int, amount, reference_code: str = "") -> Tuple[bool, str]:
        try:
            amount = float(str(amount).replace(",", "."))
        except Exception:
            return False, "El importe no es válido."

        if amount <= 0:
            return False, "El importe debe ser mayor que 0."

        points = max(1, int(amount // 10))

        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar con la base de datos."

        cursor = conn.cursor()
        try:
            conn.start_transaction()

            cursor.execute("""
                INSERT INTO loyalty_transactions (
                    user_id,
                    transaction_type,
                    purchase_amount,
                    points_delta,
                    description,
                    reference_code,
                    created_at
                ) VALUES (%s, 'purchase', %s, %s, %s, %s, NOW())
            """, (
                user_id,
                amount,
                points,
                "Compra registrada en supermercado",
                reference_code.strip() if reference_code else None
            ))

            cursor.execute("""
                UPDATE users
                SET
                    loyalty_points = COALESCE(loyalty_points, 0) + %s,
                    total_spent = COALESCE(total_spent, 0) + %s,
                    updated_at = NOW()
                WHERE id = %s
            """, (points, amount, user_id))

            conn.commit()
            return True, f"Compra registrada correctamente. Has sumado {points} puntos."
        except Error as e:
            conn.rollback()
            return False, f"Error al registrar la compra: {e}"
        finally:
            cursor.close()
            conn.close()

    def canjear_oferta(self, user_id: int, offer_id: str) -> Tuple[bool, str]:
        oferta = next((o for o in self._offers if o["id"] == offer_id), None)
        if not oferta:
            return False, "Oferta no encontrada."

        resumen = self.obtener_resumen(user_id)
        puntos_actuales = int(resumen.get("loyalty_points", 0) or 0)

        if puntos_actuales < oferta["points_cost"]:
            return False, "No tienes suficientes puntos para canjear esta oferta."

        coupon_code = self._generar_codigo_cupon(user_id, offer_id)
        expires_at = datetime.now() + timedelta(days=30)

        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar con la base de datos."

        cursor = conn.cursor()
        try:
            conn.start_transaction()

            cursor.execute("""
                INSERT INTO loyalty_transactions (
                    user_id,
                    transaction_type,
                    purchase_amount,
                    points_delta,
                    description,
                    reference_code,
                    created_at
                ) VALUES (%s, 'redeem', 0.00, %s, %s, %s, NOW())
            """, (
                user_id,
                -int(oferta["points_cost"]),
                f"Canje de recompensa: {oferta['title']}",
                coupon_code
            ))

            cursor.execute("""
                UPDATE users
                SET
                    loyalty_points = COALESCE(loyalty_points, 0) - %s,
                    updated_at = NOW()
                WHERE id = %s
            """, (int(oferta["points_cost"]), user_id))

            cursor.execute("""
                INSERT INTO loyalty_coupons (
                    user_id,
                    offer_id,
                    coupon_code,
                    title,
                    description,
                    points_cost,
                    status,
                    redeemed_at,
                    expires_at
                ) VALUES (%s, %s, %s, %s, %s, %s, 'active', NOW(), %s)
            """, (
                user_id,
                oferta["id"],
                coupon_code,
                oferta["title"],
                oferta["description"],
                int(oferta["points_cost"]),
                expires_at
            ))

            conn.commit()
            return True, f"Oferta canjeada correctamente. Cupón activo generado: {coupon_code}"
        except Error as e:
            conn.rollback()
            return False, f"Error al canjear la oferta: {e}"
        finally:
            cursor.close()
            conn.close()

    def marcar_cupon_como_usado(self, user_id: int, coupon_id: int) -> Tuple[bool, str]:
        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar con la base de datos."

        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE loyalty_coupons
                SET status = 'used', used_at = NOW()
                WHERE id = %s
                  AND user_id = %s
                  AND status = 'active'
            """, (coupon_id, user_id))
            conn.commit()

            if cursor.rowcount == 0:
                return False, "No se encontró el cupón activo."
            return True, "Cupón marcado como usado correctamente."
        except Error as e:
            conn.rollback()
            return False, f"Error al actualizar el cupón: {e}"
        finally:
            cursor.close()
            conn.close()