import os
import shutil
import time
from collections import defaultdict
from mysql.connector import Error
from models.db import get_connection


class ReviewsController:
    def __init__(self):
        os.makedirs("assets/reviews", exist_ok=True)

    def guardar_imagen_review(self, source_path: str):
        if not source_path:
            return None

        _, ext = os.path.splitext(source_path)
        if not ext:
            ext = ".png"

        filename = f"review_{int(time.time() * 1000)}{ext}"
        destino = os.path.join("assets", "reviews", filename)
        shutil.copy(source_path, destino)
        return destino.replace("\\", "/")

    def obtener_usuario_registrado(self, user_id: int = None, email: str = None):
        if not user_id and not email:
            return None

        conn = get_connection()
        if not conn:
            return None

        cursor = conn.cursor(dictionary=True)
        try:
            if user_id:
                cursor.execute("""
                    SELECT
                        id,
                        nombre,
                        email,
                        profile_image,
                        is_active
                    FROM users
                    WHERE id = %s
                      AND is_active = 1
                    LIMIT 1
                """, (user_id,))
            else:
                cursor.execute("""
                    SELECT
                        id,
                        nombre,
                        email,
                        profile_image,
                        is_active
                    FROM users
                    WHERE LOWER(email) = %s
                      AND is_active = 1
                    LIMIT 1
                """, ((email or "").strip().lower(),))

            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    def usuario_puede_valorar(self, user_id: int = None, email: str = None):
        user = self.obtener_usuario_registrado(user_id=user_id, email=email)
        if not user:
            return False, None
        return True, user

    def crear_review(self, user_id: int, rating: int, title: str, comment: str, image_paths=None):
        user = self.obtener_usuario_registrado(user_id=user_id)
        if not user:
            return False, "Usuario no registrado o inactivo."

        title = (title or "").strip()
        comment = (comment or "").strip()

        if rating < 1 or rating > 5:
            return False, "La valoración debe estar entre 1 y 5 estrellas."
        if not title:
            return False, "El título es obligatorio."
        if not comment:
            return False, "El comentario es obligatorio."

        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar con la base de datos."

        cursor = conn.cursor()
        try:
            conn.start_transaction()

            cursor.execute("""
                INSERT INTO reviews (
                    user_id,
                    rating,
                    title,
                    comment,
                    is_active,
                    created_at,
                    updated_at
                ) VALUES (%s, %s, %s, %s, 1, NOW(), NOW())
            """, (user_id, rating, title, comment))

            review_id = cursor.lastrowid

            if image_paths:
                for image_path in image_paths:
                    if image_path:
                        cursor.execute("""
                            INSERT INTO review_images (
                                review_id,
                                image_path,
                                created_at
                            ) VALUES (%s, %s, NOW())
                        """, (review_id, image_path))

            conn.commit()
            return True, "Reseña publicada correctamente."
        except Error as e:
            conn.rollback()
            return False, f"Error al guardar la reseña: {e}"
        finally:
            cursor.close()
            conn.close()

    def eliminar_review(self, review_id: int, user_id: int, is_admin: bool = False):
        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar con la base de datos."

        cursor = conn.cursor()
        try:
            if is_admin:
                cursor.execute("""
                    UPDATE reviews
                    SET is_active = 0,
                        updated_at = NOW()
                    WHERE id = %s
                """, (review_id,))
            else:
                cursor.execute("""
                    UPDATE reviews
                    SET is_active = 0,
                        updated_at = NOW()
                    WHERE id = %s
                      AND user_id = %s
                """, (review_id, user_id))

            conn.commit()

            if cursor.rowcount == 0:
                return False, "No se pudo eliminar la reseña."

            return True, "Reseña eliminada correctamente."
        except Error as e:
            conn.rollback()
            return False, f"Error al eliminar la reseña: {e}"
        finally:
            cursor.close()
            conn.close()

    def responder_review(self, review_id: int, user_id: int, response_text: str):
        response_text = (response_text or "").strip()
        if not response_text:
            return False, "La respuesta no puede estar vacía."

        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar con la base de datos."

        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT id
                FROM review_responses
                WHERE review_id = %s
                  AND is_active = 1
                LIMIT 1
            """, (review_id,))
            existente = cursor.fetchone()

            if existente:
                cursor.execute("""
                    UPDATE review_responses
                    SET response_text = %s,
                        updated_at = NOW()
                    WHERE id = %s
                """, (response_text, existente["id"]))
            else:
                cursor.execute("""
                    INSERT INTO review_responses (
                        review_id,
                        user_id,
                        response_text,
                        is_active,
                        created_at,
                        updated_at
                    ) VALUES (%s, %s, %s, 1, NOW(), NOW())
                """, (review_id, user_id, response_text))

            conn.commit()
            return True, "Respuesta oficial guardada correctamente."
        except Error as e:
            conn.rollback()
            return False, f"Error al guardar la respuesta: {e}"
        finally:
            cursor.close()
            conn.close()

    def eliminar_respuesta(self, review_id: int):
        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar con la base de datos."

        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE review_responses
                SET is_active = 0,
                    updated_at = NOW()
                WHERE review_id = %s
                  AND is_active = 1
            """, (review_id,))
            conn.commit()

            if cursor.rowcount == 0:
                return False, "No había respuesta activa para eliminar."
            return True, "Respuesta oficial eliminada."
        except Error as e:
            conn.rollback()
            return False, f"Error al eliminar la respuesta: {e}"
        finally:
            cursor.close()
            conn.close()

    def obtener_reviews(self, order_by="recent", only_with_photos=False):
        conn = get_connection()
        if not conn:
            return []

        cursor = conn.cursor(dictionary=True)
        try:
            sql = """
                SELECT
                    r.id,
                    r.user_id,
                    r.rating,
                    r.title,
                    r.comment,
                    r.is_active,
                    r.created_at,
                    r.updated_at,
                    u.nombre,
                    u.email,
                    u.profile_image
                FROM reviews r
                INNER JOIN users u ON u.id = r.user_id
                WHERE r.is_active = 1
            """

            if only_with_photos:
                sql += """
                  AND EXISTS (
                      SELECT 1
                      FROM review_images ri
                      WHERE ri.review_id = r.id
                  )
                """

            if order_by == "best":
                sql += " ORDER BY r.rating DESC, r.created_at DESC"
            else:
                sql += " ORDER BY r.created_at DESC"

            cursor.execute(sql)
            reviews = cursor.fetchall()

            if not reviews:
                return []

            review_ids = [r["id"] for r in reviews]
            format_strings = ",".join(["%s"] * len(review_ids))

            cursor.execute(f"""
                SELECT
                    id,
                    review_id,
                    image_path,
                    created_at
                FROM review_images
                WHERE review_id IN ({format_strings})
                ORDER BY id ASC
            """, tuple(review_ids))
            images = cursor.fetchall()

            cursor.execute(f"""
                SELECT
                    rr.id,
                    rr.review_id,
                    rr.user_id,
                    rr.response_text,
                    rr.created_at,
                    rr.updated_at,
                    u.nombre
                FROM review_responses rr
                INNER JOIN users u ON u.id = rr.user_id
                WHERE rr.review_id IN ({format_strings})
                  AND rr.is_active = 1
            """, tuple(review_ids))
            responses = cursor.fetchall()

            images_by_review = defaultdict(list)
            for img in images:
                images_by_review[img["review_id"]].append(img)

            responses_by_review = {}
            for resp in responses:
                responses_by_review[resp["review_id"]] = resp

            for review in reviews:
                review["images"] = images_by_review.get(review["id"], [])
                review["response"] = responses_by_review.get(review["id"])

            return reviews
        finally:
            cursor.close()
            conn.close()

    def obtener_resumen_reviews(self):
        conn = get_connection()
        if not conn:
            return {
                "total_reviews": 0,
                "average_rating": 0,
                "distribution": {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
            }

        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("""
                SELECT
                    COUNT(*) AS total_reviews,
                    COALESCE(AVG(rating), 0) AS average_rating
                FROM reviews
                WHERE is_active = 1
            """)
            resumen = cursor.fetchone() or {
                "total_reviews": 0,
                "average_rating": 0
            }

            cursor.execute("""
                SELECT rating, COUNT(*) AS total
                FROM reviews
                WHERE is_active = 1
                GROUP BY rating
            """)
            rows = cursor.fetchall()

            distribution = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
            for row in rows:
                distribution[int(row["rating"])] = int(row["total"])

            return {
                "total_reviews": int(resumen["total_reviews"] or 0),
                "average_rating": float(resumen["average_rating"] or 0),
                "distribution": distribution
            }
        finally:
            cursor.close()
            conn.close()