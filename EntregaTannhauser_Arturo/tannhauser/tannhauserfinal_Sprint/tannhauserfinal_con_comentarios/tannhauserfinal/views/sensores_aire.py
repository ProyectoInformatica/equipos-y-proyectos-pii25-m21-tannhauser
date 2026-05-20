import flet as ft
from controllers.sensor_controller import SensorController


class SensoresAireView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/sensores_aire")
        self._page = page
        self.controller = SensorController()

        self.temp_text = ft.Text("—", size=24, weight=ft.FontWeight.BOLD)
        self.hum_text = ft.Text("—", size=24, weight=ft.FontWeight.BOLD)
        self.aire_text = ft.Text("—", size=24, weight=ft.FontWeight.BOLD)

        self.controls = self.construir_ui()

    def tarjeta(self, titulo: str, icono, valor_widget: ft.Text):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(icono, size=28),
                            ft.Text(titulo, size=18, weight=ft.FontWeight.BOLD),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Divider(),
                    ft.Container(
                        content=valor_widget,
                        alignment=ft.Alignment.CENTER,
                        padding=10,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
            padding=20,
            border_radius=16,
            bgcolor=ft.Colors.BLUE_50,
            expand=True,
        )

    def construir_ui(self):
        return [
            ft.AppBar(
                title=ft.Text("Sensores de Aire"),
                center_title=True,
                bgcolor=ft.Colors.BLUE_200,
                leading=ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    on_click=lambda e: self._page.go("/principal"),
                ),
            ),
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            "Lecturas actuales del sistema",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            "Datos leídos desde la base de datos (current_state)",
                            size=14,
                            color=ft.Colors.GREY_700,
                        ),
                        ft.ResponsiveRow(
                            [
                                self.tarjeta("Temperatura", ft.Icons.THERMOSTAT, self.temp_text),
                                self.tarjeta("Humedad", ft.Icons.WATER_DROP, self.hum_text),
                                self.tarjeta("Calidad del aire", ft.Icons.AIR, self.aire_text),
                            ],
                            spacing=20,
                            run_spacing=20,
                        ),
                        ft.Row(
                            [
                                ft.Button(
                                    "Refrescar datos",
                                    icon=ft.Icons.REFRESH,
                                    on_click=self.refrescar_datos,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    spacing=20,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=20,
                expand=True,
            ),
        ]

    def did_mount(self):
        self.refrescar_datos(None)

    def refrescar_datos(self, e):
        estados = self.controller.obtener_estados_actuales_db()

        temp = estados.get("TEMP_AIR")
        hum = estados.get("HUM_AIR")
        aire = estados.get("MQ135_AIR")

        if temp and temp.get("numeric_value") is not None:
            self.temp_text.value = f"{temp['numeric_value']} °C"
        else:
            self.temp_text.value = "Sin dato"

        if hum and hum.get("numeric_value") is not None:
            self.hum_text.value = f"{hum['numeric_value']} %"
        else:
            self.hum_text.value = "Sin dato"

        if aire and aire.get("numeric_value") is not None:
            self.aire_text.value = f"{aire['numeric_value']} raw"
        else:
            self.aire_text.value = "Sin dato"

        self.update()