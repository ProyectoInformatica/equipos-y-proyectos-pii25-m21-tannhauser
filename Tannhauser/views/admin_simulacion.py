import flet as ft
from controllers.sensor_controller import SensorController
from models.session_manager import get_current_user
from models.session_manager import get_panel_route_for_current_user


class AdminSimulacionView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/admin_simulacion")
        self._page = page
        self.go = go
        self.controller = SensorController()
        self.estado_sim = False
        self.estado_text = ft.Text("", size=24, weight=ft.FontWeight.BOLD)
        self.autosave_text = ft.Text("OFF", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_400)
        self.lista_lecturas = ft.Column(scroll=ft.ScrollMode.AUTO)
        self.construir_ui()
        # Estado inicial sin lecturas
        self.estado_sim = False
        self.estado_text.value = "DETENIDA"
        self.estado_text.color = ft.Colors.RED_400

    def construir_ui(self):
        titulo = ft.Text(
            "Control Global de Simulación",
            size=32,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.CYAN_200,
        )
        subtitulo = ft.Text(
            "Gestiona la simulación de sensores en tiempo real",
            size=16,
            color=ft.Colors.WHITE70,
        )
        tarjeta_estado = ft.Container(
            width=350,
            padding=20,
            border_radius=20,
            bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.BLUE_GREY_900),
            border=ft.border.all(2, ft.Colors.CYAN_300),
            content=ft.Column(
                [
                    ft.Icon(ft.Icons.SETTINGS, size=60, color=ft.Colors.CYAN_200),
                    ft.Text("Estado de la Simulación", size=20, color=ft.Colors.CYAN_100),
                    self.estado_text,
                    ft.Text("Autoguardado:", size=16, color=ft.Colors.WHITE70),
                    self.autosave_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        tarjeta_lecturas = ft.Container(
            width=420,
            height=350,
            padding=20,
            border_radius=20,
            bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.BLUE_GREY_800),
            border=ft.border.all(2, ft.Colors.CYAN_300),
            content=ft.Column(
                [
                    ft.Text("Últimas Lecturas", size=20, color=ft.Colors.CYAN_100),
                    self.lista_lecturas,
                ],
                spacing=10,
            ),
        )
        # Botones para controlar simulación y auto-guardado de lecturas
        self.autosave_estado = False
        # Buttons: stored as attributes to allow toggling disabled states
        self.btn_iniciar_sim = ft.ElevatedButton(
            "Iniciar Simulación",
            icon=ft.Icons.PLAY_ARROW,
            bgcolor=ft.Colors.GREEN_600,
            on_click=self.iniciar_simulacion,
        )
        self.btn_detener_sim = ft.ElevatedButton(
            "Detener Simulación",
            icon=ft.Icons.STOP,
            bgcolor=ft.Colors.RED_600,
            on_click=self.detener_simulacion,
            disabled=True,
        )
        self.btn_iniciar_autosave = ft.ElevatedButton(
            "Iniciar Autoguardado",
            icon=ft.Icons.SAVE,
            bgcolor=ft.Colors.ORANGE_700,
            on_click=self.iniciar_autoguardado,
        )
        self.btn_detener_autosave = ft.ElevatedButton(
            "Detener Autoguardado",
            icon=ft.Icons.STOP,
            bgcolor=ft.Colors.INDIGO_700,
            on_click=self.detener_autoguardado,
            disabled=True,
        )
        botones = ft.Row(
            controls=[
                self.btn_iniciar_sim,
                self.btn_detener_sim,
                ft.ElevatedButton(
                    "Refrescar Estado",
                    icon=ft.Icons.REFRESH,
                    on_click=self.refrescar_estado,
                ),
                self.btn_iniciar_autosave,
                self.btn_detener_autosave,
                ft.TextButton(
                    "Volver al Panel",
                    icon=ft.Icons.ARROW_BACK,
                    on_click=lambda e: self.go(get_panel_route_for_current_user()),
                ),
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )
        self.controls = [
            ft.Column(
                controls=[
                    titulo,
                    subtitulo,
                    ft.Divider(),
                    ft.Row(
                        controls=[tarjeta_estado, tarjeta_lecturas],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=40,
                    ),
                    ft.Divider(),
                    botones,
                ],
                spacing=30,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        ]

    def refrescar_estado(self, e):
        datos = self.controller.obtener_lecturas_actuales()
        if not datos or all(v is None for v in datos.values()):
            self.estado_sim = False
            self.estado_text.value = "DETENIDA"
            self.estado_text.color = ft.Colors.RED_400
        else:
            self.estado_sim = True
            self.estado_text.value = "ACTIVA"
            self.estado_text.color = ft.Colors.GREEN_400
        self.cargar_lecturas()
        # Toggle the button states depending on whether the simulation is running
        if self.estado_sim:
            self.btn_iniciar_sim.disabled = True
            self.btn_detener_sim.disabled = False
        else:
            self.btn_iniciar_sim.disabled = False
            self.btn_detener_sim.disabled = True
        # Autosave button toggles
        if getattr(self, 'autosave_estado', False):
            self.btn_iniciar_autosave.disabled = True
            self.btn_detener_autosave.disabled = False
        else:
            self.btn_iniciar_autosave.disabled = False
            self.btn_detener_autosave.disabled = True
        self.update()

    def cargar_lecturas(self):
        self.lista_lecturas.controls.clear()
        datos = self.controller.obtener_lecturas_actuales()
        if not datos:
            self.lista_lecturas.controls.append(
                ft.Text("No hay lecturas disponibles.", color=ft.Colors.GREY_400)
            )
            return
        for sensor, valor in datos.items():
            self.lista_lecturas.controls.append(
                ft.Container(
                    padding=10,
                    border_radius=10,
                    bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.BLUE_GREY_700),
                    border=ft.border.all(1, ft.Colors.CYAN_300),
                    content=ft.Text(f"{sensor}: {valor}", color=ft.Colors.WHITE),
                )
            )

    def iniciar_simulacion(self, e):
        actor = None
        user = get_current_user()
        if user:
            actor = user.get('email')
        self.controller.iniciar_simulacion(actor)
        self.mensaje("Simulación iniciada", ft.Colors.GREEN_800)
        self.refrescar_estado(None)
        # ensure button states toggled
        self.btn_iniciar_sim.disabled = True
        self.btn_detener_sim.disabled = False
        self.update()

    def detener_simulacion(self, e):
        actor = None
        user = get_current_user()
        if user:
            actor = user.get('email')
        self.controller.detener_simulacion(actor)
        self.mensaje("Simulación detenida", ft.Colors.RED_800)
        self.refrescar_estado(None)
        # ensure button states toggled
        self.btn_iniciar_sim.disabled = False
        self.btn_detener_sim.disabled = True
        self.update()

    def iniciar_autoguardado(self, e):
        msg = self.controller.iniciar_autoguardado(intervalo=10)
        self.mensaje(msg, ft.Colors.GREEN_700)
        self.autosave_estado = True
        self.autosave_text.value = "ON"
        self.autosave_text.color = ft.Colors.LIGHT_GREEN_400
        self.page.update()

    def detener_autoguardado(self, e):
        msg = self.controller.detener_autoguardado()
        self.mensaje(msg, ft.Colors.RED_700)
        self.autosave_estado = False
        self.autosave_text.value = "OFF"
        self.autosave_text.color = ft.Colors.GREY_400
        self.page.update()

    def mensaje(self, texto, color):
        self.page.snack_bar = ft.SnackBar(ft.Text(texto), bgcolor=color)
        self.page.snack_bar.open = True
        self.page.update()
