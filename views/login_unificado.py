import flet as ft
from controllers.auth_controller import AuthController
from models.session_manager import set_current_user


def LoginUnificadoView(page: ft.Page, go):
    auth = AuthController()
    mensaje = ft.Text("", color="#FF9B9B", size=13, weight=ft.FontWeight.W_600)

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
        height=60,
        border_radius=16,
        bgcolor=ft.Colors.with_opacity(0.07, ft.Colors.WHITE),
        border_color=ft.Colors.with_opacity(0.18, ft.Colors.WHITE),
        focused_border_color="#C8F3FF",
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
        height=60,
        border_radius=16,
        bgcolor=ft.Colors.with_opacity(0.07, ft.Colors.WHITE),
        border_color=ft.Colors.with_opacity(0.18, ft.Colors.WHITE),
        focused_border_color="#C8F3FF",
        color=ft.Colors.WHITE,
        text_size=15,
        on_submit=iniciar_sesion,
    )

    logo_premium = ft.Container(
        width=208,
        height=208,
        border_radius=104,
        padding=18,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
        bgcolor=ft.Colors.with_opacity(0.94, ft.Colors.WHITE),
        border=ft.border.all(1.4, ft.Colors.with_opacity(0.40, ft.Colors.CYAN_100)),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=38,
            color=ft.Colors.with_opacity(0.28, ft.Colors.CYAN_200),
            offset=ft.Offset(0, 18),
        ),
        content=ft.Image(
            src="logo_tannhauser.png",
            fit=ft.ImageFit.CONTAIN,
        ),
    )

    panel_izquierdo = ft.Container(
        expand=True,
        content=ft.Column(
            [
                logo_premium,
                ft.Container(height=10),
                ft.Container(
                    padding=ft.Padding(12, 6, 12, 6),
                    border_radius=999,
                    bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.CYAN_100),
                    border=ft.border.all(1, ft.Colors.with_opacity(0.16, ft.Colors.CYAN_100)),
                    content=ft.Text(
                        "Supermercado inteligente",
                        size=12,
                        weight=ft.FontWeight.BOLD,
                        color="#BFF6FF",
                    ),
                ),
                ft.Text(
                    "Tannhauser",
                    size=52,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                ft.Text(
                    "Accede a tu cuenta para consultar inventario, monitorización, actividad y gestión del supermercado inteligente.",
                    size=17,
                    color=ft.Colors.with_opacity(0.78, ft.Colors.WHITE),
                    width=540,
                    text_align=ft.TextAlign.LEFT,
                ),
                ft.Container(
                    width=84,
                    height=3,
                    border_radius=999,
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment(-1, 0),
                        end=ft.Alignment(1, 0),
                        colors=["#C8F3FF", "#67E8F9", "#2B6CB0"],
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            spacing=16,
        ),
    )

    tarjeta_login = ft.Container(
        width=492,
        padding=ft.Padding(40, 38, 40, 34),
        border_radius=28,
        bgcolor="#081421",
        border=ft.border.all(1.1, ft.Colors.with_opacity(0.18, ft.Colors.WHITE)),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=46,
            color=ft.Colors.with_opacity(0.36, ft.Colors.BLACK),
            offset=ft.Offset(0, 22),
        ),
        content=ft.Column(
            [
                ft.Container(
                    width=56,
                    height=5,
                    border_radius=999,
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment(-1, 0),
                        end=ft.Alignment(1, 0),
                        colors=["#FFFFFF", "#67E8F9"],
                    ),
                ),
                ft.Text(
                    "Iniciar sesión",
                    size=34,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                ft.Text(
                    "Acceso único para clientes, empleados y administración.",
                    size=15,
                    color=ft.Colors.with_opacity(0.68, ft.Colors.WHITE),
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=10),
                email,
                password,
                mensaje,
                ft.Container(height=2),
                ft.ElevatedButton(
                    "Entrar",
                    icon=ft.Icons.ARROW_FORWARD_ROUNDED,
                    width=380,
                    height=56,
                    bgcolor="#C8F3FF",
                    color="#06111D",
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=16),
                        elevation=8,
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
            spacing=15,
        ),
    )

    contenido = ft.Container(
        expand=True,
        padding=ft.Padding(64, 44, 64, 44),
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=[
                "#030712",
                "#06111D",
                "#0A1C2D",
                "#12385C",
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
