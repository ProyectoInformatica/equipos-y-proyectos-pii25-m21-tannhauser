import flet as ft
from views.login_user import LoginUsuarioView
from views.login_admin import LoginAdminView
from views.login_super import LoginSuperView
from views.login_empleado import LoginEmpleadoView
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
from views.admin_simulacion import AdminSimulacionView
from views.inventario import InventarioView
from views.estadisticas_sensores import EstadisticasSensoresView
from models.session_manager import get_current_user
from views.admin_eliminar_usuario import AdminEliminarUsuarioView
from views.comentarios import ComentariosView
from views.admin_mapa_sensores import AdminMapaSensoresView


def main(page: ft.Page):
    page.title = "Supermercado Inteligente - Tannhäuser"
    page.window_width = 1150
    page.window_height = 720
    page.theme_mode = ft.ThemeMode.DARK

    # ❗ IMPORTANTE: Eliminar alineaciones globales (causaban pantalla negra)
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def go(route: str):
        page.go(route)

    # ---------- Vista principal con fondo ----------
    def home_view():
        color_titulo = ft.Colors.LIGHT_BLUE_200
        color_texto = ft.Colors.WHITE
        color_botones = ft.Colors.LIGHT_BLUE_400
        color_hover = ft.Colors.CYAN_200

        banner = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.LOCATION_CITY, color=ft.Colors.CYAN_300, size=50),
                    ft.Column(
                        controls=[
                            ft.Text(
                                "Proyecto Tannhäuser",
                                size=26,
                                weight=ft.FontWeight.BOLD,
                                color=ft.Colors.LIGHT_BLUE_200,
                            ),
                            ft.Text(
                                "Supermercado Inteligente",
                                size=15,
                                color=ft.Colors.CYAN_100,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=0,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=15,
            ),
            padding=18,
            bgcolor=ft.Colors.with_opacity(0.75, ft.Colors.BLUE_GREY_900),
            shadow=ft.BoxShadow(
                spread_radius=3,
                blur_radius=10,
                color=ft.Colors.CYAN_900,
                offset=ft.Offset(0, 3),
            ),
        )

        imagen_logo = ft.Icon(ft.Icons.SENSOR_OCCUPIED, color=ft.Colors.LIGHT_BLUE_200, size=150)

        titulo = ft.Text(
            "Conectando tu Supermercado con la Ciudad Inteligente",
            size=26,
            weight=ft.FontWeight.BOLD,
            color=color_titulo,
            text_align=ft.TextAlign.CENTER,
        )

        subtitulo = ft.Text(
            "Visualiza datos en tiempo real y gestiona tu entorno con sensores IoT.",
            size=17,
            color=color_texto,
            text_align=ft.TextAlign.CENTER,
        )

        botones = ft.Row(
            controls=[
                ft.ElevatedButton(
                    "Login Cliente",
                    icon=ft.Icons.PERSON,
                    style=ft.ButtonStyle(
                        bgcolor={ft.ControlState.DEFAULT: color_botones,
                                 ft.ControlState.HOVERED: color_hover},
                        color={ft.ControlState.DEFAULT: ft.Colors.BLACK},
                        shape=ft.RoundedRectangleBorder(radius=20),
                        elevation=10,
                    ),
                    on_click=lambda e: go("/login_user"),
                ),
                ft.ElevatedButton(
                    "Login Administrador",
                    icon=ft.Icons.ADMIN_PANEL_SETTINGS,
                    style=ft.ButtonStyle(
                        bgcolor={ft.ControlState.DEFAULT: color_botones,
                                 ft.ControlState.HOVERED: color_hover},
                        color={ft.ControlState.DEFAULT: ft.Colors.BLACK},
                        shape=ft.RoundedRectangleBorder(radius=20),
                        elevation=10,
                    ),
                    on_click=lambda e: go("/login_admin"),
                ),
                ft.ElevatedButton(
                    "Login Superusuario",
                    icon=ft.Icons.SUPERVISED_USER_CIRCLE,
                    style=ft.ButtonStyle(
                        bgcolor={ft.ControlState.DEFAULT: color_botones,
                                 ft.ControlState.HOVERED: color_hover},
                        color={ft.ControlState.DEFAULT: ft.Colors.BLACK},
                        shape=ft.RoundedRectangleBorder(radius=20),
                        elevation=10,
                    ),
                    on_click=lambda e: go("/login_super"),
                ),
                ft.ElevatedButton(
                    "Login Empleado",
                    icon=ft.Icons.PERSON,
                    style=ft.ButtonStyle(
                        bgcolor={ft.ControlState.DEFAULT: color_botones,
                                 ft.ControlState.HOVERED: color_hover},
                        color={ft.ControlState.DEFAULT: ft.Colors.BLACK},
                        shape=ft.RoundedRectangleBorder(radius=20),
                        elevation=10,
                    ),
                    on_click=lambda e: go("/login_empleado"),
                ),
                ft.OutlinedButton(
                    "Registrarse (Cliente)",
                    icon=ft.Icons.PERSON_ADD_ALT,
                    style=ft.ButtonStyle(
                        side={ft.ControlState.DEFAULT: ft.BorderSide(1, color_botones)} ,
                        color={ft.ControlState.DEFAULT: ft.Colors.LIGHT_BLUE_100},
                        shape=ft.RoundedRectangleBorder(radius=20),
                    ),
                    on_click=lambda e: go("/registro"),
                ),
                ft.OutlinedButton(
                    "Comentarios",
                    icon=ft.Icons.COMMENT,
                    style=ft.ButtonStyle(
                        side={ft.ControlState.DEFAULT: ft.BorderSide(1, ft.Colors.CYAN_400)},
                        color={ft.ControlState.DEFAULT: ft.Colors.CYAN_100},
                        shape=ft.RoundedRectangleBorder(radius=20),
                    ),
                    on_click=lambda e: go("/comentarios"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            wrap=True,
        )

        footer = ft.Text(
            "© 2025 Proyecto Tannhäuser – Ingeniería Informática",
            size=12,
            color=ft.Colors.CYAN_100,
            text_align=ft.TextAlign.CENTER,
        )

        main_column = ft.Column(
            [
                banner,
                ft.Container(height=20),
                imagen_logo,
                titulo,
                subtitulo,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                botones,
                ft.Divider(height=20, color=ft.Colors.TRANSPARENT),
                footer,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )

        main_container = ft.Container(
            content=main_column,
            expand=True,
            gradient=ft.LinearGradient(
                begin=ft.Alignment(0, -1),
                end=ft.Alignment(0, 1),
                colors=[ft.Colors.INDIGO_900, ft.Colors.DEEP_PURPLE_900],
            ),
            padding=20,
        )

        return ft.View(
            route="/",
            controls=[main_container],
        )

    # ---------- Sistema de rutas ----------
    def route_change(e):
        page.views.clear()
        r = page.route
        # Validación de permisos según rol de usuario
        usuario = get_current_user()
        def _denegar_acceso():
            page.snack_bar = ft.SnackBar(ft.Text("Acceso restringido: no tienes permisos para ver esta página."), bgcolor=ft.Colors.RED_600)
            page.snack_bar.open = True
            page.update()
            page.go("/")
            return
        # Rutas de sensores: solo administradores, superusuarios y empleados
        if r.startswith("/sensores_"):
            if not usuario or usuario.get("rol") not in ["administrador", "superusuario", "empleado"]:
                _denegar_acceso()
                return

        # Mapa de sensores: SOLO administrador
        # (Debe evaluarse ANTES del check genérico de rutas /admin_)
        if r == "/admin_mapa_sensores":
            if not usuario or usuario.get("rol") != "administrador":
                _denegar_acceso()
                return
        # Rutas admin: administradores y superusuarios
        if r.startswith("/admin_") or r == "/panel_admin":
            if not usuario or usuario.get("rol") not in ["administrador", "superusuario"]:
                _denegar_acceso()
                return
        # Estadísticas de sensores: solo administradores y superusuarios
        if r == "/estadisticas_sensores":
            if not usuario or usuario.get("rol") not in ["administrador", "superusuario"]:
                _denegar_acceso()
                return
        # Panel superusuario
        if r == "/panel_super":
            if not usuario or usuario.get("rol") != "superusuario":
                _denegar_acceso()
                return
        # Panel empleado
        if r == "/panel_empleado":
            if not usuario or usuario.get("rol") != "empleado":
                _denegar_acceso()
                return
        # Panel cliente
        if r == "/panel_usuario":
            if not usuario or usuario.get("rol") != "cliente":
                _denegar_acceso()
                return
        # Inventario editable: solo administradores, superusuarios y empleados
        if r == "/inventario_edit":
            if not usuario or usuario.get("rol") not in ["administrador", "superusuario", "empleado"]:
                _denegar_acceso()
                return
        if r == "/":
            page.views.append(home_view())
        elif r == "/login_user":
            page.views.append(LoginUsuarioView(page, go))
        elif r == "/login_admin":
            page.views.append(LoginAdminView(page, go))
        elif r == "/login_super":
            page.views.append(LoginSuperView(page, go))
        elif r == "/login_empleado":
            page.views.append(LoginEmpleadoView(page, go))
        elif r == "/registro":
            page.views.append(RegistroView(page, go))
        elif r == "/panel_usuario":
            page.views.append(PanelUsuarioView(page, go))
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
        elif r == "/admin_usuarios":
            page.views.append(AdminUsuariosView(page, go))
        elif r == "/admin_logs":
            page.views.append(AdminLogsView(page, go))
        elif r == "/admin_simulacion":
            page.views.append(AdminSimulacionView(page, go))
        elif r == "/inventario":
            page.views.append(InventarioView(page, go))
        elif r == "/inventario_edit":
            page.views.append(InventarioView(page, go, editable=True))
        elif r == "/admin_eliminar_usuario":
            page.views.append(AdminEliminarUsuarioView(page, go))
        elif r == "/admin_mapa_sensores":
            page.views.append(AdminMapaSensoresView(page, go))
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
    # Inicializar con home_view directamente
    page.views.append(home_view())
    page.update()


ft.app(target=main)
