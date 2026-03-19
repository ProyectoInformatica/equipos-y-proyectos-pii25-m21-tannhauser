import flet as ft
from controllers.user_controller import UserController
from controllers.auth_controller import AuthController
from models.session_manager import get_current_user


class AdminUsuariosView(ft.View):
    def __init__(self, page: ft.Page, go):
        super().__init__(route="/admin_usuarios")
        self.page = page
        self.go = go
        self.uc = UserController()
        self.auth = AuthController()

        self.lista_usuarios = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            spacing=10,
        )

        self.nombre_input = ft.TextField(label="Nombre", width=250)
        self.email_input = ft.TextField(label="Email", width=250)
        self.pass_input = ft.TextField(label="Contraseña", width=250, password=True)
        self.rol_dropdown = ft.Dropdown(
            width=250,
            label="Rol",
            options=[
                ft.dropdown.Option("cliente"),
                ft.dropdown.Option("empleado"),
                ft.dropdown.Option("administrador"),
                ft.dropdown.Option("superusuario"),
            ],
        )

        self.construir_ui()

    def did_mount(self):
        self.cargar_usuarios()

    def construir_ui(self):
        titulo = ft.Text(
            "Gestión de Usuarios",
            size=30,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.CYAN_200,
        )

        subtitulo = ft.Text(
            "Añadir, eliminar o visualizar usuarios registrados",
            size=16,
            color=ft.Colors.WHITE70,
        )

        formulario = ft.Container(
            padding=20,
            border_radius=15,
            bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.BLUE_GREY_800),
            border=ft.border.all(1, ft.Colors.CYAN_300),
            content=ft.Column(
                [
                    ft.Text("Crear nuevo usuario", size=20, color=ft.Colors.CYAN_100),
                    self.nombre_input,
                    self.email_input,
                    self.pass_input,
                    self.rol_dropdown,
                    ft.ElevatedButton(
                        "Crear Usuario",
                        icon=ft.Icons.ADD,
                        bgcolor=ft.Colors.GREEN_600,
                        on_click=self.crear_usuario,
                    ),
                ],
                spacing=10,
            ),
        )

        listado = ft.Container(
            height=450,
            width=430,
            padding=15,
            border_radius=15,
            bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.BLUE_GREY_900),
            border=ft.border.all(1, ft.Colors.CYAN_300),
            content=ft.Column(
                [
                    ft.Text("Usuarios Registrados", size=20, color=ft.Colors.CYAN_100),
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                    self.lista_usuarios,
                ],
                expand=True,
                spacing=10,
            ),
        )

        boton_volver = ft.TextButton(
            "Volver al Panel",
            icon=ft.Icons.ARROW_BACK,
            on_click=lambda e: self.go("/panel_admin"),
        )

        self.controls = [
            ft.Column(
                controls=[
                    titulo,
                    subtitulo,
                    ft.Divider(),
                    ft.Row(
                        [formulario, listado],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        spacing=40,
                    ),
                    ft.Divider(),
                    boton_volver,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=25,
                expand=True,
            )
        ]

    def cargar_usuarios(self):
        self.lista_usuarios.controls.clear()

        usuarios = self.uc.obtener_usuarios()
        for u in usuarios:
            self.lista_usuarios.controls.append(self._tarjeta_usuario(u))

        self.update()

    def _tarjeta_usuario(self, usuario):
        return ft.Container(
            padding=10,
            border_radius=10,
            bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.BLUE_GREY_700),
            border=ft.border.all(1, ft.Colors.CYAN_300),
            content=ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(f"ID: {usuario['id']}", color=ft.Colors.CYAN_100, size=13),
                            ft.Text(f"Nombre: {usuario['nombre']}", color=ft.Colors.WHITE, size=14),
                            ft.Text(f"Email: {usuario['email']}", color=ft.Colors.WHITE70, size=13),
                            ft.Text(f"Rol: {usuario['rol']}", color=ft.Colors.AMBER_200, size=13),
                        ],
                        spacing=2,
                        tight=True,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        icon_color=ft.Colors.RED_400,
                        tooltip="Eliminar usuario",
                        on_click=lambda e, email=usuario["email"]: self.eliminar_usuario(email),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        )

    def crear_usuario(self, e):
        nombre = self.nombre_input.value
        email = self.email_input.value
        password = self.pass_input.value
        rol = self.rol_dropdown.value

        if not nombre or not email or not password or not rol:
            self.mensaje("Todos los campos son obligatorios", ft.Colors.RED_600)
            return

        ok, msg = self.uc.crear_usuario(nombre, email, password, rol)
        if not ok:
            self.mensaje(msg, ft.Colors.RED_600)
            return

        self.mensaje("Usuario creado correctamente", ft.Colors.GREEN_700)

        self.nombre_input.value = ""
        self.email_input.value = ""
        self.pass_input.value = ""
        self.rol_dropdown.value = None

        self.cargar_usuarios()

    def eliminar_usuario(self, email):
        password_field = ft.TextField(
            label="Confirma contraseña del administrador",
            password=True,
            width=300,
        )

        def on_confirm(e):
            admin = get_current_user()
            if not admin or admin.get("rol") not in ["administrador", "superusuario"]:
                self.mensaje(
                    "Solo administradores o superusuarios pueden eliminar usuarios.",
                    ft.Colors.RED_700,
                )
                dlg.open = False
                self.page.update()
                return

            if admin.get("email") == email:
                self.mensaje(
                    "No puedes eliminar la cuenta con la que estás autenticado.",
                    ft.Colors.RED_700,
                )
                dlg.open = False
                self.page.update()
                return

            pwd = password_field.value or ""
            usuario_aut = self.auth.login(admin.get("email"), pwd)
            if not usuario_aut:
                self.mensaje("Contraseña incorrecta.", ft.Colors.RED_600)
                return

            actor_email = admin.get("email")
            ok, msg = self.uc.eliminar(email, actor=actor_email)

            still_exists = self.uc.buscar_por_email(email)
            if ok and still_exists:
                ok = False
                msg = "La eliminación no persistió; inténtalo de nuevo."

            color = ft.Colors.GREEN_700 if ok else ft.Colors.RED_700
            self.mensaje(msg, color)

            self.cargar_usuarios()
            self.page.update()

            dlg.open = False
            self.page.update()

        dlg = ft.AlertDialog(
            title=ft.Text("Confirmar eliminación"),
            content=ft.Column(
                [
                    ft.Text(
                        f"Introduce la contraseña del administrador para eliminar al usuario {email}."
                    ),
                    password_field,
                ],
                tight=True,
            ),
            actions=[
                ft.TextButton(
                    "Cancelar",
                    on_click=lambda e: self._cerrar_dialogo(dlg),
                ),
                ft.ElevatedButton(
                    "Confirmar",
                    bgcolor=ft.Colors.RED_700,
                    on_click=on_confirm,
                ),
            ],
        )

        self.page.dialog = dlg
        dlg.open = True
        self.page.update()

    def _cerrar_dialogo(self, dlg):
        dlg.open = False
        self.page.update()

    def mensaje(self, texto, color):
        self.page.snack_bar = ft.SnackBar(ft.Text(texto), bgcolor=color)
        self.page.snack_bar.open = True
        self.page.update()