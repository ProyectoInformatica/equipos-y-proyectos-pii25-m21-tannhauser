import os
import shutil
import time
from mysql.connector import Error
from models.db import get_connection


class ProfileController:
    def __init__(self):
        self.profile_dir = os.path.join("assets", "profile_images")
        os.makedirs(self.profile_dir, exist_ok=True)

    def _guardar_imagen(self, source_path: str):
        if not source_path or not os.path.exists(source_path):
            return None

        _, ext = os.path.splitext(source_path)
        if not ext:
            ext = ".png"

        filename = f"profile_{int(time.time() * 1000)}{ext}"
        destino = os.path.join(self.profile_dir, filename)
        shutil.copy(source_path, destino)

        return f"profile_images/{filename}"

    def obtener_usuario(self, user_id: int):
        conn = get_connection()
        if not conn:
            return None

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT
                    u.id,
                    u.nombre,
                    u.email,
                    u.profile_image,
                    LOWER(r.name) AS rol
                FROM users u
                JOIN roles r ON r.id = u.role_id
                WHERE u.id = %s
                LIMIT 1
            """, (user_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error obteniendo usuario: {e}")
            return None
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def actualizar_foto_perfil(self, user_id: int, source_path: str):
        ruta_relativa = self._guardar_imagen(source_path)
        if not ruta_relativa:
            return False, "No se pudo guardar la imagen."

        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar a la base de datos."

        cursor = None
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE users
                SET profile_image = %s,
                    updated_at = NOW()
                WHERE id = %s
            """, (ruta_relativa, user_id))
            conn.commit()
            return True, "Foto de perfil actualizada correctamente."
        except Error as e:
            if conn:
                conn.rollback()
            print(f"Error actualizando foto: {e}")
            return False, f"Error al actualizar foto: {e}"
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()