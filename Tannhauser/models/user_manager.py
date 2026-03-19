from typing import List, Dict, Optional, Tuple
from models.db import get_connection


class UserManager:
    def listar(self) -> List[Dict]:
        conn = get_connection()
        if not conn:
            return []

        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT
                u.id,
                u.role_id,
                LOWER(r.name) AS rol,
                u.nombre,
                u.email,
                u.password_hash,
                u.is_active
            FROM users u
            JOIN roles r ON u.role_id = r.id
            ORDER BY u.id
        """
        cursor.execute(query)
        users = cursor.fetchall()

        cursor.close()
        conn.close()
        return users

    def autenticar(self, email: str, password: str) -> Optional[Dict]:
        email = email.lower().strip()
        password = password.strip()

        conn = get_connection()
        if not conn:
            return None

        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT
                u.id,
                u.role_id,
                LOWER(r.name) AS rol,
                u.nombre,
                u.email,
                u.password_hash,
                u.is_active
            FROM users u
            JOIN roles r ON u.role_id = r.id
            WHERE LOWER(u.email) = %s
              AND u.is_active = 1
            LIMIT 1
        """
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and user["password_hash"] == password:
            user["rol"] = user["rol"].strip().lower()
            return user

        return None

    def registrar(self, nombre: str, email: str, password: str, rol: str = "cliente") -> Tuple[bool, str]:
        nombre = nombre.strip()
        email = email.lower().strip()
        password = password.strip()
        rol = rol.strip().lower()

        if not nombre or not email or not password or not rol:
            return False, "Completa todos los campos."

        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar a la base de datos."

        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT id FROM users WHERE LOWER(email) = %s", (email,))
        existente = cursor.fetchone()
        if existente:
            cursor.close()
            conn.close()
            return False, "Correo ya registrado."

        cursor.execute("SELECT id FROM roles WHERE LOWER(name) = %s LIMIT 1", (rol,))
        role_row = cursor.fetchone()
        if not role_row:
            cursor.close()
            conn.close()
            return False, f"Rol no válido: {rol}"

        query = """
            INSERT INTO users (role_id, nombre, email, password_hash, is_active)
            VALUES (%s, %s, %s, %s, 1)
        """
        cursor.execute(query, (role_row["id"], nombre, email, password))
        conn.commit()

        cursor.close()
        conn.close()
        return True, "Usuario registrado."

    def eliminar(self, email: str) -> Tuple[bool, str]:
        email = email.lower().strip()

        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar a la base de datos."

        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE LOWER(email) = %s", (email,))
        conn.commit()

        if cursor.rowcount == 0:
            cursor.close()
            conn.close()
            return False, "El usuario no existe."

        cursor.close()
        conn.close()
        return True, "Usuario eliminado."