import flet as ft
from controllers.auth_controller import AuthController


def RegistroView(page: ft.Page, go):
    auth = AuthController()
    selected_photo = {"path": None}

    def obtener_iniciales(texto: str) -> str:
        partes = [p for p in (texto or "").strip().split() if p]
        if len(partes) >= 2:
            return (partes[0][0] + partes[1][0]).upper()
        if len(partes) == 1:
            return partes[0][:2].upper()
        return "US"

    avatar_preview = ft.Container()

    def render_avatar_preview():
        if selected_photo["path"]:
            avatar_preview.content = ft.Container(
                width=112,
                height=112,
                border_radius=56,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=ft.Image(
                    src=selected_photo["path"],
                    fit=ft.ImageFit.COVER,
                ),
            )
        else:
            avatar_preview.content = ft.CircleAvatar(
                radius=56,
                bgcolor=ft.Colors.with_opacity(0.18, ft.Colors.CYAN_300),
                content=ft.Text(
                    obtener_iniciales(nombre.value),
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color="#9CEBFF",
                ),
            )

    def on_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            selected_photo["path"] = e.files[0].path
            render_avatar_preview()
            page.update()

    file_picker = ft.FilePicker(on_result=on_file_result)
    page.overlay.append(file_picker)

    nombre = ft.TextField(
        label="Nombre completo",
        prefix_icon=ft.Icons.PERSON,
        border_radius=16,
        border_color=ft.Colors.CYAN_300,
        focused_border_color=ft.Colors.LIGHT_BLUE_400,
        width=360,
        bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
        on_change=lambda e: (render_avatar_preview(), page.update()) if not selected_photo["path"] else None,
    )

    email = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.EMAIL,
        border_radius=16,
        border_color=ft.Colors.CYAN_300,
        focused_border_color=ft.Colors.LIGHT_BLUE_400,
        width=360,
        bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
    )

    password = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        border_radius=16,
        border_color=ft.Colors.CYAN_300,
        focused_border_color=ft.Colors.LIGHT_BLUE_400,
        width=360,
        bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
    )

    password2 = ft.TextField(
        label="Repetir contraseña",
        prefix_icon=ft.Icons.LOCK,
        password=True,
        can_reveal_password=True,
        border_radius=16,
        border_color=ft.Colors.CYAN_300,
        focused_border_color=ft.Colors.LIGHT_BLUE_400,
        width=360,
        bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
    )

    mensaje = ft.Text("", color=ft.Colors.RED_300, size=14)

    render_avatar_preview()

    def mostrar_snack(texto, ok=True):
        page.snack_bar = ft.SnackBar(
            ft.Text(texto),
            bgcolor=ft.Colors.GREEN_600 if ok else ft.Colors.RED_600,
        )
        page.snack_bar.open = True
        page.update()

    def registrar(e):
        mensaje.value = ""

        if not nombre.value or not email.value or not password.value or not password2.value:
            mensaje.value = "Completa todos los campos."
            page.update()
            return

        if password.value != password2.value:
            mensaje.value = "Las contraseñas no coinciden."
            page.update()
            return

        ok, msg = auth.register(
            nombre.value.strip(),
            email.value.strip(),
            password.value.strip(),
            profile_image_path=selected_photo["path"],
        )

        if ok:
            nombre.value = ""
            email.value = ""
            password.value = ""
            password2.value = ""
            selected_photo["path"] = None
            render_avatar_preview()
            mensaje.value = ""
            mostrar_snack("Cuenta creada correctamente. Ahora inicia sesión.", ok=True)
            go("/login")
            return

        mensaje.value = msg
        page.update()

    topbar = ft.Container(
        width=1180,
        padding=ft.Padding(24, 18, 24, 18),
        border_radius=28,
        bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
        border=ft.border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
        content=ft.Row(
            [
                ft.Row(
                    [
                        ft.Container(
                            width=68,
                            height=68,
                            border_radius=20,
                            bgcolor=ft.Colors.with_opacity(0.94, ft.Colors.WHITE),
                            padding=10,
                            content=ft.Image(
                                src="assets/logo_tannhauser.png",
                                fit=ft.ImageFit.CONTAIN,
                            ),
                        ),
                        ft.Column(
                            [
                                ft.Text(
                                    "Crear cuenta",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                                ft.Text(
                                    "Regístrate como cliente del supermercado.",
                                    size=14,
                                    color=ft.Colors.WHITE70,
                                ),
                            ],
                            spacing=4,
                        ),
                    ],
                    spacing=16,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.OutlinedButton(
                    "Volver",
                    icon=ft.Icons.ARROW_BACK_ROUNDED,
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        side=ft.BorderSide(1.1, ft.Colors.with_opacity(0.28, ft.Colors.WHITE)),
                        shape=ft.RoundedRectangleBorder(radius=16),
                    ),
                    on_click=lambda e: go("/"),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    card = ft.Container(
        width=620,
        padding=32,
        border_radius=28,
        bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
        border=ft.border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=22,
            color=ft.Colors.with_opacity(0.12, ft.Colors.BLACK),
            offset=ft.Offset(0, 10),
        ),
        content=ft.Column(
            [
                ft.Text(
                    "Nueva cuenta de cliente",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Puedes subir tu foto de perfil. Si no subes ninguna, aparecerán tus iniciales automáticamente.",
                    size=14,
                    color=ft.Colors.WHITE70,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=6),
                ft.Row([avatar_preview], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Añadir foto de perfil",
                            icon=ft.Icons.ADD_A_PHOTO_ROUNDED,
                            bgcolor="#64D7FF",
                            color=ft.Colors.BLACK,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=16),
                            ),
                            on_click=lambda e: file_picker.pick_files(
                                allow_multiple=False,
                                allowed_extensions=["png", "jpg", "jpeg", "webp"],
                            ),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(height=10),
                nombre,
                email,
                password,
                password2,
                mensaje,
                ft.Container(height=8),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Crear cuenta",
                            icon=ft.Icons.PERSON_ADD_ALT_1_ROUNDED,
                            width=190,
                            bgcolor="#64D7FF",
                            color=ft.Colors.BLACK,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=18),
                            ),
                            on_click=registrar,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Container(height=6),
                ft.Row(
                    [
                        ft.TextButton(
                            "Ya tengo cuenta",
                            icon=ft.Icons.LOGIN_ROUNDED,
                            on_click=lambda e: go("/login"),
                        ),
                        ft.TextButton(
                            "Volver al inicio",
                            icon=ft.Icons.HOME_ROUNDED,
                            on_click=lambda e: go("/"),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            spacing=14,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    contenido = ft.Container(
        expand=True,
        padding=30,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=["#050A12", "#09172A", "#0B2342", "#0E2F55"],
        ),
        content=ft.Column(
            [
                topbar,
                ft.Container(height=26),
                ft.Row([card], alignment=ft.MainAxisAlignment.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
        ),
    )

    return ft.View(
        route="/registro",
        controls=[contenido],
        padding=0,
        spacing=0,
    )