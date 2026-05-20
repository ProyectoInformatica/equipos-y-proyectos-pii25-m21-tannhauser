"""
Gestión de sesión mínima para la app: mantiene el usuario actual en memoria.
Utilidad: controlar permisos de acceso por ruta mientras la app está abierta.
"""

_current_user = None


def set_current_user(user):
    global _current_user
    _current_user = user


def get_current_user():
    return _current_user


def clear_current_user():
    global _current_user
    _current_user = None


def get_panel_route_for_current_user():
    """Return the correct panel route for the currently logged-in user.
    Falls back to root ('/') if no user or unknown role.
    """
    user = get_current_user()
    if not user:
        return "/"
    rol = user.get("rol")
    if rol == "empleado":
        return "/panel_empleado"
    if rol == "administrador":
        return "/panel_admin"
    if rol == "superusuario":
        return "/panel_super"
    if rol == "cliente":
        return "/panel_usuario"
    return "/"
