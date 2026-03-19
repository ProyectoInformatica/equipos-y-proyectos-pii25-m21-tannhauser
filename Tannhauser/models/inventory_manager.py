from typing import List, Dict, Optional
from models.db import get_connection


class InventoryManager:
    def listar(self) -> List[Dict]:
        conn = get_connection()
        if not conn:
            return []

        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT id, sku, nombre, cantidad, precio, is_active
            FROM products
            WHERE is_active = 1
            ORDER BY id
        """
        cursor.execute(query)
        items = cursor.fetchall()

        cursor.close()
        conn.close()
        return items

    def obtener_por_id(self, item_id: int) -> Optional[Dict]:
        conn = get_connection()
        if not conn:
            return None

        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT id, sku, nombre, cantidad, precio, is_active
            FROM products
            WHERE id = %s AND is_active = 1
            LIMIT 1
        """
        cursor.execute(query, (item_id,))
        item = cursor.fetchone()

        cursor.close()
        conn.close()
        return item

    def agregar_item(self, sku: str, nombre: str, cantidad: int, precio: float) -> Dict:
        conn = get_connection()
        if not conn:
            return {}

        cursor = conn.cursor(dictionary=True)
        query = """
            INSERT INTO products (sku, nombre, cantidad, precio, is_active)
            VALUES (%s, %s, %s, %s, 1)
        """
        cursor.execute(query, (sku, nombre, cantidad, precio))
        conn.commit()

        new_id = cursor.lastrowid

        cursor.close()
        conn.close()

        return {
            "id": new_id,
            "sku": sku,
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
            "is_active": 1
        }

    def actualizar_item(self, item_id: int, sku: str, nombre: str, cantidad: int, precio: float) -> bool:
        conn = get_connection()
        if not conn:
            return False

        cursor = conn.cursor()
        query = """
            UPDATE products
            SET sku = %s, nombre = %s, cantidad = %s, precio = %s
            WHERE id = %s
        """
        cursor.execute(query, (sku, nombre, cantidad, precio, item_id))
        conn.commit()

        ok = cursor.rowcount > 0

        cursor.close()
        conn.close()
        return ok

    def actualizar_cantidad(self, item_id: int, cantidad: int) -> bool:
        conn = get_connection()
        if not conn:
            return False

        cursor = conn.cursor()
        query = "UPDATE products SET cantidad = %s WHERE id = %s"
        cursor.execute(query, (cantidad, item_id))
        conn.commit()

        ok = cursor.rowcount > 0

        cursor.close()
        conn.close()
        return ok

    def eliminar_item(self, item_id: int) -> bool:
        conn = get_connection()
        if not conn:
            return False

        cursor = conn.cursor()
        query = """
            UPDATE products
            SET is_active = 0
            WHERE id = %s
        """
        cursor.execute(query, (item_id,))
        conn.commit()

        ok = cursor.rowcount > 0

        cursor.close()
        conn.close()
        return ok