import flet as ft
from controllers.reviews_controller import ReviewsController
from models.session_manager import get_current_user
from models.user_manager import UserManager


def ComentariosView(page: ft.Page, go):
    controller = ReviewsController()
    user_manager = UserManager()

    usuario_sesion = get_current_user() or {}
    session_user_id = usuario_sesion.get("id")
    user_role = (usuario_sesion.get("rol") or "").lower()
    session_email = (usuario_sesion.get("email") or "").strip().lower()

    validated_user = {"data": None}

    if session_user_id:
        ok_user, user_db = controller.usuario_puede_valorar(user_id=session_user_id, email=session_email)
        if ok_user:
            validated_user["data"] = user_db

    selected_rating = {"value": 5}
    uploaded_images = []

    current_order = {"value": "recent"}
    only_with_photos = {"value": False}

    reviews_column = ft.Column(spacing=16)
    selected_images_row = ft.Row(wrap=True, spacing=10)

    title_input = ft.TextField(
        hint_text="Título de tu valoración",
        border_radius=16,
        border_color=ft.Colors.with_opacity(0.20, ft.Colors.CYAN_200),
        focused_border_color="#67E8F9",
        bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
        width=500,
    )

    comment_input = ft.TextField(
        hint_text="Escribe tu opinión, experiencia o crítica...",
        multiline=True,
        min_lines=4,
        max_lines=8,
        border_radius=16,
        border_color=ft.Colors.with_opacity(0.20, ft.Colors.CYAN_200),
        focused_border_color="#67E8F9",
        bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
        color=ft.Colors.WHITE,
        width=700,
    )

    avg_rating_text = ft.Text("0.0", size=42, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE)
    total_reviews_text = ft.Text("0", size=18, color=ft.Colors.WHITE70)
    stars_row_summary = ft.Row(spacing=4)
    distribution_column = ft.Column(spacing=8)

    response_dialog_text = ft.TextField(
        label="Respuesta oficial",
        multiline=True,
        min_lines=3,
        max_lines=6,
        border_radius=14,
        width=500,
    )

    nombre_validado_input = ft.TextField(
        label="Usuario que publicará la reseña",
        value="Se validará al publicar" if not validated_user["data"] else validated_user["data"]["nombre"],
        read_only=True,
        border_radius=16,
        width=340,
    )

    email_validado_input = ft.TextField(
        label="Correo verificado",
        value="Se solicitará al publicar" if not validated_user["data"] else validated_user["data"]["email"],
        read_only=True,
        border_radius=16,
        width=340,
    )

    estado_validacion_text = ft.Text(
        "Puedes escribir tu valoración libremente. La validación se hará al publicar."
        if not validated_user["data"]
        else "Usuario validado correctamente. La reseña se publicará con esta cuenta.",
        size=13,
        color=ft.Colors.WHITE70 if not validated_user["data"] else ft.Colors.GREEN_300,
    )

    cred_email_input = ft.TextField(
        label="Correo electrónico",
        border_radius=14,
        width=420,
    )

    cred_password_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        border_radius=14,
        width=420,
    )

    cred_estado_text = ft.Text(
        "",
        size=13,
        color=ft.Colors.RED_300,
    )

    def show_message(texto: str, ok: bool = True):
        page.snack_bar = ft.SnackBar(
            ft.Text(texto),
            bgcolor=ft.Colors.GREEN_600 if ok else ft.Colors.RED_600
        )
        page.snack_bar.open = True
        page.update()

    def route_back():
        if user_role == "superusuario":
            return "/panel_super"
        if user_role == "administrador":
            return "/panel_admin"
        if user_role == "empleado":
            return "/panel_empleado"
        if user_role == "cliente":
            return "/panel_usuario"
        return "/"

    def render_star(icon_filled: bool, size=22):
        return ft.Icon(
            ft.Icons.STAR_ROUNDED if icon_filled else ft.Icons.STAR_BORDER_ROUNDED,
            color="#FFD166",
            size=size,
        )

    def avatar_review(profile_image, size=56):
        if profile_image:
            return ft.Container(
                width=size,
                height=size,
                border_radius=size / 2,
                clip_behavior=ft.ClipBehavior.HARD_EDGE,
                content=ft.Image(
                    src=profile_image,
                    fit=ft.ImageFit.COVER,
                ),
            )
        return ft.CircleAvatar(
            radius=size / 2,
            bgcolor=ft.Colors.with_opacity(0.18, ft.Colors.CYAN_300),
            content=ft.Icon(
                ft.Icons.PERSON_ROUNDED,
                color="#9CEBFF",
                size=size * 0.42,
            ),
        )

    def build_clickable_stars():
        controls = []
        for i in range(1, 6):
            controls.append(
                ft.IconButton(
                    icon=ft.Icons.STAR_ROUNDED if i <= selected_rating["value"] else ft.Icons.STAR_BORDER_ROUNDED,
                    icon_color="#FFD166",
                    icon_size=30,
                    on_click=lambda e, value=i: set_rating(value),
                )
            )
        return controls

    rating_controls_row = ft.Row(spacing=2)

    def set_rating(value: int):
        selected_rating["value"] = value
        rating_controls_row.controls.clear()
        rating_controls_row.controls.extend(build_clickable_stars())
        page.update()

    def actualizar_bloque_validacion():
        if validated_user["data"]:
            nombre_validado_input.value = validated_user["data"]["nombre"]
            email_validado_input.value = validated_user["data"]["email"]
            estado_validacion_text.value = "Usuario validado correctamente. La reseña se publicará con esta cuenta."
            estado_validacion_text.color = ft.Colors.GREEN_300
        else:
            nombre_validado_input.value = "Se validará al publicar"
            email_validado_input.value = "Se solicitará al publicar"
            estado_validacion_text.value = "Puedes escribir tu valoración libremente. La validación se hará al publicar."
            estado_validacion_text.color = ft.Colors.WHITE70
        page.update()

    def on_pick_result(e: ft.FilePickerResultEvent):
        if e.files:
            for f in e.files:
                saved = controller.guardar_imagen_review(f.path)
                if saved:
                    uploaded_images.append(saved)
        refresh_uploaded_images()

    def refresh_uploaded_images():
        selected_images_row.controls.clear()
        for img_path in uploaded_images:
            selected_images_row.controls.append(
                ft.Stack(
                    controls=[
                        ft.Container(
                            width=110,
                            height=110,
                            border_radius=16,
                            clip_behavior=ft.ClipBehavior.HARD_EDGE,
                            content=ft.Image(src=img_path, fit=ft.ImageFit.COVER),
                        ),
                        ft.Container(
                            alignment=ft.alignment.top_right,
                            content=ft.IconButton(
                                icon=ft.Icons.CLOSE_ROUNDED,
                                icon_color=ft.Colors.WHITE,
                                bgcolor=ft.Colors.with_opacity(0.75, ft.Colors.BLACK),
                                icon_size=16,
                                on_click=lambda e, p=img_path: remove_uploaded_image(p),
                            ),
                        ),
                    ],
                )
            )
        page.update()

    def remove_uploaded_image(path: str):
        if path in uploaded_images:
            uploaded_images.remove(path)
        refresh_uploaded_images()

    file_picker = ft.FilePicker(on_result=on_pick_result)
    page.overlay.append(file_picker)

    def limpiar_formulario_review():
        title_input.value = ""
        comment_input.value = ""
        uploaded_images.clear()
        refresh_uploaded_images()
        set_rating(5)
        page.update()

    def ejecutar_publicacion_con_usuario(user_data: dict):
        ok, msg = controller.crear_review(
            user_id=user_data["id"],
            rating=selected_rating["value"],
            title=title_input.value,
            comment=comment_input.value,
            image_paths=uploaded_images,
        )

        show_message(msg, ok)

        if ok:
            validated_user["data"] = user_data
            actualizar_bloque_validacion()
            limpiar_formulario_review()
            refrescar_reviews()

    def abrir_dialog_validacion():
        cred_estado_text.value = ""
        cred_email_input.value = validated_user["data"]["email"] if validated_user["data"] else ""
        cred_password_input.value = ""

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Validar autoría de la reseña"),
            content=ft.Container(
                width=460,
                content=ft.Column(
                    [
                        ft.Text(
                            "Para publicar esta valoración, valida tus credenciales con la cuenta con la que te registraste.",
                            size=14,
                        ),
                        cred_email_input,
                        cred_password_input,
                        cred_estado_text,
                    ],
                    tight=True,
                    spacing=12,
                )
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: page.close(dialog)),
                ft.ElevatedButton(
                    "Validar y publicar",
                    bgcolor="#67E8F9",
                    color=ft.Colors.BLACK,
                    on_click=lambda e: validar_y_publicar(dialog),
                ),
            ],
        )
        page.open(dialog)

    def validar_y_publicar(dialog):
        email = (cred_email_input.value or "").strip().lower()
        password = (cred_password_input.value or "").strip()

        if not email or not password:
            cred_estado_text.value = "Debes introducir correo y contraseña."
            page.update()
            return

        user = user_manager.autenticar(email, password)
        if not user:
            cred_estado_text.value = "Usuario no registrado o credenciales incorrectas."
            page.update()
            return

        ok_user, user_db = controller.usuario_puede_valorar(user_id=user.get("id"), email=user.get("email"))
        if not ok_user or not user_db:
            cred_estado_text.value = "Usuario no registrado o inactivo."
            page.update()
            return

        validated_user["data"] = user_db
        page.close(dialog)
        actualizar_bloque_validacion()
        ejecutar_publicacion_con_usuario(user_db)

    def publicar_review(e):
        if validated_user["data"]:
            ejecutar_publicacion_con_usuario(validated_user["data"])
        else:
            abrir_dialog_validacion()

    def eliminar_review(review_id: int):
        current_user_id = usuario_sesion.get("id")
        is_admin = user_role in ["administrador", "superusuario"]
        if not current_user_id and not is_admin:
            show_message("Debes iniciar sesión para eliminar una reseña propia.", False)
            return

        ok, msg = controller.eliminar_review(review_id, current_user_id, is_admin=is_admin)
        show_message(msg, ok)
        if ok:
            refrescar_reviews()

    def abrir_dialog_respuesta(review_id: int, respuesta_actual: str = ""):
        response_dialog_text.value = respuesta_actual or ""

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Respuesta oficial"),
            content=response_dialog_text,
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: page.close(dialog)),
                ft.TextButton(
                    "Eliminar respuesta",
                    on_click=lambda e: eliminar_respuesta(review_id, dialog),
                ),
                ft.ElevatedButton(
                    "Guardar respuesta",
                    bgcolor="#67E8F9",
                    color=ft.Colors.BLACK,
                    on_click=lambda e: guardar_respuesta(review_id, dialog),
                ),
            ],
        )
        page.open(dialog)

    def guardar_respuesta(review_id: int, dialog):
        if not session_user_id:
            page.close(dialog)
            show_message("Debes iniciar sesión como administrador para responder.", False)
            return

        ok, msg = controller.responder_review(review_id, session_user_id, response_dialog_text.value)
        page.close(dialog)
        show_message(msg, ok)
        if ok:
            refrescar_reviews()

    def eliminar_respuesta(review_id: int, dialog):
        ok, msg = controller.eliminar_respuesta(review_id)
        page.close(dialog)
        show_message(msg, ok)
        if ok:
            refrescar_reviews()

    def tarjeta_distribution(stars: int, total: int, grand_total: int):
        porcentaje = 0 if grand_total == 0 else total / grand_total
        return ft.Row(
            [
                ft.Text(f"{stars}★", width=40, color=ft.Colors.WHITE70),
                ft.ProgressBar(
                    value=porcentaje,
                    width=220,
                    color="#67E8F9",
                    bgcolor=ft.Colors.with_opacity(0.10, ft.Colors.WHITE),
                ),
                ft.Text(str(total), width=30, color=ft.Colors.WHITE70),
            ],
            spacing=10,
        )

    def bloque_respuesta_oficial(response: dict):
        return ft.Container(
            padding=16,
            border_radius=18,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.CYAN_100),
            border=ft.border.all(1, ft.Colors.with_opacity(0.12, ft.Colors.CYAN_200)),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.STORE_ROUNDED, color="#8BE3FF", size=20),
                            ft.Text(
                                "Respuesta oficial del supermercado",
                                size=14,
                                weight=ft.FontWeight.BOLD,
                                color="#8BE3FF",
                            ),
                        ],
                        spacing=8,
                    ),
                    ft.Text(
                        response.get("response_text", ""),
                        size=13,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        f"{response.get('nombre', 'Equipo')} · {response.get('updated_at') or response.get('created_at')}",
                        size=11,
                        color=ft.Colors.WHITE54,
                    ),
                ],
                spacing=8,
            ),
        )

    def build_review_card(review: dict):
        stars_controls = [render_star(i <= int(review.get("rating", 0)), size=20) for i in range(1, 6)]

        image_gallery = ft.Row(
            [
                ft.Container(
                    width=120,
                    height=120,
                    border_radius=16,
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                    content=ft.Image(src=img["image_path"], fit=ft.ImageFit.COVER),
                )
                for img in review.get("images", [])
            ],
            wrap=True,
            spacing=10,
        )

        can_delete = review.get("user_id") == session_user_id or user_role in ["administrador", "superusuario"]
        can_reply = user_role in ["administrador", "superusuario"]
        response = review.get("response")

        actions = []
        if can_reply:
            actions.append(
                ft.OutlinedButton(
                    "Responder",
                    icon=ft.Icons.REPLY_ROUNDED,
                    style=ft.ButtonStyle(
                        color=ft.Colors.WHITE,
                        side=ft.BorderSide(1, ft.Colors.with_opacity(0.22, ft.Colors.WHITE)),
                        shape=ft.RoundedRectangleBorder(radius=14),
                    ),
                    on_click=lambda e, rid=review["id"], rtext=(response.get("response_text") if response else ""): abrir_dialog_respuesta(rid, rtext),
                )
            )

        if can_delete:
            actions.append(
                ft.OutlinedButton(
                    "Eliminar",
                    icon=ft.Icons.DELETE_OUTLINE_ROUNDED,
                    style=ft.ButtonStyle(
                        color=ft.Colors.RED_300,
                        side=ft.BorderSide(1, ft.Colors.with_opacity(0.25, ft.Colors.RED_300)),
                        shape=ft.RoundedRectangleBorder(radius=14),
                    ),
                    on_click=lambda e, rid=review["id"]: eliminar_review(rid),
                )
            )

        return ft.Container(
            padding=22,
            border_radius=24,
            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
            border=ft.border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            avatar_review(review.get("profile_image"), 56),
                            ft.Column(
                                [
                                    ft.Text(
                                        review.get("nombre", "Usuario"),
                                        size=17,
                                        weight=ft.FontWeight.BOLD,
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                        review.get("email", ""),
                                        size=12,
                                        color=ft.Colors.WHITE54,
                                    ),
                                    ft.Row(stars_controls, spacing=2),
                                ],
                                spacing=4,
                                expand=True,
                            ),
                            ft.Text(
                                str(review.get("created_at", "")),
                                size=12,
                                color=ft.Colors.WHITE54,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                    ft.Text(
                        review.get("title", ""),
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        review.get("comment", ""),
                        size=14,
                        color=ft.Colors.WHITE70,
                    ),
                    image_gallery if review.get("images") else ft.Container(),
                    bloque_respuesta_oficial(response) if response else ft.Container(),
                    ft.Row(actions, alignment=ft.MainAxisAlignment.END, spacing=10) if actions else ft.Container(),
                ],
                spacing=14,
            ),
        )

    def refrescar_reviews():
        summary = controller.obtener_resumen_reviews()

        avg_rating_text.value = f"{summary['average_rating']:.1f}"
        total_reviews_text.value = f"{summary['total_reviews']} valoraciones"

        stars_row_summary.controls.clear()
        rounded = round(summary["average_rating"])
        for i in range(1, 6):
            stars_row_summary.controls.append(render_star(i <= rounded, size=24))

        distribution_column.controls.clear()
        for star in [5, 4, 3, 2, 1]:
            distribution_column.controls.append(
                tarjeta_distribution(
                    star,
                    summary["distribution"].get(star, 0),
                    summary["total_reviews"],
                )
            )

        reviews = controller.obtener_reviews(
            order_by=current_order["value"],
            only_with_photos=only_with_photos["value"],
        )

        reviews_column.controls.clear()
        if reviews:
            for review in reviews:
                reviews_column.controls.append(build_review_card(review))
        else:
            reviews_column.controls.append(
                ft.Container(
                    padding=30,
                    border_radius=20,
                    bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                    content=ft.Column(
                        [
                            ft.Icon(ft.Icons.RATE_REVIEW_ROUNDED, size=42, color=ft.Colors.WHITE60),
                            ft.Text(
                                "Todavía no hay valoraciones publicadas.",
                                size=16,
                                color=ft.Colors.WHITE70,
                            ),
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10,
                    ),
                )
            )

        page.update()

    order_dropdown = ft.Dropdown(
        width=220,
        value="recent",
        options=[
            ft.dropdown.Option("recent", "Más recientes"),
            ft.dropdown.Option("best", "Mejor valoradas"),
        ],
        border_radius=14,
        on_change=lambda e: cambiar_orden(e.control.value),
    )

    def cambiar_orden(value):
        current_order["value"] = value
        refrescar_reviews()

    only_photos_checkbox = ft.Checkbox(
        label="Solo con fotos",
        value=False,
        check_color=ft.Colors.BLACK,
        fill_color="#67E8F9",
        label_style=ft.TextStyle(color=ft.Colors.WHITE70),
        on_change=lambda e: cambiar_filtro_fotos(e.control.value),
    )

    def cambiar_filtro_fotos(value):
        only_with_photos["value"] = value
        refrescar_reviews()

    rating_controls_row.controls.extend(build_clickable_stars())
    refrescar_reviews()

    return ft.View(
        route="/comentarios",
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
                                            "Valoraciones y reseñas",
                                            size=38,
                                            weight=ft.FontWeight.BOLD,
                                            color=ft.Colors.WHITE,
                                        ),
                                        ft.Text(
                                            "Opiniones, críticas y satisfacción de clientes al estilo de una app profesional.",
                                            size=16,
                                            color=ft.Colors.WHITE70,
                                        ),
                                    ],
                                    spacing=6,
                                    expand=True,
                                ),
                                ft.OutlinedButton(
                                    "Volver",
                                    icon=ft.Icons.ARROW_BACK_ROUNDED,
                                    on_click=lambda e: go(route_back()),
                                    style=ft.ButtonStyle(
                                        color=ft.Colors.WHITE,
                                        side=ft.BorderSide(1, ft.Colors.with_opacity(0.22, ft.Colors.WHITE)),
                                        shape=ft.RoundedRectangleBorder(radius=18),
                                    ),
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        ft.Container(height=18),
                        ft.Row(
                            [
                                ft.Container(
                                    width=350,
                                    padding=24,
                                    border_radius=28,
                                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                                    border=ft.border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                "Valoración media",
                                                size=18,
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.WHITE,
                                            ),
                                            avg_rating_text,
                                            stars_row_summary,
                                            total_reviews_text,
                                            ft.Container(height=8),
                                            distribution_column,
                                        ],
                                        spacing=10,
                                    ),
                                ),
                                ft.Container(
                                    expand=True,
                                    padding=24,
                                    border_radius=28,
                                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                                    border=ft.border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                "Escribir una reseña",
                                                size=22,
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.WHITE,
                                            ),
                                            ft.Text(
                                                "Puedes escribir tu reseña sin iniciar sesión. La validación de tu cuenta se pedirá solo en el momento de publicarla.",
                                                size=14,
                                                color=ft.Colors.WHITE70,
                                            ),
                                            estado_validacion_text,
                                            ft.Row(
                                                [
                                                    nombre_validado_input,
                                                    email_validado_input,
                                                ],
                                                spacing=12,
                                                wrap=True,
                                            ),
                                            ft.Text(
                                                "Tu valoración",
                                                size=14,
                                                color=ft.Colors.WHITE60,
                                            ),
                                            rating_controls_row,
                                            title_input,
                                            comment_input,
                                            ft.Row(
                                                [
                                                    ft.ElevatedButton(
                                                        "Añadir fotos",
                                                        icon=ft.Icons.ADD_A_PHOTO_ROUNDED,
                                                        bgcolor="#67E8F9",
                                                        color=ft.Colors.BLACK,
                                                        style=ft.ButtonStyle(
                                                            shape=ft.RoundedRectangleBorder(radius=16),
                                                        ),
                                                        on_click=lambda e: file_picker.pick_files(
                                                            allow_multiple=True,
                                                            allowed_extensions=["png", "jpg", "jpeg", "webp"]
                                                        ),
                                                    ),
                                                    ft.ElevatedButton(
                                                        "Publicar reseña",
                                                        icon=ft.Icons.SEND_ROUNDED,
                                                        bgcolor="#67E8F9",
                                                        color=ft.Colors.BLACK,
                                                        style=ft.ButtonStyle(
                                                            shape=ft.RoundedRectangleBorder(radius=16),
                                                        ),
                                                        on_click=publicar_review,
                                                    ),
                                                ],
                                                spacing=12,
                                            ),
                                            selected_images_row,
                                        ],
                                        spacing=14,
                                    ),
                                ),
                            ],
                            spacing=22,
                            vertical_alignment=ft.CrossAxisAlignment.START,
                        ),
                        ft.Container(height=22),
                        ft.Container(
                            padding=24,
                            border_radius=28,
                            bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                            border=ft.border.all(1, ft.Colors.with_opacity(0.10, ft.Colors.WHITE)),
                            content=ft.Column(
                                [
                                    ft.Row(
                                        [
                                            ft.Text(
                                                "Reseñas publicadas",
                                                size=24,
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.WHITE,
                                            ),
                                            ft.Row(
                                                [
                                                    order_dropdown,
                                                    only_photos_checkbox,
                                                ],
                                                spacing=16,
                                                wrap=True,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    ),
                                    reviews_column,
                                ],
                                spacing=16,
                            ),
                        ),
                    ],
                    spacing=0,
                    scroll=ft.ScrollMode.AUTO,
                ),
            )
        ],
        padding=0,
        spacing=0,
    )