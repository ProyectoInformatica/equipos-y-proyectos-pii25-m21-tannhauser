import flet as ft
from controllers.auth_controller import AuthController
from models.session_manager import set_current_user


def LoginSuperView(page: ft.Page, go):
    auth = AuthController()

    email = ft.TextField(
        label="Correo del Superusuario",
        prefix_icon=ft.Icons.EMAIL,
        border_radius=12,
        border_color=ft.Colors.PURPLE_300,
        focused_border_color=ft.Colors.PURPLE_400,
        width=350,
    )
    password = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        border_radius=12,
        border_color=ft.Colors.PURPLE_300,
        focused_border_color=ft.Colors.PURPLE_400,
        width=350,
    )
    mensaje = ft.Text("", color=ft.Colors.RED_300)

    def intentar_login(e):
        usuario = auth.login(email.value, password.value)
        if not usuario:
            mensaje.value = "Correo o contraseña incorrectos."
        elif usuario.get("rol") != "superusuario":
            mensaje.value = "Este usuario no tiene rol de superusuario."
        else:
            mensaje.value = ""
            set_current_user(usuario)
            go("/panel_super")
        page.update()

    card = ft.Container(
        width=500,
        padding=30,
        border_radius=20,
        bgcolor=ft.Colors.with_opacity(0.9, ft.Colors.BLUE_GREY_900),
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.Colors.DEEP_PURPLE_900,
            offset=ft.Offset(0, 4),
        ),
        content=ft.Column(
            [
                ft.Text("Acceso Superusuario", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_100),
                ft.Text("Configuración global del sistema.", size=14, color=ft.Colors.GREY_400),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                email,
                password,
                mensaje,
                ft.Container(height=10),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Entrar",
                            icon=ft.Icons.SUPERVISED_USER_CIRCLE,
                            width=180,
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.DEFAULT: ft.Colors.PURPLE_400},
                                color={ft.ControlState.DEFAULT: ft.Colors.BLACK},
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=intentar_login,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.TextButton(
                            "Volver al inicio",
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: go("/"),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ],
            spacing=12,
        ),
    )

    fondo = ft.Container(
        expand=True,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=[ft.Colors.DEEP_PURPLE_900, ft.Colors.BLACK],
        ),
        content=ft.Column(
            [
                card
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    return ft.View(
        route="/login_super",
        controls=[fondo],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )

