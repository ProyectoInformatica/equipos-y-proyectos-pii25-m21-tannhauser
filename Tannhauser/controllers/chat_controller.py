from models.chat_manager import ChatManager
from models.session_manager import get_current_user

class ChatController:
    def __init__(self):
        self.manager = ChatManager()
        self.current_user = get_current_user()

    def obtener_contactos(self):
        if not self.current_user: return []
        return self.manager.get_users_for_chat(self.current_user['id'])

    def cargar_historial(self, receiver_id):
        if not self.current_user: return []
        return self.manager.get_messages(self.current_user['id'], receiver_id)

    def enviar_mensaje(self, receiver_id, texto):
        if not self.current_user or not texto.strip(): return False
        return self.manager.save_message(self.current_user['id'], receiver_id, texto.strip())