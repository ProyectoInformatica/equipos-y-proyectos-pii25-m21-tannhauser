import os
import shutil
import time
from typing import List, Dict, Optional, Tuple
from models.db import get_connection


class UserManager:
    def _guardar_imagen_perfil(self, source_path: str) -> Optional[str]:
        if not source_path or not os.path.exists(source_path):
            return None

        carpeta = os.path.join("assets", "profile_images")
        os.makedirs(carpeta, exist_ok=True)

        _, ext = os.path.splitext(source_path)
        if not ext:
            ext = ".png"

        filename = f"profile_{int(time.time() * 1000)}{ext}"
        destino = os.path.join(carpeta, filename)
        shutil.copy(source_path, destino)

        return f"profile_images/{filename}".replace("\\", "/")

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
                u.profile_image,
                u.is_active,
                u.created_at,
                u.updated_at,
                u.deactivated_at,
                u.last_login_at
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
                u.profile_image,
                u.is_active,
                u.created_at,
                u.updated_at,
                u.deactivated_at,
                u.last_login_at
            FROM users u
            JOIN roles r ON u.role_id = r.id
            WHERE LOWER(u.email) = %s
              AND u.password_hash = SHA2(%s, 256)
              AND u.is_active = 1
            LIMIT 1
        """
        cursor.execute(query, (email, password))
        user = cursor.fetchone()

        if user:
            cursor.execute(
                "UPDATE users SET last_login_at = NOW(), updated_at = NOW() WHERE id = %s",
                (user["id"],)
            )
            conn.commit()
            user["rol"] = user["rol"].strip().lower()

        cursor.close()
        conn.close()
        return user

    def registrar(
        self,
        nombre: str,
        email: str,
        password: str,
        rol: str = "cliente",
        profile_image_path: str = None
    ) -> Tuple[bool, str]:
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

        cursor.execute(
            "SELECT id FROM users WHERE LOWER(email) = %s LIMIT 1",
            (email,)
        )
        existente = cursor.fetchone()
        if existente:
            cursor.close()
            conn.close()
            return False, "Correo ya registrado."

        cursor.execute(
            "SELECT id FROM roles WHERE LOWER(code) = %s OR LOWER(name) = %s LIMIT 1",
            (rol, rol)
        )
        role_row = cursor.fetchone()
        if not role_row:
            cursor.close()
            conn.close()
            return False, f"Rol no válido: {rol}"

        profile_image = self._guardar_imagen_perfil(profile_image_path)

        query = """
            INSERT INTO users (
                role_id,
                nombre,
                email,
                password_hash,
                profile_image,
                is_active,
                created_at,
                updated_at
            )
            VALUES (%s, %s, %s, SHA2(%s, 256), %s, 1, NOW(), NOW())
        """
        cursor.execute(query, (role_row["id"], nombre, email, password, profile_image))
        conn.commit()

        cursor.close()
        conn.close()
        return True, "Usuario registrado."

    def obtener_por_email(self, email: str) -> Optional[Dict]:
        email = email.lower().strip()

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
                u.profile_image,
                u.is_active,
                u.created_at,
                u.updated_at,
                u.deactivated_at,
                u.last_login_at
            FROM users u
            JOIN roles r ON u.role_id = r.id
            WHERE LOWER(u.email) = %s
            LIMIT 1
        """
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()
        return user

    def buscar_por_nombre(self, nombre: str) -> List[Dict]:
        nombre = nombre.lower().strip()

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
                u.profile_image,
                u.is_active,
                u.created_at,
                u.updated_at,
                u.deactivated_at,
                u.last_login_at
            FROM users u
            JOIN roles r ON u.role_id = r.id
            WHERE LOWER(u.nombre) LIKE %s
            ORDER BY u.nombre, u.id
        """
        cursor.execute(query, (f"%{nombre}%",))
        users = cursor.fetchall()

        cursor.close()
        conn.close()
        return users

    def eliminar(self, email: str) -> Tuple[bool, str]:
        email = email.lower().strip()

        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar a la base de datos."

        cursor = conn.cursor()
        query = """
            UPDATE users
            SET is_active = 0,
                deactivated_at = NOW(),
                updated_at = NOW()
            WHERE LOWER(email) = %s
              AND is_active = 1
        """
        cursor.execute(query, (email,))
        conn.commit()

        if cursor.rowcount == 0:
            cursor.close()
            conn.close()
            return False, "El usuario no existe o ya está dado de baja."

        cursor.close()
        conn.close()
        return True, "Usuario dado de baja correctamente."