import flet as ft
from controllers.auth_controller import AuthController


def RegistroView(page: ft.Page, go):
    auth = AuthController()

    nombre = ft.TextField(
        label="Nombre completo",
        prefix_icon=ft.Icons.PERSON,
        border_radius=12,
        border_color=ft.Colors.CYAN_300,
        focused_border_color=ft.Colors.LIGHT_BLUE_400,
        width=350,
    )
    email = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL,
        border_radius=12,
        border_color=ft.Colors.CYAN_300,
        focused_border_color=ft.Colors.LIGHT_BLUE_400,
        width=350,
    )
    password = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        border_radius=12,
        border_color=ft.Colors.CYAN_300,
        focused_border_color=ft.Colors.LIGHT_BLUE_400,
        width=350,
    )
    password2 = ft.TextField(
        label="Repetir contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        border_radius=12,
        border_color=ft.Colors.CYAN_300,
        focused_border_color=ft.Colors.LIGHT_BLUE_400,
        width=350,
    )

    mensaje = ft.Text("", color=ft.Colors.RED_300)

    def registrar(e):
        if password.value != password2.value:
            mensaje.value = "Las contraseñas no coinciden."
            page.update()
            return

        ok, msg = auth.register(nombre.value, email.value, password.value)
        if ok:
            page.snack_bar = ft.SnackBar(ft.Text(msg))
            page.snack_bar.open = True
            go("/login_user")
        else:
            mensaje.value = msg
        page.update()

    card = ft.Container(
        width=550,
        padding=30,
        border_radius=20,
        bgcolor=ft.Colors.with_opacity(0.95, ft.Colors.BLUE_GREY_900),
        shadow=ft.BoxShadow(
            spread_radius=2,
            blur_radius=10,
            color=ft.Colors.CYAN_900,
            offset=ft.Offset(0, 4),
        ),
        content=ft.Column(
            [
                ft.Text("Registro de Cliente", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_100),
                ft.Text("Crea tu cuenta para acceder como cliente.", size=14, color=ft.Colors.GREY_400),
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                nombre,
                email,
                password,
                password2,
                mensaje,
                ft.Container(height=10),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Registrarse",
                            icon=ft.Icons.PERSON_ADD,
                            width=180,
                            style=ft.ButtonStyle(
                                bgcolor={ft.ControlState.DEFAULT: ft.Colors.LIGHT_BLUE_400},
                                color={ft.ControlState.DEFAULT: ft.Colors.BLACK},
                                shape=ft.RoundedRectangleBorder(radius=20),
                            ),
                            on_click=registrar,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.TextButton(
                            "Ya tengo cuenta",
                            icon=ft.Icons.LOGIN,
                            on_click=lambda e: go("/login_user"),
                        ),
                        ft.TextButton(
                            "Volver al inicio",
                            icon=ft.Icons.ARROW_BACK,
                            on_click=lambda e: go("/"),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
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
            colors=[ft.Colors.INDIGO_900, ft.Colors.DEEP_PURPLE_900],
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
        route="/registro",
        controls=[fondo],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )
