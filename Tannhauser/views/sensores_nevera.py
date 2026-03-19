import flet as ft
import threading
import time
from controllers.sensor_controller import SensorController
from models.session_manager import get_current_user
from models.session_manager import get_panel_route_for_current_user


class SensoresNeveraView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/sensores_nevera")
        self._page = page
        self.go = go
        self.controller = SensorController()
        self.temp_text = ft.Text("", size=22, weight=ft.FontWeight.BOLD)
        self.estado_text = ft.Text("", size=22, weight=ft.FontWeight.BOLD)
        self._simulacion_activa = False
        self._thread_actualizacion = None
        self.construir_ui()
        # Valores iniciales sin datos de sensor
        self.temp_text.value = "—"
        self.estado_text.value = "—"

    def construir_ui(self):
        titulo = ft.Text(
            "Monitor de Nevera – Temperatura y Estado",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.CYAN_200,
            text_align=ft.TextAlign.CENTER,
        )
        tarjeta_temp = self._tarjeta_sensor(
            "Temperatura interna", ft.Icons.DEVICE_THERMOSTAT, self.temp_text
        )
        tarjeta_estado = self._tarjeta_sensor(
            "Estado de la nevera", ft.Icons.KITCHEN, self.estado_text
        )
        # Botones para iniciar/detener simulación
        self.btn_iniciar = ft.ElevatedButton(
            "Iniciar Simulación",
            icon=ft.Icons.PLAY_ARROW,
            bgcolor=ft.Colors.CYAN_400,
            on_click=self.iniciar_simulacion,
        )
        self.btn_detener = ft.ElevatedButton(
            "Detener Simulación",
            icon=ft.Icons.STOP,
            bgcolor=ft.Colors.RED_700,
            on_click=self.detener_simulacion,
            disabled=True,
        )
        botones = ft.Row(
            controls=[
                self.btn_iniciar,
                self.btn_detener,
                ft.ElevatedButton(
                    "Refrescar",
                    icon=ft.Icons.REFRESH,
                    on_click=self.refrescar_datos,
                ),
                ft.TextButton(
                    "Volver al Panel",
                    on_click=lambda e: self.go(get_panel_route_for_current_user()),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )

        # Controles manuales retirados (solicitado)

        self.controls = [
            ft.Column(
                controls=[
                    titulo,
                    ft.Divider(),
                    ft.Row(
                        [tarjeta_temp, tarjeta_estado],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Divider(),
                    # Control Manual removido según solicitud del usuario
                    ft.Divider(),
                    botones,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30,
            )
        ]

    def did_mount(self):
        datos = self.controller.obtener_lecturas_actuales()
        if not datos or all(v is None for v in datos.values()):
            self.controller.generar_lecturas_manual()
        self.refrescar_datos(None)
        # button state based on simulator
        if hasattr(self, 'btn_iniciar') and hasattr(self, 'btn_detener'):
            running = self.controller.is_sim_running()
            self.btn_iniciar.disabled = bool(running)
            self.btn_detener.disabled = not bool(running)
            self._page.update()

    def _tarjeta_sensor(self, titulo, icono, valor_widget):
        return ft.Container(
            width=300,
            height=180,
            padding=20,
            bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.BLUE_GREY_800),
            border_radius=20,
            border=ft.border.all(2, ft.Colors.CYAN_300),
            content=ft.Column(
                [
                    ft.Icon(icono, size=40, color=ft.Colors.CYAN_200),
                    ft.Text(titulo, size=20, color=ft.Colors.WHITE),
                    valor_widget,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
            ),
        )

    def iniciar_simulacion(self, e):
        user = get_current_user()
        actor = user.get('email') if user else None
        self.controller.iniciar_simulacion(actor)
        self.mensaje("Simulación iniciada", ft.Colors.GREEN_800)
        self._simulacion_activa = True
        self.btn_iniciar.disabled = True
        self.btn_detener.disabled = False
        self._page.update()
        # Iniciar thread de actualización
        self._thread_actualizacion = threading.Thread(target=self._actualizar_datos_periodicamente, daemon=True)
        self._thread_actualizacion.start()

    def detener_simulacion(self, e):
        self._simulacion_activa = False
        user = get_current_user()
        actor = user.get('email') if user else None
        self.controller.detener_simulacion(actor)
        self.mensaje("Simulación detenida", ft.Colors.RED_800)
        self.btn_iniciar.disabled = False
        self.btn_detener.disabled = True
        self._page.update()

    def refrescar_datos(self, e):
        datos = self.controller.obtener_lecturas_actuales()
        if not datos or all(v is None for v in datos.values()):
            datos = self.controller.generar_lecturas_manual()
        if not datos or all(v is None for v in datos.values()):
            self.page.snack_bar = ft.SnackBar(ft.Text("No hay lecturas de sensores disponibles."), bgcolor=ft.Colors.RED_700)
            self.page.snack_bar.open = True
            self.page.update()
            self.temp_text.value = "—"
            self.estado_text.value = "—"
            self._page.update()
            return
        if datos:
            temp = datos.get("sensor_nevera")
            if temp is None:
                self.temp_text.value = "—"
                self.estado_text.value = "—"
                self._page.update()
                return
            try:
                temp_val = float(temp)
                self.temp_text.value = f"{temp_val} °C"
            except Exception:
                self.temp_text.value = str(temp)
                temp_val = None
            if temp_val is not None and temp_val <= 4:
                self.estado_text.value = "CORRECTA"
                self.estado_text.color = ft.Colors.LIGHT_GREEN_400
            elif temp_val is not None and temp_val <= 7:
                self.estado_text.value = "ALERTA"
                self.estado_text.color = ft.Colors.AMBER_400
            else:
                self.estado_text.value = "RIESGO"
                self.estado_text.color = ft.Colors.RED_400
        else:
            self.temp_text.value = "—"
            self.estado_text.value = "—"
        self._page.update()

    def mensaje(self, texto, color):
        self.page.snack_bar = ft.SnackBar(ft.Text(texto), bgcolor=color)
        self.page.snack_bar.open = True
        self.page.snack_bar.open = True
        self.page.update()

    def _actualizar_datos_periodicamente(self):
        """Actualiza los datos de la simulación cada 3 segundos"""
        while self._simulacion_activa:
            try:
                time.sleep(3)
                if self._simulacion_activa:
                    self.refrescar_datos(None)
            except Exception as ex:
                print(f"Error al actualizar datos: {ex}")
    # Funciones de control manual de la nevera removidas por petición del usuario
