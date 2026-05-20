import os
import json
import statistics
from datetime import datetime, timedelta
import flet as ft
from utils.navigation import ruta_dashboard_por_rol


class EstadisticasSensoresView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/estadisticas_sensores", padding=0, spacing=0)
        self.page = page
        self.go = go
        self.base_path = os.path.join("data", "sensors")

        self.total_sensores_text = ft.Text("0", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.total_registros_text = ft.Text("0", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
        self.consumo_total_text = ft.Text("0.0000 kWh", size=28, weight=ft.FontWeight.BOLD, color="#9CEBFF")
        self.ultima_actualizacion_text = ft.Text("Sin dato", size=22, weight=ft.FontWeight.BOLD, color="#9CEBFF")

        self.estado_archivos_column = ft.Column(spacing=8)
        self.cards_column = ft.Column(spacing=18)
        self.error_text = ft.Text("", color=ft.Colors.RED_300, size=14)

        self.controls = [self._build_ui()]

    def did_mount(self):
        self.refrescar_estadisticas()

    def _build_ui(self):
        return ft.Container(
            expand=True,
            padding=28,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, -1),
                end=ft.Alignment(1, 1),
                colors=["#050A12", "#09172A", "#0B2342", "#0E2F55"],
            ),
            content=ft.Column(
                [
                    ft.Container(
                        width=1180,
                        padding=24,
                        border_radius=28,
                        bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
                        content=ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Text(
                                            "Estadísticas de sensores",
                                            size=34,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE,
                                        ),
                                        ft.Text(
                                            "Monitoreo y análisis de datos reales recogidos por los sensores del supermercado.",
                                            size=15,
                                            color=ft.Colors.WHITE70,
                                        ),
                                    ],
                                    spacing=6,
                                ),
                                ft.Row(
                                    [
                                        ft.ElevatedButton(
                                            "Actualizar estadísticas",
                                            icon=ft.Icons.REFRESH_ROUNDED,
                                            bgcolor="#64D7FF",
                                            color=ft.Colors.BLACK,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=16),
                                            ),
                                            on_click=lambda e: self.refrescar_estadisticas(),
                                        ),
                                        ft.OutlinedButton(
                                            "Volver",
                                            icon=ft.Icons.ARROW_BACK_ROUNDED,
                                            style=ft.ButtonStyle(
                                                color=ft.Colors.WHITE,
                                                side=ft.BorderSide(1.1, ft.Colors.with_opacity(0.28, ft.Colors.WHITE)),
                                                shape=ft.RoundedRectangleBorder(radius=16),
                                            ),
                                            on_click=lambda e: self.go(ruta_dashboard_por_rol()),
                                        ),
                                    ],
                                    spacing=12,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                    ft.Container(height=18),
                    self.error_text,
                    ft.Row(
                        [
                            self._metric_card("Sensores detectados", self.total_sensores_text),
                            self._metric_card("Registros analizados", self.total_registros_text),
                            self._metric_card("Consumo total", self.consumo_total_text),
                            self._metric_card("Última actualización", self.ultima_actualizacion_text),
                        ],
                        spacing=16,
                        wrap=True,
                    ),
                    ft.Container(height=18),
                    ft.Container(
                        width=1180,
                        padding=20,
                        border_radius=24,
                        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Estado de archivos de sensores",
                                    size=20,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                                self.estado_archivos_column,
                            ],
                            spacing=12,
                        ),
                    ),
                    ft.Container(height=18),
                    self.cards_column,
                ],
                spacing=0,
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def _metric_card(self, titulo, valor_widget):
        return ft.Container(
            width=280,
            padding=22,
            border_radius=22,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
            content=ft.Column(
                [
                    ft.Text(titulo, size=14, color=ft.Colors.WHITE60),
                    valor_widget,
                ],
                spacing=10,
            ),
        )

    def _read_sensor_file(self, path):
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []

    def _to_float(self, value):
        try:
            return float(value)
        except Exception:
            return None

    def _parse_datetime(self, value):
        if not value:
            return None
        formatos = [
            "%Y-%m-%d %H:%M:%S",
            "%d/%m/%Y %H:%M:%S",
            "%Y-%m-%dT%H:%M:%S",
        ]
        for fmt in formatos:
            try:
                return datetime.strptime(value, fmt)
            except Exception:
                continue
        return None

    def _extraer_valores(self, data):
        valores = []
        timestamps = []
        consumos = []

        for item in data:
            if not isinstance(item, dict):
                continue

            value = (
                item.get("value")
                or item.get("valor")
                or item.get("temperatura")
                or item.get("humedad")
                or item.get("distancia")
                or item.get("calidad_aire")
                or item.get("intensidad")
            )

            consumo = (
                item.get("consumption_w")
                or item.get("consumo_w")
                or item.get("power_w")
                or item.get("potencia_w")
            )

            ts = (
                item.get("timestamp")
                or item.get("recorded_at")
                or item.get("fecha")
                or item.get("datetime")
            )

            fv = self._to_float(value)
            if fv is not None:
                valores.append(fv)

            fc = self._to_float(consumo)
            if fc is not None:
                consumos.append(fc)

            dt = self._parse_datetime(ts)
            if dt:
                timestamps.append(dt)

        return valores, timestamps, consumos

    def _kwh_total(self, consumos):
        if not consumos:
            return 0.0
        media_w = sum(consumos) / len(consumos)
        return media_w / 1000.0

    def _wh_ultimas_24h(self, consumos, timestamps):
        if not consumos or not timestamps or len(consumos) != len(timestamps):
            return 0.0

        ahora = max(timestamps)
        limite = ahora - timedelta(hours=24)
        valores = [c for c, t in zip(consumos, timestamps) if t >= limite]

        if not valores:
            return 0.0

        media_w = sum(valores) / len(valores)
        return media_w * 24.0

    def _stat_item(self, titulo, valor):
        return ft.Column(
            [
                ft.Text(titulo, size=13, color=ft.Colors.WHITE60),
                ft.Text(valor, size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ],
            spacing=4,
        )

    def _sensor_card(self, titulo, total_lecturas, minimo, maximo, promedio, mediana, desv, rango, ultima, consumo_medio_w, consumo_total_kwh, consumo_24h_wh):
        def v(x):
            return str(x) if x is not None else "Sin dato"

        return ft.Container(
            width=1180,
            padding=24,
            border_radius=26,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.CYAN_200)),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text(
                                titulo,
                                size=24,
                                weight=ft.FontWeight.BOLD,
                                color="#9CEBFF",
                            ),
                            ft.Text(
                                f"Total de lecturas: {total_lecturas}",
                                size=15,
                                color=ft.Colors.WHITE70,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Divider(color=ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    ft.Row(
                        [
                            self._stat_item("Mínimo", v(minimo)),
                            self._stat_item("Máximo", v(maximo)),
                            self._stat_item("Promedio", v(promedio)),
                            self._stat_item("Mediana", v(mediana)),
                            self._stat_item("Desv. estándar", v(desv)),
                            self._stat_item("Rango", v(rango)),
                        ],
                        wrap=True,
                        spacing=28,
                    ),
                    ft.Text(
                        f"Última lectura: {ultima}" if ultima else "Última lectura: Sin dato",
                        size=14,
                        color="#D7F36B",
                        italic=True,
                    ),
                    ft.Divider(color=ft.Colors.with_opacity(0.08, ft.Colors.WHITE)),
                    ft.Row(
                        [
                            self._stat_item("Media consumo", f"{consumo_medio_w:.4f} W"),
                            self._stat_item("Consumo total", f"{consumo_total_kwh:.6f} kWh"),
                            self._stat_item("Consumo últimas 24h", f"{consumo_24h_wh:.2f} Wh"),
                        ],
                        wrap=True,
                        spacing=28,
                    ),
                ],
                spacing=10,
            ),
        )

    def refrescar_estadisticas(self):
        try:
            self.error_text.value = ""
            archivos = {
                "TEMPERATURA": os.path.join(self.base_path, "sensor_temperatura.json"),
                "HUMEDAD": os.path.join(self.base_path, "sensor_humedad.json"),
                "LUZ": os.path.join(self.base_path, "sensor_luz.json"),
                "NEVERA": os.path.join(self.base_path, "sensor_nevera.json"),
                "PUERTA": os.path.join(self.base_path, "sensor_puerta.json"),
            }

            self.estado_archivos_column.controls.clear()
            self.cards_column.controls.clear()

            total_sensores = 0
            total_registros = 0
            consumo_total = 0.0
            ultima_global = None

            for nombre, ruta in archivos.items():
                data = self._read_sensor_file(ruta)
                total = len(data)

                self.estado_archivos_column.controls.append(
                    ft.Text(
                        f"{'✓' if total > 0 else '•'} {nombre}: {total} registros",
                        size=14,
                        color=ft.Colors.GREEN_300 if total > 0 else ft.Colors.WHITE54,
                    )
                )

                if total == 0:
                    continue

                total_sensores += 1
                total_registros += total

                valores, timestamps, consumos = self._extraer_valores(data)

                if timestamps:
                    ultima_local = max(timestamps)
                    if ultima_global is None or ultima_local > ultima_global:
                        ultima_global = ultima_local
                    ultima_txt = ultima_local.strftime("%d/%m/%Y %H:%M:%S")
                else:
                    ultima_txt = None

                if valores:
                    minimo = round(min(valores), 2)
                    maximo = round(max(valores), 2)
                    promedio = round(sum(valores) / len(valores), 2)
                    mediana = round(statistics.median(valores), 2)
                    desv = round(statistics.pstdev(valores), 2) if len(valores) > 1 else 0.0
                    rango = round(max(valores) - min(valores), 2)
                else:
                    minimo = maximo = promedio = mediana = desv = rango = None

                if consumos:
                    consumo_medio_w = sum(consumos) / len(consumos)
                    consumo_total_kwh = self._kwh_total(consumos)
                    consumo_24h_wh = self._wh_ultimas_24h(consumos, timestamps) if timestamps and len(consumos) == len(timestamps) else 0.0
                else:
                    consumo_medio_w = 0.0
                    consumo_total_kwh = 0.0
                    consumo_24h_wh = 0.0

                consumo_total += consumo_total_kwh

                self.cards_column.controls.append(
                    self._sensor_card(
                        titulo=nombre,
                        total_lecturas=total,
                        minimo=minimo,
                        maximo=maximo,
                        promedio=promedio,
                        mediana=mediana,
                        desv=desv,
                        rango=rango,
                        ultima=ultima_txt,
                        consumo_medio_w=consumo_medio_w,
                        consumo_total_kwh=consumo_total_kwh,
                        consumo_24h_wh=consumo_24h_wh,
                    )
                )

            self.total_sensores_text.value = str(total_sensores)
            self.total_registros_text.value = str(total_registros)
            self.consumo_total_text.value = f"{consumo_total:.6f} kWh"
            self.ultima_actualizacion_text.value = (
                ultima_global.strftime("%d/%m/%Y %H:%M:%S") if ultima_global else "Sin dato"
            )

            if not self.cards_column.controls:
                self.cards_column.controls.append(
                    ft.Container(
                        width=1180,
                        padding=24,
                        border_radius=24,
                        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                        border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                        content=ft.Text(
                            "No se han encontrado datos reales de sensores para mostrar estadísticas.",
                            size=16,
                            color=ft.Colors.WHITE70,
                        ),
                    )
                )

            self.update()
        except Exception as ex:
            self.estado_archivos_column.controls.clear()
            self.cards_column.controls.clear()
            self.error_text.value = f"Error cargando estadísticas: {ex}"
            self.update()