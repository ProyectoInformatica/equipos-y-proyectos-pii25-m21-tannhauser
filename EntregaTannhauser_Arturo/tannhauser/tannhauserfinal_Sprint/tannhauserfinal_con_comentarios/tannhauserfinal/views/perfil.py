import flet as ft
from models.session_manager import get_current_user, set_current_user
from controllers.profile_controller import ProfileController
from utils.navigation import ruta_dashboard_por_rol


def PerfilView(page: ft.Page, go):
    usuario = get_current_user() or {}
    user_id = usuario.get("id")
    controller = ProfileController()

    user_data = controller.obtener_usuario(user_id) if user_id else None

    nombre = (user_data or {}).get("nombre", "Usuario")
    email = (user_data or {}).get("email", "Sin correo")
    rol = (user_data or {}).get("rol", "cliente")
    profile_image = (user_data or {}).get("profile_image")

    selected_file = {"path": None}

    avatar_container = ft.Container()

    def render_avatar(image_path: str | None):
        if image_path:
            avatar_container.content = ft.Container(
                width=126,
                height=126,
                border_radius=63,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=ft.Image(
                    src=image_path,
                    fit=ft.BoxFit.COVER,
                ),
            )
        else:
            avatar_container.content = ft.CircleAvatar(
                radius=63,
                bgcolor=ft.Colors.with_opacity(0.18, ft.Colors.CYAN_300),
                content=ft.Icon(ft.Icons.PERSON_ROUNDED, size=52, color="#9CEBFF"),
            )

    render_avatar(profile_image)

    def mostrar_mensaje(msg, error=False):
        page.snack_bar = ft.SnackBar(
            ft.Text(msg),
            bgcolor=ft.Colors.RED_600 if error else ft.Colors.GREEN_600,
        )
        page.snack_bar.open = True
        page.update()

    def on_file_result(e: ft.FilePickerResultEvent):
        if e.files:
            selected_file["path"] = e.files[0].path
            render_avatar(selected_file["path"])
            mostrar_mensaje("Vista previa de la nueva foto cargada.")
            page.update()

    def guardar_foto(e):
        if not selected_file["path"]:
            mostrar_mensaje("Selecciona primero una imagen.", error=True)
            return

        ok, msg = controller.actualizar_foto_perfil(user_id, selected_file["path"])
        mostrar_mensaje(msg, error=not ok)

        if ok:
            nuevo = controller.obtener_usuario(user_id)
            nueva_imagen = (nuevo or {}).get("profile_image")

            render_avatar(nueva_imagen)
            selected_file["path"] = None

            sesion_actual = get_current_user() or {}
            sesion_actualizada = {
                **sesion_actual,
                "id": (nuevo or {}).get("id", sesion_actual.get("id")),
                "nombre": (nuevo or {}).get("nombre", sesion_actual.get("nombre")),
                "email": (nuevo or {}).get("email", sesion_actual.get("email")),
                "rol": (nuevo or {}).get("rol", sesion_actual.get("rol")),
                "profile_image": nueva_imagen,
            }
            set_current_user(sesion_actualizada)

            page.update()

    file_picker = ft.FilePicker(on_result=on_file_result)
    page.overlay.append(file_picker)

    contenido = ft.Container(
        expand=True,
        padding=28,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=["#050A12", "#09172A", "#0B2342", "#0E2F55"],
        ),
        content=ft.Column(
            [
                ft.Text(
                    "Mi perfil",
                    size=34,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Gestiona tu cuenta, seguridad y foto de perfil.",
                    size=15,
                    color=ft.Colors.WHITE70,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=18),
                ft.Container(
                    width=760,
                    padding=28,
                    border_radius=30,
                    bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
                    border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Column(
                        [
                            ft.Row(
                                [avatar_container],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            ft.Text(
                                nombre,
                                size=28,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                email,
                                size=16,
                                color=ft.Colors.WHITE70,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                f"Rol: {rol}",
                                size=15,
                                color="#9CEBFF",
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Text(
                                "Gestiona tus datos, tu contraseña y tu foto de perfil.",
                                size=14,
                                color=ft.Colors.WHITE60,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Container(height=12),
                            ft.Text(
                                "Foto de perfil",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Row(
                                [
                                    ft.Button(
                                        "Seleccionar nueva foto",
                                        icon=ft.Icons.UPLOAD_FILE_ROUNDED,
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
                                    ft.OutlinedButton(
                                        "Guardar foto",
                                        icon=ft.Icons.SAVE_ROUNDED,
                                        style=ft.ButtonStyle(
                                            color=ft.Colors.WHITE,
                                            side=ft.BorderSide(1.1, ft.Colors.with_opacity(0.28, ft.Colors.WHITE)),
                                            shape=ft.RoundedRectangleBorder(radius=16),
                                        ),
                                        on_click=guardar_foto,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=14,
                            ),
                            ft.Divider(color=ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                            ft.Text(
                                "Datos personales",
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.TextField(
                                label="Nombre",
                                value=nombre,
                                read_only=True,
                                border_radius=16,
                                width=460,
                            ),
                            ft.TextField(
                                label="Correo electrónico",
                                value=email,
                                read_only=True,
                                border_radius=16,
                                width=460,
                            ),
                            ft.Container(height=6),
                            ft.OutlinedButton(
                                "Volver",
                                icon=ft.Icons.ARROW_BACK_ROUNDED,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.WHITE,
                                    side=ft.BorderSide(1.1, ft.Colors.with_opacity(0.28, ft.Colors.WHITE)),
                                    shape=ft.RoundedRectangleBorder(radius=16),
                                ),
                                on_click=lambda e: go(ruta_dashboard_por_rol()),
                            ),
                        ],
                        spacing=14,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
            ],
            spacing=0,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
        ),
    )

    return ft.View(
        route="/perfil",
        controls=[contenido],
        padding=0,
        spacing=0,
    )