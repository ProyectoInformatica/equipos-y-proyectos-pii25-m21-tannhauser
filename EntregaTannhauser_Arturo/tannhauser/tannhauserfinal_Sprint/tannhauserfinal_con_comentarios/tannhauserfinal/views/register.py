import os
import shutil
import time
import flet as ft
from controllers.auth_controller import AuthController
from models.session_manager import set_current_user


def RegistroView(page: ft.Page, go):
    auth = AuthController()
    foto_perfil = {"ruta": None}

    def asegurar_directorio_perfiles():
        os.makedirs("assets/profile_pics", exist_ok=True)

    def guardar_imagen_local(source_path: str):
        if not source_path:
            return None

        asegurar_directorio_perfiles()

        _, ext = os.path.splitext(source_path)
        if not ext:
            ext = ".png"

        nombre_archivo = f"profile_{int(time.time() * 1000)}{ext}"
        destino = os.path.join("assets", "profile_pics", nombre_archivo)
        shutil.copy(source_path, destino)
        return destino.replace("\\", "/")

    avatar = ft.CircleAvatar(
        radius=46,
        bgcolor=ft.Colors.with_opacity(0.14, ft.Colors.CYAN_300),
        content=ft.Icon(ft.Icons.PERSON_ROUNDED, size=42, color="#9CEBFF"),
    )

    texto_foto = ft.Text(
        "Sin foto seleccionada",
        size=12,
        color=ft.Colors.WHITE60,
        text_align=ft.TextAlign.CENTER,
    )

    nombre = ft.TextField(
        hint_text="Nombre completo",
        prefix_icon=ft.Icons.PERSON_ROUNDED,
        border_radius=18,
        filled=True,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
        border_color=ft.Colors.with_opacity(0.18, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
        hint_style=ft.TextStyle(color=ft.Colors.WHITE54),
        width=420,
    )

    email = ft.TextField(
        hint_text="Correo electrónico",
        prefix_icon=ft.Icons.MAIL_ROUNDED,
        border_radius=18,
        filled=True,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
        border_color=ft.Colors.with_opacity(0.18, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
        hint_style=ft.TextStyle(color=ft.Colors.WHITE54),
        width=420,
    )

    password = ft.TextField(
        hint_text="Contraseña",
        prefix_icon=ft.Icons.LOCK_ROUNDED,
        password=True,
        can_reveal_password=True,
        border_radius=18,
        filled=True,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
        border_color=ft.Colors.with_opacity(0.18, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
        hint_style=ft.TextStyle(color=ft.Colors.WHITE54),
        width=420,
    )

    password2 = ft.TextField(
        hint_text="Repetir contraseña",
        prefix_icon=ft.Icons.LOCK_OUTLINE_ROUNDED,
        password=True,
        can_reveal_password=True,
        border_radius=18,
        filled=True,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
        border_color=ft.Colors.with_opacity(0.18, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
        hint_style=ft.TextStyle(color=ft.Colors.WHITE54),
        width=420,
    )

    mensaje = ft.Text("", color=ft.Colors.RED_300, size=13)

    def mostrar_mensaje(texto, color=ft.Colors.BLUE_600):
        page.snack_bar = ft.SnackBar(ft.Text(texto), bgcolor=color)
        page.snack_bar.open = True
        page.update()

    def on_file_result(e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            ruta_local = e.files[0].path
            ruta_guardada = guardar_imagen_local(ruta_local)

            if ruta_guardada:
                foto_perfil["ruta"] = ruta_guardada
                avatar.foreground_image_src = ruta_guardada
                avatar.content = None
                texto_foto.value = "Foto seleccionada correctamente"
                page.update()

    file_picker = ft.FilePicker(on_result=on_file_result)
    page.overlay.append(file_picker)

    def registrar(e):
        mensaje.value = ""

        nombre_val = (nombre.value or "").strip()
        email_val = (email.value or "").strip().lower()
        pass_val = password.value or ""
        pass2_val = password2.value or ""

        if not nombre_val or not email_val or not pass_val or not pass2_val:
            mensaje.value = "Completa todos los campos obligatorios."
            page.update()
            return

        if pass_val != pass2_val:
            mensaje.value = "Las contraseñas no coinciden."
            page.update()
            return

        if len(pass_val) < 6:
            mensaje.value = "La contraseña debe tener al menos 6 caracteres."
            page.update()
            return

        ok, msg = auth.register(
            nombre_val,
            email_val,
            pass_val,
            foto_perfil["ruta"],
        )

        if ok:
            user = auth.manager.obtener_por_email(email_val)
            if user:
                set_current_user(user)
                mostrar_mensaje("Cuenta creada correctamente.", ft.Colors.GREEN_600)
                go("/panel_usuario")
            else:
                mostrar_mensaje("Cuenta creada, pero no se pudo iniciar sesión automáticamente.", ft.Colors.AMBER_600)
                go("/login")
        else:
            mensaje.value = msg

        page.update()

    lado_izquierdo = ft.Container(
        expand=True,
        padding=ft.Padding(46, 40, 46, 40),
        content=ft.Column(
            [
                ft.Image(
                    src="assets/logo_tannhauser.png",
                    width=240,
                    fit=ft.BoxFit.CONTAIN,
                ),
                ft.Container(height=34),
                ft.Text(
                    "Únete a Tannhauser",
                    size=44,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                ft.Text(
                    "Crea tu cuenta para acceder al sistema, consultar sensores, inventario, actividad y toda la operativa del supermercado inteligente.",
                    size=18,
                    color=ft.Colors.WHITE70,
                    width=560,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
    )

    lado_derecho = ft.Container(
        width=560,
        padding=34,
        border_radius=30,
        bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=26,
            color=ft.Colors.with_opacity(0.14, ft.Colors.BLACK),
            offset=ft.Offset(0, 10),
        ),
        content=ft.Column(
            [
                ft.Text(
                    "Crear cuenta",
                    size=34,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Registro con foto de perfil opcional.",
                    size=15,
                    color=ft.Colors.WHITE70,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=8),
                ft.Column(
                    [
                        avatar,
                        texto_foto,
                        ft.TextButton(
                            "Subir foto de perfil",
                            icon=ft.Icons.UPLOAD_FILE_ROUNDED,
                            style=ft.ButtonStyle(color="#9CEBFF"),
                            on_click=lambda e: file_picker.pick_files(
                                allow_multiple=False,
                                allowed_extensions=["png", "jpg", "jpeg", "webp"],
                            ),
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=8,
                ),
                ft.Container(height=8),
                nombre,
                email,
                password,
                password2,
                mensaje,
                ft.Container(height=8),
                ft.Button(
                    "Registrarse",
                    icon=ft.Icons.PERSON_ADD_ALT_1_ROUNDED,
                    width=420,
                    height=52,
                    bgcolor="#64D7FF",
                    color=ft.Colors.BLACK,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=18),
                    ),
                    on_click=registrar,
                ),
                ft.Container(height=6),
                ft.Row(
                    [
                        ft.TextButton(
                            "Ya tengo cuenta",
                            icon=ft.Icons.LOGIN_ROUNDED,
                            style=ft.ButtonStyle(color=ft.Colors.WHITE70),
                            on_click=lambda e: go("/login"),
                        ),
                        ft.TextButton(
                            "Volver al inicio",
                            icon=ft.Icons.ARROW_BACK_ROUNDED,
                            style=ft.ButtonStyle(color=ft.Colors.WHITE70),
                            on_click=lambda e: go("/"),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=14,
        ),
    )

    fondo = ft.Container(
        expand=True,
        padding=32,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=[
                "#050A12",
                "#09172A",
                "#0B2342",
                "#0E2F55",
            ],
        ),
        content=ft.Row(
            [
                lado_izquierdo,
                lado_derecho,
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    return ft.View(
        route="/registro",
        controls=[fondo],
        padding=0,
        spacing=0,
    )