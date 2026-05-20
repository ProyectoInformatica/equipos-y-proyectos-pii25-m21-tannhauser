import flet as ft
from models.session_manager import get_current_user, set_current_user


def PanelAdminView(page: ft.Page, go):
    usuario = get_current_user() or {}
    nombre = usuario.get("nombre", "Administrador")

    def cerrar_sesion(e):
        set_current_user(None)
        go("/")

    def card_opcion(icono, titulo, texto, ruta, color_icono="#9CEBFF"):
        return ft.Container(
            width=320,
            padding=24,
            border_radius=26,
            bgcolor=ft.Colors.with_opacity(0.11, ft.Colors.BLACK),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=16,
                color=ft.Colors.with_opacity(0.10, ft.Colors.BLACK),
                offset=ft.Offset(0, 8),
            ),
            content=ft.Column(
                [
                    ft.Container(
                        width=56,
                        height=56,
                        border_radius=18,
                        bgcolor=ft.Colors.with_opacity(0.14, ft.Colors.CYAN_300),
                        alignment=ft.Alignment.CENTER,
                        content=ft.Icon(icono, size=30, color=color_icono),
                    ),
                    ft.Text(
                        titulo,
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        texto,
                        size=14,
                        color=ft.Colors.WHITE70,
                    ),
                    ft.Container(height=4),
                    ft.Button(
                        "Abrir",
                        icon=ft.Icons.ARROW_FORWARD_ROUNDED,
                        bgcolor="#64D7FF",
                        color=ft.Colors.BLACK,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=16),
                        ),
                        on_click=lambda e: go(ruta),
                    ),
                ],
                spacing=14,
            ),
        )

    header = ft.Container(
        width=1180,
        padding=ft.Padding(28, 22, 28, 22),
        border_radius=28,
        bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
        content=ft.Row(
            [
                ft.Row(
                    [
                        ft.Container(
                            width=72,
                            height=72,
                            border_radius=22,
                            bgcolor=ft.Colors.with_opacity(0.94, ft.Colors.WHITE),
                            padding=10,
                            content=ft.Image(
                                src="assets/logo_tannhauser.png",
                                fit=ft.BoxFit.CONTAIN,
                            ),
                        ),
                        ft.Column(
                            [
                                ft.Text(
                                    "Centro de administración",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                                ft.Text(
                                    f"Bienvenido, {nombre}",
                                    size=15,
                                    color=ft.Colors.WHITE70,
                                ),
                            ],
                            spacing=4,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    spacing=18,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.OutlinedButton(
                            "Volver al inicio",
                            icon=ft.Icons.HOME_ROUNDED,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                side=ft.BorderSide(
                                    1.1,
                                    ft.Colors.with_opacity(0.28, ft.Colors.WHITE),
                                ),
                                shape=ft.RoundedRectangleBorder(radius=16),
                            ),
                            on_click=lambda e: go("/"),
                        ),
                        ft.Button(
                            "Cerrar sesión",
                            icon=ft.Icons.LOGOUT_ROUNDED,
                            bgcolor="#64D7FF",
                            color=ft.Colors.BLACK,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=16),
                            ),
                            on_click=cerrar_sesion,
                        ),
                    ],
                    spacing=12,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    resumen = ft.Container(
        width=1180,
        padding=28,
        border_radius=28,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
        content=ft.Row(
            [
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        [
                            ft.Text(
                                "Control ejecutivo de la plataforma",
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                "Gestiona usuarios, sensores, actividad, inventario, alertas, cámara y estadísticas desde un panel moderno y unificado. El administrador dispone de control operativo completo, salvo la creación de nuevos administradores o superusuarios.",
                                size=16,
                                color=ft.Colors.WHITE70,
                                width=760,
                            ),
                        ],
                        spacing=12,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                ),
                ft.Container(
                    width=280,
                    padding=22,
                    border_radius=24,
                    bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.BLACK),
                    border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Column(
                        [
                            ft.Text("Nivel de acceso", size=14, color=ft.Colors.WHITE60),
                            ft.Text(
                                "Administrador",
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color="#9CEBFF",
                            ),
                            ft.Text(
                                "Acceso completo de gestión y supervisión, con restricciones sobre la creación de roles administrativos superiores.",
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
                "Consulta y administra cuentas del sistema. No permite crear administradores ni superusuarios.",
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
                ft.Icons.QUERY_STATS_ROUNDED,
                "Estadísticas",
                "Consulta métricas, consumo y datos agregados de sensores reales.",
                "/estadisticas_sensores",
            ),
            card_opcion(
                ft.Icons.MAP_ROUNDED,
                "Mapa de sensores",
                "Visualiza el estado de sensores dentro del sistema.",
                "/admin_mapa_sensores",
            ),
            card_opcion(
                ft.Icons.VIDEOCAM_ROUNDED,
                "Cámara",
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
                "Consulta alertas activas, historial y acceso rápido al sensor afectado.",
                "/admin_alertas",
            ),
            card_opcion(
                ft.Icons.TUNE_ROUNDED,
                "Umbrales",
                "Configura reglas y niveles de disparo de alertas automáticas.",
                "/admin_umbrales",
            ),
        ],
        wrap=True,
        spacing=20,
        run_spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
    )

    contenido = ft.Container(
        expand=True,
        padding=30,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=[
                "#050A12",
                "#09172A",
                "#0B2342",
                "#0E2F55",
            ],
        ),
        content=ft.Column(
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
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
        ),
    )

    return ft.View(
        route="/panel_admin",
        controls=[contenido],
        padding=0,
        spacing=0,
    )