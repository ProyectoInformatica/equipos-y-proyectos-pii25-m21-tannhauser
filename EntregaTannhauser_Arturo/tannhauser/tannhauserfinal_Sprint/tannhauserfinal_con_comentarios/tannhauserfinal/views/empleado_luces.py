import flet as ft
from controllers.luces_controller import LucesController


def EmpleadoLucesView(page: ft.Page, go):
    controller = LucesController()
    lista_luces = ft.Column(spacing=18)

    def mostrar_mensaje(msg, error=False):
        page.snack_bar = ft.SnackBar(
            ft.Text(msg),
            bgcolor=ft.Colors.RED_600 if error else ft.Colors.GREEN_600
        )
        page.snack_bar.open = True
        page.update()

    def crear_card_luz(luz: dict):
        switch_estado = ft.Switch(
            value=luz.get("encendida", False),
            active_color="#64D7FF",
        )

        intensidad_text = ft.Text(
            f"{int(luz.get('intensidad', 0))} %",
            size=14,
            color=ft.Colors.WHITE70,
        )

        slider_intensidad = ft.Slider(
            min=0,
            max=100,
            divisions=20,
            value=int(luz.get("intensidad", 0)),
            expand=True,
            active_color="#64D7FF",
            inactive_color=ft.Colors.with_opacity(0.18, ft.Colors.WHITE),
        )

        def on_slider_change(e):
            intensidad_text.value = f"{int(slider_intensidad.value)} %"
            page.update()

        slider_intensidad.on_change = on_slider_change

        def guardar_luz(e):
            ok, msg = controller.guardar_luz(
                luz["device_id"],
                bool(switch_estado.value),
                int(slider_intensidad.value),
            )
            mostrar_mensaje(msg, error=not ok)
            if ok:
                refrescar_luces()

        return ft.Container(
            width=1180,
            padding=22,
            border_radius=22,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Row(
                                [
                                    ft.Container(
                                        width=52,
                                        height=52,
                                        border_radius=16,
                                        bgcolor=ft.Colors.with_opacity(0.14, ft.Colors.CYAN_300),
                                        alignment=ft.Alignment.CENTER,
                                        content=ft.Icon(ft.Icons.LIGHTBULB_ROUNDED, color="#9CEBFF", size=26),
                                    ),
                                    ft.Column(
                                        [
                                            ft.Text(
                                                luz.get("device_name", "Luz"),
                                                size=20,
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.WHITE,
                                            ),
                                            ft.Text(
                                                f"Código: {luz.get('device_code', '—')} · Ubicación: {luz.get('location_name', 'Sin ubicación')}",
                                                size=13,
                                                color=ft.Colors.WHITE60,
                                            ),
                                        ],
                                        spacing=4,
                                    ),
                                ],
                                spacing=14,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Container(
                                padding=ft.Padding(14, 8, 14, 8),
                                border_radius=999,
                                bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.WHITE),
                                content=ft.Text(
                                    "Encendida" if switch_estado.value else "Apagada",
                                    size=13,
                                    color=ft.Colors.WHITE,
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Container(height=6),
                    ft.Row(
                        [
                            ft.Text("Estado", width=110, color=ft.Colors.WHITE70),
                            switch_estado,
                            ft.Text("Apagada", color=ft.Colors.WHITE60),
                            ft.Text(" / ", color=ft.Colors.WHITE38),
                            ft.Text("Encendida", color=ft.Colors.WHITE60),
                        ],
                        spacing=10,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.Text("Intensidad", width=110, color=ft.Colors.WHITE70),
                            slider_intensidad,
                            intensidad_text,
                        ],
                        spacing=12,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.Button(
                                "Guardar cambios",
                                icon=ft.Icons.SAVE_ROUNDED,
                                bgcolor="#64D7FF",
                                color=ft.Colors.BLACK,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=16),
                                ),
                                on_click=guardar_luz,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
                spacing=14,
            ),
        )

    def refrescar_luces():
        luces = controller.listar_luces()
        lista_luces.controls.clear()

        if not luces:
            lista_luces.controls.append(
                ft.Container(
                    width=1180,
                    padding=24,
                    border_radius=20,
                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                    border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Column(
                        [
                            ft.Text(
                                "No se han encontrado dispositivos de luz",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                "Revisa la tabla devices y asegúrate de tener dispositivos como light_01, light_02, etc.",
                                size=14,
                                color=ft.Colors.WHITE70,
                            ),
                        ],
                        spacing=8,
                    ),
                )
            )
        else:
            for luz in luces:
                lista_luces.controls.append(crear_card_luz(luz))

        page.update()

    refrescar_luces()

    contenido = ft.Container(
        expand=True,
        padding=24,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=["#050A12", "#09172A", "#0B2342", "#0E2F55"],
        ),
        content=ft.Column(
            [
                ft.Container(
                    width=1180,
                    padding=22,
                    border_radius=24,
                    bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
                    border=ft.Border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
                    content=ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text(
                                        "Control de luces",
                                        size=30,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                        "Enciende o apaga las luces disponibles y ajusta la intensidad de cada una.",
                                        size=14,
                                        color=ft.Colors.WHITE70,
                                    ),
                                ],
                                spacing=6,
                            ),
                            ft.Row(
                                [
                                    ft.OutlinedButton(
                                        "Volver al panel",
                                        icon=ft.Icons.ARROW_BACK_ROUNDED,
                                        style=ft.ButtonStyle(
                                            color=ft.Colors.WHITE,
                                            side=ft.BorderSide(1.1, ft.Colors.with_opacity(0.28, ft.Colors.WHITE)),
                                            shape=ft.RoundedRectangleBorder(radius=16),
                                        ),
                                        on_click=lambda e: go("/panel_empleado"),
                                    ),
                                    ft.Button(
                                        "Refrescar",
                                        icon=ft.Icons.REFRESH_ROUNDED,
                                        bgcolor="#64D7FF",
                                        color=ft.Colors.BLACK,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=16),
                                        ),
                                        on_click=lambda e: refrescar_luces(),
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
                lista_luces,
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    return ft.View(
        route="/empleado_luces",
        controls=[contenido],
        padding=0,
        spacing=0,
    )