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

    def register(
        self,
        nombre: str,
        email: str,
        password: str,
        rol: str = "cliente",
        actor_rol: str = "cliente",
        profile_image: str = None,
    ):
        ok, msg = self.manager.registrar(
            nombre=nombre,
            email=email,
            password=password,
            rol=rol,
            actor_rol=actor_rol,
            profile_image=profile_image,
        )
        if ok:
            self.fm.registrar_actividad(email, "REGISTER")
        return ok, msg