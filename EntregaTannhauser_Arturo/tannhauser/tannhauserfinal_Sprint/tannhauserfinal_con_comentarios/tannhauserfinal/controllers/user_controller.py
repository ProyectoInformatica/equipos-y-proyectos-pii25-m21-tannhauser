from models.user_manager import UserManager
from models.file_manager import FileManager


class UserController:
    def __init__(self):
        self.manager = UserManager()
        self.fm = FileManager()

    def listar(self):
        return self.manager.listar()

    def obtener_usuarios(self):
        return self.manager.listar()

    def buscar_por_email(self, email: str):
        return self.manager.obtener_por_email(email)

    def buscar_por_nombre(self, nombre: str):
        return self.manager.buscar_por_nombre(nombre)

    def eliminar(self, email: str, actor: str = None):
        user = self.manager.obtener_por_email(email)
        if not user:
            return False, "El usuario no existe."

        ok, msg = self.manager.eliminar(email)
        if ok:
            actor_label = actor if actor else email
            self.fm.registrar_actividad(actor_label, f"BAJA_USUARIO target={email}")
        return ok, msg

    def eliminar_por_nombre(self, nombre: str):
        encontrados = self.manager.buscar_por_nombre(nombre)
        if not encontrados:
            return False, "Usuario no encontrado por nombre."
        if len(encontrados) > 1:
            emails = ", ".join([u["email"] for u in encontrados])
            return False, f"Varios usuarios coinciden con ese nombre. Especifica email: {emails}"
        return self.eliminar(encontrados[0]["email"])

    def login(self, email: str, password: str):
        user = self.manager.autenticar(email, password)
        if user:
            self.fm.registrar_actividad(user["email"], "LOGIN")
        return user

    def crear_usuario(self, nombre, email, password, rol):
        ok, msg = self.manager.registrar(nombre, email, password, rol)
        if ok:
            self.fm.registrar_actividad(email, "CREAR_USUARIO")
        return ok, msg

    def eliminar_usuario(self, email):
        return self.eliminar(email)