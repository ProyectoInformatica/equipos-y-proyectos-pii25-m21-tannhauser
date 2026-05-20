import flet as ft
import asyncio
from views.login_unificado import LoginUnificadoView
from views.register import RegistroView
from views.panel_user import PanelUsuarioView
from views.panel_empleado import PanelEmpleadoView
from views.panel_admin import PanelAdminView
from views.panel_super import PanelSuperView
from views.sensores_aire import SensoresAireView
from views.sensores_luz import SensoresLuzView
from views.sensores_nevera import SensoresNeveraView
from views.sensores_puerta import SensoresPuertaView
from views.admin_usuarios import AdminUsuariosView
from views.admin_logs import AdminLogsView
from views.inventario import InventarioView
from views.estadisticas_sensores import EstadisticasSensoresView
from models.session_manager import get_current_user
from views.admin_eliminar_usuario import AdminEliminarUsuarioView
from views.comentarios import ComentariosView
from views.admin_mapa_sensores import AdminMapaSensoresView
from views.admin_camara import AdminCamaraView
from views.admin_alertas import AdminAlertasView
from views.admin_umbrales import AdminUmbralesView
from views.perfil import PerfilView
from views.fidelidad import FidelidadView
from controllers.alerta_controller import AlertaController
from views.empleado_sensores import EmpleadoSensoresView
from views.empleado_luces import EmpleadoLucesView
from views.empleado_fidelidad import EmpleadoFidelidadView
from file_manager import FileManager


