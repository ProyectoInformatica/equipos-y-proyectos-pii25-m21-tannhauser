import flet as ft
import threading
import time
from controllers.sensor_controller import SensorController
from models.session_manager import get_current_user
from models.session_manager import get_panel_route_for_current_user


class SensoresLuzView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/sensores_luz")
        self._page = page
        self.go = go
        self.controller = SensorController()
        self.estado_luz = False
        self.brillo_actual = 50  # Brillo inicial 50%
        self.luz_text = ft.Text("", size=22, weight=ft.FontWeight.BOLD)
        self.estado_text = ft.Text(
            "", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_200
        )
        self.brillo_text = ft.Text(f"{self.brillo_actual}%", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.YELLOW_300)
        self._simulacion_activa = False
        self._thread_actualizacion = None
        self.construir_ui()
        # Valor inicial sin datos de sensor
        self.luz_text.value = "—"

    def construir_ui(self):
        titulo = ft.Text(
            "Sensor de Luz – Control e Intensidad",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.YELLOW_200,
            text_align=ft.TextAlign.CENTER,
        )
        tarjeta_luz = self._tarjeta_sensor(
            "Intensidad de luz", ft.Icons.LIGHT_MODE, self.luz_text
        )
        tarjeta_estado = self._tarjeta_sensor(
            "Estado de la luz", ft.Icons.LIGHTBULB, self.estado_text
        )
        
        # Control de brillo con Slider
        control_brillo = ft.Container(
            padding=20,
            width=400,
            border_radius=12,
            bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.YELLOW_800),
            border=ft.border.all(2, ft.Colors.YELLOW_300),
            content=ft.Column(
                [
                    ft.Text("Control de Brillo", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.YELLOW_200),
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.BRIGHTNESS_LOW, size=30, color=ft.Colors.YELLOW_200),
                            ft.Slider(
                                min=0,
                                max=100,
                                value=self.brillo_actual,
                                width=250,
                                on_change=self.cambiar_brillo,
                            ),
                            ft.Icon(ft.Icons.BRIGHTNESS_HIGH, size=30, color=ft.Colors.ORANGE_400),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    ),
                    self.brillo_text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
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
                ft.ElevatedButton(
                    "Encender Luz",
                    icon=ft.Icons.LIGHTBULB,
                    bgcolor=ft.Colors.LIGHT_GREEN_400,
                    on_click=self.encender_luz,
                ),
                ft.ElevatedButton(
                    "Apagar Luz",
                    icon=ft.Icons.LIGHTBULB_OUTLINE,
                    bgcolor=ft.Colors.RED_400,
                    on_click=self.apagar_luz,
                ),
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
        self.controls = [
            ft.Column(
                controls=[
                    titulo,
                    ft.Divider(),
                    ft.Row(
                        [tarjeta_luz, tarjeta_estado],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Divider(),
                    ft.Text("Ajusta el Brillo", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.YELLOW_200),
                    control_brillo,
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
            border=ft.border.all(2, ft.Colors.YELLOW_300),
            content=ft.Column(
                [
                    ft.Icon(icono, size=40, color=ft.Colors.YELLOW_200),
                    ft.Text(titulo, size=20, color=ft.Colors.WHITE),
                    valor_widget,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=5,
            ),
        )

    def encender_luz(self, e):
        self.estado_luz = True
        self.estado_text.value = "ENCENDIDA"
        self.estado_text.color = ft.Colors.LIGHT_GREEN_400
        self._page.update()

    def apagar_luz(self, e):
        self.estado_luz = False
        self.estado_text.value = "APAGADA"
        self.estado_text.color = ft.Colors.RED_400
        self._page.update()

    def cambiar_brillo(self, e):
        """Cambia el brillo de la luz"""
        try:
            # e.control.value may be float; coerce to int
            brillo_valor = int(round(float(e.control.value)))
            self.brillo_actual = brillo_valor
            self.brillo_text.value = f"{brillo_valor}%"

            # Actualizar también la tarjeta superior inmediatamente
            self.luz_text.value = f"{brillo_valor}%"
            if brillo_valor < 20:
                self.luz_text.color = ft.Colors.GREY_400
            elif brillo_valor < 50:
                self.luz_text.color = ft.Colors.AMBER_400
            else:
                self.luz_text.color = ft.Colors.YELLOW_300

            # Guardar el brillo como lectura del sensor
            try:
                self.controller.fm.guardar_lectura_sensor("sensor_luz", brillo_valor)
            except Exception:
                # fallback: if controller.fm not available or fails, ignore but log
                print("Warning: no se pudo guardar la lectura del sensor de luz")

            print(f"Brillo ajustado a: {brillo_valor}%")

            # Actualizar la interfaz
            self._page.update()
        except Exception as ex:
            print(f"Error al cambiar brillo: {ex}")
            import traceback
            traceback.print_exc()

    def iniciar_simulacion(self, e):
        user = get_current_user()
        actor = user.get('email') if user else None
        self.controller.iniciar_simulacion(actor)
        self.mensaje("Simulación iniciada", ft.Colors.GREEN_700)
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
        # Mostrar el brillo actual como intensidad de luz
        nivel = self.brillo_actual
        self.luz_text.value = f"{nivel}%"
        
        # Cambiar color según el brillo
        if nivel < 20:
            self.luz_text.color = ft.Colors.GREY_400
        elif nivel < 50:
            self.luz_text.color = ft.Colors.AMBER_400
        else:
            self.luz_text.color = ft.Colors.YELLOW_300
        
        self._page.update()

    def mensaje(self, texto, color):
        self.page.snack_bar = ft.SnackBar(ft.Text(texto), bgcolor=color)
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
