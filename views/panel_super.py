import flet as ft
from models.session_manager import get_current_user
from utils.ui_premium import (
    premium_page,
    premium_header,
    secondary_button,
    action_card,
    status_badge,
    SURFACE,
)


def PanelSuperView(page: ft.Page, go):
    usuario = get_current_user() or {}
    nombre = usuario.get("nombre", "Superusuario")

    def card_opcion(icono, titulo, texto, ruta):
        return action_card(icono, titulo, texto, "Abrir", on_click=lambda e: go(ruta))

    header = premium_header(
        "Centro de administracion global",
        "Bienvenido",
        name=nombre,
        actions=[
            secondary_button("Mi perfil", ft.Icons.PERSON_ROUNDED, on_click=lambda e: go("/perfil")),
        ],
    )

    resumen = ft.Container(
        width=1180,
        padding=28,
        border_radius=28,
        bgcolor=SURFACE,
        border=ft.border.all(1.1, ft.Colors.with_opacity(0.15, ft.Colors.WHITE)),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=32,
            color=ft.Colors.with_opacity(0.26, ft.Colors.BLACK),
            offset=ft.Offset(0, 16),
        ),
        content=ft.Row(
            [
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    status_badge("Control total", "gold"),
                                    status_badge("Administracion", "cyan"),
                                    status_badge("Energia", "green"),
                                ],
                                spacing=10,
                                wrap=True,
                            ),
                            ft.Text(
                                "Control total de la plataforma",
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                "Administra usuarios, actividad, inventario, sensores, camara, alertas, umbrales y sostenibilidad desde un solo panel.",
                                size=16,
                                color=ft.Colors.WHITE70,
                                width=700,
                            ),
                        ],
                        spacing=12,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                ),
                ft.Container(
                    width=260,
                    padding=22,
                    border_radius=24,
                    bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.BLACK),
                    border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Column(
                        [
                            ft.Text("Nivel de acceso", size=14, color=ft.Colors.WHITE60),
                            ft.Text("Superusuario", size=24, weight=ft.FontWeight.BOLD, color="#9CEBFF"),
                            ft.Text(
                                "Permisos completos sobre la administracion de la plataforma.",
                                size=13,
                                color=ft.Colors.WHITE70,
                            ),
                        ],
                        spacing=8,
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    grid = ft.Row(
        [
            card_opcion(
                ft.Icons.GROUPS_2_ROUNDED,
                "Usuarios",
                "Consulta, crea y administra cuentas y permisos del sistema.",
                "/admin_usuarios",
            ),
            card_opcion(
                ft.Icons.RECEIPT_LONG_ROUNDED,
                "Logs del sistema",
                "Revisa actividad, eventos y trazabilidad operativa.",
                "/admin_logs",
            ),
            card_opcion(
                ft.Icons.INVENTORY_2_ROUNDED,
                "Inventario editable",
                "Actualiza stock y gestiona productos directamente.",
                "/inventario_edit",
            ),
        ],
        wrap=True,
        spacing=20,
        run_spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    grid2 = ft.Row(
        [
            card_opcion(
                ft.Icons.ECO_ROUNDED,
                "Energia y sostenibilidad",
                "Analiza consumo, historico, eficiencia, CO2 y recomendaciones de ahorro.",
                "/energia",
            ),
            card_opcion(
                ft.Icons.MAP_ROUNDED,
                "Mapa de sensores",
                "Visualiza el estado de sensores dentro del sistema.",
                "/admin_mapa_sensores",
            ),
            card_opcion(
                ft.Icons.VIDEOCAM_ROUNDED,
                "Camara",
                "Acceso a la interfaz y al stream de la ESP32-CAM.",
                "/admin_camara",
            ),
        ],
        wrap=True,
        spacing=20,
        run_spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    grid3 = ft.Row(
        [
            card_opcion(
                ft.Icons.NOTIFICATIONS_ACTIVE_ROUNDED,
                "Alertas",
                "Consulta el historial de alertas y accede rapidamente al sensor afectado.",
                "/admin_alertas",
            ),
            card_opcion(
                ft.Icons.TUNE_ROUNDED,
                "Umbrales",
                "Configura los valores que disparan alertas automaticas.",
                "/admin_umbrales",
            ),
        ],
        wrap=True,
        spacing=20,
        run_spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    contenido = premium_page(
        [
            header,
            ft.Container(height=18),
            resumen,
            ft.Container(height=24),
            grid,
            ft.Container(height=20),
            grid2,
            ft.Container(height=20),
            grid3,
        ]
    )

    return ft.View(
        route="/panel_super",
        controls=[contenido],
        padding=0,
        spacing=0,
    )
