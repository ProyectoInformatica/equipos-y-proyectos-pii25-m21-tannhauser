import asyncio
import flet as ft

from models.energy_manager import EnergyManager
from utils.ui_premium import (
    ACCENT_STRONG,
    CHAMPAGNE,
    SURFACE_SOFT,
    TEXT_MUTED,
    metric_card,
    premium_card,
    premium_header,
    premium_page,
    primary_button,
    secondary_button,
    status_badge,
)


class EnergiaView(ft.View):
    REFRESH_SECONDS = 10

    ICONS_BY_KIND = {
        "dht11": ft.Icons.THERMOSTAT_ROUNDED,
        "temperature": ft.Icons.THERMOSTAT_ROUNDED,
        "humidity": ft.Icons.WATER_DROP_ROUNDED,
        "mq135": ft.Icons.AIR_ROUNDED,
        "hc_sr04": ft.Icons.SENSORS_ROUNDED,
        "distance": ft.Icons.STRAIGHTEN_ROUNDED,
        "lcd16x2": ft.Icons.DISPLAY_SETTINGS_ROUNDED,
        "door": ft.Icons.DOOR_FRONT_DOOR_ROUNDED,
        "ldr": ft.Icons.WB_SUNNY_ROUNDED,
        "light": ft.Icons.LIGHTBULB_ROUNDED,
        "esp32_cam": ft.Icons.VIDEOCAM_ROUNDED,
        "camera": ft.Icons.VIDEOCAM_ROUNDED,
        "fridge": ft.Icons.KITCHEN_ROUNDED,
        "esp32": ft.Icons.MEMORY_ROUNDED,
        "generic": ft.Icons.SENSORS_ROUNDED,
    }

    def __init__(self, page: ft.Page, go):
        super().__init__(route="/energia", padding=0, spacing=0)
        self.page = page
        self.go = go
        self.manager = EnergyManager()
        self._running = False

        self.hero_slot = ft.Container(width=1180)
        self.metrics_slot = ft.Container(width=1180)
        self.history_slot = ft.Container(width=1180)
        self.devices_slot = ft.Container(width=1180)
        self.sustainability_slot = ft.Container(width=1180)
        self.last_update_text = ft.Text("Actualizando...", size=13, color=TEXT_MUTED)

        self.controls = [self._build()]
        self.refresh(None)

    def did_mount(self):
        self._running = True
        self.page.run_task(self._auto_refresh)

    def will_unmount(self):
        self._running = False

    async def _auto_refresh(self):
        while self._running:
            await asyncio.sleep(self.REFRESH_SECONDS)
            if self._running:
                self.refresh(None)

    def _build(self):
        header = premium_header(
            "Energia y sostenibilidad",
            "Consumo estimado de DHT11, MQ135, HC-SR04 y LCD 16x2.",
            actions=[
                secondary_button("Volver al panel", ft.Icons.ARROW_BACK_ROUNDED, on_click=lambda e: self.go("/panel_super")),
                primary_button("Refrescar", ft.Icons.REFRESH_ROUNDED, on_click=self.refresh),
            ],
        )
        return premium_page(
            [
                header,
                ft.Container(height=10),
                self.last_update_text,
                ft.Container(height=18),
                self.hero_slot,
                ft.Container(height=22),
                self.metrics_slot,
                ft.Container(height=22),
                self.history_slot,
                ft.Container(height=22),
                self.devices_slot,
                ft.Container(height=22),
                self.sustainability_slot,
            ]
        )

    def fmt(self, value, suffix="", decimals=2):
        try:
            return f"{float(value):.{decimals}f}{suffix}"
        except Exception:
            return f"-{suffix}"

    def progress_bar(self, value, max_value, color=ACCENT_STRONG, height=10):
        pct = 0 if max_value <= 0 else max(0, min(1, float(value) / float(max_value)))
        return ft.Container(
            height=height,
            border_radius=999,
            bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.WHITE),
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            content=ft.Row(
                [
                    ft.Container(expand=max(0.01, pct), bgcolor=color),
                    ft.Container(expand=max(0.01, 1 - pct), bgcolor=ft.Colors.TRANSPARENT),
                ],
                spacing=0,
            ),
        )

    def icon_for_device(self, device):
        return self.ICONS_BY_KIND.get(device.get("kind"), ft.Icons.SENSORS_ROUNDED)

    def device_card(self, device, max_power):
        power = float(device.get("power_w") or 0)
        if power >= max_power * 0.75:
            color = CHAMPAGNE
        elif power >= max_power * 0.35:
            color = "#B8FFE1"
        else:
            color = ACCENT_STRONG

        return premium_card(
            col={"xs": 12, "md": 6, "lg": 4},
            padding=20,
            border_radius=24,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                width=54,
                                height=54,
                                border_radius=18,
                                bgcolor=ft.Colors.with_opacity(0.13, color),
                                border=ft.border.all(1, ft.Colors.with_opacity(0.16, color)),
                                alignment=ft.alignment.center,
                                content=ft.Icon(self.icon_for_device(device), color=color, size=28),
                            ),
                            ft.Column(
                                [
                                    ft.Text(device["device_name"], size=17, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    ft.Text(device["location_name"], size=12, color=TEXT_MUTED),
                                ],
                                spacing=3,
                                expand=True,
                            ),
                        ],
                        spacing=12,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            status_badge(device["kind"], "gold" if color == CHAMPAGNE else "cyan"),
                            ft.Text(self.fmt(power, " W", 3), size=19, weight=ft.FontWeight.BOLD, color=color),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    self.progress_bar(power, max_power, color),
                    ft.Row(
                        [
                            ft.Text(f"Dia {self.fmt(device['daily_wh'], ' Wh')}", size=12, color=TEXT_MUTED),
                            ft.Text(f"Mes {self.fmt(device['monthly_kwh'], ' kWh', 3)}", size=12, color=TEXT_MUTED),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Text(f"{device['device_code']} - {device['source']}", size=11, color=ft.Colors.WHITE38),
                ],
                spacing=12,
            ),
        )

    def history_chart(self, history):
        if not history:
            return premium_card(
                width=1180,
                padding=24,
                border_radius=28,
                content=ft.Text("Aun no hay snapshots energeticos guardados.", color=TEXT_MUTED, size=15),
            )

        values = [float(row.get("total_watts") or 0) for row in history]
        max_value = max(values) or 1
        bars = []
        for row, value in zip(history, values):
            dt = row.get("created_at")
            label = dt.strftime("%H:%M") if hasattr(dt, "strftime") else str(dt)[11:16]
            bars.append(
                ft.Column(
                    [
                        ft.Container(
                            width=24,
                            height=max(14, min(140, int((value / max_value) * 140))),
                            border_radius=8,
                            bgcolor=CHAMPAGNE if value == max_value else ACCENT_STRONG,
                            tooltip=f"{self.fmt(value, ' W', 3)} - {label}",
                        ),
                        ft.Text(label, size=10, color=ft.Colors.WHITE54, rotate=ft.Rotate(0)),
                    ],
                    spacing=6,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.END,
                )
            )

        return premium_card(
            width=1180,
            padding=24,
            border_radius=28,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Evolucion del consumo", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            status_badge(f"{len(history)} snapshots", "cyan"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Text("Historico guardado en MySQL. La vista refresca cada 10s; la BD se escribe como maximo una vez por minuto.", color=TEXT_MUTED, size=13),
                    ft.Container(
                        height=180,
                        alignment=ft.alignment.bottom_center,
                        content=ft.Row(bars, spacing=10, alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.END),
                    ),
                ],
                spacing=14,
            ),
        )

    def recommendation_card(self, text, index):
        color = CHAMPAGNE if index == 0 else ACCENT_STRONG
        return ft.Container(
            padding=18,
            border_radius=22,
            bgcolor=ft.Colors.with_opacity(0.08, color),
            border=ft.border.all(1, ft.Colors.with_opacity(0.16, color)),
            content=ft.Row(
                [
                    ft.Container(
                        width=38,
                        height=38,
                        border_radius=13,
                        bgcolor=ft.Colors.with_opacity(0.13, color),
                        alignment=ft.alignment.center,
                        content=ft.Icon(ft.Icons.ECO_ROUNDED, color=color, size=21),
                    ),
                    ft.Text(text, size=14, color=ft.Colors.WHITE, expand=True),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def refresh(self, e):
        data = self.manager.resumen(persist=True)
        totals = data["totals"]
        devices = data["devices"]
        history = data.get("history") or []
        assumptions = data["assumptions"]
        state = totals["state"]
        top_device = totals.get("top_device") or {}
        max_power = max([float(device["power_w"]) for device in devices] or [1])
        saved = data.get("snapshot_saved")

        self.last_update_text.value = "Ultima actualizacion local: ahora - snapshot guardado" if saved else "Ultima actualizacion local: ahora - snapshot reutilizado por limite de escritura"

        self.hero_slot.content = premium_card(
            width=1180,
            padding=28,
            border_radius=28,
            content=ft.Row(
                [
                    ft.Column(
                        [
                            ft.Row(
                                [
                                    status_badge("Solo superusuario", "gold"),
                                    status_badge(state["label"], state["tone"]),
                                ],
                                spacing=10,
                                wrap=True,
                            ),
                            ft.Text("Estado energetico de sensores reales", size=34, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Text(f"{state['summary']} El consumo mostrado es estimado salvo que exista consumption_w en readings.", size=16, color=TEXT_MUTED, width=680),
                            self.progress_bar(totals["efficiency_pct"], 100, "#B8FFE1" if totals["efficiency_pct"] >= 70 else CHAMPAGNE, 12),
                            ft.Text(f"Eficiencia global estimada: {self.fmt(totals['efficiency_pct'], '%', 1)}", size=14, color=ft.Colors.WHITE70),
                        ],
                        spacing=12,
                        expand=True,
                    ),
                    ft.Container(
                        width=282,
                        padding=22,
                        border_radius=24,
                        bgcolor=SURFACE_SOFT,
                        border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                        content=ft.Column(
                            [
                                ft.Icon(self.icon_for_device(top_device), color=CHAMPAGNE, size=36),
                                ft.Text("Mayor consumidor", size=13, color=ft.Colors.WHITE60),
                                ft.Text(top_device.get("device_name", "Sin datos"), size=21, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                ft.Text(self.fmt(top_device.get("power_w", 0), " W", 3), size=18, color=CHAMPAGNE, weight=ft.FontWeight.BOLD),
                            ],
                            spacing=8,
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

        self.metrics_slot.content = ft.ResponsiveRow(
            [
                metric_card(ft.Icons.ELECTRIC_BOLT_ROUNDED, "Consumo actual estimado", self.fmt(totals["instant_w"], " W", 3), assumptions["scope"], "gold", col={"xs": 12, "md": 4, "lg": 3}),
                metric_card(ft.Icons.CALENDAR_TODAY_ROUNDED, "Consumo diario estimado", self.fmt(totals["daily_kwh"], " kWh", 3), self.fmt(totals["daily_wh"], " Wh"), "cyan", col={"xs": 12, "md": 4, "lg": 3}),
                metric_card(ft.Icons.DATE_RANGE_ROUNDED, "Consumo mensual estimado", self.fmt(totals["monthly_kwh"], " kWh", 3), f"{totals['device_count']} dispositivos reales", "cyan", col={"xs": 12, "md": 4, "lg": 3}),
                metric_card(ft.Icons.EURO_ROUNDED, "Coste mensual", self.fmt(totals["cost_month_eur"], " EUR"), f"{assumptions['price_eur_kwh']} EUR/kWh", "gold", col={"xs": 12, "md": 4, "lg": 3}),
                metric_card(ft.Icons.CLOUD_ROUNDED, "CO2 mensual", self.fmt(totals["co2_month_kg"], " kg"), f"{assumptions['co2_kg_kwh']} kg/kWh", "cyan", col={"xs": 12, "md": 4, "lg": 3}),
                metric_card(ft.Icons.SAVINGS_ROUNDED, "Ahorro potencial", "5-15%", "Muestreo adaptativo y backlight LCD", "gold", col={"xs": 12, "md": 4, "lg": 3}),
            ],
            spacing=16,
            run_spacing=16,
        )

        self.history_slot.content = self.history_chart(history)

        self.devices_slot.content = premium_card(
            width=1180,
            padding=24,
            border_radius=28,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Desglose por sensor real", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            status_badge("DHT11 / MQ135 / HC-SR04 / LCD", "cyan"),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Text("Cards visuales centradas en sensores reales; si hay readings.consumption_w se usa como dato medido.", color=TEXT_MUTED, size=14),
                    ft.ResponsiveRow(
                        [self.device_card(device, max_power) for device in sorted(devices, key=lambda item: item["power_w"], reverse=True)],
                        spacing=16,
                        run_spacing=16,
                    ),
                ],
                spacing=14,
            ),
        )

        self.sustainability_slot.content = ft.ResponsiveRow(
            [
                premium_card(
                    col={"xs": 12, "md": 6},
                    padding=24,
                    border_radius=28,
                    content=ft.Column(
                        [
                            ft.Text("Recomendaciones automaticas", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Column([self.recommendation_card(text, i) for i, text in enumerate(data["recommendations"])], spacing=12),
                        ],
                        spacing=14,
                    ),
                ),
                premium_card(
                    col={"xs": 12, "md": 6},
                    padding=24,
                    border_radius=28,
                    content=ft.Column(
                        [
                            ft.Text("Escalabilidad energetica", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Text("Arquitectura preparada para crecer sin cambiar la base del historico energetico.", size=14, color=TEXT_MUTED),
                            ft.Divider(color=ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                            ft.Column(
                                [
                                    self.architecture_item(item)
                                    for item in data.get("architecture", [])
                                ],
                                spacing=10,
                            ),
                            ft.Text(f"Huella estimada mensual: {self.fmt(totals['co2_month_kg'], ' kg CO2')}. Objetivo: {assumptions['target_monthly_kwh']} kWh/mes.", color=ft.Colors.WHITE70),
                        ],
                        spacing=12,
                    ),
                ),
            ],
            spacing=16,
            run_spacing=16,
        )

        try:
            self.update()
        except AssertionError:
            pass

    def architecture_item(self, item):
        icon_name = item.get("icon", "sensors")
        icon = {
            "hub": ft.Icons.HUB_ROUNDED,
            "history": ft.Icons.HISTORY_ROUNDED,
            "sensors": ft.Icons.SENSORS_ROUNDED,
        }.get(icon_name, ft.Icons.SENSORS_ROUNDED)
        return ft.Container(
            padding=14,
            border_radius=18,
            bgcolor=ft.Colors.with_opacity(0.06, CHAMPAGNE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.16, CHAMPAGNE)),
            content=ft.Row(
                [
                    ft.Icon(icon, color=CHAMPAGNE, size=22),
                    ft.Column(
                        [
                            ft.Text(item.get("label", "Modulo"), size=14, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Text(item.get("detail", ""), size=12, color=TEXT_MUTED),
                        ],
                        spacing=2,
                        expand=True,
                    ),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
