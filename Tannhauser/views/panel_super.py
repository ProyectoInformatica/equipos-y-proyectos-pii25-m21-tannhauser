import flet as ft
from models.session_manager import clear_current_user


def PanelSuperView(page: ft.Page, go):
    titulo = ft.Text("Panel de Superusuario", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_100)
    subtitulo = ft.Text(
        "Desde aquí se podrán gestionar administradores, configuración global, etc.",
        size=15,
        color=ft.Colors.GREY_300,
    )

    btn_ir_admin = ft.ElevatedButton(
        "Ir al Panel de Administración",
        icon=ft.Icons.ADMIN_PANEL_SETTINGS,
        style=ft.ButtonStyle(
            bgcolor={ft.ControlState.DEFAULT: ft.Colors.PURPLE_400},
            color={ft.ControlState.DEFAULT: ft.Colors.BLACK},
            shape=ft.RoundedRectangleBorder(radius=20),
        ),
        on_click=lambda e: go("/panel_admin"),
    )

    btn_logout = ft.ElevatedButton(
        "Cerrar sesión",
        icon=ft.Icons.LOGOUT,
        style=ft.ButtonStyle(
            bgcolor={ft.ControlState.DEFAULT: ft.Colors.RED_400},
            color={ft.ControlState.DEFAULT: ft.Colors.WHITE},
            shape=ft.RoundedRectangleBorder(radius=20),
        ),
        on_click=lambda e: (clear_current_user(), go("/")),
    )

    contenido = ft.Container(
        expand=True,
        padding=30,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=[ft.Colors.DEEP_PURPLE_900, ft.Colors.BLACK],
        ),
        content=ft.Column(
            [
                titulo,
                subtitulo,
                ft.Container(
                    content=ft.Text("Opciones avanzadas (en construcción)...", color=ft.Colors.GREY_400),
                    padding=20,
                    border_radius=15,
                    bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.BLUE_GREY_800),
                ),
                ft.Container(height=20),
                btn_ir_admin,
                ft.Container(height=10),
                    ft.ElevatedButton(
                        "Eliminar Usuario",
                        icon=ft.Icons.DELETE,
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.DEFAULT: ft.Colors.RED_700},
                            color={ft.ControlState.DEFAULT: ft.Colors.WHITE},
                            shape=ft.RoundedRectangleBorder(radius=20),
                        ),
                        on_click=lambda e: go("/admin_eliminar_usuario"),
                    ),
                ft.ElevatedButton(
                    "Ver Inventario",
                    icon=ft.Icons.INVENTORY_2,
                    style=ft.ButtonStyle(
                        bgcolor={ft.ControlState.DEFAULT: ft.Colors.GREEN_400},
                        color={ft.ControlState.DEFAULT: ft.Colors.BLACK},
                        shape=ft.RoundedRectangleBorder(radius=20),
                    ),
                    on_click=lambda e: go("/inventario"),
                ),
                ft.ElevatedButton(
                    "📊 Estadísticas de Sensores",
                    icon=ft.Icons.ANALYTICS,
                    style=ft.ButtonStyle(
                        bgcolor={ft.ControlState.DEFAULT: ft.Colors.CYAN_400},
                        color={ft.ControlState.DEFAULT: ft.Colors.BLACK},
                        shape=ft.RoundedRectangleBorder(radius=20),
                    ),
                    on_click=lambda e: go("/estadisticas_sensores"),
                ),
                ft.Container(height=10),
                btn_logout,
            ],
            spacing=12,
        ),
    )

    return ft.View(
        route="/panel_super",
        controls=[contenido],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
    )

