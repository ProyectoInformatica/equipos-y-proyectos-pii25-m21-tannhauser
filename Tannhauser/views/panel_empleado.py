import flet as ft
from models.session_manager import clear_current_user
from controllers.sensor_controller import SensorController


class PanelEmpleadoView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/panel_empleado")
        self._page = page
        self.go = go
        self.sensor_controller = SensorController()
        self.construir_ui()

    def construir_ui(self):
        titulo = ft.Text("Panel del Empleado", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_200, text_align=ft.TextAlign.CENTER)
        subtitulo = ft.Text("Monitorización de sensores y acceso al inventario", size=16, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER)

        tarjeta_aire = self._tarjeta("Sensores del Aire", "Temperatura, humedad y puertas", ft.Icons.AIR, "/sensores_aire")
        tarjeta_luz = self._tarjeta("Luces", "Intensidad y estado de luces", ft.Icons.LIGHT_MODE, "/sensores_luz")
        tarjeta_nevera = self._tarjeta("Nevera Inteligente", "Temperatura y estado de la nevera", ft.Icons.KITCHEN, "/sensores_nevera")
        tarjeta_inventario = self._tarjeta("Inventario", "Ver stock y existencias", ft.Icons.INVENTORY_2, "/inventario_edit")

        boton_logout = ft.ElevatedButton("Cerrar Sesión", icon=ft.Icons.LOGOUT, bgcolor=ft.Colors.RED_600, on_click=lambda e: (clear_current_user(), self.go("/")), width=220)

        self.controls = [
            ft.Column(controls=[
                titulo,
                subtitulo,
                ft.Divider(),
                ft.Row([tarjeta_aire, tarjeta_luz, tarjeta_nevera], alignment=ft.MainAxisAlignment.CENTER, spacing=40),
                ft.Divider(),
                ft.Row([tarjeta_inventario], alignment=ft.MainAxisAlignment.CENTER, spacing=40),
                ft.Divider(),
                boton_logout
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=20)
        ]

    def _tarjeta(self, titulo, descripcion, icono, ruta):
        return ft.Container(
            width=280,
            height=220,
            padding=20,
            border_radius=20,
            bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.BLUE_GREY_800),
            border=ft.border.all(2, ft.Colors.CYAN_300),
            ink=True,
            on_click=lambda e: self.go(ruta),
            content=ft.Column([
                ft.Icon(icono, size=60, color=ft.Colors.CYAN_200),
                ft.Text(titulo, size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                ft.Text(descripcion, size=14, color=ft.Colors.WHITE70, text_align=ft.TextAlign.CENTER),
            ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10)
        )
