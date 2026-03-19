import flet as ft
import threading
import time
from controllers.sensor_controller import SensorController
from models.session_manager import get_panel_route_for_current_user, get_current_user

class SensoresAireView(ft.View):
    def __init__(self, page, go):
        super().__init__("/sensores_aire")
        self._page = page
        self.go = go
        self.controller = SensorController()

        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.vertical_alignment = ft.MainAxisAlignment.START

        # Textos de sensores
        self.temp_text = ft.Text("—", size=24)
        self.hum_text = ft.Text("—", size=24)
        self.puerta_text = ft.Text("—", size=24)

        self.btn_iniciar = None
        self.btn_detener = None
        self._simulacion_activa = False
        self._thread_actualizacion = None
        self.construir_ui()

    # ----------------------------------------------------------
    def construir_ui(self):
        # prepare buttons as attributes so we can toggle disabled states later
        self.btn_iniciar = ft.ElevatedButton(
            "Iniciar Simulación",
            icon=ft.Icons.PLAY_ARROW,
            on_click=self.iniciar_simulacion,
            bgcolor=ft.Colors.BLUE_700,
        )
        self.btn_detener = ft.ElevatedButton(
            "Detener Simulación",
            icon=ft.Icons.STOP,
            on_click=self.detener_simulacion,
            bgcolor=ft.Colors.RED_700,
            disabled=True,
        )

        def tarjeta(nombre, icono, control):
            return ft.Container(
                padding=15,
                width=350,
                border_radius=12,
                bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.BLUE_GREY_800),
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Icon(icono, size=40, color=ft.Colors.CYAN_300),
                                ft.Text(nombre, size=20, weight=ft.FontWeight.BOLD),
                            ]
                        ),
                        ft.Divider(),
                        control,
                    ]
                )
            )

        self.controls = [
            ft.Column(
                [
                    ft.Text("Sensores de Aire", size=32, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_200),

                    tarjeta("Temperatura", ft.Icons.DEVICE_THERMOSTAT, self.temp_text),
                    tarjeta("Humedad", ft.Icons.WATER_DROP, self.hum_text),
                    tarjeta("Puerta", ft.Icons.SENSOR_DOOR, self.puerta_text),

                    # Controles manuales removidos según solicitud del usuario

                    ft.ElevatedButton(
                        "Refrescar",
                        icon=ft.Icons.REFRESH,
                        on_click=self.refrescar_datos,
                        bgcolor=ft.Colors.BLUE_700
                    ),
                    # Simulador control buttons
                    self.btn_iniciar,
                    self.btn_detener,

                    ft.ElevatedButton(
                        "Volver al Panel",
                        icon=ft.Icons.ARROW_BACK,
                        on_click=lambda e: self.go(get_panel_route_for_current_user()),
                        bgcolor=ft.Colors.BLUE_GREY_700,
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ]

    def did_mount(self):
        # On view mount, make sure we have readings to display
        datos = self.controller.obtener_lecturas_actuales()
        if not datos or all(v is None for v in datos.values()):
            # generate manual readings if none exist
            self.controller.generar_lecturas_manual()
        self.refrescar_datos(None)
        # set button states based on controller simulator running state
        if hasattr(self, 'btn_iniciar') and hasattr(self, 'btn_detener'):
            running = self.controller.is_sim_running()
            self.btn_iniciar.disabled = bool(running)
            self.btn_detener.disabled = not bool(running)
            self._page.update()

    def iniciar_simulacion(self, e):
        user = get_current_user()
        actor = user.get('email') if user else None
        self.controller.iniciar_simulacion(actor)
        self.mensaje("Simulación iniciada", ft.Colors.GREEN_700)
        self._simulacion_activa = True
        if hasattr(self, 'btn_iniciar') and hasattr(self, 'btn_detener'):
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
        self.mensaje("Simulación detenida", ft.Colors.RED_700)
        if hasattr(self, 'btn_iniciar') and hasattr(self, 'btn_detener'):
            self.btn_iniciar.disabled = False
            self.btn_detener.disabled = True
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

    # Funciones de control manual eliminadas por petición del usuario

    # ----------------------------------------------------------
    def refrescar_datos(self, e):
        datos = self.controller.obtener_lecturas_actuales()
        if not datos or all(v is None for v in datos.values()):
            datos = self.controller.generar_lecturas_manual()

        if not datos or all(v is None for v in datos.values()):
            self.temp_text.value = "—"
            self.hum_text.value = "—"
            self.puerta_text.value = "—"
            self._page.update()
            return

        # Temperatura
        t = datos.get("sensor_temperatura")
        try:
            t_val = float(t) if t is not None else None
            self.temp_text.value = f"{t_val} °C" if t_val is not None else "—"
        except Exception:
            self.temp_text.value = str(t) if t is not None else "—"
            t_val = None

        # Humedad
        h = datos.get("sensor_humedad")
        try:
            h_val = int(float(h)) if h is not None else None
            self.hum_text.value = f"{h_val} %" if h_val is not None else "—"
        except Exception:
            self.hum_text.value = str(h) if h is not None else "—"
            h_val = None

        # Puerta
        p = datos.get("sensor_puerta")
        if p is None:
            self.puerta_text.value = "—"
        elif isinstance(p, str) and p.lower().startswith("a"):
            self.puerta_text.value = "ABIERTA"
        elif isinstance(p, str) and p.lower().startswith("c"):
            self.puerta_text.value = "CERRADA"
        elif isinstance(p, bool):
            self.puerta_text.value = "ABIERTA" if p else "CERRADA"
        else:
            self.puerta_text.value = str(p)

        self._page.update()
