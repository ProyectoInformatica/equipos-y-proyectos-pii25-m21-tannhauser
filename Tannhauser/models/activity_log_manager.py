from models.db import get_connection


class ActivityLogManager:
    def registrar(self, user_email: str, action: str) -> bool:
        user_email = (user_email or "").strip().lower()
        action = (action or "").strip()

        if not action:
            return False

        conn = get_connection()
        if not conn:
            return False

        cursor = conn.cursor(dictionary=True)

        user_id = None
        if user_email:
            cursor.execute(
                "SELECT id FROM users WHERE LOWER(email) = %s LIMIT 1",
                (user_email,)
            )
            row = cursor.fetchone()
            if row:
                user_id = row["id"]

        mensaje = f"Acción registrada: {action}"
        metadata = '{"origen": "app"}'

        query = """
            INSERT INTO activity_log (user_id, log_level, action, message, logged_at, metadata)
            VALUES (%s, 'INFO', %s, %s, NOW(6), %s)
        """
        cursor.execute(query, (user_id, action.lower(), mensaje, metadata))
        conn.commit()

        ok = cursor.rowcount > 0

        cursor.close()
        conn.close()
        return ok