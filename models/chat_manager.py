import mimetypes
import os
import shutil
import uuid
from typing import Any

from mysql.connector import Error

from models.db import get_connection


ALL_CHAT_ROLES = {"cliente", "empleado", "administrador", "superusuario"}
INTERNAL_CHAT_ROLES = {"empleado", "administrador", "superusuario"}
GROUP_CREATOR_ROLES = {"administrador", "superusuario"}
DIRECT_CREATOR_ROLES = {"empleado", "administrador", "superusuario"}


class ChatManager:
    upload_dir = os.path.join("assets", "chat_uploads")
    asset_prefix = "chat_uploads"

    create_tables_sql = [
        """
        CREATE TABLE IF NOT EXISTS chat_groups (
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
            name VARCHAR(120) NOT NULL,
            description VARCHAR(255) DEFAULT NULL,
            created_by BIGINT UNSIGNED NOT NULL,
            created_by_role VARCHAR(40) DEFAULT NULL,
            group_type VARCHAR(30) NOT NULL DEFAULT 'group',
            is_direct TINYINT(1) NOT NULL DEFAULT 0,
            direct_key VARCHAR(190) DEFAULT NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            is_active TINYINT(1) NOT NULL DEFAULT 1,
            PRIMARY KEY (id),
            KEY idx_chat_groups_active (is_active),
            KEY idx_chat_groups_created_by (created_by),
            UNIQUE KEY uq_chat_direct_key (direct_key),
            CONSTRAINT fk_chat_groups_created_by
                FOREIGN KEY (created_by) REFERENCES users(id)
                ON DELETE RESTRICT
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """,
        """
        CREATE TABLE IF NOT EXISTS chat_group_members (
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
            group_id BIGINT UNSIGNED NOT NULL,
            user_id BIGINT UNSIGNED NOT NULL,
            role_in_group VARCHAR(40) NOT NULL DEFAULT 'member',
            joined_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            UNIQUE KEY uq_chat_group_member (group_id, user_id),
            KEY idx_chat_group_members_user (user_id),
            CONSTRAINT fk_chat_group_members_group
                FOREIGN KEY (group_id) REFERENCES chat_groups(id)
                ON DELETE CASCADE,
            CONSTRAINT fk_chat_group_members_user
                FOREIGN KEY (user_id) REFERENCES users(id)
                ON DELETE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """,
        """
        CREATE TABLE IF NOT EXISTS chat_attachments (
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
            message_id BIGINT UNSIGNED DEFAULT NULL,
            original_filename VARCHAR(255) NOT NULL,
            stored_filename VARCHAR(255) NOT NULL,
            file_path VARCHAR(500) NOT NULL,
            mime_type VARCHAR(120) DEFAULT NULL,
            file_size BIGINT UNSIGNED DEFAULT NULL,
            uploaded_by BIGINT UNSIGNED NOT NULL,
            uploaded_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            KEY idx_chat_attachments_message (message_id),
            KEY idx_chat_attachments_uploaded_by (uploaded_by),
            CONSTRAINT fk_chat_attachments_uploaded_by
                FOREIGN KEY (uploaded_by) REFERENCES users(id)
                ON DELETE RESTRICT
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """,
        """
        CREATE TABLE IF NOT EXISTS chat_messages (
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
            group_id BIGINT UNSIGNED DEFAULT NULL,
            sender_id BIGINT UNSIGNED NOT NULL,
            receiver_id BIGINT UNSIGNED DEFAULT NULL,
            message TEXT DEFAULT NULL,
            message_text TEXT DEFAULT NULL,
            message_type VARCHAR(30) NOT NULL DEFAULT 'text',
            attachment_id BIGINT UNSIGNED DEFAULT NULL,
            created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            is_deleted TINYINT(1) NOT NULL DEFAULT 0,
            PRIMARY KEY (id),
            KEY idx_chat_messages_group_created (group_id, created_at),
            KEY idx_chat_messages_sender (sender_id),
            KEY idx_chat_messages_attachment (attachment_id),
            CONSTRAINT fk_chat_messages_group
                FOREIGN KEY (group_id) REFERENCES chat_groups(id)
                ON DELETE CASCADE,
            CONSTRAINT fk_chat_messages_sender
                FOREIGN KEY (sender_id) REFERENCES users(id)
                ON DELETE RESTRICT,
            CONSTRAINT fk_chat_messages_attachment
                FOREIGN KEY (attachment_id) REFERENCES chat_attachments(id)
                ON DELETE SET NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """,
    ]

    def __init__(self):
        self.last_error = None

    def ensure_tables(self) -> bool:
        self.last_error = None
        try:
            os.makedirs(self.upload_dir, exist_ok=True)
        except OSError as e:
            self.last_error = f"No se pudo preparar assets/chat_uploads: {e}"
            return False

        conn = get_connection()
        if not conn:
            self.last_error = "No se pudo conectar con la base de datos."
            return False

        cursor = conn.cursor()
        try:
            for sql in self.create_tables_sql:
                cursor.execute(sql)
            conn.commit()
            self._upgrade_existing_schema(conn)
            return True
        except Error as e:
            self.last_error = f"Error preparando tablas de chat: {e}"
            print(self.last_error)
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    def _columns(self, conn, table: str) -> dict[str, dict[str, Any]]:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SHOW COLUMNS FROM {table}")
        rows = {row["Field"]: row for row in cursor.fetchall()}
        cursor.close()
        return rows

    def _indexes(self, conn, table: str) -> set[str]:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SHOW INDEX FROM {table}")
        rows = {row["Key_name"] for row in cursor.fetchall()}
        cursor.close()
        return rows

    def _add_column_if_missing(self, conn, table: str, column: str, definition: str):
        if column not in self._columns(conn, table):
            cursor = conn.cursor()
            cursor.execute(f"ALTER TABLE {table} ADD COLUMN {definition}")
            cursor.close()

    def _add_index_if_missing(self, conn, table: str, index_name: str, ddl: str):
        if index_name not in self._indexes(conn, table):
            cursor = conn.cursor()
            cursor.execute(ddl)
            cursor.close()

    def _upgrade_existing_schema(self, conn):
        self._add_column_if_missing(conn, "chat_groups", "created_by_role", "created_by_role VARCHAR(40) DEFAULT NULL AFTER created_by")
        self._add_column_if_missing(conn, "chat_groups", "group_type", "group_type VARCHAR(30) NOT NULL DEFAULT 'group' AFTER created_by_role")
        self._add_column_if_missing(conn, "chat_groups", "is_direct", "is_direct TINYINT(1) NOT NULL DEFAULT 0 AFTER group_type")
        self._add_column_if_missing(conn, "chat_groups", "direct_key", "direct_key VARCHAR(190) DEFAULT NULL AFTER is_direct")
        self._add_index_if_missing(conn, "chat_groups", "uq_chat_direct_key", "ALTER TABLE chat_groups ADD UNIQUE KEY uq_chat_direct_key (direct_key)")

        columns = self._columns(conn, "chat_messages")
        cursor = conn.cursor()
        if "group_id" not in columns:
            cursor.execute("ALTER TABLE chat_messages ADD COLUMN group_id BIGINT UNSIGNED DEFAULT NULL AFTER id")
        if "receiver_id" in columns and "NO" == columns["receiver_id"]["Null"]:
            cursor.execute("ALTER TABLE chat_messages MODIFY receiver_id BIGINT UNSIGNED DEFAULT NULL")
        if "message" in columns and "NO" == columns["message"]["Null"]:
            cursor.execute("ALTER TABLE chat_messages MODIFY message TEXT DEFAULT NULL")
        cursor.close()
        self._add_column_if_missing(conn, "chat_messages", "message_text", "message_text TEXT DEFAULT NULL AFTER message")
        self._add_column_if_missing(conn, "chat_messages", "message_type", "message_type VARCHAR(30) NOT NULL DEFAULT 'text' AFTER message_text")
        self._add_column_if_missing(conn, "chat_messages", "attachment_id", "attachment_id BIGINT UNSIGNED DEFAULT NULL AFTER message_type")
        self._add_column_if_missing(conn, "chat_messages", "is_deleted", "is_deleted TINYINT(1) NOT NULL DEFAULT 0 AFTER created_at")
        self._add_index_if_missing(conn, "chat_messages", "idx_chat_messages_group_created", "ALTER TABLE chat_messages ADD KEY idx_chat_messages_group_created (group_id, created_at)")
        self._add_index_if_missing(conn, "chat_messages", "idx_chat_messages_attachment", "ALTER TABLE chat_messages ADD KEY idx_chat_messages_attachment (attachment_id)")
        conn.commit()

    def normalize_role(self, role: str) -> str:
        return (role or "").strip().lower()

    def role_allowed(self, role: str) -> bool:
        return self.normalize_role(role) in ALL_CHAT_ROLES

    def can_create_group(self, role: str) -> bool:
        return self.normalize_role(role) in GROUP_CREATOR_ROLES

    def can_create_direct(self, role: str) -> bool:
        return self.normalize_role(role) in DIRECT_CREATOR_ROLES

    def _user_row(self, user_id: int) -> dict[str, Any] | None:
        conn = get_connection()
        if not conn:
            return None
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(
                """
                SELECT u.id, u.nombre, u.email, LOWER(r.name) AS rol, u.profile_image, u.is_active
                FROM users u
                JOIN roles r ON r.id = u.role_id
                WHERE u.id = %s AND u.is_active = 1
                LIMIT 1
                """,
                (user_id,),
            )
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    def list_chat_users(self, actor: dict[str, Any] | None = None, mode: str = "group") -> list[dict[str, Any]]:
        if not self.ensure_tables():
            return []
        actor = actor or {}
        actor_role = self.normalize_role(actor.get("rol"))
        actor_id = actor.get("id")
        conn = get_connection()
        if not conn:
            return []
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(
                """
                SELECT u.id, u.nombre, u.email, LOWER(r.name) AS rol, u.profile_image
                FROM users u
                JOIN roles r ON r.id = u.role_id
                WHERE u.is_active = 1
                ORDER BY FIELD(LOWER(r.name), 'superusuario', 'administrador', 'empleado', 'cliente'), u.nombre, u.email
                """
            )
            users = cursor.fetchall() or []
            return [u for u in users if self._user_selectable_for(actor_role, actor_id, u, mode)]
        except Error as e:
            self.last_error = f"Error leyendo usuarios de chat: {e}"
            print(self.last_error)
            return []
        finally:
            cursor.close()
            conn.close()

    def _user_selectable_for(self, actor_role: str, actor_id: int, user: dict[str, Any], mode: str) -> bool:
        target_role = self.normalize_role(user.get("rol"))
        if user.get("id") == actor_id:
            return True
        if mode == "direct":
            if actor_role == "superusuario":
                return True
            if actor_role == "administrador":
                return target_role in {"empleado", "cliente"}
            if actor_role == "empleado":
                return target_role in INTERNAL_CHAT_ROLES
            return False
        if actor_role == "superusuario":
            return target_role in ALL_CHAT_ROLES
        if actor_role == "administrador":
            return target_role in {"administrador", "empleado", "cliente"}
        return False

    def get_groups_for_user(self, user_id: int, role: str) -> list[dict[str, Any]]:
        if not self.ensure_tables():
            return []
        role = self.normalize_role(role)
        if not self.role_allowed(role) or not user_id:
            return []
        conn = get_connection()
        if not conn:
            return []
        cursor = conn.cursor(dictionary=True)
        try:
            base_select = """
                SELECT
                    g.id, g.name, g.description, g.created_by, g.created_by_role,
                    g.group_type, g.is_direct, g.direct_key, g.created_at, g.is_active,
                    u.nombre AS creator_name,
                    (SELECT COUNT(*) FROM chat_group_members gm_count WHERE gm_count.group_id = g.id) AS member_count,
                    (SELECT MAX(m.created_at) FROM chat_messages m WHERE m.group_id = g.id AND COALESCE(m.is_deleted, 0) = 0) AS last_message_at
                FROM chat_groups g
                JOIN users u ON u.id = g.created_by
            """
            if role == "superusuario":
                cursor.execute(
                    base_select
                    + """
                    WHERE g.is_active = 1
                    ORDER BY COALESCE((SELECT MAX(m2.created_at) FROM chat_messages m2 WHERE m2.group_id = g.id AND COALESCE(m2.is_deleted, 0) = 0), g.created_at) DESC
                    """
                )
            else:
                cursor.execute(
                    base_select
                    + """
                    JOIN chat_group_members gm ON gm.group_id = g.id AND gm.user_id = %s
                    WHERE g.is_active = 1
                    ORDER BY COALESCE((SELECT MAX(m2.created_at) FROM chat_messages m2 WHERE m2.group_id = g.id AND COALESCE(m2.is_deleted, 0) = 0), g.created_at) DESC
                    """,
                    (user_id,),
                )
            return cursor.fetchall() or []
        except Error as e:
            self.last_error = f"Error leyendo grupos de chat: {e}"
            print(self.last_error)
            return []
        finally:
            cursor.close()
            conn.close()

    def create_group(self, name: str, description: str, created_by: int, members: list[int], actor: dict[str, Any] | None = None) -> tuple[bool, str, int | None]:
        if not self.ensure_tables():
            return False, self.last_error or "No se pudieron preparar las tablas del chat.", None
        actor = actor or {}
        actor_role = self.normalize_role(actor.get("rol"))
        if not self.can_create_group(actor_role):
            return False, "No tienes permisos para crear grupos.", None
        name = (name or "").strip()
        description = (description or "").strip()
        if not name:
            return False, "El grupo necesita un nombre.", None

        allowed_users = {int(u["id"]) for u in self.list_chat_users(actor, mode="group")}
        member_ids = sorted({int(m) for m in members if m and int(m) in allowed_users})
        if created_by not in member_ids:
            member_ids.append(int(created_by))
        if len(member_ids) < 2:
            return False, "Selecciona al menos un participante ademas de ti.", None

        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar con la base de datos.", None
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO chat_groups (name, description, created_by, created_by_role, group_type, is_direct, direct_key, created_at, is_active)
                VALUES (%s, %s, %s, %s, 'group', 0, NULL, NOW(), 1)
                """,
                (name, description, created_by, actor_role),
            )
            group_id = cursor.lastrowid
            for user_id in member_ids:
                role_in_group = "owner" if user_id == created_by else "member"
                cursor.execute(
                    """
                    INSERT INTO chat_group_members (group_id, user_id, role_in_group, joined_at)
                    VALUES (%s, %s, %s, NOW())
                    ON DUPLICATE KEY UPDATE role_in_group = VALUES(role_in_group)
                    """,
                    (group_id, user_id, role_in_group),
                )
            conn.commit()
            return True, "Grupo creado correctamente.", group_id
        except Error as e:
            conn.rollback()
            self.last_error = f"Error creando grupo: {e}"
            return False, self.last_error, None
        finally:
            cursor.close()
            conn.close()

    def create_or_get_direct_chat(self, actor: dict[str, Any], target_user_id: int) -> tuple[bool, str, int | None]:
        if not self.ensure_tables():
            return False, self.last_error or "No se pudieron preparar las tablas del chat.", None
        actor_id = int(actor.get("id") or 0)
        actor_role = self.normalize_role(actor.get("rol"))
        target_user_id = int(target_user_id or 0)
        if not actor_id or not target_user_id or actor_id == target_user_id:
            return False, "Selecciona un usuario distinto.", None
        if not self.can_create_direct(actor_role):
            return False, "Tu rol no puede iniciar chats directos.", None
        target = self._user_row(target_user_id)
        if not target or not self._user_selectable_for(actor_role, actor_id, target, "direct"):
            return False, "No puedes iniciar chat directo con ese usuario.", None

        first, second = sorted([actor_id, target_user_id])
        direct_key = f"direct:{first}:{second}"
        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar con la base de datos.", None
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT id FROM chat_groups WHERE direct_key = %s AND is_active = 1 LIMIT 1", (direct_key,))
            existing = cursor.fetchone()
            if existing:
                return True, "Conversacion directa abierta.", existing["id"]

            actor_name = actor.get("nombre") or actor.get("email") or "Usuario"
            target_name = target.get("nombre") or target.get("email") or "Usuario"
            cursor.execute(
                """
                INSERT INTO chat_groups (name, description, created_by, created_by_role, group_type, is_direct, direct_key, created_at, is_active)
                VALUES (%s, %s, %s, %s, 'direct', 1, %s, NOW(), 1)
                """,
                (f"Directo: {actor_name} / {target_name}", "Conversacion directa", actor_id, actor_role, direct_key),
            )
            group_id = cursor.lastrowid
            for uid, role_in_group in [(actor_id, "owner"), (target_user_id, "member")]:
                cursor.execute(
                    """
                    INSERT INTO chat_group_members (group_id, user_id, role_in_group, joined_at)
                    VALUES (%s, %s, %s, NOW())
                    ON DUPLICATE KEY UPDATE role_in_group = VALUES(role_in_group)
                    """,
                    (group_id, uid, role_in_group),
                )
            conn.commit()
            return True, "Conversacion directa creada.", group_id
        except Error as e:
            conn.rollback()
            self.last_error = f"Error creando chat directo: {e}"
            return False, self.last_error, None
        finally:
            cursor.close()
            conn.close()

    def check_user_access(self, group_id: int, user_id: int, role: str) -> bool:
        role = self.normalize_role(role)
        if not self.role_allowed(role) or not group_id or not user_id:
            return False
        if role == "superusuario":
            return True
        conn = get_connection()
        if not conn:
            return False
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(
                "SELECT id FROM chat_group_members WHERE group_id = %s AND user_id = %s LIMIT 1",
                (group_id, user_id),
            )
            return cursor.fetchone() is not None
        except Error as e:
            self.last_error = f"Error validando acceso al grupo: {e}"
            print(self.last_error)
            return False
        finally:
            cursor.close()
            conn.close()

    def get_messages(self, group_id: int, user: dict[str, Any], limit: int = 80) -> list[dict[str, Any]]:
        if not self.ensure_tables():
            return []
        if not self.check_user_access(group_id, user.get("id"), user.get("rol")):
            return []
        conn = get_connection()
        if not conn:
            return []
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute(
                """
                SELECT m.id, m.group_id, m.sender_id,
                       COALESCE(m.message_text, m.message) AS message_text,
                       m.message_type, m.attachment_id, m.created_at,
                       u.nombre AS sender_name, LOWER(r.name) AS sender_role,
                       a.original_filename, a.file_path, a.mime_type, a.file_size
                FROM chat_messages m
                JOIN users u ON u.id = m.sender_id
                JOIN roles r ON r.id = u.role_id
                LEFT JOIN chat_attachments a ON a.id = m.attachment_id
                WHERE m.group_id = %s AND COALESCE(m.is_deleted, 0) = 0
                ORDER BY m.created_at DESC
                LIMIT %s
                """,
                (group_id, int(limit)),
            )
            return list(reversed(cursor.fetchall() or []))
        except Error as e:
            self.last_error = f"Error leyendo mensajes de chat: {e}"
            print(self.last_error)
            return []
        finally:
            cursor.close()
            conn.close()

    def send_message(self, group_id: int, sender_id: int, text: str, user: dict[str, Any]) -> tuple[bool, str]:
        if not self.ensure_tables():
            return False, self.last_error or "No se pudieron preparar las tablas del chat."
        text = (text or "").strip()
        if not text:
            return False, "Escribe un mensaje."
        if not self.check_user_access(group_id, sender_id, user.get("rol")):
            return False, "No tienes acceso a este grupo."
        return self._insert_message(group_id, sender_id, text, "text", None)

    def _insert_message(self, group_id: int, sender_id: int, text: str, message_type: str, attachment_id: int | None) -> tuple[bool, str]:
        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar con la base de datos."
        cursor = conn.cursor()
        legacy_text = text or ("Archivo adjunto" if attachment_id else "")
        try:
            cursor.execute(
                """
                INSERT INTO chat_messages (
                    group_id, sender_id, receiver_id, message, message_text, message_type, attachment_id, created_at, is_deleted
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), 0)
                """,
                (group_id, sender_id, sender_id, legacy_text, text, message_type, attachment_id),
            )
            message_id = cursor.lastrowid
            if attachment_id:
                cursor.execute("UPDATE chat_attachments SET message_id = %s WHERE id = %s", (message_id, attachment_id))
            conn.commit()
            return True, "Mensaje enviado." if not attachment_id else "Archivo enviado."
        except Error as e:
            conn.rollback()
            self.last_error = f"Error guardando mensaje: {e}"
            return False, self.last_error
        finally:
            cursor.close()
            conn.close()

    def send_file_message(self, group_id: int, sender_id: int, source_path: str, text: str, user: dict[str, Any]) -> tuple[bool, str]:
        if not self.ensure_tables():
            return False, self.last_error or "No se pudieron preparar las tablas del chat."
        if not self.check_user_access(group_id, sender_id, user.get("rol")):
            return False, "No tienes acceso a este grupo."
        if not source_path or not os.path.exists(source_path):
            return False, "No se pudo leer el archivo seleccionado."

        original = os.path.basename(source_path)
        safe_original = "".join(ch for ch in original if ch.isalnum() or ch in (" ", ".", "_", "-")).strip() or "archivo"
        _, ext = os.path.splitext(safe_original)
        stored = f"chat_{uuid.uuid4().hex}{ext.lower()}"
        os.makedirs(self.upload_dir, exist_ok=True)
        dest = os.path.join(self.upload_dir, stored)
        shutil.copy2(source_path, dest)

        mime_type = mimetypes.guess_type(safe_original)[0] or "application/octet-stream"
        file_size = os.path.getsize(dest)
        file_path = f"{self.asset_prefix}/{stored}".replace("\\", "/")
        message_type = "image" if mime_type.startswith("image/") else "file"

        conn = get_connection()
        if not conn:
            return False, "No se pudo conectar con la base de datos."
        cursor = conn.cursor()
        legacy_text = (text or "").strip() or safe_original
        try:
            cursor.execute(
                """
                INSERT INTO chat_attachments (
                    original_filename, stored_filename, file_path, mime_type, file_size, uploaded_by, uploaded_at
                )
                VALUES (%s, %s, %s, %s, %s, %s, NOW())
                """,
                (safe_original, stored, file_path, mime_type, file_size, sender_id),
            )
            attachment_id = cursor.lastrowid
            cursor.execute(
                """
                INSERT INTO chat_messages (
                    group_id, sender_id, receiver_id, message, message_text, message_type, attachment_id, created_at, is_deleted
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, NOW(), 0)
                """,
                (group_id, sender_id, sender_id, legacy_text, (text or "").strip(), message_type, attachment_id),
            )
            message_id = cursor.lastrowid
            cursor.execute("UPDATE chat_attachments SET message_id = %s WHERE id = %s", (message_id, attachment_id))
            conn.commit()
            return True, "Archivo enviado."
        except Error as e:
            conn.rollback()
            return False, f"Error guardando adjunto: {e}"
        finally:
            cursor.close()
            conn.close()
