import io
import json
import base64
import flet as ft

try:
    import qrcode
except Exception:
    qrcode = None

from models.session_manager import get_current_user, set_current_user
from controllers.fidelidad_controller import FidelidadController
from models.user_manager import UserManager


def PanelUsuarioView(page: ft.Page, go):
    usuario = get_current_user() or {}
    loyalty = FidelidadController()
    user_manager = UserManager()

    user_id = usuario.get("id")
    nombre = usuario.get("nombre", "Cliente")
    email = usuario.get("email", "cliente@tannhauser.com")
    rol = usuario.get("rol", "cliente")

    usuario_actualizado = None
    try:
        if email:
            usuario_actualizado = user_manager.obtener_por_email(email)
    except Exception as e:
        print(f"Error actualizando datos de usuario en panel_user: {e}")

    if usuario_actualizado:
        nombre = usuario_actualizado.get("nombre", nombre)
        email = usuario_actualizado.get("email", email)
        rol = usuario_actualizado.get("rol", rol)

    foto_perfil = (
        (usuario_actualizado.get("profile_image") if usuario_actualizado else None)
        or usuario.get("profile_image")
        or usuario.get("foto_perfil")
        or usuario.get("foto")
        or usuario.get("avatar")
        or None
    )

    resumen = loyalty.obtener_resumen(user_id) if user_id else {
        "loyalty_points": 0,
        "total_spent": 0.0,
        "nivel": "Bronce"
    }

    ofertas = loyalty.obtener_ofertas(user_id) if user_id else []
    cupones_activos = loyalty.obtener_cupones_activos(user_id) if user_id else []

    puntos = int(resumen.get("loyalty_points", 0) or 0)
    gasto_total = float(resumen.get("total_spent", 0) or 0)
    nivel = resumen.get("nivel", "Bronce")

    def cerrar_sesion(e):
        set_current_user(None)
        go("/")

    def avatar_usuario(radius=34):
        size = radius * 2
        if foto_perfil:
            return ft.Container(
                width=size,
                height=size,
                border_radius=radius,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=ft.Image(
                    src=foto_perfil,
                    fit=ft.BoxFit.COVER,
                ),
            )

        return ft.CircleAvatar(
            radius=radius,
            bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.CYAN_300),
            content=ft.Icon(
                ft.Icons.PERSON_ROUNDED,
                size=max(26, int(radius * 0.95)),
                color="#9CEBFF",
            ),
        )

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

    payload_qr = json.dumps({
        "type": "tannhauser_loyalty",
        "user_id": user_id,
        "name": nombre,
        "email": email,
    })
    qr_b64 = generar_qr_base64(payload_qr)

    def stat_card(icono, titulo, valor, subtitulo, color_icono="#9CEBFF"):
        return ft.Container(
            col={"xs": 12, "sm": 6, "md": 4},
            padding=20,
            border_radius=24,
            bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                width=46,
                                height=46,
                                border_radius=14,
                                bgcolor=ft.Colors.with_opacity(0.14, ft.Colors.CYAN_300),
                                alignment=ft.Alignment.CENTER,
                                content=ft.Icon(icono, color=color_icono, size=24),
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        titulo,
                                        size=14,
                                        color=ft.Colors.WHITE60,
                                    ),
                                    ft.Text(
                                        str(valor),
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE,
                                    ),
                                ],
                                spacing=2,
                            ),
                        ],
                        spacing=12,
                    ),
                    ft.Text(
                        subtitulo,
                        size=13,
                        color=ft.Colors.WHITE70,
                    ),
                ],
                spacing=12,
            ),
        )

    def action_card(icono, titulo, texto, boton_texto, ruta, color_icono="#9CEBFF"):
        return ft.Container(
            col={"xs": 12, "sm": 6, "md": 4},
            padding=24,
            border_radius=26,
            bgcolor=ft.Colors.with_opacity(0.11, ft.Colors.BLACK),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=16,
                color=ft.Colors.with_opacity(0.10, ft.Colors.BLACK),
                offset=ft.Offset(0, 8),
            ),
            content=ft.Column(
                [
                    ft.Container(
                        width=58,
                        height=58,
                        border_radius=18,
                        bgcolor=ft.Colors.with_opacity(0.14, ft.Colors.CYAN_300),
                        alignment=ft.Alignment.CENTER,
                        content=ft.Icon(icono, size=30, color=color_icono),
                    ),
                    ft.Text(
                        titulo,
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        texto,
                        size=14,
                        color=ft.Colors.WHITE70,
                    ),
                    ft.Container(height=4),
                    ft.Button(
                        boton_texto,
                        icon=ft.Icons.ARROW_FORWARD_ROUNDED,
                        bgcolor="#64D7FF",
                        color=ft.Colors.BLACK,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=16),
                        ),
                        on_click=lambda e: go(ruta),
                    ),
                ],
                spacing=14,
            ),
        )

    def offer_card(oferta: dict):
        disponible = oferta.get("can_redeem", False)
        return ft.Container(
            col={"xs": 12, "sm": 6, "md": 4},
            padding=20,
            border_radius=24,
            bgcolor=ft.Colors.with_opacity(0.09, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
            content=ft.Column(
                [
                    ft.Container(
                        padding=ft.Padding(12, 6, 12, 6),
                        border_radius=999,
                        bgcolor=ft.Colors.with_opacity(0.14, ft.Colors.CYAN_300),
                        content=ft.Text(
                            oferta.get("badge", "OFERTA"),
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            color="#64D7FF",
                        ),
                    ),
                    ft.Text(
                        oferta.get("title", "Oferta"),
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        oferta.get("description", ""),
                        size=14,
                        color=ft.Colors.WHITE70,
                    ),
                    ft.Container(height=4),
                    ft.Text(
                        f"Disponible con {oferta.get('points_cost', 0)} puntos",
                        size=13,
                        color="#9CEBFF",
                        weight=ft.FontWeight.W_600,
                    ),
                    ft.Container(
                        padding=ft.Padding(10, 8, 10, 8),
                        border_radius=14,
                        bgcolor=ft.Colors.with_opacity(
                            0.10,
                            ft.Colors.GREEN_300 if disponible else ft.Colors.AMBER_300
                        ),
                        content=ft.Text(
                            "Canjeable ahora" if disponible else "Te faltan puntos",
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.WHITE,
                        ),
                    )
                ],
                spacing=10,
            ),
        )

    def coupon_card(cupon: dict):
        codigo = cupon.get("coupon_code", "SIN-CODIGO")
        titulo = cupon.get("title", "Cupón activo")
        descripcion = cupon.get("description", "")
        expires_at = cupon.get("expires_at")

        return ft.Container(
            col={"xs": 12, "sm": 6},
            padding=20,
            border_radius=24,
            bgcolor=ft.Colors.with_opacity(0.09, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.CYAN_200)),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                width=48,
                                height=48,
                                border_radius=14,
                                bgcolor=ft.Colors.with_opacity(0.14, ft.Colors.GREEN_300),
                                alignment=ft.Alignment.CENTER,
                                content=ft.Icon(
                                    ft.Icons.CONFIRMATION_NUMBER_ROUNDED,
                                    color="#B8FFE1",
                                    size=24,
                                ),
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        titulo,
                                        size=18,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                        "Cupón activo listo para usar en caja",
                                        size=12,
                                        color=ft.Colors.WHITE60,
                                    ),
                                ],
                                spacing=3,
                                expand=True,
                            ),
                            ft.Container(
                                padding=ft.Padding(10, 6, 10, 6),
                                border_radius=999,
                                bgcolor=ft.Colors.with_opacity(0.16, ft.Colors.GREEN_300),
                                content=ft.Text(
                                    "Activo",
                                    color="#CFFFE5",
                                    size=12,
                                    weight=ft.FontWeight.BOLD,
                                ),
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Text(
                        descripcion or "Cupón de fidelidad generado correctamente.",
                        size=13,
                        color=ft.Colors.WHITE70,
                    ),
                    ft.Container(
                        padding=ft.Padding(12, 10, 12, 10),
                        border_radius=16,
                        bgcolor=ft.Colors.with_opacity(0.07, ft.Colors.BLACK),
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Código de cupón",
                                    size=12,
                                    color=ft.Colors.WHITE54,
                                ),
                                ft.Text(
                                    codigo,
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color="#8BE3FF",
                                    selectable=True,
                                ),
                            ],
                            spacing=4,
                        )
                    ),
                    ft.Text(
                        f"Validez: {expires_at}" if expires_at else "Validez disponible en sistema",
                        size=12,
                        color=ft.Colors.WHITE54,
                    ),
                    ft.Text(
                        "Enséñalo o escanéalo en caja para aplicarlo en la compra.",
                        size=12,
                        color=ft.Colors.WHITE70,
                    ),
                ],
                spacing=12,
            ),
        )

    header = ft.Container(
        width=1180,
        padding=ft.Padding(28, 22, 28, 22),
        border_radius=28,
        bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
        content=ft.Row(
            [
                ft.Row(
                    [
                        ft.Container(
                            width=72,
                            height=72,
                            border_radius=22,
                            bgcolor=ft.Colors.with_opacity(0.94, ft.Colors.WHITE),
                            padding=10,
                            content=ft.Image(
                                src="assets/logo_tannhauser.png",
                                fit=ft.BoxFit.CONTAIN,
                            ),
                        ),
                        ft.Column(
                            [
                                ft.Text(
                                    "Área de cliente",
                                    size=30,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                                ft.Text(
                                    f"Bienvenido, {nombre}",
                                    size=15,
                                    color=ft.Colors.WHITE70,
                                ),
                            ],
                            spacing=4,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ],
                    spacing=18,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.OutlinedButton(
                            "Mi perfil",
                            icon=ft.Icons.PERSON_ROUNDED,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                side=ft.BorderSide(
                                    1.1,
                                    ft.Colors.with_opacity(0.28, ft.Colors.WHITE),
                                ),
                                shape=ft.RoundedRectangleBorder(radius=16),
                            ),
                            on_click=lambda e: go("/perfil"),
                        ),
                        ft.OutlinedButton(
                            "Volver al inicio",
                            icon=ft.Icons.HOME_ROUNDED,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                side=ft.BorderSide(
                                    1.1,
                                    ft.Colors.with_opacity(0.28, ft.Colors.WHITE),
                                ),
                                shape=ft.RoundedRectangleBorder(radius=16),
                            ),
                            on_click=lambda e: go("/"),
                        ),
                        ft.Button(
                            "Cerrar sesión",
                            icon=ft.Icons.LOGOUT_ROUNDED,
                            bgcolor="#64D7FF",
                            color=ft.Colors.BLACK,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=16),
                            ),
                            on_click=cerrar_sesion,
                        ),
                    ],
                    spacing=12,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    hero = ft.Container(
        width=1180,
        padding=28,
        border_radius=28,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
        content=ft.Row(
            [
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        [
                            ft.Text(
                                "Tu experiencia inteligente de compra",
                                size=40,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                "Consulta inventario, accede a tu perfil, utiliza tu QR de fidelización, revisa cupones activos y aprovecha descuentos exclusivos desde una única experiencia unificada.",
                                size=16,
                                color=ft.Colors.WHITE70,
                                width=720,
                            ),
                            ft.Row(
                                [
                                    ft.Button(
                                        "Ver inventario",
                                        icon=ft.Icons.INVENTORY_2_ROUNDED,
                                        bgcolor="#64D7FF",
                                        color=ft.Colors.BLACK,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=16),
                                        ),
                                        on_click=lambda e: go("/inventario"),
                                    ),
                                    ft.OutlinedButton(
                                        "Abrir fidelidad",
                                        icon=ft.Icons.QR_CODE_2_ROUNDED,
                                        style=ft.ButtonStyle(
                                            color=ft.Colors.WHITE,
                                            side=ft.BorderSide(
                                                1.1,
                                                ft.Colors.with_opacity(0.28, ft.Colors.WHITE),
                                            ),
                                            shape=ft.RoundedRectangleBorder(radius=16),
                                        ),
                                        on_click=lambda e: go("/fidelidad"),
                                    ),
                                ],
                                spacing=12,
                            ),
                        ],
                        spacing=14,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                ),
                ft.Container(
                    width=330,
                    padding=22,
                    border_radius=24,
                    bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.BLACK),
                    border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    avatar_usuario(),
                                    ft.Column(
                                        [
                                            ft.Text(
                                                nombre,
                                                size=20,
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.WHITE,
                                            ),
                                            ft.Text(
                                                email,
                                                size=13,
                                                color=ft.Colors.WHITE70,
                                            ),
                                            ft.Text(
                                                f"Rol: {rol}",
                                                size=12,
                                                color="#9CEBFF",
                                            ),
                                        ],
                                        spacing=3,
                                    ),
                                ],
                                spacing=12,
                            ),
                            ft.Divider(color=ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                            ft.Text("Nivel de fidelidad", size=14, color=ft.Colors.WHITE60),
                            ft.Text(
                                nivel,
                                size=26,
                                weight=ft.FontWeight.BOLD,
                                color="#9CEBFF",
                            ),
                            ft.Text(
                                "Accede a promociones, recompensas y cupones personalizados desde tu cuenta.",
                                size=13,
                                color=ft.Colors.WHITE70,
                            ),
                        ],
                        spacing=10,
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    stats = ft.ResponsiveRow(
        [
            stat_card(
                ft.Icons.STARS_ROUNDED,
                "Puntos acumulados",
                puntos,
                "Tus puntos actuales disponibles dentro del programa de fidelización.",
            ),
            stat_card(
                ft.Icons.PAYMENTS_ROUNDED,
                "Gasto acumulado",
                f"{gasto_total:.2f} €",
                "Importe total registrado en tu historial de compras.",
            ),
            stat_card(
                ft.Icons.CONFIRMATION_NUMBER_ROUNDED,
                "Cupones activos",
                len(cupones_activos),
                "Recompensas disponibles para utilizar ahora mismo en caja.",
            ),
        ],
        spacing=18,
        run_spacing=18,
    )

    acciones = ft.ResponsiveRow(
        [
            action_card(
                ft.Icons.INVENTORY_2_ROUNDED,
                "Inventario",
                "Consulta el catálogo del supermercado con el diseño actualizado y disponibilidad real.",
                "Abrir inventario",
                "/inventario",
            ),
            action_card(
                ft.Icons.PERSON_ROUNDED,
                "Mi perfil",
                "Actualiza tus datos, cambia tu contraseña y modifica tu foto de perfil.",
                "Ir a mi perfil",
                "/perfil",
            ),
            action_card(
                ft.Icons.QR_CODE_2_ROUNDED,
                "Fidelidad",
                "Gestiona tu QR, registra compras, revisa tu historial y canjea recompensas.",
                "Abrir fidelidad",
                "/fidelidad",
            ),
        ],
        spacing=18,
        run_spacing=18,
    )

    fidelidad_section = ft.Container(
        width=1180,
        padding=24,
        border_radius=28,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
        content=ft.Row(
            [
                ft.Container(
                    width=290,
                    padding=18,
                    border_radius=22,
                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.BLACK),
                    border=ft.Border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                    content=ft.Column(
                        [
                            ft.Text(
                                "QR de fidelidad",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.Container(
                                padding=12,
                                border_radius=20,
                                bgcolor=ft.Colors.WHITE,
                                content=ft.Image(
                                    src_base64=qr_b64 if qr_b64 else None,
                                    width=210,
                                    height=210,
                                    fit=ft.BoxFit.CONTAIN,
                                ) if qr_b64 else ft.Icon(
                                    ft.Icons.QR_CODE_2_ROUNDED,
                                    size=90,
                                    color=ft.Colors.BLACK,
                                ),
                            ),
                            ft.Text(
                                f"ID cliente: {user_id}",
                                size=13,
                                color="#9CEBFF",
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                        spacing=12,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                ),
                ft.Container(
                    expand=True,
                    content=ft.Column(
                        [
                            ft.Text(
                                "Centro de fidelización",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                            ft.Text(
                                "Accede a tu QR personal, registra compras para sumar puntos, revisa movimientos y gestiona recompensas activas con una experiencia totalmente integrada.",
                                size=15,
                                color=ft.Colors.WHITE70,
                            ),
                            ft.Row(
                                [
                                    ft.Button(
                                        "Abrir fidelidad",
                                        icon=ft.Icons.QR_CODE_SCANNER_ROUNDED,
                                        bgcolor="#64D7FF",
                                        color=ft.Colors.BLACK,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=16),
                                        ),
                                        on_click=lambda e: go("/fidelidad"),
                                    ),
                                    ft.OutlinedButton(
                                        "Ver cupones activos",
                                        icon=ft.Icons.CONFIRMATION_NUMBER_ROUNDED,
                                        style=ft.ButtonStyle(
                                            color=ft.Colors.WHITE,
                                            side=ft.BorderSide(
                                                1.1,
                                                ft.Colors.with_opacity(0.28, ft.Colors.WHITE),
                                            ),
                                            shape=ft.RoundedRectangleBorder(radius=16),
                                        ),
                                        on_click=lambda e: go("/fidelidad"),
                                    ),
                                ],
                                spacing=12,
                            ),
                        ],
                        spacing=14,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                    ),
                ),
            ],
            spacing=22,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    cupones_section = ft.Container(
        width=1180,
        padding=24,
        border_radius=28,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
        content=ft.Column(
            [
                ft.Text(
                    "Cupones activos",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                ft.Text(
                    "Tus recompensas activas aparecen aquí listas para enseñarlas o escanearlas en caja.",
                    size=15,
                    color=ft.Colors.WHITE70,
                ),
                ft.ResponsiveRow(
                    [coupon_card(c) for c in cupones_activos] if cupones_activos else [
                        ft.Container(
                            col={"xs": 12},
                            padding=20,
                            border_radius=20,
                            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                            content=ft.Text(
                                "Todavía no tienes cupones activos. Cuando canjees una oferta, aparecerá aquí automáticamente.",
                                color=ft.Colors.WHITE70,
                                size=14,
                            ),
                        )
                    ],
                    spacing=18,
                    run_spacing=18,
                ),
            ],
            spacing=16,
        ),
    )

    ofertas_section = ft.Container(
        width=1180,
        padding=24,
        border_radius=28,
        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
        border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
        content=ft.Column(
            [
                ft.Text(
                    "Descuentos y ofertas disponibles",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                ft.Text(
                    "Estas recompensas están disponibles dentro del sistema de fidelización y se pueden canjear desde tu centro de fidelidad.",
                    size=15,
                    color=ft.Colors.WHITE70,
                ),
                ft.ResponsiveRow(
                    [offer_card(oferta) for oferta in ofertas] if ofertas else [
                        ft.Container(
                            col={"xs": 12},
                            padding=20,
                            border_radius=20,
                            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                            content=ft.Text(
                                "No hay ofertas activas disponibles en este momento.",
                                color=ft.Colors.WHITE70,
                                size=14,
                            ),
                        )
                    ],
                    spacing=18,
                    run_spacing=18,
                ),
            ],
            spacing=16,
        ),
    )

    contenido = ft.Container(
        expand=True,
        padding=30,
        gradient=ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(1, 1),
            colors=[
                "#050A12",
                "#09172A",
                "#0B2342",
                "#0E2F55",
            ],
        ),
        content=ft.Column(
            [
                header,
                ft.Container(height=18),
                hero,
                ft.Container(height=22),
                stats,
                ft.Container(height=22),
                acciones,
                ft.Container(height=22),
                fidelidad_section,
                ft.Container(height=22),
                cupones_section,
                ft.Container(height=22),
                ofertas_section,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
            scroll=ft.ScrollMode.AUTO,
        ),
    )

    return ft.View(
        route="/panel_usuario",
        controls=[contenido],
        padding=0,
        spacing=0,
    )