import flet as ft
from controllers.alerta_controller import AlertaController
from models.session_manager import get_current_user
from utils.navigation import ruta_dashboard_por_rol


def AdminAlertasView(page: ft.Page, go):
    controller = AlertaController()
    usuario = get_current_user() or {}
    rol = usuario.get("rol", "administrador")

    alertas_activas_column = ft.Column(spacing=14)
    historial_column = ft.Column(spacing=14)

    def mostrar_mensaje(msg, error=False):
        page.snack_bar = ft.SnackBar(
            ft.Text(msg),
            bgcolor=ft.Colors.RED_600 if error else ft.Colors.GREEN_600,
        )
        page.snack_bar.open = True
        page.update()

    def color_severity(sev):
        sev = (sev or "info").lower()
        if sev == "critical":
            return "#F87171"
        if sev == "warning":
            return "#FBBF24"
        return "#67E8F9"

    def ir_sensor(evento):
        ruta = controller.ruta_para_evento(evento, rol)
        go(ruta)

    def resolver_alerta(alerta_id):
        if not hasattr(controller, "resolver_alerta"):
            mostrar_mensaje("Tu controller actual no tiene implementar resolver_alerta().", error=True)
            return

        ok, msg = controller.resolver_alerta(alerta_id)
        mostrar_mensaje(msg, error=not ok)
        if ok:
            refrescar()

    def _card_alerta(a, activa=True):
        sev = (a.get("severity") or "info").lower()
        color = color_severity(sev)
        titulo = a.get("title") or "Alerta"
        descripcion = a.get("description") or "Sin descripción"
        fecha = str(a.get("event_time") or a.get("created_at") or "Sin fecha")
        sensor = (
            (a.get("payload_json") or {}).get("state_code")
            or a.get("device_code")
            or "Sin dato"
        )

        acciones = [
            ft.OutlinedButton(
                "Ir al sensor",
                icon=ft.Icons.ARROW_FORWARD_ROUNDED,
                style=ft.ButtonStyle(
                    color=ft.Colors.WHITE,
                    side=ft.BorderSide(1.0, ft.Colors.with_opacity(0.22, ft.Colors.WHITE)),
                    shape=ft.RoundedRectangleBorder(radius=14),
                ),
                on_click=lambda e: ir_sensor(a),
            )
        ]

        if activa:
            acciones.append(
                ft.Button(
                    "Resolver",
                    icon=ft.Icons.CHECK_CIRCLE_ROUNDED,
                    bgcolor="#64D7FF",
                    color=ft.Colors.BLACK,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=14),
                    ),
                    on_click=lambda e: resolver_alerta(a.get("id")),
                )
            )

        return ft.Container(
            width=1180,
            padding=20,
            border_radius=22,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.Container(
                                        padding=ft.Padding(12, 6, 12, 6),
                                        border_radius=999,
                                        bgcolor=ft.Colors.with_opacity(0.18, color),
                                        content=ft.Text(
                                            sev.upper(),
                                            size=12,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE,
                                        ),
                                    ),
                                    ft.Text(
                                        titulo,
                                        size=18,
                                        weight=ft.FontWeight.BOLD,
                                        color=color,
                                    ),
                                ],
                                spacing=10,
                            ),
                            ft.Text(
                                fecha,
                                size=12,
                                color=ft.Colors.WHITE54,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Text(
                        descripcion,
                        size=14,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        f"Sensor afectado: {sensor}",
                        size=13,
                        color=ft.Colors.WHITE70,
                    ),
                    ft.Row(
                        acciones,
                        alignment=ft.MainAxisAlignment.END,
                        spacing=10,
                    ),
                ],
                spacing=10,
            ),
        )

    def refrescar():
        alertas_activas_column.controls.clear()
        historial_column.controls.clear()

        activas = []
        historial = []

        if hasattr(controller, "listar_alertas_activas"):
            activas = controller.listar_alertas_activas() or []
        elif hasattr(controller, "obtener_alertas_activas"):
            activas = controller.obtener_alertas_activas() or []

        if hasattr(controller, "listar_historial_alertas"):
            historial = controller.listar_historial_alertas() or []
        elif hasattr(controller, "obtener_historial_alertas"):
            historial = controller.obtener_historial_alertas() or []

        if not activas:
            alertas_activas_column.controls.append(
                ft.Text("No hay alertas activas.", color=ft.Colors.WHITE70)
            )
        else:
            for a in activas:
                alertas_activas_column.controls.append(_card_alerta(a, activa=True))

        if not historial:
            historial_column.controls.append(
                ft.Text("No hay historial de alertas resueltas.", color=ft.Colors.WHITE70)
            )
        else:
            for a in historial:
                historial_column.controls.append(_card_alerta(a, activa=False))

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
                    border=ft.Border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
                    content=ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text(
                                        "Centro de alertas",
                                        size=34,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                        "Consulta alertas activas, resuelve incidencias y revisa el historial.",
                                        size=15,
                                        color=ft.Colors.WHITE70,
                                    ),
                                ],
                                spacing=6,
                            ),
                            ft.Row(
                                [
                                    ft.Button(
                                        "Refrescar",
                                        icon=ft.Icons.REFRESH_ROUNDED,
                                        bgcolor="#64D7FF",
                                        color=ft.Colors.BLACK,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=16),
                                        ),
                                        on_click=lambda e: refrescar(),
                                    ),
                                    ft.OutlinedButton(
                                        "Volver al panel",
                                        icon=ft.Icons.ARROW_BACK_ROUNDED,
                                        style=ft.ButtonStyle(
                                            color=ft.Colors.WHITE,
                                            side=ft.BorderSide(1.1, ft.Colors.with_opacity(0.28, ft.Colors.WHITE)),
                                            shape=ft.RoundedRectangleBorder(radius=16),
                                        ),
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
                ft.Container(
                    width=1180,
                    padding=20,
                    border_radius=24,
                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                    border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Column(
                        [
                            ft.Text("Alertas activas", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            alertas_activas_column,
                        ],
                        spacing=14,
                    ),
                ),
                ft.Container(height=18),
                ft.Container(
                    width=1180,
                    padding=20,
                    border_radius=24,
                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                    border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Column(
                        [
                            ft.Text("Historial de alertas", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            historial_column,
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
        route="/admin_alertas",
        controls=[contenido],
        padding=0,
        spacing=0,
    )