import flet as ft
import threading
import time
from controllers.sensor_controller import SensorController
from models.session_manager import get_current_user
from models.session_manager import get_panel_route_for_current_user


class SensoresPuertaView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/sensores_puerta")
        self._page = page
        self.go = go
        self.controller = SensorController()
        self.estado_puerta = False
        self.contador_entrada = 0
        self.contador_salida = 0
        self.puerta_text = ft.Text("", size=22, weight=ft.FontWeight.BOLD)
        self.timestamp_text = ft.Text(
            "", size=14, weight=ft.FontWeight.NORMAL, color=ft.Colors.CYAN_100
        )
        self.entrada_text = ft.Text("0", size=40, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_400)
        self.salida_text = ft.Text("0", size=40, weight=ft.FontWeight.BOLD, color=ft.Colors.RED_400)
        self._simulacion_activa = False
        self._thread_actualizacion = None
        self.construir_ui()
        # Valor inicial sin datos de sensor
        self.puerta_text.value = "—"

    def construir_ui(self):
        titulo = ft.Text(
            "Sensor de Puerta – Monitorización de Acceso",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.PURPLE_200,
            text_align=ft.TextAlign.CENTER,
        )
        tarjeta_puerta = self._tarjeta_sensor(
            "Estado de la Puerta", ft.Icons.DOOR_FRONT_DOOR, self.puerta_text
        )
        
        # Tarjetas de contadores
        tarjeta_entrada = self._tarjeta_contador(
            "Entrada", ft.Icons.LOGIN, self.entrada_text, ft.Colors.GREEN_400
        )
        tarjeta_salida = self._tarjeta_contador(
            "Salida", ft.Icons.LOGOUT, self.salida_text, ft.Colors.RED_400
        )
        
        contadores = ft.Row(
            [tarjeta_entrada, tarjeta_salida],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
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
            [self.btn_iniciar, self.btn_detener],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )

        # Botones de control manual
        botones_control = ft.Row(
            [
                ft.ElevatedButton(
                    "Abrir Puerta",
                    icon=ft.Icons.ARROW_UPWARD,
                    bgcolor=ft.Colors.GREEN_400,
                    on_click=self.abrir_puerta,
                ),
                ft.ElevatedButton(
                    "Cerrar Puerta",
                    icon=ft.Icons.ARROW_DOWNWARD,
                    bgcolor=ft.Colors.RED_400,
                    on_click=self.cerrar_puerta,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )

        boton_atras = ft.ElevatedButton(
            "Atrás",
            icon=ft.Icons.ARROW_BACK,
            on_click=self.ir_atras,
        )

        boton_panel_admin = ft.ElevatedButton(
            "Panel de Administrador",
            icon=ft.Icons.ADMIN_PANEL_SETTINGS,
            bgcolor=ft.Colors.ORANGE_700,
            on_click=self.ir_panel_admin,
        )

        self.controls = [
            ft.Column(
                [
                    titulo,
                    ft.Divider(),
                    tarjeta_puerta,
                    self.timestamp_text,
                    ft.Divider(height=20),
                    ft.Text("Contadores de Tráfico", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.CYAN_200),
                    contadores,
                    ft.Divider(height=20),
                    ft.Text("Control Manual", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.YELLOW_200),
                    botones_control,
                    ft.Divider(height=30),
                    botones,
                    ft.Divider(height=30),
                    ft.Row(
                        [boton_atras, boton_panel_admin],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                scroll=ft.ScrollMode.AUTO,
            )
        ]

        # Cargar datos iniciales
        self.cargar_datos()

    def cargar_datos(self):
        lecturas = self.controller.obtener_lecturas_historicas("sensor_puerta")
        if lecturas:
            # Contar entradas y salidas
            self.contador_entrada = 0
            self.contador_salida = 0
            
            for lectura in lecturas:
                evento = lectura.get("evento", "").lower()
                if evento == "entrada":
                    self.contador_entrada += 1
                elif evento == "salida":
                    self.contador_salida += 1
            
            ultima_lectura = lecturas[-1]
            # Estado de la puerta (abierta/cerrada)
            estado = ultima_lectura.get("estado", "Desconocido")
            self.puerta_text.value = estado
            
            if estado == "abierta":
                self.puerta_text.color = ft.Colors.RED_400
            else:
                self.puerta_text.color = ft.Colors.GREEN_400
            
            # Timestamp
            timestamp = ultima_lectura.get("timestamp", "No disponible")
            self.timestamp_text.value = f"Última actualización: {timestamp}"
        else:
            self.puerta_text.value = "Sin datos"
            self.puerta_text.color = ft.Colors.ORANGE_400
            self.timestamp_text.value = "No hay lecturas disponibles"
        
        # Actualizar contadores
        self.entrada_text.value = str(self.contador_entrada)
        self.salida_text.value = str(self.contador_salida)
        
        self._page.update()

    def _tarjeta_sensor(self, titulo, icono, valor_widget):
        return ft.Container(
            width=400,
            height=200,
            padding=20,
            border_radius=10,
            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.PURPLE_600),
            border=ft.border.all(2, ft.Colors.PURPLE_300),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(icono, size=50, color=ft.Colors.PURPLE_200),
                            ft.Text(
                                titulo,
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                    ),
                    valor_widget,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
            ),
        )

    def _tarjeta_contador(self, titulo, icono, valor_widget, color):
        return ft.Container(
            width=180,
            height=180,
            padding=20,
            border_radius=10,
            bgcolor=ft.Colors.with_opacity(0.1, color),
            border=ft.border.all(2, color),
            content=ft.Column(
                [
                    ft.Row(
                        [ft.Icon(icono, size=40, color=color)],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Text(
                        titulo,
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=color,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    valor_widget,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
            ),
        )

    def iniciar_simulacion(self, e):
        """Inicia la simulación del sensor de puerta"""
        try:
            self.controller.iniciar_simulacion(actor='USUARIO')
            self._simulacion_activa = True
            self.btn_iniciar.disabled = True
            self.btn_detener.disabled = False
            self._page.update()
            
            # Iniciar thread de actualización periódica
            import threading
            self._thread_actualizacion = threading.Thread(target=self._actualizar_datos_periodicamente, daemon=True)
            self._thread_actualizacion.start()
            
            self.cargar_datos()
        except Exception as ex:
            print(f"Error al iniciar simulación: {ex}")

    def detener_simulacion(self, e):
        """Detiene la simulación del sensor de puerta"""
        try:
            self._simulacion_activa = False
            self.controller.detener_simulacion(actor='USUARIO')
            self.btn_iniciar.disabled = False
            self.btn_detener.disabled = True
            self._page.update()
            self.cargar_datos()
        except Exception as ex:
            print(f"Error al detener simulación: {ex}")

    def _actualizar_datos_periodicamente(self):
        """Actualiza los datos de la simulación cada 3 segundos"""
        while self._simulacion_activa:
            try:
                time.sleep(3)  # Actualizar cada 3 segundos
                if self._simulacion_activa:
                    self.cargar_datos()
            except Exception as ex:
                print(f"Error al actualizar datos: {ex}")

    def ir_atras(self, e):
        usuario = get_current_user()
        ruta = get_panel_route_for_current_user(usuario)
        self.go(ruta)

    def ir_panel_admin(self, e):
        """Navega al panel del administrador"""
        self.go("/panel_admin")

    def abrir_puerta(self, e):
        """Abre la puerta manualmente"""
        try:
            self.puerta_text.value = "abierta"
            self.puerta_text.color = ft.Colors.RED_400
            self.timestamp_text.value = f"Puerta abierta manualmente"
            self.contador_entrada += 1
            self.entrada_text.value = str(self.contador_entrada)
            self._page.update()
            # Guardar la acción
            from datetime import datetime
            lectura = {
                "timestamp": datetime.now().isoformat(),
                "valor": "abierta",
                "evento": "entrada"
            }
            self.controller.fm.guardar_lectura_sensor("sensor_puerta", "abierta")
        except Exception as ex:
            print(f"Error al abrir puerta: {ex}")

    def cerrar_puerta(self, e):
        """Cierra la puerta manualmente"""
        try:
            self.puerta_text.value = "cerrada"
            self.puerta_text.color = ft.Colors.GREEN_400
            self.timestamp_text.value = f"Puerta cerrada manualmente"
            self.contador_salida += 1
            self.salida_text.value = str(self.contador_salida)
            self._page.update()
            # Guardar la acción
            from datetime import datetime
            self.controller.fm.guardar_lectura_sensor("sensor_puerta", "cerrada")
        except Exception as ex:
            print(f"Error al cerrar puerta: {ex}")
