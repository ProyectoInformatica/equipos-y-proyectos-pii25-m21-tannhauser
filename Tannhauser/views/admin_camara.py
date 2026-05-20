import flet as ft
from utils.navigation import ruta_dashboard_por_rol


def AdminCamaraView(page: ft.Page, go):
    stream_url = ft.TextField(
        label="URL del stream de la cámara",
        value="http://192.168.1.100:81/stream",
        border_radius=16,
        width=520,
    )

    snapshot_url = ft.TextField(
        label="URL de captura estática",
        value="http://192.168.1.100/capture",
        border_radius=16,
        width=520,
    )

    estado_text = ft.Text(
        "Configura la URL real de tu ESP32-CAM para visualizar el stream o una imagen.",
        size=14,
        color=ft.Colors.WHITE70,
    )

    preview_image = ft.Image(
        src=snapshot_url.value,
        width=900,
        height=500,
        fit=ft.ImageFit.CONTAIN,
        border_radius=20,
    )

    def mostrar_mensaje(msg, error=False):
        page.snack_bar = ft.SnackBar(
            ft.Text(msg),
            bgcolor=ft.Colors.RED_600 if error else ft.Colors.GREEN_600,
        )
        page.snack_bar.open = True
        page.update()

    def cargar_snapshot(e=None):
        preview_image.src = snapshot_url.value.strip()
        estado_text.value = f"Vista cargada desde: {snapshot_url.value.strip()}"
        page.update()

    def copiar_stream(e=None):
        page.set_clipboard(stream_url.value.strip())
        mostrar_mensaje("URL del stream copiada al portapapeles.")

    def copiar_snapshot(e=None):
        page.set_clipboard(snapshot_url.value.strip())
        mostrar_mensaje("URL de captura copiada al portapapeles.")

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
                ft.Container(
                    width=1180,
                    padding=24,
                    border_radius=28,
                    bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
                    border=ft.border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
                    content=ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text(
                                        "Cámara de seguridad",
                                        size=34,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                        "Vista de monitorización de la ESP32-CAM y accesos rápidos al stream.",
                                        size=15,
                                        color=ft.Colors.WHITE70,
                                    ),
                                ],
                                spacing=6,
                            ),
                            ft.OutlinedButton(
                                "Volver al panel",
                                icon=ft.Icons.ARROW_BACK_ROUNDED,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.WHITE,
                                    side=ft.BorderSide(1.1, ft.Colors.with_opacity(0.28, ft.Colors.WHITE)),
                                    shape=ft.RoundedRectangleBorder(radius=16),
                                ),
                                on_click=lambda e: go(ruta_dashboard_por_rol()),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(height=18),
                ft.Container(
                    width=1180,
                    padding=22,
                    border_radius=24,
                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                    border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Column(
                        [
                            ft.Text(
                                "Configuración de acceso",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Row(
                                [
                                    stream_url,
                                    ft.OutlinedButton(
                                        "Copiar stream",
                                        icon=ft.Icons.CONTENT_COPY_ROUNDED,
                                        style=ft.ButtonStyle(
                                            color=ft.Colors.WHITE,
                                            side=ft.BorderSide(1.0, ft.Colors.with_opacity(0.22, ft.Colors.WHITE)),
                                            shape=ft.RoundedRectangleBorder(radius=14),
                                        ),
                                        on_click=copiar_stream,
                                    ),
                                ],
                                spacing=12,
                                wrap=True,
                            ),
                            ft.Row(
                                [
                                    snapshot_url,
                                    ft.ElevatedButton(
                                        "Cargar vista",
                                        icon=ft.Icons.REFRESH_ROUNDED,
                                        bgcolor="#64D7FF",
                                        color=ft.Colors.BLACK,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=14),
                                        ),
                                        on_click=cargar_snapshot,
                                    ),
                                    ft.OutlinedButton(
                                        "Copiar captura",
                                        icon=ft.Icons.CONTENT_COPY_ROUNDED,
                                        style=ft.ButtonStyle(
                                            color=ft.Colors.WHITE,
                                            side=ft.BorderSide(1.0, ft.Colors.with_opacity(0.22, ft.Colors.WHITE)),
                                            shape=ft.RoundedRectangleBorder(radius=14),
                                        ),
                                        on_click=copiar_snapshot,
                                    ),
                                ],
                                spacing=12,
                                wrap=True,
                            ),
                            estado_text,
                        ],
                        spacing=14,
                    ),
                ),
                ft.Container(height=18),
                ft.Container(
                    width=1180,
                    padding=20,
                    border_radius=24,
                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                    border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Column(
                        [
                            ft.Text(
                                "Vista actual",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Container(
                                border_radius=20,
                                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                content=preview_image,
                            ),
                        ],
                        spacing=14,
                    ),
                ),
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    return ft.View(
        route="/admin_camara",
        controls=[contenido],
        padding=0,
        spacing=0,
    )