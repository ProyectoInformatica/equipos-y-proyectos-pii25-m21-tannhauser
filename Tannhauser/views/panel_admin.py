import flet as ft
from controllers.sensor_controller import SensorController
from controllers.user_controller import UserController
from models.session_manager import clear_current_user
from models.session_manager import get_current_user


class PanelAdminView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/panel_admin")
        self._page = page
        self.go = go
        self.sensor_controller = SensorController()
        self.user_controller = UserController()
        self.construir_ui()

    def construir_ui(self):
        titulo = ft.Text(
            "Panel del Administrador",
            size=32,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.CYAN_200,
            text_align=ft.TextAlign.CENTER,
        )

        subtitulo = ft.Text(
            "Herramientas administrativas y monitorización del sistema",
            size=17,
            color=ft.Colors.WHITE70,
            text_align=ft.TextAlign.CENTER,
        )

        tarjeta_aire = self._tarjeta(
            "Sensores del Aire",
            "Temperatura, humedad y puertas",
            ft.Icons.AIR,
            "/sensores_aire",
        )

        tarjeta_luz = self._tarjeta(
            "Luces",
            "Intensidad y encendido",
            ft.Icons.LIGHT_MODE,
            "/sensores_luz",
        )

        tarjeta_nevera = self._tarjeta(
            "Nevera Inteligente",
            "Temperatura interna y estado",
            ft.Icons.KITCHEN,
            "/sensores_nevera",
        )

        tarjeta_puerta = self._tarjeta(
            "Sensor de Puerta",
            "Monitorización de acceso",
            ft.Icons.DOOR_FRONT_DOOR,
            "/sensores_puerta",
        )

        tarjeta_usuarios = self._tarjeta(
            "Gestión de Usuarios",
            "Ver y modificar usuarios registrados",
            ft.Icons.GROUP,
            "/admin_usuarios",
        )

        tarjeta_logs = self._tarjeta(
            "Actividad del Sistema",
            "Registros y logs recientes",
            ft.Icons.LIST_ALT,
            "/admin_logs",
        )

        tarjeta_simulacion = self._tarjeta(
            "Simulación Global",
            "Controlar simulación de sensores",
            ft.Icons.PLAY_CIRCLE,
            "/admin_simulacion",
        )

        tarjeta_inventario = self._tarjeta(
            "Inventario",
            "Ver stock y existencias",
            ft.Icons.INVENTORY_2,
            "/inventario_edit",
        )

        tarjeta_eliminar = self._tarjeta(
            "Eliminar Usuario",
            "Eliminar usuario por nombre o email",
            ft.Icons.DELETE,
            "/admin_eliminar_usuario",
        )

        tarjeta_estadisticas = self._tarjeta(
            "📊 Estadísticas de Sensores",
            "Análisis y monitoreo de datos",
            ft.Icons.ANALYTICS,
            "/estadisticas_sensores",
        )

        # SOLO el rol administrador verá el acceso al mapa
        current = get_current_user()
        tarjeta_mapa = None
        if current and current.get("rol") == "administrador":
            tarjeta_mapa = self._tarjeta(
                "🗺️ Mapa de Sensores",
                "Planta del súper con puntos IoT",
                ft.Icons.MAP,
                "/admin_mapa_sensores",
            )

        boton_logout = ft.ElevatedButton(
            "Cerrar Sesión",
            icon=ft.Icons.LOGOUT,
            bgcolor=ft.Colors.RED_600,
            on_click=lambda e: self._logout(e),
            width=220,
        )

        self.controls = [
            ft.Column(
                controls=[
                    titulo,
                    subtitulo,
                    ft.Divider(height=10),
                    ft.Row(
                        [tarjeta_aire, tarjeta_luz, tarjeta_nevera, tarjeta_puerta],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                        wrap=True,
                    ),
                    ft.Divider(height=10),
                    ft.Row(
                        [tarjeta_usuarios, tarjeta_logs, tarjeta_simulacion, tarjeta_inventario, tarjeta_eliminar],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                        wrap=True,
                    ),
                    ft.Divider(height=10),
                    ft.Row(
                        [c for c in [tarjeta_estadisticas, tarjeta_mapa] if c is not None],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    ft.Divider(height=10),
                    boton_logout,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
                scroll=ft.ScrollMode.AUTO,
            )
        ]

    def _tarjeta(self, titulo, descripcion, icono, ruta):
        return ft.Container(
            width=200,
            height=160,
            padding=15,
            border_radius=20,
            bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.BLUE_GREY_800),
            border=ft.border.all(2, ft.Colors.CYAN_300),
            ink=True,
            on_click=lambda e: self.go(ruta),
            content=ft.Column(
                [
                    ft.Icon(icono, size=45, color=ft.Colors.CYAN_200),
                    ft.Text(titulo, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text(
                        descripcion,
                        size=12,
                        color=ft.Colors.WHITE70,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
            ),
        )

    def _logout(self, e=None):
        clear_current_user()
        self.go("/")
