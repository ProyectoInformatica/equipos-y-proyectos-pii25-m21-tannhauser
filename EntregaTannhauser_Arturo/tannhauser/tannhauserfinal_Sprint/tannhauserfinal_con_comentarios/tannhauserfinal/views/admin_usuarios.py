import flet as ft
from controllers.auth_controller import AuthController
from models.user_manager import UserManager
from models.session_manager import get_current_user


class AdminUsuariosView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/admin_usuarios", padding=0, spacing=0)
        self.page = page
        self.go = go
        self.auth = AuthController()
        self.manager = UserManager()
        self.usuario_actual = get_current_user() or {}
        self.rol_actual = (self.usuario_actual.get("rol") or "").lower()

        self.nombre_input = ft.TextField(
            label="Nombre completo",
            border_radius=16,
            width=320,
        )
        self.email_input = ft.TextField(
            label="Correo electrónico",
            border_radius=16,
            width=320,
        )
        self.password_input = ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
            border_radius=16,
            width=320,
        )

        opciones_rol = [
            ft.dropdown.Option("cliente", "Cliente"),
            ft.dropdown.Option("empleado", "Empleado"),
        ]
        if self.rol_actual == "superusuario":
            opciones_rol.append(ft.dropdown.Option("administrador", "Administrador"))

        self.rol_dropdown = ft.Dropdown(
            label="Rol del nuevo usuario",
            value="cliente",
            options=opciones_rol,
            border_radius=16,
            width=240,
        )

        self.busqueda_input = ft.TextField(
            hint_text="Buscar por nombre o email",
            prefix_icon=ft.Icons.SEARCH_ROUNDED,
            border_radius=18,
            border_color=ft.Colors.with_opacity(0.20, ft.Colors.CYAN_200),
            focused_border_color="#67E8F9",
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
            color=ft.Colors.WHITE,
            width=420,
            on_change=self.refrescar_lista,
        )

        self.users_column = ft.Column(spacing=14)

        self.controls = [self._build_ui()]
        self.refrescar_lista()

    def _mostrar_mensaje(self, texto: str, ok: bool = True):
        self.page.snack_bar = ft.SnackBar(
            ft.Text(texto),
            bgcolor=ft.Colors.GREEN_600 if ok else ft.Colors.RED_600,
        )
        self.page.snack_bar.open = True
        self.page.update()

    def _crear_usuario(self, e):
        nombre = (self.nombre_input.value or "").strip()
        email = (self.email_input.value or "").strip()
        password = (self.password_input.value or "").strip()
        rol = (self.rol_dropdown.value or "cliente").strip().lower()

        ok, msg = self.auth.register(
            nombre=nombre,
            email=email,
            password=password,
            rol=rol,
            actor_rol=self.rol_actual,
        )

        self._mostrar_mensaje(msg, ok)

        if ok:
            self.nombre_input.value = ""
            self.email_input.value = ""
            self.password_input.value = ""
            self.rol_dropdown.value = "cliente"
            self.refrescar_lista()

        self.page.update()

    def _dar_baja_usuario(self, email: str):
        ok, msg = self.manager.eliminar(email)
        self._mostrar_mensaje(msg, ok)
        if ok:
            self.refrescar_lista()

    def _tarjeta_usuario(self, user: dict):
        rol = (user.get("rol") or "").lower()
        activo = bool(user.get("is_active", 0))

        if rol == "superusuario":
            badge_color = "#F59E0B"
        elif rol == "administrador":
            badge_color = "#67E8F9"
        elif rol == "empleado":
            badge_color = "#A78BFA"
        else:
            badge_color = "#34D399"

        puede_dar_baja = (
            activo
            and user.get("email") != self.usuario_actual.get("email")
            and rol != "superusuario"
        )

        return ft.Container(
            width=1180,
            padding=20,
            border_radius=22,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
            content=ft.Row(
                [
                    ft.Row(
                        [
                            ft.CircleAvatar(
                                radius=28,
                                foreground_image_src=user.get("profile_image"),
                                bgcolor=ft.Colors.with_opacity(0.14, ft.Colors.CYAN_300),
                                content=ft.Icon(ft.Icons.PERSON_ROUNDED, color="#9CEBFF")
                                if not user.get("profile_image") else None,
                            ),
                            ft.Column(
                                [
                                    ft.Text(
                                        user.get("nombre", "Sin nombre"),
                                        size=18,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                        user.get("email", ""),
                                        size=13,
                                        color=ft.Colors.WHITE70,
                                    ),
                                    ft.Text(
                                        f"Creado: {user.get('created_at')}",
                                        size=12,
                                        color=ft.Colors.WHITE54,
                                    ),
                                ],
                                spacing=4,
                            ),
                        ],
                        spacing=14,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                padding=ft.Padding(12, 6, 12, 6),
                                border_radius=999,
                                bgcolor=ft.Colors.with_opacity(0.14, ft.Colors.WHITE),
                                content=ft.Text(
                                    "Activo" if activo else "Inactivo",
                                    size=12,
                                    color=ft.Colors.WHITE,
                                ),
                            ),
                            ft.Container(
                                padding=ft.Padding(12, 6, 12, 6),
                                border_radius=999,
                                bgcolor=ft.Colors.with_opacity(0.18, badge_color),
                                content=ft.Text(
                                    rol.capitalize(),
                                    size=12,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                            ),
                            ft.OutlinedButton(
                                "Dar de baja",
                                icon=ft.Icons.PERSON_REMOVE_ROUNDED,
                                disabled=not puede_dar_baja,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.RED_300,
                                    side=ft.BorderSide(1, ft.Colors.with_opacity(0.25, ft.Colors.RED_300)),
                                    shape=ft.RoundedRectangleBorder(radius=14),
                                ),
                                on_click=lambda e, correo=user.get("email"): self._dar_baja_usuario(correo),
                            ),
                        ],
                        spacing=10,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def refrescar_lista(self, e=None):
        texto = (self.busqueda_input.value or "").strip().lower()
        usuarios = self.manager.listar()

        if texto:
            usuarios = [
                u for u in usuarios
                if texto in (u.get("nombre", "").lower()) or texto in (u.get("email", "").lower())
            ]

        self.users_column.controls.clear()

        if not usuarios:
            self.users_column.controls.append(
                ft.Container(
                    width=1180,
                    padding=24,
                    border_radius=20,
                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                    border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                    content=ft.Text(
                        "No se han encontrado usuarios.",
                        size=16,
                        color=ft.Colors.WHITE70,
                    ),
                )
            )
        else:
            for user in usuarios:
                self.users_column.controls.append(self._tarjeta_usuario(user))

        self.page.update()

    def _build_ui(self):
        permiso_texto = (
            "Como administrador puedes crear clientes y empleados."
            if self.rol_actual == "administrador"
            else "Como superusuario puedes crear clientes, empleados y administradores."
        )

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
                        border=ft.Border.all(1, ft.Colors.with_opacity(0.14, ft.Colors.WHITE)),
                        content=ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Text(
                                            "Gestión de usuarios",
                                            size=32,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE,
                                        ),
                                        ft.Text(
                                            "Administra las cuentas del sistema desde una vista moderna y centralizada.",
                                            size=15,
                                            color=ft.Colors.WHITE70,
                                        ),
                                        ft.Text(
                                            permiso_texto,
                                            size=13,
                                            color="#9CEBFF",
                                        ),
                                    ],
                                    spacing=6,
                                ),
                                ft.OutlinedButton(
                                    "Volver",
                                    icon=ft.Icons.ARROW_BACK_ROUNDED,
                                    style=ft.ButtonStyle(
                                        color=ft.Colors.WHITE,
                                        side=ft.BorderSide(1.1, ft.Colors.with_opacity(0.28, ft.Colors.WHITE)),
                                        shape=ft.RoundedRectangleBorder(radius=16),
                                    ),
                                    on_click=lambda e: self.go("/panel_super" if self.rol_actual == "superusuario" else "/panel_admin"),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ),
                    ft.Container(height=18),
                    ft.Container(
                        width=1180,
                        padding=24,
                        border_radius=28,
                        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                        border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                        content=ft.Column(
                            [
                                ft.Text(
                                    "Crear nuevo usuario",
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                                ft.Text(
                                    "Completa los datos y selecciona el rol permitido según tu nivel de acceso.",
                                    size=14,
                                    color=ft.Colors.WHITE70,
                                ),
                                ft.Row(
                                    [
                                        self.nombre_input,
                                        self.email_input,
                                        self.password_input,
                                    ],
                                    wrap=True,
                                    spacing=14,
                                ),
                                ft.Row(
                                    [
                                        self.rol_dropdown,
                                        ft.Button(
                                            "Crear usuario",
                                            icon=ft.Icons.PERSON_ADD_ALT_1_ROUNDED,
                                            bgcolor="#64D7FF",
                                            color=ft.Colors.BLACK,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=16),
                                            ),
                                            on_click=self._crear_usuario,
                                        ),
                                    ],
                                    spacing=14,
                                    wrap=True,
                                ),
                            ],
                            spacing=14,
                        ),
                    ),
                    ft.Container(height=18),
                    ft.Container(
                        width=1180,
                        padding=20,
                        border_radius=24,
                        bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                        border=ft.Border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.WHITE)),
                        content=ft.Column(
                            [
                                ft.Row(
                                    [
                                        ft.Text(
                                            "Usuarios registrados",
                                            size=22,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE,
                                        ),
                                        self.busqueda_input,
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                self.users_column,
                            ],
                            spacing=16,
                        ),
                    ),
                ],
                spacing=0,
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )