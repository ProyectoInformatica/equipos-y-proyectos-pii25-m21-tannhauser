import asyncio
from datetime import datetime
import time
import urllib.error
import urllib.request

import flet as ft

from utils.navigation import ruta_dashboard_por_rol
from utils.ui_premium import (
    ACCENT_STRONG,
    CHAMPAGNE,
    TEXT_MUTED,
    glass_panel,
    premium_snackbar,
    premium_dropdown,
    premium_text_field,
    primary_button,
    secondary_button,
    status_badge,
)


def AdminCamaraView(page: ft.Page, go):
    auto_refresh = {"running": False}
    refresh_config = {"mode": "0.5", "seconds": 0.5}
    health_check = {"last_at": 0.0}

    stream_url = premium_text_field(
        ft.TextField(
            label="URL del stream de la camara",
            value="http://172.20.10.2:81/stream",
            border_radius=16,
            width=520,
        )
    )
    snapshot_url = premium_text_field(
        ft.TextField(
            label="URL de captura estatica",
            value="http://172.20.10.2/capture",
            border_radius=16,
            width=520,
        )
    )
    refresh_dropdown = premium_dropdown(
        ft.Dropdown(
            label="Frecuencia",
            value="0.5",
            width=170,
            options=[
                ft.dropdown.Option("0.5", "0.5s"),
                ft.dropdown.Option("1", "1s"),
                ft.dropdown.Option("2", "2s"),
                ft.dropdown.Option("manual", "Manual"),
            ],
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
        src="",
        width=920,
        height=518,
        fit=ft.ImageFit.COVER,
        gapless_playback=True,
        error_content=ft.Container(
            width=920,
            height=518,
            alignment=ft.alignment.center,
            padding=28,
            bgcolor="#030712",
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.VIDEOCAM_OFF_ROUNDED, color=CHAMPAGNE, size=42),
                    ft.Text(
                        "Camara offline o sin respuesta",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        "El visor mantiene el modo snapshot rapido y volvera a mostrar imagen cuando la ESP32-CAM responda.",
                        size=13,
                        color=TEXT_MUTED,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    def mostrar_mensaje(msg, error=False):
        page.snack_bar = premium_snackbar(msg, ok=not error)
        page.snack_bar.open = True
        page.update()

    def snapshot_con_cache_buster(url):
        separator = "&" if "?" in url else "?"
        return f"{url}{separator}t={int(time.time() * 1000)}"

    async def comprobar_estado_camara(url, mostrar_aviso=False):
        def leer_cabecera_snapshot():
            with urllib.request.urlopen(url, timeout=1.2) as response:
                response.read(64)

        try:
            await asyncio.to_thread(leer_cabecera_snapshot)
        except (urllib.error.URLError, TimeoutError, OSError):
            estado_text.value = "Camara offline o sin respuesta. Comprueba IP, alimentacion y red."
            estado_badge_slot.content = status_badge("Offline", "neutral")
            if mostrar_aviso:
                mostrar_mensaje("La camara no responde. Se mantiene el visor snapshot rapido.", True)
        else:
            estado_badge_slot.content = status_badge("Online", "green")
        page.update()

    def cargar_snapshot(e=None, comprobar=True):
        url = snapshot_url.value.strip()
        if not url:
            estado_text.value = "No hay URL de captura configurada."
            estado_badge_slot.content = status_badge("Sin origen", "neutral")
            mostrar_mensaje("Configura una URL de captura.", True)
            return

        preview_image.src = snapshot_con_cache_buster(url)
        estado_text.value = f"Vista integrada desde snapshot: {url}"
        ultimo_refresco_text.value = f"Ultimo refresco: {datetime.now().strftime('%H:%M:%S')}"
        estado_badge_slot.content = status_badge("Refrescando", "cyan")
        page.update()
        ahora = time.time()
        if comprobar and (e is not None or ahora - health_check["last_at"] >= 5):
            health_check["last_at"] = ahora
            page.run_task(comprobar_estado_camara, preview_image.src, e is not None)

    async def bucle_auto_refresco():
        while auto_refresh["running"]:
            seconds = refresh_config["seconds"]
            if seconds is None:
                auto_refresh["running"] = False
                auto_button_slot.content = auto_button()
                estado_badge_slot.content = status_badge("Manual", "neutral")
                page.update()
                break
            await asyncio.sleep(seconds)
            if auto_refresh["running"]:
                cargar_snapshot(comprobar=True)

    def auto_button():
        return secondary_button(
            "Detener auto" if auto_refresh["running"] else "Auto-refresco",
            icon=ft.Icons.PAUSE_ROUNDED if auto_refresh["running"] else ft.Icons.PLAY_ARROW_ROUNDED,
            on_click=alternar_auto_refresco,
        )

    def cambiar_frecuencia(e=None):
        value = refresh_dropdown.value or "0.5"
        if value == "manual":
            refresh_config["mode"] = "manual"
            refresh_config["seconds"] = None
            auto_refresh["running"] = False
            auto_button_slot.content = auto_button()
            estado_badge_slot.content = status_badge("Manual", "neutral")
            estado_text.value = "Refresco manual activo. Usa Refrescar ahora para pedir un snapshot."
        else:
            refresh_config["mode"] = value
            refresh_config["seconds"] = float(value)
            estado_text.value = f"Auto-refresco configurado cada {value}s."
            estado_badge_slot.content = status_badge(
                "Auto ON" if auto_refresh["running"] else "Auto OFF",
                "green" if auto_refresh["running"] else "neutral",
            )
        page.update()

    def alternar_auto_refresco(e=None):
        if refresh_config["seconds"] is None:
            mostrar_mensaje("Selecciona 0.5s, 1s o 2s para activar auto-refresco.", True)
            estado_badge_slot.content = status_badge("Manual", "neutral")
            page.update()
            return
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
    refresh_dropdown.on_change = cambiar_frecuencia
    initial_snapshot = snapshot_url.value.strip()
    preview_image.src = snapshot_con_cache_buster(initial_snapshot)
    estado_text.value = f"Vista integrada desde snapshot: {initial_snapshot}"
    ultimo_refresco_text.value = f"Ultimo refresco: {datetime.now().strftime('%H:%M:%S')}"

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
                                    refresh_dropdown,
                                    primary_button("Refrescar ahora", icon=ft.Icons.REFRESH_ROUNDED, on_click=cargar_snapshot),
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
