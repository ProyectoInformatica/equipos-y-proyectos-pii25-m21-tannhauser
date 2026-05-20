import flet as ft
from models.db import get_connection
from utils.navigation import ruta_dashboard_por_rol


class AdminLogsView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/admin_logs", padding=0, spacing=0)
        self.page = page
        self.go = go

        self.buscar_input = ft.TextField(
            hint_text="Buscar por acción, mensaje, usuario o nivel...",
            prefix_icon=ft.Icons.SEARCH_ROUNDED,
            border_radius=16,
            width=420,
            bgcolor=ft.Colors.with_opacity(0.06, ft.Colors.WHITE),
            color=ft.Colors.WHITE,
            border_color=ft.Colors.with_opacity(0.18, ft.Colors.WHITE),
            focused_border_color="#64D7FF",
            on_change=self.refrescar_logs,
        )

        self.logs_column = ft.Column(spacing=14)
        self.error_text = ft.Text("", color=ft.Colors.RED_300, size=14)

        self.controls = [self._build_ui()]

    def did_mount(self):
        self.refrescar_logs()

    def _build_ui(self):
        return ft.Container(
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
                                            "Actividad del sistema",
                                            size=34,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE,
                                        ),
                                        ft.Text(
                                            "Registros reales generados por usuarios y sensores del sistema.",
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
                                            on_click=lambda e: self.refrescar_logs(),
                                        ),
                                        ft.OutlinedButton(
                                            "Volver al panel",
                                            icon=ft.Icons.ARROW_BACK_ROUNDED,
                                            style=ft.ButtonStyle(
                                                color=ft.Colors.WHITE,
                                                side=ft.BorderSide(1.1, ft.Colors.with_opacity(0.28, ft.Colors.WHITE)),
                                                shape=ft.RoundedRectangleBorder(radius=16),
                                            ),
                                            on_click=lambda e: self.go(ruta_dashboard_por_rol()),
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
                                ft.Row(
                                    [
                                        ft.Text(
                                            "Registros recientes",
                                            size=22,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE,
                                        ),
                                        self.buscar_input,
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                self.error_text,
                                self.logs_column,
                            ],
                            spacing=16,
                        ),
                    ),
                ],
                spacing=0,
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def _color_nivel(self, nivel: str):
        nivel = (nivel or "").upper()
        if nivel == "ERROR":
            return "#F87171"
        if nivel == "WARNING":
            return "#FBBF24"
        return "#67E8F9"

    def _leer_logs(self):
        conn = get_connection()
        if not conn:
            raise Exception("No se pudo conectar a la base de datos.")

        cursor = None
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT
                    al.id,
                    al.user_id,
                    al.log_level,
                    al.action,
                    al.message,
                    al.logged_at,
                    al.metadata,
                    u.nombre,
                    u.email
                FROM activity_log al
                LEFT JOIN users u ON u.id = al.user_id
                ORDER BY al.logged_at DESC, al.id DESC
                LIMIT 200
            """)
            return cursor.fetchall()
        finally:
            if cursor:
                cursor.close()
            if conn and conn.is_connected():
                conn.close()

    def _card_log(self, log):
        nivel = str(log.get("log_level") or "INFO").upper()
        color_nivel = self._color_nivel(nivel)
        nombre = str(log.get("nombre") or "Sistema")
        email = str(log.get("email") or "sin email")
        accion = str(log.get("action") or "Sin acción")
        mensaje = str(log.get("message") or "Sin mensaje")
        fecha = str(log.get("logged_at") or "Sin fecha")
        metadata = log.get("metadata")

        return ft.Container(
            width=1180,
            padding=18,
            border_radius=20,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.Container(
                                        padding=ft.Padding(12, 6, 12, 6),
                                        border_radius=999,
                                        bgcolor=ft.Colors.with_opacity(0.20, ft.Colors.WHITE),
                                        content=ft.Text(
                                            nivel,
                                            color=ft.Colors.WHITE,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ),
                                    ft.Text(
                                        accion,
                                        size=17,
                                        weight=ft.FontWeight.BOLD,
                                        color=color_nivel,
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
                        f"{nombre} · {email}",
                        size=13,
                        color=ft.Colors.WHITE70,
                    ),
                    ft.Text(
                        mensaje,
                        size=14,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        str(metadata),
                        size=12,
                        color=ft.Colors.WHITE54,
                        selectable=True,
                    ) if metadata else ft.Container(),
                ],
                spacing=8,
            ),
        )

    def refrescar_logs(self, e=None):
        try:
            self.error_text.value = ""
            texto = (self.buscar_input.value or "").strip().lower()
            logs = self._leer_logs()

            if texto:
                filtrados = []
                for log in logs:
                    bloque = " ".join([
                        str(log.get("log_level") or ""),
                        str(log.get("action") or ""),
                        str(log.get("message") or ""),
                        str(log.get("nombre") or ""),
                        str(log.get("email") or ""),
                        str(log.get("metadata") or ""),
                    ]).lower()
                    if texto in bloque:
                        filtrados.append(log)
                logs = filtrados

            self.logs_column.controls.clear()

            if not logs:
                self.logs_column.controls.append(
                    ft.Container(
                        width=1180,
                        padding=24,
                        border_radius=20,
                        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                        border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                        content=ft.Text(
                            "No se han encontrado registros para mostrar.",
                            size=16,
                            color=ft.Colors.WHITE70,
                        ),
                    )
                )
            else:
                for log in logs:
                    self.logs_column.controls.append(self._card_log(log))

            self.update()
        except Exception as ex:
            self.logs_column.controls.clear()
            self.error_text.value = f"Error cargando logs: {ex}"
            self.update()