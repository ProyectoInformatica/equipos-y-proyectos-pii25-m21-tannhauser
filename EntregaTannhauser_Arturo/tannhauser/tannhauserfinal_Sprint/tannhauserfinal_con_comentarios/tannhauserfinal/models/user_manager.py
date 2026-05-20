from typing import List, Dict, Optional, Tuple
from models.db import get_connection


class UserManager:
    def _has_column(self, cursor, column_name: str) -> bool:
        cursor.execute("SHOW COLUMNS FROM users LIKE %s", (column_name,))
        return cursor.fetchone() is not None

    def _ensure_column(self, cursor, conn, column_name: str, definition: str) -> None:
        if not self._has_column(cursor, column_name):
            cursor.execute(f"ALTER TABLE users ADD COLUMN {column_name} {definition}")
            conn.commit()

    def _ensure_user_columns(self, cursor, conn) -> None:
        self._ensure_column(cursor, conn, "last_login_at", "DATETIME DEFAULT NULL")
        self._ensure_column(cursor, conn, "deactivated_at", "DATETIME DEFAULT NULL")

    def _select_column(self, cursor, column_name: str) -> str:
        if self._has_column(cursor, column_name):
            return f"u.{column_name},"
        return f"NULL AS {column_name},"

    def listar(self) -> List[Dict]:
        conn = get_connection()
        if not conn:
            return []

        cursor = conn.cursor(dictionary=True)
        self._ensure_user_columns(cursor, conn)
        query = f"""
            SELECT
                u.id,
                u.role_id,
                LOWER(r.code) AS rol_code,
                LOWER(r.name) AS rol,
                u.nombre,
                u.email,
                u.password_hash,
                u.is_active,
                u.created_at,
                u.updated_at,
                {self._select_column(cursor, 'deactivated_at')}
                {self._select_column(cursor, 'last_login_at')}
                u.profile_image
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
        self._ensure_user_columns(cursor, conn)
        query = f"""
            SELECT
                u.id,
                u.role_id,
                LOWER(r.code) AS rol_code,
                LOWER(r.name) AS rol,
                u.nombre,
                u.email,
                u.password_hash,
                u.is_active,
                u.created_at,
                u.updated_at,
                {self._select_column(cursor, 'deactivated_at')}
                {self._select_column(cursor, 'last_login_at')}
                u.profile_image
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
            if self._has_column(cursor, "last_login_at"):
                cursor.execute(
                    "UPDATE users SET last_login_at = NOW(), updated_at = NOW() WHERE id = %s",
                    (user["id"],)
                )
            else:
                cursor.execute(
                    "UPDATE users SET updated_at = NOW() WHERE id = %s",
                    (user["id"],)
                )
            conn.commit()
            user["rol"] = (user["rol"] or "").strip().lower()
            user["rol_code"] = (user["rol_code"] or "").strip().lower()

        cursor.close()
        conn.close()
        return user

    def _roles_permitidos_para_actor(self, actor_rol: str) -> List[str]:
        actor_rol = (actor_rol or "").strip().lower()

        if actor_rol == "superusuario":
            return ["cliente", "empleado", "administrador"]

        if actor_rol == "administrador":
            return ["cliente", "empleado"]

        return ["cliente"]

    def registrar(
        self,
        nombre: str,
        email: str,
        password: str,
        rol: str = "cliente",
        actor_rol: str = "cliente",
        profile_image: Optional[str] = None,
    ) -> Tuple[bool, str]:
        nombre = nombre.strip()
        email = email.lower().strip()
        password = password.strip()
        rol = rol.strip().lower()
        actor_rol = actor_rol.strip().lower()

        if not nombre or not email or not password or not rol:
            return False, "Completa todos los campos."

        roles_permitidos = self._roles_permitidos_para_actor(actor_rol)
        if rol not in roles_permitidos:
            return False, "No tienes permisos para crear ese tipo de usuario."

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

        query = """
            INSERT INTO users (
                role_id,
                nombre,
                email,
                password_hash,
                is_active,
                created_at,
                updated_at,
                profile_image
            )
            VALUES (%s, %s, %s, SHA2(%s, 256), 1, NOW(), NOW(), %s)
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
        self._ensure_user_columns(cursor, conn)
        query = f"""
            SELECT
                u.id,
                u.role_id,
                LOWER(r.code) AS rol_code,
                LOWER(r.name) AS rol,
                u.nombre,
                u.email,
                u.is_active,
                u.created_at,
                u.updated_at,
                {self._select_column(cursor, 'deactivated_at')}
                {self._select_column(cursor, 'last_login_at')}
                u.profile_image
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
        self._ensure_user_columns(cursor, conn)
        query = f"""
            SELECT
                u.id,
                u.role_id,
                LOWER(r.code) AS rol_code,
                LOWER(r.name) AS rol,
                u.nombre,
                u.email,
                u.is_active,
                u.created_at,
                u.updated_at,
                {self._select_column(cursor, 'deactivated_at')}
                {self._select_column(cursor, 'last_login_at')}
                u.profile_image
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
        self._ensure_user_columns(cursor, conn)
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