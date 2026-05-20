import asyncio
import flet as ft
from controllers.sensor_controller import SensorController


class EmpleadoSensoresView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/empleado_sensores", padding=0, spacing=0)
        self._page = page
        self.go = go
        self.controller = SensorController()
        self._running = False

        self.temp_text = ft.Text("—", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.hum_text = ft.Text("—", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.aire_text = ft.Text("—", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.dist_text = ft.Text("—", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.luz_text = ft.Text("—", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.intensidad_text = ft.Text("—", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.nevera_text = ft.Text("—", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.ultima_actualizacion = ft.Text("Última actualización: —", size=13, color=ft.Colors.WHITE70)

        self.detalle_column = ft.Column(spacing=10)

        self.controls = self._build_ui()

    def _sensor_card(self, titulo: str, valor_widget: ft.Text, icono):
        return ft.Container(
            col={"xs": 12, "sm": 6, "md": 4, "lg": 3},
            padding=18,
            border_radius=20,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                width=44,
                                height=44,
                                border_radius=14,
                                bgcolor=ft.Colors.with_opacity(0.14, ft.Colors.CYAN_300),
                                alignment=ft.alignment.center,
                                content=ft.Icon(icono, color="#9CEBFF", size=22),
                            ),
                            ft.Text(
                                titulo,
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                        ],
                        spacing=10,
                    ),
                    ft.Container(height=8),
                    valor_widget,
                ],
                spacing=8,
            ),
        )

    def _build_ui(self):
        contenido = ft.Container(
            expand=True,
            padding=24,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, -1),
                end=ft.Alignment(1, 1),
                colors=["#050A12", "#09172A", "#0B2342", "#0E2F55"],
            ),
            content=ft.Column(
                [
                    ft.Container(
                        width=1180,
                        padding=22,
                        border_radius=24,
                        bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
                        content=ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Text(
                                            "Estado de sensores",
                                            size=30,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE,
                                        ),
                                        ft.Text(
                                            "Vista de consulta para el empleado. Solo muestra el estado actual de los sensores del sistema.",
                                            size=14,
                                            color=ft.Colors.WHITE70,
                                        ),
                                        self.ultima_actualizacion,
                                    ],
                                    spacing=6,
                                ),
                                ft.Row(
                                    [
                                        ft.OutlinedButton(
                                            "Volver al panel",
                                            icon=ft.Icons.ARROW_BACK_ROUNDED,
                                            style=ft.ButtonStyle(
                                                color=ft.Colors.WHITE,
                                                side=ft.BorderSide(1.1, ft.Colors.with_opacity(0.28, ft.Colors.WHITE)),
                                                shape=ft.RoundedRectangleBorder(radius=16),
                                            ),
                                            on_click=lambda e: self.go("/panel_empleado"),
                                        ),
                                        ft.ElevatedButton(
                                            "Refrescar",
                                            icon=ft.Icons.REFRESH_ROUNDED,
                                            bgcolor="#64D7FF",
                                            color=ft.Colors.BLACK,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=16),
                                            ),
                                            on_click=self.refrescar_datos,
                                        ),
                                    ],
                                    spacing=12,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                    ft.Container(height=18),
                    ft.ResponsiveRow(
                        [
                            self._sensor_card("Temperatura", self.temp_text, ft.Icons.THERMOSTAT_ROUNDED),
                            self._sensor_card("Humedad", self.hum_text, ft.Icons.WATER_DROP_ROUNDED),
                            self._sensor_card("Calidad del aire", self.aire_text, ft.Icons.AIR_ROUNDED),
                            self._sensor_card("Distancia", self.dist_text, ft.Icons.STRAIGHTEN_ROUNDED),
                            self._sensor_card("Luz", self.luz_text, ft.Icons.LIGHTBULB_ROUNDED),
                            self._sensor_card("Intensidad luz", self.intensidad_text, ft.Icons.TUNE_ROUNDED),
                            self._sensor_card("Nevera", self.nevera_text, ft.Icons.KITCHEN_ROUNDED),
                        ],
                        spacing=16,
                        run_spacing=16,
                    ),
                    ft.Container(height=16),
                    ft.Container(
                        width=1180,
                        padding=18,
                        border_radius=20,
                        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Detalle técnico",
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                                self.detalle_column,
                            ],
                            spacing=12,
                        ),
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

        return [contenido]

    def did_mount(self):
        self._running = True
        self.refrescar_datos(None)
        self._page.run_task(self._auto_refresh)

    def will_unmount(self):
        self._running = False

    async def _auto_refresh(self):
        while self._running:
            await asyncio.sleep(3)
            if self._running:
                self.refrescar_datos(None)

    def refrescar_datos(self, e):
        estados = self.controller.obtener_estados_actuales_db()

        temp = estados.get("TEMP_AIR")
        hum = estados.get("HUM_AIR")
        aire = estados.get("MQ135_AIR")
        dist = estados.get("DISTANCE_CM")
        luz = estados.get("LIGHT_STATE")
        intensidad = estados.get("LIGHT_INTENSITY")
        nevera = estados.get("FRIDGE_TEMP")

        def num(row):
            if row and row.get("numeric_value") is not None:
                return row.get("numeric_value")
            return None

        temp_val = num(temp)
        hum_val = num(hum)
        aire_val = num(aire)
        dist_val = num(dist)
        intensidad_val = num(intensidad)
        nevera_val = num(nevera)

        luz_val = "Sin dato"
        if luz:
            raw = str(luz.get("state_value") or "").strip().lower()
            if raw in ["on", "encendida", "1", "true", "activo"]:
                luz_val = "Encendida"
            elif raw in ["off", "apagada", "0", "false", "inactivo"]:
                luz_val = "Apagada"
            else:
                luz_val = luz.get("state_value") or "Sin dato"

        self.temp_text.value = f"{temp_val} °C" if temp_val is not None else "Sin dato"
        self.hum_text.value = f"{hum_val} %" if hum_val is not None else "Sin dato"
        self.aire_text.value = f"{aire_val} raw" if aire_val is not None else "Sin dato"
        self.dist_text.value = f"{dist_val} cm" if dist_val is not None else "Sin dato"
        self.luz_text.value = luz_val
        self.intensidad_text.value = f"{intensidad_val} %" if intensidad_val is not None else "Sin dato"
        self.nevera_text.value = f"{nevera_val} °C" if nevera_val is not None else "Sin dato"

        ultima = None
        for row in [temp, hum, aire, dist, luz, intensidad, nevera]:
            if row and row.get("updated_at"):
                if ultima is None or row["updated_at"] > ultima:
                    ultima = row["updated_at"]

        self.ultima_actualizacion.value = f"Última actualización: {ultima}" if ultima else "Última actualización: Sin dato"

        self.detalle_column.controls.clear()
        detalles = [
            ("TEMP_AIR", temp),
            ("HUM_AIR", hum),
            ("MQ135_AIR", aire),
            ("DISTANCE_CM", dist),
            ("LIGHT_STATE", luz),
            ("LIGHT_INTENSITY", intensidad),
            ("FRIDGE_TEMP", nevera),
        ]

        for codigo, row in detalles:
            if row:
                texto = (
                    f"{codigo} → value={row.get('state_value')} | "
                    f"numeric={row.get('numeric_value')} | "
                    f"source={row.get('source')} | "
                    f"updated_at={row.get('updated_at')}"
                )
            else:
                texto = f"{codigo} → Sin dato"

            self.detalle_column.controls.append(
                ft.Container(
                    padding=12,
                    border_radius=12,
                    bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.BLACK),
                    content=ft.Text(
                        texto,
                        size=13,
                        color=ft.Colors.WHITE,
                        selectable=True,
                    ),
                )
            )

        self.update()