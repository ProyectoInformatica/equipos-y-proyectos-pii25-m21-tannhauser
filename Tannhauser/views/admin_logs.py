import flet as ft
from models.file_manager import FileManager


class AdminLogsView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/admin_logs")
        self._page = page
        self.go = go
        self.fm = FileManager()
        self.lista_logs = ft.Column(scroll=ft.ScrollMode.AUTO)
        self.busqueda = ft.TextField(
            label="Buscar...", width=300, on_change=self.aplicar_filtro
        )
        self.construir_ui()
    def did_mount(self):
        # Llamamos a cargar_logs en did_mount para asegurarnos de que la vista
        # ya ha sido montada y `self.update()` pueda ejecutarse sin errores.
        self.cargar_logs()

    def construir_ui(self):
        titulo = ft.Text(
            "Actividad del Sistema",
            size=32,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.CYAN_200,
        )
        subtitulo = ft.Text(
            "Registros generados en tiempo real por usuarios y sensores",
            size=16,
            color=ft.Colors.WHITE70,
        )
        contenedor_logs = ft.Container(
            height=450,
            padding=15,
            border_radius=15,
            bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.BLUE_GREY_900),
            border=ft.border.all(1, ft.Colors.CYAN_300),
            content=self.lista_logs,
        )
        botones = ft.Row(
            controls=[
                ft.ElevatedButton(
                    "Refrescar",
                    icon=ft.Icons.REFRESH,
                    on_click=lambda e: self.cargar_logs(),
                ),
                ft.TextButton(
                    "Volver al Panel",
                    icon=ft.Icons.ARROW_BACK,
                    on_click=lambda e: self.go("/panel_admin"),
                ),
            ],
            spacing=20,
        )
        self.controls = [
            ft.Column(
                [
                    titulo,
                    subtitulo,
                    ft.Divider(),
                    self.busqueda,
                    contenedor_logs,
                    ft.Divider(),
                    botones,
                ],
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]

    def cargar_logs(self):
        self.lista_logs.controls.clear()
        ruta_log = self.fm.ACTIVITY_LOG
        try:
            with open(ruta_log, "r", encoding="utf-8") as f:
                lineas = f.readlines()
        except FileNotFoundError:
            self.lista_logs.controls.append(
                ft.Text("No hay registros aún.", color=ft.Colors.GREY_400)
            )
            self.safe_update()
            return
        for linea in lineas:
            self.lista_logs.controls.append(self._tarjeta_log(linea.strip()))
        self.safe_update()

    def aplicar_filtro(self, e):
        texto = self.busqueda.value.lower()
        self.lista_logs.controls.clear()
        ruta_log = self.fm.ACTIVITY_LOG
        try:
            with open(ruta_log, "r", encoding="utf-8") as f:
                lineas = f.readlines()
        except Exception:
            return
        for linea in lineas:
            if texto in linea.lower():
                self.lista_logs.controls.append(self._tarjeta_log(linea.strip()))
        self.safe_update()

    def _tarjeta_log(self, texto):
        return ft.Container(
            padding=10,
            margin=5,
            border_radius=10,
            bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.BLUE_GREY_700),
            border=ft.border.all(1, ft.Colors.CYAN_300),
            content=ft.Text(texto, color=ft.Colors.WHITE),
        )

    def safe_update(self):
        # Evita llamar a update() si la vista aún no está montada en la página
        try:
            if hasattr(self, "page") and hasattr(self.page, "views") and self in self.page.views:
                self.update()
        except Exception:
            # No queremos que un error al actualizar la interfaz rompa la función de carga
            pass
