import flet as ft
from controllers.auth_controller import AuthController
from models.session_manager import set_current_user


def LoginUnificadoView(page: ft.Page, go):
    auth = AuthController()
    mensaje = ft.Text("", color="#FF7B7B", size=14)

    def ruta_por_rol(usuario):
        rol = (usuario.get("rol") or "").strip().lower()

        if rol == "cliente":
            return "/panel_usuario"
        elif rol == "empleado":
            return "/panel_empleado"
        elif rol == "administrador":
            return "/panel_admin"
        elif rol == "superusuario":
            return "/panel_super"
        return None

    def iniciar_sesion(e):
        correo = (email.value or "").strip().lower()
        clave = (password.value or "").strip()

        if not correo or not clave:
            mensaje.value = "Introduce correo y contraseña."
            page.update()
            return

        usuario = auth.login(correo, clave)

        if not usuario:
            mensaje.value = "Correo o contraseña incorrectos."
            page.update()
            return

        destino = ruta_por_rol(usuario)
        if not destino:
            mensaje.value = "Tu cuenta no tiene un rol válido."
            page.update()
            return

        mensaje.value = ""
        set_current_user(usuario)
        go(destino)

    email = ft.TextField(
        label="Correo electrónico",
        hint_text="Introduce tu correo",
        prefix_icon=ft.Icons.EMAIL_OUTLINED,
        width=380,
        height=58,
        border_radius=18,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
        border_color="#2C4E86",
        focused_border_color="#5FD1FF",
        color=ft.Colors.WHITE,
        text_size=15,
        on_submit=iniciar_sesion,
    )

    password = ft.TextField(
        label="Contraseña",
        hint_text="Introduce tu contraseña",
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        password=True,
        can_reveal_password=True,
        width=380,
        height=58,
        border_radius=18,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
        border_color="#2C4E86",
        focused_border_color="#5FD1FF",
        color=ft.Colors.WHITE,
        text_size=15,
        on_submit=iniciar_sesion,
    )

    panel_izquierdo = ft.Container(
        expand=True,
        content=ft.Column(
            [
                ft.Image(
                    src="assets/logo_tannhauser.png",
                    width=220,
                    height=220,
                    fit=ft.BoxFit.CONTAIN,
                ),
                ft.Text(
                    "Tannhauser",
                    size=42,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                ft.Text(
                    "Accede a tu cuenta para consultar inventario, monitorización, actividad y gestión del supermercado inteligente.",
                    size=16,
                    color=ft.Colors.WHITE70,
                    width=500,
                    text_align=ft.TextAlign.LEFT,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=14,
        ),
    )

    tarjeta_login = ft.Container(
        width=470,
        padding=36,
        border_radius=30,
        bgcolor=ft.Colors.with_opacity(0.14, ft.Colors.BLACK),
        border=ft.Border.all(1.2, ft.Colors.with_opacity(0.22, ft.Colors.WHITE)),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=30,
            color=ft.Colors.with_opacity(0.18, ft.Colors.BLACK),
            offset=ft.Offset(0, 10),
        ),
        content=ft.Column(
            [
                ft.Text(
                    "Iniciar sesión",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                ft.Text(
                    "Acceso único para clientes, empleados y administración.",
                    size=14,
                    color=ft.Colors.WHITE70,
                ),
                ft.Container(height=8),
                email,
                password,
                mensaje,
                ft.Container(height=4),
                ft.Button(
                    "Entrar",
                    icon=ft.Icons.ARROW_FORWARD_ROUNDED,
                    width=380,
                    height=54,
                    bgcolor="#5FD1FF",
                    color=ft.Colors.BLACK,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=18),
                    ),
                    on_click=iniciar_sesion,
                ),
                ft.Row(
                    [
                        ft.TextButton(
                            "Volver al inicio",
                            icon=ft.Icons.ARROW_BACK_ROUNDED,
                            on_click=lambda e: go("/"),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=14,
        ),
    )

    contenido = ft.Container(
        expand=True,
        padding=40,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=[
                "#071018",
                "#10233F",
                "#0F2A4F",
                "#153969",
            ],
        ),
        content=ft.Row(
            [
                panel_izquierdo,
                tarjeta_login,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    return ft.View(
        route="/login",
        controls=[contenido],
        padding=0,
        spacing=0,
    )