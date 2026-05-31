import asyncio
from datetime import datetime

import flet as ft

from utils.navigation import ruta_dashboard_por_rol
from utils.ui_premium import (
    ACCENT_STRONG,
    CHAMPAGNE,
    TEXT_MUTED,
    glass_panel,
    premium_snackbar,
    premium_text_field,
    primary_button,
    secondary_button,
    status_badge,
)


def AdminCamaraView(page: ft.Page, go):
    auto_refresh = {"running": False}
    refresh_seconds = 5

    stream_url = premium_text_field(
        ft.TextField(
            label="URL del stream de la camara",
            value="http://192.168.1.100:81/stream",
            border_radius=16,
            width=520,
        )
    )
    snapshot_url = premium_text_field(
        ft.TextField(
            label="URL de captura estatica",
            value="http://192.168.1.100/capture",
            border_radius=16,
            width=520,
        )
    )

    estado_text = ft.Text(
        "Configura la URL real de tu ESP32-CAM para visualizar una captura integrada.",
        size=14,
        color=TEXT_MUTED,
    )
    ultimo_refresco_text = ft.Text("Ultimo refresco: pendiente", size=12, color=ft.Colors.WHITE54)
    estado_badge_slot = ft.Container(content=status_badge("Snapshot listo", "cyan"))
    auto_button_slot = ft.Container()

    preview_image = ft.Image(
        src=snapshot_url.value,
        width=920,
        height=518,
        fit=ft.ImageFit.COVER,
    )

    def mostrar_mensaje(msg, error=False):
        page.snack_bar = premium_snackbar(msg, ok=not error)
        page.snack_bar.open = True
        page.update()

    def cargar_snapshot(e=None):
        url = snapshot_url.value.strip()
        if not url:
            estado_text.value = "No hay URL de captura configurada."
            estado_badge_slot.content = status_badge("Sin origen", "neutral")
            mostrar_mensaje("Configura una URL de captura.", True)
            return

        separator = "&" if "?" in url else "?"
        preview_image.src = f"{url}{separator}t={int(datetime.now().timestamp())}"
        estado_text.value = f"Vista integrada desde snapshot: {url}"
        ultimo_refresco_text.value = f"Ultimo refresco: {datetime.now().strftime('%H:%M:%S')}"
        estado_badge_slot.content = status_badge("Refrescado", "green")
        page.update()

    async def bucle_auto_refresco():
        while auto_refresh["running"]:
            await asyncio.sleep(refresh_seconds)
            if auto_refresh["running"]:
                cargar_snapshot()

    def auto_button():
        return secondary_button(
            "Detener auto" if auto_refresh["running"] else "Auto-refresco",
            icon=ft.Icons.PAUSE_ROUNDED if auto_refresh["running"] else ft.Icons.PLAY_ARROW_ROUNDED,
            on_click=alternar_auto_refresco,
        )

    def alternar_auto_refresco(e=None):
        auto_refresh["running"] = not auto_refresh["running"]
        auto_button_slot.content = auto_button()
        estado_badge_slot.content = status_badge(
            "Auto ON" if auto_refresh["running"] else "Auto OFF",
            "green" if auto_refresh["running"] else "neutral",
        )
        page.update()
        if auto_refresh["running"]:
            cargar_snapshot()
            page.run_task(bucle_auto_refresco)

    def copiar_stream(e=None):
        page.set_clipboard(stream_url.value.strip())
        mostrar_mensaje("URL del stream copiada al portapapeles.")

    def copiar_snapshot(e=None):
        page.set_clipboard(snapshot_url.value.strip())
        mostrar_mensaje("URL de captura copiada al portapapeles.")

    auto_button_slot.content = auto_button()

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
                glass_panel(
                    width=1180,
                    padding=24,
                    border_radius=28,
                    accent=CHAMPAGNE,
                    content=ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Row(
                                        [status_badge("Camara integrada", "gold"), estado_badge_slot],
                                        spacing=10,
                                        wrap=True,
                                    ),
                                    ft.Text(
                                        "Camara de seguridad",
                                        size=34,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                        "Visor premium integrado para ESP32-CAM con snapshot embebido y refresco seguro.",
                                        size=15,
                                        color=TEXT_MUTED,
                                    ),
                                ],
                                spacing=6,
                            ),
                            secondary_button(
                                "Volver al panel",
                                icon=ft.Icons.ARROW_BACK_ROUNDED,
                                on_click=lambda e: go(ruta_dashboard_por_rol()),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(height=18),
                glass_panel(
                    width=1180,
                    padding=22,
                    border_radius=24,
                    accent=ACCENT_STRONG,
                    content=ft.Column(
                        [
                            ft.Text("Configuracion de acceso", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Row(
                                [
                                    stream_url,
                                    secondary_button("Copiar stream", icon=ft.Icons.CONTENT_COPY_ROUNDED, on_click=copiar_stream),
                                ],
                                spacing=12,
                                wrap=True,
                            ),
                            ft.Row(
                                [
                                    snapshot_url,
                                    primary_button("Refrescar visor", icon=ft.Icons.REFRESH_ROUNDED, on_click=cargar_snapshot),
                                    secondary_button("Copiar captura", icon=ft.Icons.CONTENT_COPY_ROUNDED, on_click=copiar_snapshot),
                                    auto_button_slot,
                                ],
                                spacing=12,
                                wrap=True,
                            ),
                            estado_text,
                            ultimo_refresco_text,
                        ],
                        spacing=14,
                    ),
                ),
                ft.Container(height=18),
                glass_panel(
                    width=1180,
                    padding=20,
                    border_radius=24,
                    accent=CHAMPAGNE,
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Text("Visor integrado", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    status_badge("Snapshot embebido", "cyan"),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            ft.Container(
                                border_radius=20,
                                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                bgcolor="#030712",
                                border=ft.border.all(1, ft.Colors.with_opacity(0.18, CHAMPAGNE)),
                                content=ft.Stack(
                                    [
                                        preview_image,
                                        ft.Container(
                                            left=18,
                                            top=18,
                                            padding=ft.Padding(12, 7, 12, 7),
                                            border_radius=999,
                                            bgcolor=ft.Colors.with_opacity(0.52, ft.Colors.BLACK),
                                            content=ft.Row(
                                                [
                                                    ft.Icon(ft.Icons.FIBER_MANUAL_RECORD_ROUNDED, size=12, color="#B8FFE1"),
                                                    ft.Text("LIVE SNAPSHOT", size=11, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                                ],
                                                spacing=7,
                                                tight=True,
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            ft.Text(
                                "Si el MJPEG no se renderiza directamente en Flet, este visor usa capturas actualizables. El stream queda como opcion secundaria copiable.",
                                size=12,
                                color=TEXT_MUTED,
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
