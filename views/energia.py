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
    secondary_button,
    status_badge,
)


def EnergiaView(page: ft.Page, go):
    manager = EnergyManager()
    data = manager.resumen()
    totals = data["totals"]
    devices = data["devices"]
    assumptions = data["assumptions"]
    top_device = totals.get("top_device") or {}
    max_power = max([device["power_w"] for device in devices] or [1])

    def fmt(value, suffix="", decimals=2):
        try:
            return f"{float(value):.{decimals}f}{suffix}"
        except Exception:
            return f"-{suffix}"

    def progress_bar(value, max_value, color=ACCENT_STRONG):
        pct = 0 if max_value <= 0 else max(0, min(1, float(value) / float(max_value)))
        return ft.Container(
            height=10,
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

    def device_row(device):
        if device["power_w"] >= max_power * 0.75:
            color = CHAMPAGNE
        elif device["power_w"] >= max_power * 0.35:
            color = "#B8FFE1"
        else:
            color = ACCENT_STRONG

        return premium_card(
            padding=18,
            border_radius=22,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text(device["device_name"], size=17, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    ft.Text(
                                        f"{device['device_code']} · {device['location_name']} · {device['source']}",
                                        size=12,
                                        color=TEXT_MUTED,
                                    ),
                                ],
                                spacing=4,
                                expand=True,
                            ),
                            status_badge(device["kind"], "gold" if color == CHAMPAGNE else "cyan"),
                            ft.Text(fmt(device["power_w"], " W", 3), size=18, weight=ft.FontWeight.BOLD, color=color),
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    progress_bar(device["power_w"], max_power, color),
                    ft.Row(
                        [
                            ft.Text(f"Dia: {fmt(device['daily_wh'], ' Wh')}", size=12, color=TEXT_MUTED),
                            ft.Text(f"Mes: {fmt(device['monthly_kwh'], ' kWh', 3)}", size=12, color=TEXT_MUTED),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ],
                spacing=12,
            ),
        )

    def recommendation_card(text, index):
        return ft.Container(
            padding=18,
            border_radius=22,
            bgcolor=ft.Colors.with_opacity(0.07, CHAMPAGNE if index == 0 else ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.13, CHAMPAGNE if index == 0 else ft.Colors.WHITE)),
            content=ft.Row(
                [
                    ft.Container(
                        width=38,
                        height=38,
                        border_radius=13,
                        bgcolor=ft.Colors.with_opacity(0.13, CHAMPAGNE),
                        alignment=ft.alignment.center,
                        content=ft.Icon(ft.Icons.ECO_ROUNDED, color=CHAMPAGNE, size=21),
                    ),
                    ft.Text(text, size=14, color=ft.Colors.WHITE, expand=True),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    state = totals["state"]
    header = premium_header(
        "Eficiencia energetica",
        "Consumo estimado, sostenibilidad y recomendaciones de ahorro.",
        actions=[secondary_button("Volver al panel", ft.Icons.ARROW_BACK_ROUNDED, on_click=lambda e: go("/panel_super"))],
    )

    hero = premium_card(
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
                        ft.Text("Estado sostenible del supermercado", size=34, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text(state["summary"], size=16, color=TEXT_MUTED, width=640),
                        ft.Container(height=8),
                        progress_bar(totals["efficiency_pct"], 100, "#B8FFE1" if totals["efficiency_pct"] >= 70 else CHAMPAGNE),
                        ft.Text(f"Eficiencia global estimada: {fmt(totals['efficiency_pct'], '%', 1)}", size=14, color=ft.Colors.WHITE70),
                    ],
                    spacing=12,
                    expand=True,
                ),
                ft.Container(
                    width=270,
                    padding=22,
                    border_radius=24,
                    bgcolor=SURFACE_SOFT,
                    border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Column(
                        [
                            ft.Icon(ft.Icons.BOLT_ROUNDED, color=CHAMPAGNE, size=34),
                            ft.Text("Mayor consumo", size=13, color=ft.Colors.WHITE60),
                            ft.Text(top_device.get("device_name", "Sin datos"), size=21, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Text(fmt(top_device.get("power_w", 0), " W", 3), size=18, color=CHAMPAGNE, weight=ft.FontWeight.BOLD),
                        ],
                        spacing=8,
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    metrics = ft.ResponsiveRow(
        [
            metric_card(ft.Icons.ELECTRIC_BOLT_ROUNDED, "Consumo instantaneo", fmt(totals["instant_w"], " W", 3), "Estimado en tiempo real", "gold", col={"xs": 12, "md": 4, "lg": 3}),
            metric_card(ft.Icons.CALENDAR_TODAY_ROUNDED, "Consumo diario", fmt(totals["daily_kwh"], " kWh", 3), f"{fmt(totals['daily_wh'], ' Wh')}", "cyan", col={"xs": 12, "md": 4, "lg": 3}),
            metric_card(ft.Icons.DATE_RANGE_ROUNDED, "Consumo mensual", fmt(totals["monthly_kwh"], " kWh", 3), f"{totals['device_count']} dispositivos estimados", "cyan", col={"xs": 12, "md": 4, "lg": 3}),
            metric_card(ft.Icons.EURO_ROUNDED, "Coste mensual", fmt(totals["cost_month_eur"], " EUR"), f"{assumptions['price_eur_kwh']} EUR/kWh", "gold", col={"xs": 12, "md": 4, "lg": 3}),
            metric_card(ft.Icons.CLOUD_ROUNDED, "CO2 mensual", fmt(totals["co2_month_kg"], " kg"), f"{assumptions['co2_kg_kwh']} kg/kWh", "cyan", col={"xs": 12, "md": 4, "lg": 3}),
            metric_card(ft.Icons.ECO_ROUNDED, "Eficiencia", fmt(totals["efficiency_pct"], "%", 1), f"Objetivo: {assumptions['target_monthly_kwh']} kWh/mes", "gold", col={"xs": 12, "md": 4, "lg": 3}),
        ],
        spacing=16,
        run_spacing=16,
    )

    chart = premium_card(
        width=1180,
        padding=24,
        border_radius=28,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Consumo por dispositivo", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        status_badge("Estimacion local", "cyan"),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Text("Barras normalizadas segun el mayor consumo detectado.", size=14, color=TEXT_MUTED),
                ft.Column([device_row(device) for device in sorted(devices, key=lambda item: item["power_w"], reverse=True)], spacing=12),
            ],
            spacing=14,
        ),
    )

    sustainability = ft.ResponsiveRow(
        [
            premium_card(
                col={"xs": 12, "md": 6},
                padding=24,
                border_radius=28,
                content=ft.Column(
                    [
                        ft.Text("Recomendaciones automaticas", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Column([recommendation_card(text, i) for i, text in enumerate(data["recommendations"])], spacing=12),
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
                        ft.Text("Datos ecosostenibles", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                        ft.Text("El calculo combina dispositivos activos, estados disponibles y potencias razonables por tipo.", size=14, color=TEXT_MUTED),
                        ft.Divider(color=ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                        ft.Text(f"Ahorro potencial recomendado: 8-18% si se reducen luces y muestreo fuera de horario.", color=ft.Colors.WHITE70),
                        ft.Text(f"Huella estimada mensual: {fmt(totals['co2_month_kg'], ' kg CO2')}.", color=ft.Colors.WHITE70),
                        ft.Text("El modulo es read-only: no escribe en base de datos ni cambia configuracion de dispositivos.", color=ft.Colors.WHITE70),
                    ],
                    spacing=12,
                ),
            ),
        ],
        spacing=16,
        run_spacing=16,
    )

    content = premium_page(
        [
            header,
            ft.Container(height=18),
            hero,
            ft.Container(height=22),
            metrics,
            ft.Container(height=22),
            chart,
            ft.Container(height=22),
            sustainability,
        ]
    )

    return ft.View(route="/energia", controls=[content], padding=0, spacing=0)
