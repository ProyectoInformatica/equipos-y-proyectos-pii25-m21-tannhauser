import os

import flet as ft

from controllers.sensor_controller import SensorController
from utils.navigation import ruta_dashboard_por_rol
from utils.ui_premium import (
    CHAMPAGNE,
    TEXT_MUTED,
    glass_panel,
    primary_button,
    secondary_button,
    status_badge,
)


MAP_ASSET_PATH = os.path.join("assets", "supermercado_3d_premium.png")
MAP_IMAGE_SRC = "supermercado_3d_premium.png"
STAGE_W = 980
STAGE_H = 620

REAL_SENSORS = [
    {
        "key": "dht11",
        "name": "DHT11",
        "type": "Temperatura / humedad",
        "location": "Zona central ambiental",
        "code": "TEMP_AIR / HUM_AIR",
        "description": "Lectura ambiental del pasillo principal y confort interior.",
        "power": "0.010 W estimado",
        "icon": ft.Icons.THERMOSTAT_ROUNDED,
        "color": "#B8FFE1",
        "x": 510,
        "y": 285,
        "needles": ["temp", "temperatura", "hum", "humedad", "humidity", "dht", "dht11"],
        "fallback": "22.4 C / 48 %",
    },
    {
        "key": "mq135",
        "name": "MQ135",
        "type": "Calidad de aire",
        "location": "Zona izquierda / calidad del aire",
        "code": "MQ135_AIR",
        "description": "Control de calidad de aire en la zona con mayor intercambio exterior.",
        "power": "0.900 W estimado",
        "icon": ft.Icons.AIR_ROUNDED,
        "color": CHAMPAGNE,
        "x": 285,
        "y": 315,
        "needles": ["mq135", "mq-135", "aire", "air", "calidad"],
        "fallback": "415 ppm",
    },
    {
        "key": "hc_sr04",
        "name": "HC-SR04",
        "type": "Ultrasonidos / acceso",
        "location": "Entrada inferior / puerta principal",
        "code": "DISTANCE_CM",
        "description": "Deteccion de presencia o paso en el acceso del supermercado.",
        "power": "0.075 W estimado",
        "icon": ft.Icons.SENSORS_ROUNDED,
        "color": "#9CEBFF",
        "x": 500,
        "y": 530,
        "needles": ["hc-sr04", "hcsr04", "hc_sr04", "distancia", "distance", "puerta"],
        "fallback": "86 cm",
    },
    {
        "key": "lcd16x2",
        "name": "LCD 16x2",
        "type": "Display 16x2",
        "location": "Zona derecha / mostrador o control",
        "code": "LCD_16X2",
        "description": "Panel local de informacion para caja, estado y mensajes operativos.",
        "power": "0.350 W estimado",
        "icon": ft.Icons.DISPLAY_SETTINGS_ROUNDED,
        "color": "#D9C8FF",
        "x": 735,
        "y": 330,
        "needles": ["lcd", "16x2", "display", "pantalla"],
        "fallback": "Display operativo",
    },
]


