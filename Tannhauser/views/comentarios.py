import flet as ft
from models.session_manager import get_current_user
from models.comment_manager import CommentManager


def ComentariosView(page: ft.Page, go_router):
    cm = CommentManager()

    txt_comentario = ft.TextField(
        label="Escribe tu opinión sobre Tannhäuser...",
        multiline=True,
        min_lines=3,
        max_lines=5,
        bgcolor=ft.Colors.BLUE_GREY_900,
        border_color=ft.Colors.CYAN_200,
        color=ft.Colors.WHITE,
        border_radius=10
    )

    lista_visual = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, height=400)

    def cargar_comentarios():
        return cm.listar()

    def renderizar_lista():
        lista_visual.controls.clear()
        comentarios_db = cargar_comentarios()

        for com in comentarios_db:
            fecha = com["created_at"].strftime("%Y-%m-%d %H:%M") if com.get("created_at") else ""

            lista_visual.controls.append(
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Row(
                                [
                                    ft.Icon(ft.Icons.PERSON, color=ft.Colors.CYAN_100),
                                    ft.Text(
                                        f"{com['usuario_alias']}",
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.CYAN_100
                                    ),
                                    ft.Text(
                                        fecha,
                                        size=12,
                                        color=ft.Colors.GREY_400
                                    ),
                                ]
                            ),
                            ft.Text(com["texto"], color=ft.Colors.WHITE, size=15)
                        ]
                    ),
                    padding=15,
                    bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.BLACK),
                    border=ft.border.all(1, ft.Colors.CYAN_900),
                    border_radius=10
                )
            )

        page.update()

    def agregar_comentario(e):
        if not txt_comentario.value or not txt_comentario.value.strip():
            return

        usuario_actual = get_current_user()

        if usuario_actual:
            user_id = usuario_actual.get("id")
            nombre_usuario = usuario_actual.get("nombre", "Anónimo")
            rol = usuario_actual.get("rol", "").capitalize()
            etiqueta_usuario = f"{nombre_usuario} ({rol})" if rol else nombre_usuario
        else:
            user_id = None
            etiqueta_usuario = "Anónimo"

        ok = cm.agregar(user_id, etiqueta_usuario, txt_comentario.value)

        if not ok:
            page.snack_bar = ft.SnackBar(
                ft.Text("No se pudo guardar el comentario."),
                bgcolor=ft.Colors.RED_600
            )
            page.snack_bar.open = True
            page.update()
            return

        txt_comentario.value = ""
        renderizar_lista()

        page.snack_bar = ft.SnackBar(
            ft.Text("¡Comentario guardado correctamente!"),
            bgcolor=ft.Colors.GREEN_600
        )
        page.snack_bar.open = True
        page.update()

    renderizar_lista()

    return ft.View(
        route="/comentarios",
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            [
                                ft.IconButton(
                                    ft.Icons.ARROW_BACK,
                                    on_click=lambda e: go_router("/"),
                                    icon_color=ft.Colors.CYAN_200
                                ),
                                ft.Text(
                                    "Buzón de Comentarios",
                                    size=28,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.LIGHT_BLUE_200
                                ),
                            ]
                        ),
                        ft.Divider(color=ft.Colors.CYAN_900),
                        ft.Container(
                            content=ft.Column(
                                [
                                    txt_comentario,
                                    ft.ElevatedButton(
                                        "Enviar Comentario",
                                        icon=ft.Icons.SAVE,
                                        bgcolor=ft.Colors.LIGHT_BLUE_700,
                                        color=ft.Colors.WHITE,
                                        on_click=agregar_comentario
                                    )
                                ]
                            ),
                            padding=20,
                            bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.BLUE_GREY_800),
                            border_radius=15
                        ),
                        ft.Divider(height=30, color=ft.Colors.TRANSPARENT),
                        ft.Text("Historial de opiniones:", size=18, color=ft.Colors.CYAN_100),
                        lista_visual
                    ],
                ),
                padding=40,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment(0, -1),
                    end=ft.Alignment(0, 1),
                    colors=[ft.Colors.INDIGO_900, ft.Colors.DEEP_PURPLE_900],
                ),
                expand=True
            )
        ]
    )