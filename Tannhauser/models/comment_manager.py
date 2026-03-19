from typing import List, Dict
from models.db import get_connection


class CommentManager:
    def listar(self) -> List[Dict]:
        conn = get_connection()
        if not conn:
            return []

        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT
                id,
                user_id,
                usuario_alias,
                texto,
                created_at
            FROM comments
            ORDER BY created_at DESC, id DESC
        """
        cursor.execute(query)
        comentarios = cursor.fetchall()

        cursor.close()
        conn.close()
        return comentarios

    def agregar(self, user_id, usuario_alias: str, texto: str) -> bool:
        usuario_alias = (usuario_alias or "Anónimo").strip()
        texto = (texto or "").strip()

        if not texto:
            return False

        conn = get_connection()
        if not conn:
            return False

        cursor = conn.cursor()
        query = """
            INSERT INTO comments (user_id, usuario_alias, texto, created_at)
            VALUES (%s, %s, %s, NOW())
        """
        cursor.execute(query, (user_id, usuario_alias, texto))
        conn.commit()

        ok = cursor.rowcount > 0

        cursor.close()
        conn.close()
        return ok