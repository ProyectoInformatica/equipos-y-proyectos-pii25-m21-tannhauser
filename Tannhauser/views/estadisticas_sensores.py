"""
Vista para mostrar estadísticas de sensores.
Permite visualizar datos, gráficos y alertas de los sensores del sistema.
"""

import flet as ft
from controllers.estadisticas_controller import EstadisticasController
from datetime import datetime
import csv
from pathlib import Path


def EstadisticasSensoresView(page: ft.Page, go):
    """Vista para mostrar estadísticas de sensores"""
    
    stats_controller = EstadisticasController()
    
    # (Se obtendrá dinámicamente dentro de las funciones de actualización)
    
    # Encabezado
    titulo = ft.Text(
        "📊 Estadísticas de Sensores",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.CYAN_300,
    )
    
    subtitulo = ft.Text(
        "Monitoreo en tiempo real de sensores del supermercado",
        size=14,
        color=ft.Colors.GREY_300,
    )
    
    # Información de conexión (para debugging)
    info_conexion = ft.Column(spacing=5)
    
    # Contenedor para las estadísticas
    contenedor_stats = ft.Column(spacing=15, scroll=ft.ScrollMode.AUTO)
    
    def actualizar_info_conexion():
        """Actualiza la información de conexión"""
        info_conexion.controls.clear()

        # Encabezado de información
        info_conexion.controls.append(
            ft.Text(
                "ℹ️ Estado de Conexión de Archivos",
                size=12,
                color=ft.Colors.GREY_500,
                weight=ft.FontWeight.BOLD
            )
        )

        # Obtener información fresca del controlador
        try:
            conexion_info = stats_controller.verificar_conexion_archivos()
            rutas_info = stats_controller.obtener_ruta_archivos_sensores()
        except Exception as e:
            conexion_info = {}
            rutas_info = {"directorio_base": "data/sensores"}

        for sensor, info in conexion_info.items():
            if info.get("conectado"):
                estado_text = ft.Text(
                    f"✓ {sensor}: {info.get('total_registros', 0)} registros",
                    size=10,
                    color=ft.Colors.GREEN_300
                )
            else:
                estado_text = ft.Text(
                    f"✗ {sensor}: Error",
                    size=10,
                    color=ft.Colors.RED_300
                )
            info_conexion.controls.append(estado_text)

        info_conexion.controls.append(
            ft.Text(
                f"Directorio: {rutas_info.get('directorio_base', 'data/sensores')}",
                size=9,
                color=ft.Colors.GREY_600,
                italic=True
            )
        )
    
    def actualizar_estadisticas():
        """Actualiza el contenido de estadísticas"""
        contenedor_stats.controls.clear()
        
        try:
            todas_stats = stats_controller.obtener_todas_estadisticas()
            consumo_24h = stats_controller.obtener_consumo_ultimas_24h()
            alertas = stats_controller.obtener_alertas()
            # cargar medias y kWh desde CSVs generados en tools/
            media_map = {}
            kwh_map = {}
            try:
                tools_dir = Path(__file__).resolve().parents[2] / 'tools'
                medias_file = tools_dir / 'consumo_medias.csv'
                kwh_file = tools_dir / 'consumo_kwh.csv'
                if medias_file.exists():
                    with medias_file.open('r', encoding='utf-8') as fh:
                        reader = csv.DictReader(fh)
                        for r in reader:
                            try:
                                media_map[r['sensor']] = float(r.get('mean_w', 0))
                            except Exception:
                                pass
                if kwh_file.exists():
                    with kwh_file.open('r', encoding='utf-8') as fh:
                        reader = csv.DictReader(fh)
                        for r in reader:
                            try:
                                kwh_map[r['sensor']] = float(r.get('total_kwh', 0))
                            except Exception:
                                pass
            except Exception:
                media_map = {}
                kwh_map = {}
            
            # Mostrar alertas si las hay
            if alertas:
                contenedor_alertas = ft.Container(
                    bgcolor=ft.Colors.RED_900,
                    border_radius=10,
                    padding=15,
                    border=ft.border.all(2, ft.Colors.RED_500),
                )
                alertas_text = [ft.Text("⚠️ ALERTAS DETECTADAS:", weight=ft.FontWeight.BOLD, color=ft.Colors.RED_200)]
                for alerta in alertas:
                    alertas_text.append(
                        ft.Text(
                            f"• {alerta['sensor']}: {alerta['mensaje']}",
                            color=ft.Colors.ORANGE_300,
                            size=12
                        )
                    )
                contenedor_alertas.content = ft.Column(alertas_text, spacing=5)
                contenedor_stats.controls.append(contenedor_alertas)
                contenedor_stats.controls.append(ft.Container(height=10))
            
            # Mostrar estadísticas por sensor
            for nombre_sensor, stats in todas_stats.items():
                if stats.get("estado") == "sin_datos":
                    # Sensor sin datos
                    tarjeta = ft.Container(
                        bgcolor=ft.Colors.GREY_900,
                        border_radius=10,
                        padding=15,
                        border=ft.border.all(1, ft.Colors.GREY_700),
                        content=ft.Column([
                            ft.Text(
                                nombre_sensor.replace("sensor_", "").upper(),
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.GREY_500,
                                size=14
                            ),
                            ft.Text("Sin datos disponibles", color=ft.Colors.GREY_400, size=12),
                        ], spacing=8)
                    )
                else:
                    # Sensor con datos
                    contenido_tarjeta = []
                    
                    # Nombre del sensor
                    contenido_tarjeta.append(
                        ft.Text(
                            f"🔹 {nombre_sensor.replace('sensor_', '').upper()}",
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.CYAN_300,
                            size=14
                        )
                    )
                    
                    # Total de lecturas
                    contenido_tarjeta.append(
                        ft.Text(
                            f"Total de lecturas: {stats.get('total_lecturas', 0)}",
                            color=ft.Colors.GREY_300,
                            size=11
                        )
                    )
                    
                    # Estadísticas para sensores numéricos
                    if stats.get("tipo_dato") == "numerico" or "promedio" in stats:
                        contenido_tarjeta.append(ft.Divider(height=1, color=ft.Colors.GREY_700))
                        
                        stats_row1 = ft.Row([
                            ft.Column([
                                ft.Text("Mínimo", size=10, color=ft.Colors.GREY_400),
                                ft.Text(f"{stats.get('minimo', 'N/A')}", size=12, color=ft.Colors.BLUE_300, weight=ft.FontWeight.BOLD),
                            ], tight=True, spacing=2),
                            ft.Column([
                                ft.Text("Máximo", size=10, color=ft.Colors.GREY_400),
                                ft.Text(f"{stats.get('maximo', 'N/A')}", size=12, color=ft.Colors.RED_300, weight=ft.FontWeight.BOLD),
                            ], tight=True, spacing=2),
                            ft.Column([
                                ft.Text("Promedio", size=10, color=ft.Colors.GREY_400),
                                ft.Text(f"{stats.get('promedio', 'N/A')}", size=12, color=ft.Colors.GREEN_300, weight=ft.FontWeight.BOLD),
                            ], tight=True, spacing=2),
                            ft.Column([
                                ft.Text("Mediana", size=10, color=ft.Colors.GREY_400),
                                ft.Text(f"{stats.get('mediana', 'N/A')}", size=12, color=ft.Colors.YELLOW_300, weight=ft.FontWeight.BOLD),
                            ], tight=True, spacing=2),
                        ], spacing=15, expand=True)
                        
                        contenido_tarjeta.append(stats_row1)
                        
                        # Desviación estándar y rango
                        if stats.get('desviacion_estandar') is not None:
                            stats_row2 = ft.Row([
                                ft.Column([
                                    ft.Text("Desv. Estándar", size=10, color=ft.Colors.GREY_400),
                                    ft.Text(f"{stats.get('desviacion_estandar', 'N/A')}", size=12, color=ft.Colors.PURPLE_300, weight=ft.FontWeight.BOLD),
                                ], tight=True, spacing=2),
                                ft.Column([
                                    ft.Text("Rango", size=10, color=ft.Colors.GREY_400),
                                    ft.Text(f"{stats.get('rango', 'N/A')}", size=12, color=ft.Colors.INDIGO_300, weight=ft.FontWeight.BOLD),
                                ], tight=True, spacing=2),
                            ], spacing=15)
                            contenido_tarjeta.append(stats_row2)
                    
                    # Estadísticas para sensores de texto
                    elif stats.get("tipo_dato") == "texto":
                        contenido_tarjeta.append(ft.Divider(height=1, color=ft.Colors.GREY_700))
                        valores_unicos = stats.get('valores', [])
                        contenido_tarjeta.append(
                            ft.Text(f"Valores únicos: {', '.join(map(str, valores_unicos))}", size=11, color=ft.Colors.GREY_300)
                        )
                    
                    # Última lectura
                    ultima_lectura = stats.get("ultima_lectura", {})
                    if ultima_lectura:
                        contenido_tarjeta.append(ft.Divider(height=1, color=ft.Colors.GREY_700))
                        timestamp = ultima_lectura.get("timestamp", "N/A")
                        if isinstance(timestamp, str):
                            try:
                                dt = datetime.fromisoformat(timestamp)
                                timestamp = dt.strftime("%d/%m/%Y %H:%M:%S")
                            except:
                                pass
                        
                        contenido_tarjeta.append(
                            ft.Text(
                                f"Última lectura: {ultima_lectura.get('valor', 'N/A')} ({timestamp})",
                                size=10,
                                color=ft.Colors.LIME_300,
                                italic=True
                            )
                        )

                    # Media de consumo (W) desde CSV
                    media_csv = media_map.get(nombre_sensor)
                    if media_csv is not None:
                        contenido_tarjeta.append(ft.Divider(height=1, color=ft.Colors.GREY_700))
                        contenido_tarjeta.append(
                            ft.Text(
                                f"Media consumo: {round(media_csv,4)} W",
                                size=11,
                                color=ft.Colors.CYAN_100
                            )
                        )

                    # Consumo total (kWh) desde CSV
                    total_kwh = kwh_map.get(nombre_sensor)
                    if total_kwh is not None:
                        contenido_tarjeta.append(
                            ft.Text(
                                f"Consumo total: {round(total_kwh,6)} kWh",
                                size=11,
                                color=ft.Colors.AMBER_300
                            )
                        )

                    # Consumo estimado últimas 24h (Wh)
                    consumo_sensor = consumo_24h.get(nombre_sensor)
                    if consumo_sensor is not None:
                        contenido_tarjeta.append(ft.Divider(height=1, color=ft.Colors.GREY_700))
                        contenido_tarjeta.append(
                            ft.Text(
                                f"Consumo últimas 24h: {consumo_sensor} Wh",
                                size=11,
                                color=ft.Colors.AMBER_300
                            )
                        )
                    
                    tarjeta = ft.Container(
                        bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.CYAN_900),
                        border_radius=10,
                        padding=15,
                        border=ft.border.all(1, ft.Colors.CYAN_500),
                        content=ft.Column(contenido_tarjeta, spacing=8)
                    )
                
                contenedor_stats.controls.append(tarjeta)
        
        except Exception as e:
            contenedor_stats.controls.append(
                ft.Container(
                    bgcolor=ft.Colors.RED_900,
                    border_radius=10,
                    padding=15,
                    content=ft.Text(f"Error al cargar estadísticas: {str(e)}", color=ft.Colors.RED_200)
                )
            )
        
        page.update()
    
    # Botón de actualizar
    btn_actualizar = ft.ElevatedButton(
        "🔄 Actualizar Estadísticas",
        icon=ft.Icons.REFRESH,
        style=ft.ButtonStyle(
            bgcolor={ft.ControlState.DEFAULT: ft.Colors.CYAN_400},
            color={ft.ControlState.DEFAULT: ft.Colors.BLACK},
            shape=ft.RoundedRectangleBorder(radius=20),
        ),
        on_click=lambda e: (actualizar_info_conexion(), actualizar_estadisticas()),
        width=250,
    )
    
    # Botón de volver
    btn_volver = ft.ElevatedButton(
        "← Volver",
        icon=ft.Icons.ARROW_BACK,
        style=ft.ButtonStyle(
            bgcolor={ft.ControlState.DEFAULT: ft.Colors.RED_400},
            color={ft.ControlState.DEFAULT: ft.Colors.WHITE},
            shape=ft.RoundedRectangleBorder(radius=20),
        ),
        on_click=lambda e: go("/panel_super"),
        width=250,
    )
    
    # Encabezado con botones
    header = ft.Column([
        titulo,
        subtitulo,
        ft.Container(height=15),
        ft.Row([btn_actualizar, btn_volver], spacing=10),
        ft.Divider(height=20, color=ft.Colors.GREY_700),
    ], spacing=5)
    
    # Contenido principal
    contenido = ft.Container(
        expand=True,
        padding=30,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(0, -1),
            end=ft.Alignment(0, 1),
            colors=[ft.Colors.GREY_900, ft.Colors.BLACK],
        ),
        content=ft.Column([
            header,
            ft.Container(
                bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.GREY_800),
                border_radius=8,
                padding=10,
                content=info_conexion
            ),
            ft.Container(expand=True, content=contenedor_stats),
        ], expand=True, spacing=10),
    )
    
    # Cargar estadísticas e información de conexión al abrir la vista
    actualizar_info_conexion()
    actualizar_estadisticas()
    
    return ft.View(
        route="/estadisticas_sensores",
        controls=[contenido],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.START,
    )
