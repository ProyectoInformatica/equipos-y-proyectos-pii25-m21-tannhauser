from models.user_manager import UserManager
from models.file_manager import FileManager


class UserController:
    """Controlador de usuarios para paneles y administración"""

    def __init__(self):
        self.manager = UserManager()
        self.fm = FileManager()

    # ---- Métodos originales del proyecto ----
    def listar(self):
        return self.manager.listar()

    def eliminar(self, email: str, actor: str = None):
        ok, msg = self.manager.eliminar(email)
        if ok:
            actor_label = actor if actor else email
            self.fm.registrar_actividad(actor_label, f"ELIMINAR_USUARIO target={email}")
        return ok, msg

    # ---- Métodos extra para vistas nuevas ----
    def obtener_usuarios(self):
        """Devuelve la lista completa de usuarios"""
        return self.manager.listar()

    def buscar_por_email(self, email: str):
        email = email.lower().strip()
        for u in self.manager.listar():
            if u["email"].lower() == email:
                return u
        return None

    def buscar_por_nombre(self, nombre: str):
        nombre = nombre.lower().strip()
        encontrados = [u for u in self.manager.listar() if nombre in u.get("nombre", "").lower()]
        return encontrados

    def eliminar_por_nombre(self, nombre: str):
        encontrados = self.buscar_por_nombre(nombre)
        if not encontrados:
            return False, "Usuario no encontrado por nombre."
        if len(encontrados) > 1:
            # Si hay múltiples coincidencias, pedimos claridad por email
            emails = ", ".join([u["email"] for u in encontrados])
            return False, f"Varios usuarios coinciden con ese nombre. Especifica email: {emails}"
        # única coincidencia: eliminar por email
        email = encontrados[0]["email"]
        return self.eliminar(email)

    def login(self, email: str, password: str):
        """Login simple usando UserManager (no reemplaza AuthController)."""
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
        # mantiene compatibilidad: permite pasar actor en el futuro
        return self.eliminar(email)
