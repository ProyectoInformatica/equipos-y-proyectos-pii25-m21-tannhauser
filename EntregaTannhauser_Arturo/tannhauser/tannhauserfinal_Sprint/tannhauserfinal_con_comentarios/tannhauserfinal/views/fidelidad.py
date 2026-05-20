import flet as ft
import io
import json
import base64

try:
    import qrcode
except Exception:
    qrcode = None

from controllers.fidelidad_controller import FidelidadController
from models.session_manager import get_current_user


def FidelidadView(page: ft.Page, go):
    controller = FidelidadController()
    usuario = get_current_user() or {}
    user_id = usuario.get("id")
    nombre = usuario.get("nombre", "Cliente")

    puntos_text = ft.Text("0", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    gasto_text = ft.Text("0.00 €", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    nivel_text = ft.Text("Bronce", size=28, weight=ft.FontWeight.BOLD, color="#8BE3FF")

    compra_input = ft.TextField(
        hint_text="Importe de la compra (€)",
        border_radius=18,
        border_color=ft.Colors.with_opacity(0.25, ft.Colors.CYAN_200),
        focused_border_color="#67E8F9",
        bgcolor=ft.Colors.with_opacity(0.04, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
        width=280,
    )

    referencia_input = ft.TextField(
        hint_text="Referencia / ticket (opcional)",
        border_radius=18,
        border_color=ft.Colors.with_opacity(0.25, ft.Colors.CYAN_200),
        focused_border_color="#67E8F9",
        bgcolor=ft.Colors.with_opacity(0.04, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
        width=300,
    )

    qr_image = ft.Image(width=240, height=240, fit=ft.BoxFit.CONTAIN)
    qr_label = ft.Text("", color="#8BE3FF", size=14, text_align=ft.TextAlign.CENTER)

    cupones_activos_column = ft.Column(spacing=14)
    ofertas_column = ft.Column(spacing=14)
    historial_column = ft.Column(spacing=12)

    def show_message(texto: str, ok: bool = True):
        page.snack_bar = ft.SnackBar(
            ft.Text(texto),
            bgcolor=ft.Colors.GREEN_600 if ok else ft.Colors.RED_600
        )
        page.snack_bar.open = True
        page.update()

    def generar_qr_base64(data: str):
        if qrcode is None:
            return None
        try:
            qr = qrcode.QRCode(version=1, box_size=8, border=2)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            buffer = io.BytesIO()
            img.save(buffer, format="PNG")
            return base64.b64encode(buffer.getvalue()).decode("utf-8")
        except Exception:
            return None

    def ruta_volver():
        return "/panel_usuario"

    def registrar_compra(e):
        ok, msg = controller.registrar_compra(
            user_id,
            compra_input.value,
            referencia_input.value
        )
        show_message(msg, ok)
        if ok:
            compra_input.value = ""
            referencia_input.value = ""
            refrescar_todo()

    def canjear_oferta(oferta_id: str):
        ok, msg = controller.canjear_oferta(user_id, oferta_id)
        show_message(msg, ok)
        if ok:
            refrescar_todo()

    def marcar_usado(coupon_id: int):
        ok, msg = controller.marcar_cupon_como_usado(user_id, coupon_id)
        show_message(msg, ok)
        if ok:
            refrescar_todo()

    def copiar_codigo(codigo: str):
        try:
            page.set_clipboard(codigo)
            show_message(f"Código copiado: {codigo}", True)
        except Exception:
            show_message(f"Código del cupón: {codigo}", True)

    def caja_resumen(titulo: str, valor_control: ft.Control):
        return ft.Container(
            expand=True,
            padding=22,
            border_radius=22,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.08, ft.Colors.WHITE)),
            content=ft.Column(
                [
                    ft.Text(titulo, size=14, color=ft.Colors.WHITE60),
                    valor_control,
                ],
                spacing=10,
            ),
        )

    def tarjeta_cupon(cupon: dict):
        codigo = cupon.get("coupon_code", "SIN-CODIGO")
        titulo = cupon.get("title", "Cupón")
        descripcion = cupon.get("description", "")
        expires_at = cupon.get("expires_at")
        return ft.Container(
            padding=18,
            border_radius=20,
            bgcolor=ft.Colors.with_opacity(0.07, ft.Colors.CYAN_100),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.CYAN_200)),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text(titulo, size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    ft.Text(descripcion, size=13, color=ft.Colors.WHITE70),
                                ],
                                spacing=6,
                                expand=True
                            ),
                            ft.Container(
                                padding=ft.Padding(12, 6, 12, 6),
                                border_radius=999,
                                bgcolor=ft.Colors.with_opacity(0.16, ft.Colors.GREEN_300),
                                content=ft.Text("Activo", color="#CFFFE5", size=12, weight=ft.FontWeight.BOLD),
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Container(height=4),
                    ft.Text(f"Código: {codigo}", size=15, weight=ft.FontWeight.BOLD, color="#8BE3FF"),
                    ft.Text(
                        "Muéstralo o escanéalo en caja para aplicarlo en la compra.",
                        size=13,
                        color=ft.Colors.WHITE70
                    ),
                    ft.Text(
                        f"Válido hasta: {expires_at}" if expires_at else "Validez disponible en sistema",
                        size=12,
                        color=ft.Colors.WHITE54
                    ),
                    ft.Row(
                        [
                            ft.OutlinedButton(
                                "Copiar código",
                                icon=ft.Icons.CONTENT_COPY_ROUNDED,
                                on_click=lambda e, c=codigo: copiar_codigo(c),
                                style=ft.ButtonStyle(
                                    color=ft.Colors.WHITE,
                                    side=ft.BorderSide(1, ft.Colors.with_opacity(0.22, ft.Colors.WHITE)),
                                    shape=ft.RoundedRectangleBorder(radius=14),
                                ),
                            ),
                            ft.Button(
                                "Marcar como usado",
                                icon=ft.Icons.CHECK_CIRCLE_ROUNDED,
                                on_click=lambda e, cid=cupon["id"]: marcar_usado(cid),
                                bgcolor="#67E8F9",
                                color=ft.Colors.BLACK,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=14),
                                ),
                            ),
                        ],
                        spacing=12
                    )
                ],
                spacing=10,
            ),
        )

    def tarjeta_oferta(oferta: dict):
        disponible = oferta.get("can_redeem", False)
        return ft.Container(
            padding=22,
            border_radius=22,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.08, ft.Colors.WHITE)),
            content=ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(oferta["title"], size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Text(oferta["description"], size=13, color=ft.Colors.WHITE70),
                            ft.Text(
                                f"{oferta['badge']} · {oferta['points_cost']} puntos",
                                size=13,
                                weight=ft.FontWeight.BOLD,
                                color="#8BE3FF",
                            ),
                        ],
                        spacing=8,
                        expand=True,
                    ),
                    ft.Button(
                        "Canjear",
                        icon=ft.Icons.REDEEM_ROUNDED,
                        on_click=lambda e, oid=oferta["id"]: canjear_oferta(oid),
                        disabled=not disponible,
                        bgcolor="#67E8F9" if disponible else ft.Colors.GREY_700,
                        color=ft.Colors.BLACK if disponible else ft.Colors.WHITE60,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=16),
                        ),
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def tarjeta_historial(item: dict):
        tipo = item.get("transaction_type", "")
        icono = ft.Icons.SHOPPING_BAG_ROUNDED
        color = "#8BE3FF"
        etiqueta = "Compra"

        if tipo == "redeem":
            icono = ft.Icons.REDEEM_ROUNDED
            color = "#FFD166"
            etiqueta = "Canje"
        elif tipo == "adjustment":
            icono = ft.Icons.TUNE_ROUNDED
            color = "#FF8A8A"
            etiqueta = "Ajuste"

        points_delta = item.get("points_delta", 0)
        signo = "+" if points_delta > 0 else ""

        return ft.Container(
            padding=16,
            border_radius=18,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.06, ft.Colors.WHITE)),
            content=ft.Row(
                [
                    ft.Container(
                        width=46,
                        height=46,
                        border_radius=14,
                        bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.CYAN_100),
                        alignment=ft.Alignment.CENTER,
                        content=ft.Icon(icono, color=color, size=24),
                    ),
                    ft.Column(
                        [
                            ft.Text(etiqueta, size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                            ft.Text(item.get("description") or "-", size=13, color=ft.Colors.WHITE70),
                            ft.Text(
                                f"Referencia: {item.get('reference_code') or '—'} · Fecha: {item.get('created_at')}",
                                size=12,
                                color=ft.Colors.WHITE54,
                            ),
                        ],
                        spacing=5,
                        expand=True,
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                f"{signo}{points_delta} pts",
                                size=16,
                                weight=ft.FontWeight.BOLD,
                                color="#8BE3FF" if points_delta >= 0 else "#FFD166",
                                text_align=ft.TextAlign.RIGHT,
                            ),
                            ft.Text(
                                f"{float(item.get('purchase_amount') or 0):.2f} €",
                                size=12,
                                color=ft.Colors.WHITE60,
                                text_align=ft.TextAlign.RIGHT,
                            ),
                        ],
                        spacing=5,
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                    )
                ],
                spacing=14,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def refrescar_todo():
        resumen = controller.obtener_resumen(user_id)

        puntos_text.value = str(resumen.get("loyalty_points", 0))
        gasto_text.value = f"{float(resumen.get('total_spent', 0) or 0):.2f} €"
        nivel_text.value = resumen.get("nivel", "Bronce")

        payload_qr = json.dumps({
            "type": "tannhauser_loyalty",
            "user_id": user_id,
            "name": nombre,
        })
        qr_b64 = generar_qr_base64(payload_qr)
        if qr_b64:
            qr_image.src_base64 = qr_b64
        qr_label.value = f"ID cliente: {user_id}"

        cupones_activos = controller.obtener_cupones_activos(user_id)
        cupones_activos_column.controls.clear()
        if cupones_activos:
            for cupon in cupones_activos:
                cupones_activos_column.controls.append(tarjeta_cupon(cupon))
        else:
            cupones_activos_column.controls.append(
                ft.Container(
                    padding=18,
                    border_radius=18,
                    bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                    content=ft.Text(
                        "Todavía no tienes cupones activos. Cuando canjees una recompensa aparecerá aquí para usarla en caja.",
                        color=ft.Colors.WHITE70,
                        size=14,
                    ),
                )
            )

        ofertas_column.controls.clear()
        for oferta in controller.obtener_ofertas(user_id):
            ofertas_column.controls.append(tarjeta_oferta(oferta))

        historial_column.controls.clear()
        historial = controller.obtener_historial(user_id)
        if historial:
            for item in historial:
                historial_column.controls.append(tarjeta_historial(item))
        else:
            historial_column.controls.append(
                ft.Text("No hay movimientos todavía.", color=ft.Colors.WHITE70, size=14)
            )

        page.update()

    vista = ft.View(
        route="/fidelidad",
        padding=0,
        spacing=0,
        controls=[
            ft.Container(
                expand=True,
                padding=28,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                    colors=["#050A12", "#09172A", "#0B2342", "#0E2F55"],
                ),
                content=ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Text(
                                            "Fidelidad y recompensas",
                                            size=38,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE,
                                        ),
                                        ft.Text(
                                            "Escanea tu QR, registra compras, acumula puntos y utiliza tus cupones activos en caja.",
                                            size=16,
                                            color=ft.Colors.WHITE70,
                                        ),
                                    ],
                                    spacing=6,
                                    expand=True,
                                ),
                                ft.OutlinedButton(
                                    "Volver al panel",
                                    icon=ft.Icons.ARROW_BACK_ROUNDED,
                                    on_click=lambda e: go(ruta_volver()),
                                    style=ft.ButtonStyle(
                                        color=ft.Colors.WHITE,
                                        side=ft.BorderSide(1, ft.Colors.with_opacity(0.22, ft.Colors.WHITE)),
                                        shape=ft.RoundedRectangleBorder(radius=18),
                                    ),
                                )
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        ft.Container(height=10),
                        ft.Row(
                            [
                                ft.Container(
                                    width=330,
                                    padding=22,
                                    border_radius=28,
                                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                                    border=ft.Border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                                    content=ft.Column(
                                        [
                                            ft.Text("QR de cliente", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                            ft.Container(height=6),
                                            ft.Container(
                                                padding=10,
                                                border_radius=18,
                                                bgcolor=ft.Colors.WHITE,
                                                content=qr_image,
                                            ),
                                            qr_label,
                                            ft.Text(
                                                "Enséñalo en caja para identificar tu cuenta y registrar la compra.",
                                                size=13,
                                                color=ft.Colors.WHITE70,
                                                text_align=ft.TextAlign.CENTER,
                                            ),
                                        ],
                                        spacing=12,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                ),
                                ft.Container(
                                    expand=True,
                                    padding=22,
                                    border_radius=28,
                                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                                    border=ft.Border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                                    content=ft.Column(
                                        [
                                            ft.Row(
                                                [
                                                    caja_resumen("Puntos", puntos_text),
                                                    caja_resumen("Gasto acumulado", gasto_text),
                                                    caja_resumen("Nivel", nivel_text),
                                                ],
                                                spacing=16,
                                            ),
                                            ft.Divider(color=ft.Colors.with_opacity(0.10, ft.Colors.WHITE), height=34),
                                            ft.Text("Registrar compra", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                            ft.Text(
                                                "Tras escanear el QR en caja, introduce el importe final de la compra para sumar puntos automáticamente.",
                                                size=14,
                                                color=ft.Colors.WHITE70,
                                            ),
                                            ft.Row(
                                                [
                                                    compra_input,
                                                    referencia_input,
                                                    ft.Button(
                                                        "Sumar puntos",
                                                        icon=ft.Icons.QR_CODE_SCANNER_ROUNDED,
                                                        on_click=registrar_compra,
                                                        bgcolor="#67E8F9",
                                                        color=ft.Colors.BLACK,
                                                        style=ft.ButtonStyle(
                                                            shape=ft.RoundedRectangleBorder(radius=18),
                                                            padding=ft.Padding(24, 18, 24, 18),
                                                        ),
                                                    )
                                                ],
                                                spacing=14,
                                                wrap=True,
                                            )
                                        ],
                                        spacing=14,
                                    ),
                                )
                            ],
                            spacing=22,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                        ),
                        ft.Container(height=22),
                        ft.Container(
                            padding=24,
                            border_radius=28,
                            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                            border=ft.Border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                            content=ft.Column(
                                [
                                    ft.Text("Cupones activos", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    ft.Text(
                                        "Aquí aparecen las recompensas activas listas para utilizar en caja.",
                                        size=14,
                                        color=ft.Colors.WHITE70,
                                    ),
                                    cupones_activos_column
                                ],
                                spacing=14,
                            ),
                        ),
                        ft.Container(height=22),
                        ft.Container(
                            padding=24,
                            border_radius=28,
                            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                            border=ft.Border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                            content=ft.Column(
                                [
                                    ft.Text("Ofertas y descuentos", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    ft.Text(
                                        "Canjea tus puntos por recompensas disponibles para tu cuenta.",
                                        size=14,
                                        color=ft.Colors.WHITE70,
                                    ),
                                    ofertas_column,
                                ],
                                spacing=14,
                            ),
                        ),
                        ft.Container(height=22),
                        ft.Container(
                            padding=24,
                            border_radius=28,
                            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                            border=ft.Border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                            content=ft.Column(
                                [
                                    ft.Text("Historial de fidelidad", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                                    historial_column,
                                ],
                                spacing=14,
                            ),
                        ),
                    ],
                    spacing=0,
                    scroll=ft.ScrollMode.AUTO,
                ),
            )
        ]
    )

    if user_id:
        refrescar_todo()

    return vista