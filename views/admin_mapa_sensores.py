import flet as ft
from controllers.sensor_controller import SensorController
from utils.navigation import ruta_dashboard_por_rol
from utils.ui_premium import premium_empty_state, primary_button, secondary_button


def AdminMapaSensoresView(page: ft.Page, go):
    controller = SensorController()
    sensores_column = ft.Column(spacing=14)

    def refrescar():
        sensores_column.controls.clear()

        datos = {}
        if hasattr(controller, "obtener_estados_actuales_db"):
            datos = controller.obtener_estados_actuales_db() or {}

        if not datos:
            sensores_column.controls.append(
                premium_empty_state("No hay estados de sensores disponibles.", ft.Icons.SENSORS_OFF_ROUNDED, width=1180)
            )
        else:
            for codigo, row in datos.items():
                sensores_column.controls.append(
                    ft.Container(
                        width=1180,
                        padding=18,
                        border_radius=20,
                        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                        content=ft.Column(
                            [
                                ft.Text(
                                    codigo,
                                    size=18,
                                    weight=ft.FontWeight.BOLD,
                                    color="#9CEBFF",
                                ),
                                ft.Text(
                                    f"Valor: {row.get('state_value')} | Numérico: {row.get('numeric_value')}",
                                    color=ft.Colors.WHITE,
                                ),
                                ft.Text(
                                    f"Actualizado: {row.get('updated_at')} | Fuente: {row.get('source')}",
                                    color=ft.Colors.WHITE70,
                                    size=13,
                                ),
                            ],
                            spacing=6,
                        ),
                    )
                )

        page.update()

    refrescar()

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
                                        "Mapa de sensores",
                                        size=34,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                        "Vista general del estado actual de los sensores del supermercado.",
                                        size=15,
                                        color=ft.Colors.WHITE70,
                                    ),
                                ],
                                spacing=6,
                            ),
                            ft.Row(
                                [
                                    primary_button(
                                        "Refrescar",
                                        icon=ft.Icons.REFRESH_ROUNDED,
                                        on_click=lambda e: refrescar(),
                                    ),
                                    secondary_button(
                                        "Volver al panel",
                                        icon=ft.Icons.ARROW_BACK_ROUNDED,
                                        on_click=lambda e: go(ruta_dashboard_por_rol()),
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
                sensores_column,
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
