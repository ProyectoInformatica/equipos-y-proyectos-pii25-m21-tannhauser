from models.user_manager import UserManager
from models.file_manager import FileManager


class AuthController:
    def __init__(self):
        self.manager = UserManager()
        self.fm = FileManager()

    def login(self, email: str, password: str):
        user = self.manager.autenticar(email, password)
        if user:
            self.fm.registrar_actividad(user["email"], "LOGIN")
        return user

    def register(self, nombre: str, email: str, password: str):
        ok, msg = self.manager.registrar(nombre, email, password)
        if ok:
            self.fm.registrar_actividad(email, "REGISTER")
        return ok, msg
