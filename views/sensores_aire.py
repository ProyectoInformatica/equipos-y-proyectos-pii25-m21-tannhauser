import flet as ft
from controllers.sensor_controller import SensorController
from utils.ui_premium import premium_card, premium_header, premium_page, primary_button, secondary_button


class SensoresAireView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/sensores_aire", padding=0, spacing=0)
        self._page = page
        self.controller = SensorController()

        self.temp_text = ft.Text("-", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.hum_text = ft.Text("-", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.aire_text = ft.Text("-", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)

        self.controls = self.construir_ui()

    def tarjeta(self, titulo: str, icono, valor_widget: ft.Text):
        valor_widget.color = ft.Colors.WHITE
        return premium_card(
            col={"xs": 12, "md": 4},
            padding=22,
            border_radius=24,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(icono, size=28, color="#C8F3FF"),
                            ft.Text(titulo, size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Divider(color=ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    ft.Container(content=valor_widget, alignment=ft.alignment.center, padding=10),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
        )

    def construir_ui(self):
        return [
            premium_page(
                [
                    premium_header(
                        "Sensores de aire",
                        "Lecturas actuales desde current_state.",
                        actions=[
                            secondary_button(
                                "Volver",
                                ft.Icons.ARROW_BACK_ROUNDED,
                                on_click=lambda e: self._page.go("/principal"),
                            )
                        ],
                    ),
                    ft.Container(height=18),
                    ft.ResponsiveRow(
                        [
                            self.tarjeta("Temperatura", ft.Icons.THERMOSTAT, self.temp_text),
                            self.tarjeta("Humedad", ft.Icons.WATER_DROP, self.hum_text),
                            self.tarjeta("Calidad del aire", ft.Icons.AIR, self.aire_text),
                        ],
                        spacing=20,
                        run_spacing=20,
                    ),
                    ft.Container(height=16),
                    primary_button("Refrescar datos", ft.Icons.REFRESH_ROUNDED, self.refrescar_datos),
                ]
            ),
        ]

    def did_mount(self):
        self.refrescar_datos(None)

    def refrescar_datos(self, e):
        estados = self.controller.obtener_estados_actuales_db()

        temp = estados.get("TEMP_AIR")
        hum = estados.get("HUM_AIR")
        aire = estados.get("MQ135_AIR")

        self.temp_text.value = f"{temp['numeric_value']} C" if temp and temp.get("numeric_value") is not None else "Sin dato"
        self.hum_text.value = f"{hum['numeric_value']} %" if hum and hum.get("numeric_value") is not None else "Sin dato"
        self.aire_text.value = f"{aire['numeric_value']} raw" if aire and aire.get("numeric_value") is not None else "Sin dato"

        self.update()
