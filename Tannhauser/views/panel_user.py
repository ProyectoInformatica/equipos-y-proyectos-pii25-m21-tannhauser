import flet as ft
from models.session_manager import clear_current_user


class PanelUsuarioView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/panel_usuario")
        self._page = page
        self.go = go
        self.construir_ui()

    def construir_ui(self):
        titulo = ft.Text(
            "Panel de Cliente",
            size=32,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.CYAN_200,
            text_align=ft.TextAlign.CENTER,
        )

        subtitulo = ft.Text(
            "Visualiza el stock disponible en el supermercado",
            size=18,
            color=ft.Colors.WHITE70,
            text_align=ft.TextAlign.CENTER,
        )

        # Los clientes no pueden acceder a los sensores: mostramos directamente el Inventario (solo lectura)
        tarjeta_inventario = self._tarjeta(
            "Inventario",
            "Ver el stock del supermercado",
            ft.Icons.INVENTORY_2,
            "/inventario",
        )

        boton_logout = ft.ElevatedButton(
            "Cerrar Sesión",
            icon=ft.Icons.LOGOUT,
            bgcolor=ft.Colors.RED_600,
            on_click=lambda e: self._logout(e),
            width=200,
        )

        self.controls = [
            ft.Column(
                controls=[
                    titulo,
                    subtitulo,
                    ft.Divider(color=ft.Colors.CYAN_100),
                    ft.Row(
                        [tarjeta_inventario],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=40,
                    ),
                    ft.Divider(),
                    boton_logout,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30,
            )
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
            # Los clientes pueden acceder al inventario (u otras rutas permitidas)
            on_click=lambda e: self.go(ruta),
            content=ft.Column(
                [
                    ft.Icon(icono, size=60, color=ft.Colors.CYAN_200),
                    ft.Text(titulo, size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    ft.Text(
                        descripcion,
                        size=14,
                        color=ft.Colors.WHITE70,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
        )

    def _no_permisos(self):
        self.page.snack_bar = ft.SnackBar(
            ft.Text("Acceso restringido: solo administradores, superusuarios y empleados pueden ver los sensores."),
            bgcolor=ft.Colors.RED_600,
        )
        self.page.snack_bar.open = True
        self.page.update()

    def _logout(self, e=None):
        clear_current_user()
        self.go("/")