def AdminMapaSensoresView(page: ft.Page, go):
    controller = SensorController()
    selected = {"key": "dht11"}
    current_data = {"rows": {}}
    map_slot = ft.Container(width=STAGE_W)
    detail_slot = ft.Container(width=360)

    def error_view(message):
        return ft.View(
            route="/admin_mapa_sensores",
            controls=[
                ft.Container(
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
                                width=760,
                                padding=30,
                                border_radius=30,
                                accent="#FFB4B8",
                                content=ft.Column(
                                    [
                                        status_badge("Mapa de sensores", "gold"),
                                        ft.Icon(ft.Icons.ERROR_OUTLINE_ROUNDED, color="#FFB4B8", size=50),
                                        ft.Text("No se pudo cargar el render 3D", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER),
                                        ft.Text(message, size=14, color=TEXT_MUTED, text_align=ft.TextAlign.CENTER),
                                        secondary_button("Volver al panel", ft.Icons.ARROW_BACK_ROUNDED, on_click=lambda e: go(ruta_dashboard_por_rol())),
                                    ],
                                    spacing=14,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                )
            ],
            padding=0,
            spacing=0,
        )

    if not os.path.exists(MAP_ASSET_PATH):
        return error_view("Falta assets/supermercado_3d_premium.png. La vista no dibuja un mapa alternativo para evitar volver al pseudo-3D manual.")

    def obtener_datos():
        try:
            if hasattr(controller, "obtener_estados_actuales_db"):
                return controller.obtener_estados_actuales_db() or {}
        except Exception as e:
            print(f"Error leyendo datos reales para mapa: {e}")
        return {}

    def lectura_para(sensor):
        for codigo, row in (current_data["rows"] or {}).items():
            if not row:
                continue
            haystack = f"{codigo} {row.get('device_code', '')} {row.get('state_code', '')} {row.get('source', '')}".lower()
            if any(needle in haystack for needle in sensor["needles"]):
                return codigo, row
        return sensor["code"], None

    def sensor_actual():
        return next((s for s in REAL_SENSORS if s["key"] == selected["key"]), REAL_SENSORS[0])

    def seleccionar(sensor):
        selected["key"] = sensor["key"]
        render()

    def refrescar(e=None):
        current_data["rows"] = obtener_datos()
        render()

    def estado_sensor(sensor):
        codigo, row = lectura_para(sensor)
        if row and (row.get("state_value") is not None or row.get("numeric_value") is not None):
            return "Online", "green", codigo, row
        return "Offline", "neutral", codigo, None

    def format_lectura(sensor, row):
        if not row:
            return sensor["fallback"]
        value = row.get("state_value")
        numeric = row.get("numeric_value")
        if value not in (None, ""):
            return value
        if numeric not in (None, ""):
            return numeric
        return sensor["fallback"]

    def sensor_node(sensor):
        is_selected = selected["key"] == sensor["key"]
        status, tone, _, _ = estado_sensor(sensor)
        halo = 98 if is_selected else 84
        node = 64 if is_selected else 56
        return ft.Container(
            left=sensor["x"] - halo / 2,
            top=sensor["y"] - halo / 2,
            content=ft.Stack(
                [
                    ft.Container(
                        width=halo,
                        height=halo,
                        border_radius=halo / 2,
                        bgcolor=ft.Colors.with_opacity(0.12 if is_selected else 0.07, sensor["color"]),
                        border=ft.border.all(1.2, ft.Colors.with_opacity(0.34 if is_selected else 0.18, sensor["color"])),
                    ),
                    ft.Container(
                        left=(halo - node) / 2,
                        top=8,
                        width=node,
                        height=node,
                        border_radius=22,
                        bgcolor=ft.Colors.with_opacity(0.94, "#07111F"),
                        border=ft.border.all(2 if is_selected else 1.2, sensor["color"]),
                        shadow=ft.BoxShadow(
                            spread_radius=0,
                            blur_radius=28 if is_selected else 18,
                            color=ft.Colors.with_opacity(0.42, sensor["color"]),
                            offset=ft.Offset(0, 12),
                        ),
                        alignment=ft.alignment.center,
                        tooltip=f"{sensor['name']} - {status}",
                        on_click=lambda e, s=sensor: seleccionar(s),
                        content=ft.Icon(sensor["icon"], color=sensor["color"], size=30 if is_selected else 25),
                    ),
                    ft.Container(
                        left=halo - 28,
                        top=10,
                        width=18,
                        height=18,
                        border_radius=9,
                        bgcolor="#B8FFE1" if tone == "green" else "#8A93A3",
                        border=ft.border.all(2, "#07111F"),
                    ),
                    ft.Container(
                        left=(halo - 82) / 2,
                        top=node + 15,
                        width=82,
                        padding=ft.Padding(8, 4, 8, 4),
                        border_radius=999,
                        bgcolor=ft.Colors.with_opacity(0.90, "#07111F"),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.26, sensor["color"])),
                        alignment=ft.alignment.center,
                        content=ft.Text(sensor["name"], size=10, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ),
                ],
                width=halo,
                height=halo + 18,
            ),
        )

    def map_legend():
        return ft.Container(
            padding=ft.Padding(14, 10, 14, 10),
            border_radius=20,
            bgcolor=ft.Colors.with_opacity(0.055, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
            content=ft.Row(
                [
                    ft.Row(
                        [
                            ft.Container(width=10, height=10, border_radius=5, bgcolor=s["color"]),
                            ft.Text(s["name"], size=12, color=TEXT_MUTED),
                        ],
                        spacing=6,
                        tight=True,
                    )
                    for s in REAL_SENSORS
                ],
                spacing=16,
                wrap=True,
            ),
        )

    def build_map():
        return glass_panel(
            width=STAGE_W,
            padding=20,
            border_radius=32,
            accent=CHAMPAGNE,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Row(
                                        [
                                            status_badge("Render 3D premium", "gold"),
                                            status_badge("Sensores clicables", "cyan"),
                                        ],
                                        spacing=8,
                                        wrap=True,
                                    ),
                                    ft.Text("Supermercado Tannhauser", size=25, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    ft.Text("Render real del supermercado con sensores superpuestos por zona.", size=13, color=TEXT_MUTED),
                                ],
                                spacing=5,
                            ),
                            secondary_button("", icon=ft.Icons.REFRESH_ROUNDED, width=52, on_click=refrescar),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Container(
                        width=STAGE_W,
                        height=STAGE_H,
                        clip_behavior=ft.ClipBehavior.HARD_EDGE,
                        border_radius=30,
                        bgcolor="#030712",
                        border=ft.border.all(1, ft.Colors.with_opacity(0.14, CHAMPAGNE)),
                        content=ft.Stack(
                            [
                                ft.Image(
                                    src=MAP_IMAGE_SRC,
                                    width=STAGE_W,
                                    height=STAGE_H,
                                    fit=ft.ImageFit.COVER,
                                ),
                                ft.Container(
                                    left=0,
                                    top=0,
                                    width=STAGE_W,
                                    height=STAGE_H,
                                    gradient=ft.LinearGradient(
                                        begin=ft.Alignment(-1, -1),
                                        end=ft.Alignment(1, 1),
                                        colors=[
                                            ft.Colors.with_opacity(0.05, "#FFFFFF"),
                                            ft.Colors.with_opacity(0.00, "#FFFFFF"),
                                            ft.Colors.with_opacity(0.22, "#030712"),
                                        ],
                                    ),
                                ),
                                *[sensor_node(sensor) for sensor in REAL_SENSORS],
                            ],
                            width=STAGE_W,
                            height=STAGE_H,
                        ),
                    ),
                    map_legend(),
                ],
                spacing=14,
            ),
        )

    def info_line(label, value):
        return ft.Container(
            padding=ft.Padding(0, 2, 0, 2),
            content=ft.Row(
                [
                    ft.Text(label, size=12, color=ft.Colors.WHITE54, width=104),
                    ft.Text(str(value), size=13, color=ft.Colors.WHITE, expand=True),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        )

    def detail_card():
        sensor = sensor_actual()
        status, tone, codigo, row = estado_sensor(sensor)
        lectura = format_lectura(sensor, row)
        actualizado = row.get("updated_at") if row else "Demo local"
        fuente = row.get("source") if row else "Fallback demo"

        return glass_panel(
            width=360,
            padding=24,
            border_radius=32,
            accent=sensor["color"],
            content=ft.Column(
                [
                    ft.Container(
                        height=150,
                        border_radius=28,
                        bgcolor=ft.Colors.with_opacity(0.11, sensor["color"]),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.22, sensor["color"])),
                        alignment=ft.alignment.center,
                        content=ft.Stack(
                            [
                                ft.Container(
                                    width=118,
                                    height=118,
                                    border_radius=38,
                                    bgcolor=ft.Colors.with_opacity(0.16, sensor["color"]),
                                    border=ft.border.all(1.4, ft.Colors.with_opacity(0.30, sensor["color"])),
                                    alignment=ft.alignment.center,
                                    content=ft.Icon(sensor["icon"], color=sensor["color"], size=58),
                                ),
                                ft.Container(right=16, top=14, content=status_badge(status, tone)),
                            ],
                        ),
                    ),
                    ft.Text(sensor["name"], size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text(sensor["description"], size=13, color=TEXT_MUTED),
                    ft.Divider(color=ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                    info_line("Nombre", sensor["name"]),
                    info_line("Tipo", sensor["type"]),
                    info_line("Ubicacion", sensor["location"]),
                    info_line("Codigo", codigo),
                    info_line("Lectura", lectura),
                    info_line("Actualizado", actualizado),
                    info_line("Fuente", fuente),
                    info_line("Consumo", sensor["power"]),
                    info_line("Estado", status),
                    ft.Container(
                        padding=14,
                        border_radius=20,
                        bgcolor=ft.Colors.with_opacity(0.07, CHAMPAGNE),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.15, CHAMPAGNE)),
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.TOUCH_APP_ROUNDED, color=CHAMPAGNE, size=20),
                                ft.Text("Pulsa un sensor sobre el render para cambiar el detalle.", size=12, color=TEXT_MUTED, expand=True),
                            ],
                            spacing=10,
                        ),
                    ),
                ],
                spacing=13,
            ),
        )

    def render():
        map_slot.content = build_map()
        detail_slot.content = detail_card()
        try:
            page.update()
        except AssertionError:
            pass

    current_data["rows"] = obtener_datos()
    render()

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
                    border_radius=30,
                    accent=CHAMPAGNE,
                    content=ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Row(
                                        [status_badge("Mapa premium", "gold"), status_badge("Imagen real", "cyan")],
                                        spacing=10,
                                        wrap=True,
                                    ),
                                    ft.Text("Mapa de sensores", size=34, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    ft.Text("Dashboard del render 3D con detalle operativo por sensor.", size=15, color=TEXT_MUTED),
                                ],
                                spacing=6,
                            ),
                            ft.Row(
                                [
                                    primary_button("Refrescar", icon=ft.Icons.REFRESH_ROUNDED, on_click=refrescar),
                                    secondary_button("Volver al panel", icon=ft.Icons.ARROW_BACK_ROUNDED, on_click=lambda e: go(ruta_dashboard_por_rol())),
                                ],
                                spacing=12,
                                wrap=True,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(height=18),
                ft.ResponsiveRow(
                    [
                        ft.Container(col={"xs": 12, "lg": 8}, content=map_slot),
                        ft.Container(col={"xs": 12, "lg": 4}, content=detail_slot),
                    ],
                    spacing=18,
                    run_spacing=18,
                ),
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    return ft.View(
        route="/admin_mapa_sensores",
        controls=[contenido],
        padding=0,
        spacing=0,
    )
