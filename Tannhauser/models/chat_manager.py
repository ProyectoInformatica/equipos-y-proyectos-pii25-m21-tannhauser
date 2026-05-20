from models.db import get_connection

class ChatManager:
    def get_users_for_chat(self, exclude_user_id):
        """Obtiene la lista de usuarios con los que se puede chatear, excluyendo al actual."""
        conn = get_connection()
        if not conn: return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, nombre, email, role_id FROM users WHERE id != %s AND is_active = 1", (exclude_user_id,))
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return users

    def get_messages(self, user1_id, user2_id):
        """Obtiene el historial de chat entre dos usuarios."""
        conn = get_connection()
        if not conn: return []
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT sender_id, message, DATE_FORMAT(created_at, '%H:%i') as hora
            FROM chat_messages 
            WHERE (sender_id = %s AND receiver_id = %s) OR (sender_id = %s AND receiver_id = %s)
            ORDER BY created_at ASC
        """
        cursor.execute(query, (user1_id, user2_id, user2_id, user1_id))
        msgs = cursor.fetchall()
        cursor.close()
        conn.close()
        return msgs

    def save_message(self, sender_id, receiver_id, message):
        """Guarda un nuevo mensaje en la base de datos."""
        conn = get_connection()
        if not conn: return False
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO chat_messages (sender_id, receiver_id, message) VALUES (%s, %s, %s)",
            (sender_id, receiver_id, message)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True