from models.session_manager import get_current_user


def ruta_dashboard_por_rol():
    usuario = get_current_user() or {}
    rol = (usuario.get("rol") or "").strip().lower()

    if rol == "superusuario":
        return "/panel_super"
    if rol == "administrador":
        return "/panel_admin"
    if rol == "empleado":
        return "/panel_empleado"
    if rol == "cliente":
        return "/panel_usuario"
    return "/"