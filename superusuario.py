class SuperUsuario(Administrador):
    def __init__(self, db: JSONDB):
        super().__init__(db)
        self.usuarios._sesion_id = self._asegurar_superusuario()

    def _scenario_superusr(self):
        """Retorna los usuarios con rol superusuario"""
        if not self.db.data["usuarios"]:
            raise RuntimeError("No hay usuarios registrados.")
        
        for uid, u in self.db.data["usuarios"].items():
            if u.get("rol") == "superusuario":
                return int(uid)
        uid = self.db.allocate_user_id()
        sup = Usuario(uid, "SuperUser", "super@sys.com", "superusuario").to_dict()
        self.db.data["usuarios"][str(uid)] = sup
        self.db.save()
        return uid

    def _asegurar_superusuario(self):
        """Forzar a que la sesión sea de un superusuario."""
        try:
            return self._scenario_superusr()
        except Exception as e:
            raise RuntimeError(f"No se pudo asegurar sesión de superusuario: {e}")


    def crear_usuario(self, nombre: str, email: str, tipo: str = "usuario") -> Usuario:
        """Crea un usuario sin restricciones de tipo o rol."""
        uid = self.db.allocate_user_id()
        u = Usuario(uid, nombre, email, tipo)
        self.db.data["usuarios"][str(uid)] = u.to_dict()
        self.db.save()
        self.actividad.anotar("superusuario", "crear_usuario", f"{u.id}:{u.rol}")
        return u

    def borrar_usuario(self, user_id: int):
        """Borra un usuario aunque sea administrador o superusuario."""
        u = self.db.data["usuarios"].get(str(user_id))
        if not u:
            raise ReglasNegocioError("Usuario inexistente.")
        del self.db.data["usuarios"][str(user_id)]
        self.db.save()
        self.actividad.anotar("superusuario", "borrar_usuario", str(user_id))
