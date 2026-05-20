import flet as ft
from controllers.caja_fidelidad_controller import CajaFidelidadController


def EmpleadoFidelidadView(page: ft.Page, go):
    controller = CajaFidelidadController()
    cliente_actual = {"data": None}

    qr_input = ft.TextField(
        label="Contenido del QR del cliente",
        hint_text="Escanea o pega aquí el contenido del QR",
        prefix_icon=ft.Icons.QR_CODE_SCANNER_ROUNDED,
        border_radius=16,
        width=420,
        bgcolor=ft.Colors.with_opacity(0.06, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
        border_color=ft.Colors.with_opacity(0.18, ft.Colors.WHITE),
        focused_border_color="#64D7FF",
    )

    importe_input = ft.TextField(
        label="Importe de la compra (€)",
        prefix_icon=ft.Icons.EURO_ROUNDED,
        border_radius=16,
        width=240,
        bgcolor=ft.Colors.with_opacity(0.06, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
        border_color=ft.Colors.with_opacity(0.18, ft.Colors.WHITE),
        focused_border_color="#64D7FF",
    )

    referencia_input = ft.TextField(
        label="Referencia / ticket",
        prefix_icon=ft.Icons.RECEIPT_LONG_ROUNDED,
        border_radius=16,
        width=300,
        bgcolor=ft.Colors.with_opacity(0.06, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
        border_color=ft.Colors.with_opacity(0.18, ft.Colors.WHITE),
        focused_border_color="#64D7FF",
    )

    cliente_nombre = ft.Text("—", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    cliente_email = ft.Text("—", size=14, color=ft.Colors.WHITE70)
    cliente_puntos = ft.Text("0", size=20, weight=ft.FontWeight.BOLD, color="#9CEBFF")
    cliente_gasto = ft.Text("0.00 €", size=20, weight=ft.FontWeight.BOLD, color="#9CEBFF")
    cliente_card = ft.Container(visible=False)

    def mostrar_mensaje(msg, error=False):
        page.snack_bar = ft.SnackBar(
            ft.Text(msg),
            bgcolor=ft.Colors.RED_600 if error else ft.Colors.GREEN_600
        )
        page.snack_bar.open = True
        page.update()

    def render_cliente(cliente):
        cliente_actual["data"] = cliente
        cliente_nombre.value = cliente.get("nombre", "Sin nombre")
        cliente_email.value = cliente.get("email", "Sin email")
        cliente_puntos.value = str(cliente.get("loyalty_points", 0))
        cliente_gasto.value = f"{float(cliente.get('loyalty_total_spent', 0)):.2f} €"
        cliente_card.visible = True
        page.update()

    def validar_qr(e):
        ok, msg, cliente = controller.obtener_cliente_por_qr(qr_input.value)
        if not ok:
            cliente_actual["data"] = None
            cliente_card.visible = False
            mostrar_mensaje(msg, error=True)
            return

        render_cliente(cliente)
        mostrar_mensaje(msg)

    def registrar_compra(e):
        cliente = cliente_actual.get("data")
        if not cliente:
            mostrar_mensaje("Primero debes validar el QR del cliente.", error=True)
            return

        ok, msg, actualizado = controller.registrar_compra(
            cliente["id"],
            importe_input.value,
            referencia_input.value,
        )

        if not ok:
            mostrar_mensaje(msg, error=True)
            return

        render_cliente(actualizado)
        importe_input.value = ""
        referencia_input.value = ""
        mostrar_mensaje(msg)

    cliente_card.content = ft.Container(
        width=1180,
        padding=22,
        border_radius=22,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
        border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("Cliente validado", size=14, color=ft.Colors.WHITE60),
                        cliente_nombre,
                        cliente_email,
                    ],
                    spacing=6,
                ),
                ft.Row(
                    [
                        ft.Container(
                            width=180,
                            padding=18,
                            border_radius=18,
                            bgcolor=ft.Colors.with_opacity(0.07, ft.Colors.WHITE),
                            content=ft.Column(
                                [
                                    ft.Text("Puntos actuales", size=13, color=ft.Colors.WHITE60),
                                    cliente_puntos,
                                ],
                                spacing=6,
                            ),
                        ),
                        ft.Container(
                            width=220,
                            padding=18,
                            border_radius=18,
                            bgcolor=ft.Colors.with_opacity(0.07, ft.Colors.WHITE),
                            content=ft.Column(
                                [
                                    ft.Text("Gasto acumulado", size=13, color=ft.Colors.WHITE60),
                                    cliente_gasto,
                                ],
                                spacing=6,
                            ),
                        ),
                    ],
                    spacing=14,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

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
                    border=ft.border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
                    content=ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text(
                                        "Caja y fidelización",
                                        size=30,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                        "Escanea el QR del cliente en caja, valida su perfil y registra la compra para sumar puntos automáticamente.",
                                        size=14,
                                        color=ft.Colors.WHITE70,
                                    ),
                                    ft.Text(
                                        "Un lector de QR conectado al PC funciona como teclado y puede rellenar el campo automáticamente.",
                                        size=13,
                                        color=ft.Colors.WHITE54,
                                    ),
                                ],
                                spacing=6,
                            ),
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
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(height=18),
                ft.Container(
                    width=1180,
                    padding=22,
                    border_radius=22,
                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                    border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Column(
                        [
                            ft.Text(
                                "Validación de cliente",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Row(
                                [
                                    qr_input,
                                    ft.ElevatedButton(
                                        "Validar QR",
                                        icon=ft.Icons.VERIFIED_USER_ROUNDED,
                                        bgcolor="#64D7FF",
                                        color=ft.Colors.BLACK,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=16),
                                        ),
                                        on_click=validar_qr,
                                    ),
                                ],
                                spacing=14,
                                wrap=True,
                            ),
                        ],
                        spacing=14,
                    ),
                ),
                ft.Container(height=16),
                cliente_card,
                ft.Container(height=16),
                ft.Container(
                    width=1180,
                    padding=22,
                    border_radius=22,
                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                    border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Column(
                        [
                            ft.Text(
                                "Registrar compra",
                                size=20,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                "Introduce el importe de la compra y, si quieres, el número de ticket o referencia.",
                                size=14,
                                color=ft.Colors.WHITE70,
                            ),
                            ft.Row(
                                [
                                    importe_input,
                                    referencia_input,
                                    ft.ElevatedButton(
                                        "Registrar y sumar puntos",
                                        icon=ft.Icons.ADD_CARD_ROUNDED,
                                        bgcolor="#64D7FF",
                                        color=ft.Colors.BLACK,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=16),
                                        ),
                                        on_click=registrar_compra,
                                    ),
                                ],
                                spacing=14,
                                wrap=True,
                            ),
                            ft.Text(
                                "Regla actual: mínimo 1 punto por compra y, en general, 1 punto por cada 10 €.",
                                size=13,
                                color=ft.Colors.WHITE54,
                            ),
                        ],
                        spacing=14,
                    ),
                ),
            ],
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    return ft.View(
        route="/empleado_fidelidad",
        controls=[contenido],
        padding=0,
        spacing=0,
    )