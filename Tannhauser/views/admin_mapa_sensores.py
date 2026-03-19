import flet as ft
import json


class AdminMapaSensoresView(ft.View):
    """Mapa interactivo de sensores.

    Nota de seguridad: esta vista se protege en main.py para que SOLO el rol
    'administrador' pueda acceder a la ruta.
    """

    def __init__(self, page: ft.Page, go):
        super().__init__(route="/admin_mapa_sensores")
        self._page = page
        self.go = go

        self._search = ft.TextField(
            label="Buscar sensor (tipo o zona)",
            prefix_icon=ft.Icons.SEARCH,
            border_radius=14,
            dense=True,
            on_change=self._on_filter_change,
        )
        self._type_filter = ft.Dropdown(
            label="Filtrar por tipo",
            dense=True,
            border_radius=14,
            on_change=self._on_filter_change,
            options=[],
        )

        # --- Datos (se puede migrar a un JSON externo si lo preferís) ---
        sensors_json = """
        [
            {"x": 900, "y": 780, "type": "Cámara OV2640", "desc": "Entrada principal", "info": {"Ubicación": "Entrada", "Función": "Flujo de personas y seguridad", "Estado": "Activo"}},
            {"x": 500, "y": 780, "type": "Cámara OV2640", "desc": "Cajas", "info": {"Ubicación": "Cajas", "Función": "Supervisión de colas", "Estado": "Activo"}},
            {"x": 930, "y": 500, "type": "DHT22", "desc": "Frutas y Verduras", "info": {"Ubicación": "Frutas", "Temp": "18°C", "Humedad": "70%"}},
            {"x": 80, "y": 300, "type": "DHT11", "desc": "Lácteos", "info": {"Ubicación": "Lácteos", "Temp": "4°C", "Estado": "OK"}},
            {"x": 220, "y": 300, "type": "DHT22", "desc": "Congelados", "info": {"Ubicación": "Congelados", "Temp": "-20°C", "Estado": "OK"}},
            {"x": 380, "y": 80, "type": "DHT11", "desc": "Panadería", "info": {"Ubicación": "Panadería", "Temp": "23°C", "Humedad": "45%"}},
            {"x": 580, "y": 80, "type": "MQ-2", "desc": "Pescadería", "info": {"Ubicación": "Pescadería", "Humo": "Normal", "Alerta": "No"}},
            {"x": 730, "y": 80, "type": "DHT11", "desc": "Carnicería", "info": {"Ubicación": "Carnicería", "Temp": "2°C", "Estado": "OK"}},
            {"x": 880, "y": 80, "type": "DHT11", "desc": "Charcutería", "info": {"Ubicación": "Charcutería", "Temp": "3°C", "Estado": "OK"}},
            {"x": 340, "y": 400, "type": "LDR", "desc": "Pasillo Bebidas", "info": {"Ubicación": "Bebidas", "Luz": "Media", "Iluminación": "Ajustada"}},
            {"x": 410, "y": 400, "type": "LDR", "desc": "Pasillo Secos 1", "info": {"Ubicación": "Secos 1", "Luz": "Alta"}},
            {"x": 490, "y": 400, "type": "HC-SR04", "desc": "Puerta automática", "info": {"Ubicación": "Cerca puerta", "Función": "Apertura automática"}},
            {"x": 560, "y": 400, "type": "LED", "desc": "Pasillo Hogar", "info": {"Ubicación": "Hogar", "Función": "Señalización"}},
            {"x": 710, "y": 400, "type": "LDR", "desc": "Pasillo Secos 2", "info": {"Ubicación": "Secos 2", "Luz": "Baja"}},
            {"x": 150, "y": 780, "type": "G1/2 Caudalímetro", "desc": "Farmacia/Baños", "info": {"Ubicación": "Farmacia", "Consumo agua": "120 L/h"}},
            {"x": 100, "y": 700, "type": "MQ-2", "desc": "Área personal", "info": {"Ubicación": "Baños", "Calidad aire": "Buena"}}
        ]
        """
        self.sensors_data = json.loads(sensors_json)

        # Stack del mapa + lista de marcadores, para poder refrescar al filtrar.
        self._stack = ft.Stack(width=1100, height=800)
        self._markers: list[ft.Control] = []

        # Diálogo modal de detalle
        self._dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Información del Sensor"),
            content=ft.Text("Cargando..."),
            actions=[
                ft.TextButton("Cerrar", on_click=self._close_dlg),
            ],
        )
        self._page.overlay.append(self._dlg)

        self._sensor_list = ft.Column(spacing=8, scroll=ft.ScrollMode.AUTO)

        # Construcción UI
        self._build()

    # ---------------- UI helpers ----------------
    def _build(self):
        # Opciones del filtro por tipo
        tipos = sorted({s["type"] for s in self.sensors_data})
        self._type_filter.options = [ft.dropdown.Option("(Todos)")] + [ft.dropdown.Option(t) for t in tipos]
        self._type_filter.value = "(Todos)"

        header = ft.Container(
            padding=16,
            border_radius=18,
            bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.CYAN_900),
            border=ft.border.all(1, ft.Colors.CYAN_700),
            content=ft.Row(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.MAP, size=34, color=ft.Colors.CYAN_200),
                            ft.Column(
                                spacing=2,
                                controls=[
                                    ft.Text(
                                        "Mapa de Sensores IoT",
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.CYAN_100,
                                    ),
                                    ft.Text(
                                        "Vista de planta + puntos interactivos · Solo Administrador",
                                        size=12,
                                        color=ft.Colors.WHITE70,
                                    ),
                                ],
                            ),
                        ],
                        spacing=12,
                    ),
                    ft.Row(
                        controls=[
                            ft.ElevatedButton(
                                "Volver",
                                icon=ft.Icons.ARROW_BACK,
                                on_click=lambda e: self.go("/panel_admin"),
                            ),
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        )

        sidebar = ft.Container(
            width=360,
            padding=14,
            border_radius=18,
            bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.BLUE_GREY_900),
            border=ft.border.all(1, ft.Colors.BLUE_GREY_700),
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Text("Filtros", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_100),
                    self._search,
                    self._type_filter,
                    ft.Divider(height=10),
                    ft.Row(
                        controls=[
                            ft.Container(width=14, height=14, bgcolor=ft.Colors.RED_400, border_radius=7),
                            ft.Text("Sensor (clic para detalle)", color=ft.Colors.WHITE70, size=12),
                        ],
                        spacing=8,
                    ),
                    ft.Divider(height=10),
                    ft.Text("Sensores", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_100),
                    self._sensor_list,
                ],
            ),
        )

        map_container = ft.Container(
            expand=True,
            padding=12,
            border_radius=18,
            bgcolor=ft.Colors.with_opacity(0.06, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.BLUE_GREY_600),
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=12,
                color=ft.Colors.with_opacity(0.25, ft.Colors.BLACK),
                offset=ft.Offset(0, 6),
            ),
            content=self._stack,
        )

        body = ft.Row(
            controls=[sidebar, map_container],
            spacing=14,
            expand=True,
        )

        self.controls = [
            ft.Container(
                expand=True,
                padding=16,
                content=ft.Column(
                    controls=[
                        header,
                        ft.Container(height=12),
                        body,
                    ],
                    expand=True,
                ),
            )
        ]

        self._render_map_base()
        self._render_sensors()

    def _render_map_base(self):
        """Dibuja la planta/base del supermercado (sin marcadores)."""
        self._stack.controls.clear()

        # Fondo + borde exterior
        self._stack.controls.append(
            ft.Container(
                width=1100,
                height=800,
                border_radius=16,
                bgcolor="#FFFFFF",
            )
        )
        self._stack.controls.append(
            ft.Container(
                width=1100,
                height=800,
                border_radius=16,
                border=ft.border.all(4, ft.Colors.BLACK),
            )
        )

        # Sección superior (zona mostradores)
        self._stack.controls.append(
            ft.Container(left=180, top=20, width=840, height=120, bgcolor="#F6F7F9", border_radius=10)
        )

        def zona(left, top, w, h, color, text, size=14):
            return ft.Container(
                left=left,
                top=top,
                width=w,
                height=h,
                bgcolor=color,
                border_radius=10,
                border=ft.border.all(1, ft.Colors.with_opacity(0.25, ft.Colors.BLACK)),
                content=ft.Container(
                    padding=8,
                    content=ft.Text(
                        text,
                        weight=ft.FontWeight.BOLD,
                        size=size,
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.BLACK,
                    ),
                    alignment=ft.alignment.center,
                ),
            )

        # Zonas
        self._stack.controls.append(zona(180, 20, 210, 120, "#FFE7C2", "PANADERÍA\nY PASTELERÍA"))
        self._stack.controls.append(zona(390, 20, 210, 120, "#D6ECFF", "PESCADERÍA", 16))
        self._stack.controls.append(zona(600, 20, 210, 120, "#FFD6D8", "CARNICERÍA", 16))
        self._stack.controls.append(zona(810, 20, 210, 120, "#FFD7EA", "CHARCUTERÍA", 16))
        self._stack.controls.append(zona(850, 160, 220, 440, "#DDF5DF", "FRUTAS\nY VERDURAS", 18))
        self._stack.controls.append(zona(40, 160, 140, 300, "#D7F6FF", "LÁCTEOS\nY REFRIG.", 12))
        self._stack.controls.append(zona(190, 160, 140, 300, "#E3E6FF", "CONGELADOS", 14))
        self._stack.controls.append(zona(40, 620, 280, 140, "#D2F3ED", "COSMÉTICA\nY FARMACIA", 18))
        self._stack.controls.append(zona(400, 650, 350, 100, "#DDF5DF", "CAJAS", 24))

        # Pasillos centrales (7)
        for i in range(7):
            x = 350 + i * 100
            self._stack.controls.append(
                ft.Container(
                    left=x,
                    top=160,
                    width=70,
                    height=400,
                    bgcolor="#A6B3BA",
                    border_radius=8,
                    border=ft.border.all(2, "#4B5C63"),
                )
            )

        etiquetas = ["BEBIDAS", "ALIM. SECOS", "LIMPIEZA", "HOGAR", "HOGAR", "ALIM. SECOS", "ALIM. SECOS"]
        for i, etiqueta in enumerate(etiquetas):
            self._stack.controls.append(
                ft.Text(
                    etiqueta,
                    left=356 + i * 100,
                    top=570,
                    size=11,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLACK,
                )
            )

        # Entrada + flechas
        self._stack.controls.append(ft.Text("ENTRADA", left=900, top=700, size=22, weight=ft.FontWeight.BOLD, color="#1E88E5"))
        self._stack.controls.append(ft.Text("→", left=100, top=450, size=46, color="#9E9E9E"))
        self._stack.controls.append(ft.Text("→", left=750, top=600, size=46, color="#9E9E9E"))
        self._stack.controls.append(ft.Text("↓", left=500, top=750, size=46, color="#9E9E9E"))

    def _render_sensors(self):
        """Renderiza marcadores + lista lateral aplicando filtros."""
        # Limpia marcadores antiguos
        for m in self._markers:
            if m in self._stack.controls:
                self._stack.controls.remove(m)
        self._markers.clear()
        self._sensor_list.controls.clear()

        query = (self._search.value or "").strip().lower()
        tipo = self._type_filter.value

        def visible(sensor: dict) -> bool:
            if tipo and tipo != "(Todos)" and sensor["type"] != tipo:
                return False
            if query:
                hay = f"{sensor['type']} {sensor['desc']}".lower()
                if query not in hay:
                    return False
            return True

        sensores = [s for s in self.sensors_data if visible(s)]

        # Lista lateral
        for s in sensores:
            self._sensor_list.controls.append(self._sensor_tile(s))

        # Marcadores
        for sensor in sensores:
            self._markers.append(self._sensor_marker(sensor))
        self._stack.controls.extend(self._markers)

        self._page.update()

    def _sensor_tile(self, sensor: dict) -> ft.Control:
        return ft.Container(
            padding=10,
            border_radius=14,
            bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.BLUE_GREY_800),
            border=ft.border.all(1, ft.Colors.BLUE_GREY_700),
            ink=True,
            on_click=lambda e, s=sensor: self._show_info(s),
            content=ft.Row(
                spacing=10,
                controls=[
                    ft.Container(width=12, height=12, bgcolor=ft.Colors.RED_400, border_radius=6),
                    ft.Column(
                        spacing=0,
                        expand=True,
                        controls=[
                            ft.Text(sensor["desc"], size=13, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Text(sensor["type"], size=11, color=ft.Colors.WHITE70),
                        ],
                    ),
                    ft.Icon(ft.Icons.CHEVRON_RIGHT, size=18, color=ft.Colors.WHITE54),
                ],
            ),
        )

    def _sensor_marker(self, sensor: dict) -> ft.Control:
        # Círculo con borde + pequeño brillo
        return ft.Container(
            left=sensor["x"] - 16,
            top=sensor["y"] - 16,
            width=32,
            height=32,
            border_radius=16,
            bgcolor=ft.Colors.RED_500,
            border=ft.border.all(2, ft.Colors.WHITE),
            tooltip=f"{sensor['type']}\n{sensor['desc']}",
            ink=True,
            on_click=lambda e, s=sensor: self._show_info(s),
            content=ft.Icon(ft.Icons.SENSORS, size=16, color=ft.Colors.WHITE),
            alignment=ft.alignment.center,
        )

    # ---------------- events ----------------
    def _close_dlg(self, e=None):
        self._dlg.open = False
        self._page.update()

    def _show_info(self, sensor: dict):
        details = "\n".join([f"{k}: {v}" for k, v in sensor.get("info", {}).items()])
        self._dlg.title = ft.Text(f"{sensor['type']} · {sensor['desc']}")
        self._dlg.content = ft.Text(details or "Sin detalles", size=14)
        self._dlg.open = True
        self._page.update()

    def _on_filter_change(self, e=None):
        self._render_sensors()