def main(page: ft.Page):
    page.title = "Tannhauser"
    page.window_width = 1280
    page.window_height = 800
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#050A12"
    fm = FileManager()
    fm.inicializar_tabla_nuevo_sensor()
    alerta_controller = AlertaController()
    ultimo_evento_id = {"valor": 0}
    cola_alertas = []
    alerta_mostrando = {"valor": False}
    ruta_critica_actual = {"valor": "/"}

    def go(route: str):
        page.go(route)

    def texto_operador(op):
        if op == "gt":
            return ">"
        if op == "lt":
            return "<"
        return str(op)

    def formatear_valor(v):
        if v is None:
            return "Sin dato"
        try:
            vf = float(v)
            if vf.is_integer():
                return str(int(vf))
            return f"{vf:.2f}"
        except Exception:
            return str(v)

    def info_block(icono, titulo, valor_widget):
        return ft.Container(
            col={"xs": 12, "sm": 6},
            padding=16,
            border_radius=18,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.08, ft.Colors.WHITE)),
            content=ft.Row(
                [
                    ft.Container(
                        width=42,
                        height=42,
                        border_radius=14,
                        bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.RED_300),
                        alignment=ft.alignment.center,
                        content=ft.Icon(icono, size=20, color="#FFC1C1"),
                    ),
                    ft.Column(
                        [
                            ft.Text(
                                titulo,
                                size=11,
                                color=ft.Colors.WHITE54,
                                weight=ft.FontWeight.W_500,
                            ),
                            valor_widget,
                        ],
                        spacing=4,
                        expand=True,
                    ),
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    critical_eyebrow = ft.Text(
        "ALERTA CRÍTICA",
        size=11,
        weight=ft.FontWeight.BOLD,
        color="#FF8A8A",
        text_align=ft.TextAlign.CENTER,
    )

    critical_title = ft.Text(
        "Incidencia crítica detectada",
        size=27,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.WHITE,
        text_align=ft.TextAlign.CENTER,
    )

    critical_desc = ft.Text(
        "",
        size=14,
        color=ft.Colors.WHITE70,
        text_align=ft.TextAlign.CENTER,
        max_lines=3,
    )

    critical_sensor_value = ft.Text(
        "—",
        size=14,
        weight=ft.FontWeight.W_600,
        color=ft.Colors.WHITE,
    )

    critical_time_value = ft.Text(
        "—",
        size=14,
        weight=ft.FontWeight.W_600,
        color=ft.Colors.WHITE,
    )

    critical_value_detected = ft.Text(
        "—",
        size=14,
        weight=ft.FontWeight.W_600,
        color=ft.Colors.WHITE,
    )

    critical_rule_value = ft.Text(
        "—",
        size=14,
        weight=ft.FontWeight.W_600,
        color=ft.Colors.WHITE,
    )

    premium_alert_badge = ft.Container(
        width=78,
        height=78,
        border_radius=24,
        bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.RED_300),
        border=ft.border.all(1.2, ft.Colors.with_opacity(0.20, ft.Colors.RED_100)),
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=18,
            color=ft.Colors.with_opacity(0.18, ft.Colors.RED_300),
            offset=ft.Offset(0, 6),
        ),
        content=ft.Icon(
            ft.Icons.WARNING_AMBER_ROUNDED,
            size=40,
            color="#FFE0E0",
        ),
    )

    critical_card = ft.Container(
        width=540,
        border_radius=30,
        bgcolor="#0B1220",
        border=ft.border.all(1.2, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
        shadow=ft.BoxShadow(
            spread_radius=0,
            blur_radius=42,
            color=ft.Colors.with_opacity(0.42, ft.Colors.BLACK),
            offset=ft.Offset(0, 18),
        ),
        animate_opacity=250,
        animate_scale=250,
        scale=1,
        opacity=1,
        content=ft.Column(
            [
                ft.Container(
                    height=5,
                    border_radius=ft.border_radius.only(
                        top_left=30,
                        top_right=30,
                    ),
                    gradient=ft.LinearGradient(
                        begin=ft.Alignment(-1, 0),
                        end=ft.Alignment(1, 0),
                        colors=["#FF7B7B", "#EF4444", "#B91C1C"],
                    ),
                ),
                ft.Container(
                    padding=28,
                    content=ft.Column(
                        [
                            premium_alert_badge,
                            critical_eyebrow,
                            critical_title,
                            critical_desc,
                            ft.Container(
                                padding=ft.Padding(14, 10, 14, 10),
                                border_radius=999,
                                bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                                content=ft.Text(
                                    "Esta alerta requiere intervención inmediata.",
                                    size=12,
                                    color=ft.Colors.WHITE54,
                                    italic=True,
                                    text_align=ft.TextAlign.CENTER,
                                ),
                            ),
                            ft.Container(height=2),
                            ft.ResponsiveRow(
                                [
                                    info_block(
                                        ft.Icons.SENSORS_ROUNDED,
                                        "Sensor afectado",
                                        critical_sensor_value,
                                    ),
                                    info_block(
                                        ft.Icons.SCHEDULE_ROUNDED,
                                        "Momento detectado",
                                        critical_time_value,
                                    ),
                                    info_block(
                                        ft.Icons.SHOW_CHART_ROUNDED,
                                        "Valor detectado",
                                        critical_value_detected,
                                    ),
                                    info_block(
                                        ft.Icons.TUNE_ROUNDED,
                                        "Regla activada",
                                        critical_rule_value,
                                    ),
                                ],
                                spacing=12,
                                run_spacing=12,
                            ),
                            ft.Container(height=4),
                            ft.Row(
                                [
                                    ft.OutlinedButton(
                                        "Descartar",
                                        icon=ft.Icons.CLOSE_ROUNDED,
                                        height=48,
                                        style=ft.ButtonStyle(
                                            color=ft.Colors.WHITE,
                                            side=ft.BorderSide(
                                                1.1,
                                                ft.Colors.with_opacity(0.18, ft.Colors.WHITE),
                                            ),
                                            shape=ft.RoundedRectangleBorder(radius=16),
                                            padding=ft.Padding(20, 0, 20, 0),
                                        ),
                                        on_click=lambda e: cerrar_overlay_critico(),
                                    ),
                                    ft.ElevatedButton(
                                        "Ir al sensor",
                                        icon=ft.Icons.ARROW_FORWARD_ROUNDED,
                                        height=48,
                                        bgcolor="#67E8F9",
                                        color=ft.Colors.BLACK,
                                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=16),
                                            padding=ft.Padding(20, 0, 20, 0),
                                        ),
                                        on_click=lambda e: ir_al_sensor_critico(),
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=14,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=14,
                    ),
                ),
            ],
            spacing=0,
        ),
    )

    critical_overlay = ft.Container(
        visible=False,
        width=page.window_width,
        height=page.window_height,
        bgcolor=ft.Colors.with_opacity(0.68, ft.Colors.BLACK),
        alignment=ft.alignment.center,
        content=ft.Stack(
            controls=[
                ft.Container(
                    width=620,
                    height=620,
                    border_radius=310,
                    blur=120,
                    bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.RED_300),
                ),
                critical_card,
            ],
            alignment=ft.alignment.center,
        ),
    )

    page.overlay.clear()
    page.overlay.append(critical_overlay)

    def actualizar_tamano_overlay(e=None):
        critical_overlay.width = page.window_width
        critical_overlay.height = page.window_height
        page.update()

    page.on_resized = actualizar_tamano_overlay

    def cerrar_overlay_critico():
        critical_overlay.visible = False
        alerta_mostrando["valor"] = False
        page.update()
        mostrar_siguiente_alerta()

    def ir_al_sensor_critico():
        critical_overlay.visible = False
        alerta_mostrando["valor"] = False
        page.update()
        go(ruta_critica_actual["valor"])
        mostrar_siguiente_alerta()

    def mostrar_siguiente_alerta():
        if alerta_mostrando["valor"]:
            return
        if not cola_alertas:
            return

        evento = cola_alertas.pop(0)
        alerta_mostrando["valor"] = True

        usuario = get_current_user() or {}
        rol = usuario.get("rol", "superusuario")
        ruta_destino = alerta_controller.ruta_para_evento(evento, rol)

        severity = (evento.get("severity") or "info").lower()
        titulo = evento.get("title") or "Alerta"
        descripcion = evento.get("description") or "Se ha detectado una condición anómala."
        event_time = evento.get("event_time")
        payload = evento.get("payload_json", {}) or {}

        valor = payload.get("valor")
        umbral = payload.get("umbral")
        operador = payload.get("operador")
        sensor = payload.get("state_code") or evento.get("device_code") or "Sin dato"

        if severity == "critical":
            regla = "Sin detalle"
            if operador is not None and umbral is not None:
                regla = f"valor {texto_operador(operador)} {formatear_valor(umbral)}"

            critical_title.value = titulo
            critical_desc.value = descripcion
            critical_sensor_value.value = str(sensor)
            critical_time_value.value = str(event_time)
            critical_value_detected.value = formatear_valor(valor)
            critical_rule_value.value = regla

            ruta_critica_actual["valor"] = ruta_destino
            critical_overlay.visible = True
            page.update()
            return

        if severity == "warning":
            def cerrar_banner(e=None):
                if page.banner:
                    page.banner.open = False
                alerta_mostrando["valor"] = False
                page.update()
                mostrar_siguiente_alerta()

            def ir_sensor_banner(e=None):
                if page.banner:
                    page.banner.open = False
                alerta_mostrando["valor"] = False
                page.update()
                go(ruta_destino)
                mostrar_siguiente_alerta()

            page.banner = ft.Banner(
                bgcolor=ft.Colors.AMBER_100,
                leading=ft.Icon(
                    ft.Icons.WARNING_AMBER_ROUNDED,
                    color=ft.Colors.AMBER_800,
                ),
                content=ft.Column(
                    [
                        ft.Text(
                            f"ALERTA: {titulo}",
                            color=ft.Colors.BLACK,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(descripcion, color=ft.Colors.BLACK),
                    ],
                    spacing=4,
                ),
                actions=[
                    ft.TextButton("Cerrar", on_click=cerrar_banner),
                    ft.TextButton("Ir al sensor", on_click=ir_sensor_banner),
                ],
            )
            page.banner.open = True
            page.update()
            return

        def snack_ir_sensor(e=None):
            alerta_mostrando["valor"] = False
            page.update()
            go(ruta_destino)
            mostrar_siguiente_alerta()

        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"{titulo}: {descripcion}"),
            action="Ir al sensor",
            on_action=snack_ir_sensor,
            bgcolor=ft.Colors.BLUE_600,
            duration=4000,
        )
        page.snack_bar.open = True
        alerta_mostrando["valor"] = False
        page.update()

    async def bucle_alertas():
        while True:
            try:
                usuario = get_current_user()
                if usuario:
                    nuevos = alerta_controller.obtener_eventos_nuevos(ultimo_evento_id["valor"])
                    if nuevos:
                        for evento in nuevos:
                            ultimo_evento_id["valor"] = max(
                                ultimo_evento_id["valor"], evento["id"]
                            )
                            cola_alertas.append(evento)
                        mostrar_siguiente_alerta()
            except Exception as e:
                print(f"Error en bucle_alertas: {e}")

            await asyncio.sleep(2)

    def home_view():
        logo_block = ft.Container(
            width=86,
            height=86,
            border_radius=24,
            bgcolor=ft.Colors.with_opacity(0.94, ft.Colors.WHITE),
            padding=12,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=18,
                color=ft.Colors.with_opacity(0.16, ft.Colors.BLACK),
                offset=ft.Offset(0, 6),
            ),
            content=ft.Image(
                src="assets/logo_tannhauser.png",
                fit=ft.ImageFit.CONTAIN,
            ),
        )

        topbar = ft.Container(
            width=1180,
            padding=ft.Padding(26, 18, 26, 18),
            border_radius=28,
            bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=18,
                color=ft.Colors.with_opacity(0.10, ft.Colors.BLACK),
                offset=ft.Offset(0, 8),
            ),
            content=ft.Row(
                [
                    ft.Row(
                        [
                            logo_block,
                            ft.Text(
                                "Tannhauser",
                                size=30,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.WHITE,
                            ),
                        ],
                        spacing=18,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.TextButton(
                                "Valoraciones",
                                style=ft.ButtonStyle(color=ft.Colors.WHITE70),
                                on_click=lambda e: go("/comentarios"),
                            ),
                            ft.OutlinedButton(
                                "Crear cuenta",
                                icon=ft.Icons.PERSON_ADD_ALT_1_ROUNDED,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.WHITE,
                                    side=ft.BorderSide(
                                        1.1,
                                        ft.Colors.with_opacity(0.28, ft.Colors.WHITE),
                                    ),
                                    shape=ft.RoundedRectangleBorder(radius=18),
                                ),
                                on_click=lambda e: go("/registro"),
                            ),
                            ft.ElevatedButton(
                                "Iniciar sesión",
                                icon=ft.Icons.LOGIN_ROUNDED,
                                bgcolor="#64D7FF",
                                color=ft.Colors.BLACK,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=18),
                                ),
                                on_click=lambda e: go("/login"),
                            ),
                        ],
                        spacing=12,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

        hero_left = ft.Column(
            [
                ft.Container(
                    padding=ft.Padding(14, 8, 14, 8),
                    border_radius=20,
                    bgcolor=ft.Colors.with_opacity(0.14, ft.Colors.CYAN_300),
                    content=ft.Text(
                        "Supermercado inteligente",
                        color="#9CEBFF",
                        size=13,
                        weight=ft.FontWeight.W_600,
                    ),
                ),
                ft.Text(
                    "La nueva forma de gestionar un supermercado conectado.",
                    size=48,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                    width=650,
                ),
                ft.Text(
                    "Controla inventario, usuarios, sensores, actividad y operativa diaria desde una única plataforma visual, moderna y preparada para crecer.",
                    size=17,
                    color=ft.Colors.WHITE70,
                    width=640,
                ),
                ft.Container(height=6),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Entrar en la plataforma",
                            icon=ft.Icons.ARROW_FORWARD_ROUNDED,
                            height=54,
                            bgcolor="#64D7FF",
                            color=ft.Colors.BLACK,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=18),
                                padding=ft.Padding(24, 0, 24, 0),
                            ),
                            on_click=lambda e: go("/login"),
                        ),
                        ft.OutlinedButton(
                            "Ver valoraciones",
                            icon=ft.Icons.STAR_ROUNDED,
                            height=54,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                side=ft.BorderSide(
                                    1.1,
                                    ft.Colors.with_opacity(0.28, ft.Colors.WHITE),
                                ),
                                shape=ft.RoundedRectangleBorder(radius=18),
                                padding=ft.Padding(24, 0, 24, 0),
                            ),
                            on_click=lambda e: go("/comentarios"),
                        ),
                    ],
                    spacing=14,
                ),
                ft.Container(height=10),
                ft.Row(
                    [
                        _mini_stat("Usuarios", "Acceso por roles"),
                        _mini_stat("Inventario", "Control centralizado"),
                        _mini_stat("Sensores", "Lecturas en tiempo real"),
                    ],
                    spacing=12,
                    wrap=True,
                ),
            ],
            spacing=18,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        )

        right_scroll_content = ft.Column(
            [
                _metric_card("Usuarios", "Control por roles y accesos seguros."),
                _metric_card("Inventario", "Stock centralizado, editable y sincronizado."),
                _metric_card("Sensores", "Lecturas, estados e históricos almacenados en MySQL."),
                _metric_card("Actividad", "Registro completo de acciones del sistema."),
                _metric_card("Valoraciones", "Canal de opinión accesible desde la aplicación."),
                _metric_card("Escalabilidad", "Arquitectura preparada para nuevas integraciones y telemetría."),
            ],
            spacing=14,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

        hero_right = ft.Container(
            width=430,
            height=500,
            border_radius=34,
            padding=28,
            bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.BLACK),
            border=ft.border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=24,
                color=ft.Colors.with_opacity(0.14, ft.Colors.BLACK),
                offset=ft.Offset(0, 10),
            ),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                width=48,
                                height=48,
                                border_radius=16,
                                bgcolor=ft.Colors.with_opacity(0.16, ft.Colors.CYAN_300),
                                alignment=ft.alignment.center,
                                content=ft.Icon(
                                    ft.Icons.STACKED_LINE_CHART_ROUNDED,
                                    color="#9CEBFF",
                                    size=24,
                                ),
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        "Centro de control",
                                        size=24,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                        "Visión general de la plataforma",
                                        size=13,
                                        color=ft.Colors.WHITE60,
                                    ),
                                ],
                                spacing=2,
                            ),
                        ],
                        spacing=12,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Container(height=10),
                    ft.Text(
                        "Supervisa los bloques principales del sistema desde una experiencia unificada. Si hay más módulos, puedes desplazarte dentro de este panel.",
                        size=14,
                        color=ft.Colors.WHITE70,
                    ),
                    ft.Container(height=10),
                    ft.Container(expand=True, content=right_scroll_content),
                ],
                spacing=8,
                expand=True,
            ),
        )

        hero = ft.Container(
            width=1180,
            expand=True,
            padding=ft.Padding(6, 28, 6, 6),
            content=ft.Row(
                [
                    ft.Container(expand=True, content=hero_left),
                    hero_right,
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

        footer = ft.Text(
            "Tannhauser",
            size=14,
            color=ft.Colors.WHITE54,
            text_align=ft.TextAlign.CENTER,
        )

        contenido = ft.Container(
            expand=True,
            padding=30,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(-1, -1),
                end=ft.Alignment(1, 1),
                colors=["#050A12", "#09172A", "#0B2342", "#0E2F55"],
            ),
            content=ft.Column(
                [
                    topbar,
                    ft.Container(height=20),
                    hero,
                    ft.Container(height=18),
                    footer,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=0,
            ),
        )

        return ft.View(route="/", controls=[contenido], padding=0, spacing=0)

    def route_change(e):
        page.views.clear()
        r = page.route
        usuario = get_current_user()

        def _denegar_acceso():
            page.snack_bar = ft.SnackBar(
                ft.Text("Acceso restringido: no tienes permisos para ver esta página."),
                bgcolor=ft.Colors.RED_600,
            )
            page.snack_bar.open = True
            page.update()
            page.go("/")
            return

        if r.startswith("/sensores_"):
            if not usuario or usuario.get("rol") not in ["administrador", "superusuario", "empleado"]:
                _denegar_acceso()
                return

        if r in ["/empleado_sensores", "/empleado_luces", "/empleado_fidelidad"]:
            if not usuario or usuario.get("rol") not in ["empleado", "administrador", "superusuario"]:
                _denegar_acceso()
                return

        if r == "/admin_mapa_sensores":
            if not usuario or usuario.get("rol") not in ["administrador", "superusuario"]:
                _denegar_acceso()
                return

        if r.startswith("/admin_") or r == "/panel_admin":
            if not usuario or usuario.get("rol") not in ["administrador", "superusuario"]:
                _denegar_acceso()
                return

        if r == "/estadisticas_sensores":
            if not usuario or usuario.get("rol") not in ["administrador", "superusuario"]:
                _denegar_acceso()
                return

        if r == "/panel_super":
            if not usuario or usuario.get("rol") != "superusuario":
                _denegar_acceso()
                return

        if r == "/panel_empleado":
            if not usuario or usuario.get("rol") != "empleado":
                _denegar_acceso()
                return

        if r == "/panel_usuario":
            if not usuario or usuario.get("rol") != "cliente":
                _denegar_acceso()
                return

        if r == "/perfil":
            if not usuario or usuario.get("rol") != "cliente":
                _denegar_acceso()
                return

        if r == "/fidelidad":
            if not usuario or usuario.get("rol") != "cliente":
                _denegar_acceso()
                return

        if r == "/inventario_edit":
            if not usuario or usuario.get("rol") not in ["administrador", "superusuario", "empleado"]:
                _denegar_acceso()
                return

        if r == "/":
            page.views.append(home_view())
        elif r == "/login":
            page.views.append(LoginUnificadoView(page, go))
        elif r == "/registro":
            page.views.append(RegistroView(page, go))
        elif r == "/panel_usuario":
            page.views.append(PanelUsuarioView(page, go))
        elif r == "/perfil":
            page.views.append(PerfilView(page, go))
        elif r == "/fidelidad":
            page.views.append(FidelidadView(page, go))
        elif r == "/panel_admin":
            page.views.append(PanelAdminView(page, go))
        elif r == "/panel_empleado":
            page.views.append(PanelEmpleadoView(page, go))
        elif r == "/panel_super":
            page.views.append(PanelSuperView(page, go))
        elif r == "/sensores_aire":
            page.views.append(SensoresAireView(page, go))
        elif r == "/sensores_luz":
            page.views.append(SensoresLuzView(page, go))
        elif r == "/sensores_nevera":
            page.views.append(SensoresNeveraView(page, go))
        elif r == "/sensores_puerta":
            page.views.append(SensoresPuertaView(page, go))
        elif r == "/empleado_sensores":
            page.views.append(EmpleadoSensoresView(page, go))
        elif r == "/empleado_luces":
            page.views.append(EmpleadoLucesView(page, go))
        elif r == "/empleado_fidelidad":
            page.views.append(EmpleadoFidelidadView(page, go))
        elif r == "/admin_usuarios":
            page.views.append(AdminUsuariosView(page, go))
        elif r == "/admin_logs":
            page.views.append(AdminLogsView(page, go))
        elif r == "/inventario":
            page.views.append(InventarioView(page, go))
        elif r == "/inventario_edit":
            page.views.append(InventarioView(page, go, editable=True))
        elif r == "/admin_eliminar_usuario":
            page.views.append(AdminEliminarUsuarioView(page, go))
        elif r == "/admin_mapa_sensores":
            page.views.append(AdminMapaSensoresView(page, go))
        elif r == "/admin_camara":
            page.views.append(AdminCamaraView(page, go))
        elif r == "/admin_alertas":
            page.views.append(AdminAlertasView(page, go))
        elif r == "/admin_umbrales":
            page.views.append(AdminUmbralesView(page, go))
        elif r == "/comentarios":
            page.views.append(ComentariosView(page, go))
        elif r == "/estadisticas_sensores":
            page.views.append(EstadisticasSensoresView(page, go))
        else:
            page.views.append(
                ft.View(
                    r,
                    controls=[
                        ft.Text("404 - Página no encontrada", size=24),
                        ft.TextButton("Volver al inicio", on_click=lambda e: go("/")),
                    ],
                )
            )

        page.update()

    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            page.go(page.views[-1].route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.views.append(home_view())
    page.update()
    page.run_task(bucle_alertas)


def _metric_card(titulo, texto):
    return ft.Container(
        padding=18,
        border_radius=22,
        bgcolor=ft.Colors.with_opacity(0.09, ft.Colors.WHITE),
        border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
        content=ft.Column(
            [
                ft.Text(
                    titulo,
                    size=17,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                ft.Text(
                    texto,
                    size=13,
                    color=ft.Colors.WHITE70,
                ),
            ],
            spacing=6,
        ),
    )


def _mini_stat(titulo, texto):
    return ft.Container(
        padding=ft.Padding(14, 12, 14, 12),
        border_radius=20,
        bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
        border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
        content=ft.Column(
            [
                ft.Text(
                    titulo,
                    size=14,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                ft.Text(
                    texto,
                    size=12,
                    color=ft.Colors.WHITE60,
                ),
            ],
            spacing=4,
        ),
    )


ft.app(target=main, assets_dir="assets")