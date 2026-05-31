CREATE TABLE IF NOT EXISTS chat_groups (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    name VARCHAR(120) NOT NULL,
    description VARCHAR(255) DEFAULT NULL,
    created_by BIGINT UNSIGNED NOT NULL,
    created_by_role VARCHAR(40) DEFAULT NULL,
    avatar_path VARCHAR(500) DEFAULT NULL,
    avatar_filename VARCHAR(255) DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS chat_group_members (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    group_id BIGINT UNSIGNED NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    role_in_group VARCHAR(40) NOT NULL DEFAULT 'member',
    nickname VARCHAR(100) DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS chat_messages (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    group_id BIGINT UNSIGNED DEFAULT NULL,
    sender_id BIGINT UNSIGNED NOT NULL,
    receiver_id BIGINT UNSIGNED DEFAULT NULL,
    message TEXT DEFAULT NULL,
    message_text TEXT DEFAULT NULL,
    message_type VARCHAR(30) NOT NULL DEFAULT 'text',
    poll_id BIGINT UNSIGNED DEFAULT NULL,
    attachment_id BIGINT UNSIGNED DEFAULT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_deleted TINYINT(1) NOT NULL DEFAULT 0,
    deleted_by BIGINT UNSIGNED DEFAULT NULL,
    deleted_at DATETIME DEFAULT NULL,
    PRIMARY KEY (id),
    KEY idx_chat_messages_group_created (group_id, created_at),
    KEY idx_chat_messages_sender (sender_id),
    KEY idx_chat_messages_poll (poll_id),
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS chat_polls (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    group_id BIGINT UNSIGNED NOT NULL,
    question VARCHAR(255) NOT NULL,
    created_by BIGINT UNSIGNED NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    PRIMARY KEY (id),
    KEY idx_chat_polls_group (group_id),
    CONSTRAINT fk_chat_polls_group
        FOREIGN KEY (group_id) REFERENCES chat_groups(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_chat_polls_created_by
        FOREIGN KEY (created_by) REFERENCES users(id)
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS chat_poll_options (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    poll_id BIGINT UNSIGNED NOT NULL,
    option_text VARCHAR(180) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_chat_poll_options_poll (poll_id),
    CONSTRAINT fk_chat_poll_options_poll
        FOREIGN KEY (poll_id) REFERENCES chat_polls(id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS chat_poll_votes (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    poll_id BIGINT UNSIGNED NOT NULL,
    option_id BIGINT UNSIGNED NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    voted_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_chat_poll_vote (poll_id, user_id),
    KEY idx_chat_poll_votes_option (option_id),
    CONSTRAINT fk_chat_poll_votes_poll
        FOREIGN KEY (poll_id) REFERENCES chat_polls(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_chat_poll_votes_option
        FOREIGN KEY (option_id) REFERENCES chat_poll_options(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_chat_poll_votes_user
        FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS chat_user_clears (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    group_id BIGINT UNSIGNED NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    cleared_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_chat_user_clear (group_id, user_id),
    KEY idx_chat_user_clears_user (user_id),
    CONSTRAINT fk_chat_user_clears_group
        FOREIGN KEY (group_id) REFERENCES chat_groups(id)
        ON DELETE CASCADE,
    CONSTRAINT fk_chat_user_clears_user
        FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Si las tablas ya existian desde una version anterior, aplica solo las lineas
-- que correspondan a columnas o indices que falten. El manager de Python hace
-- esta adaptacion automaticamente al abrir el chat.
--
-- ALTER TABLE chat_groups ADD COLUMN created_by_role VARCHAR(40) DEFAULT NULL AFTER created_by;
-- ALTER TABLE chat_groups ADD COLUMN avatar_path VARCHAR(500) DEFAULT NULL AFTER created_by_role;
-- ALTER TABLE chat_groups ADD COLUMN avatar_filename VARCHAR(255) DEFAULT NULL AFTER avatar_path;
-- ALTER TABLE chat_groups ADD COLUMN group_type VARCHAR(30) NOT NULL DEFAULT 'group' AFTER created_by_role;
-- ALTER TABLE chat_groups ADD COLUMN is_direct TINYINT(1) NOT NULL DEFAULT 0 AFTER group_type;
-- ALTER TABLE chat_groups ADD COLUMN direct_key VARCHAR(190) DEFAULT NULL AFTER is_direct;
-- ALTER TABLE chat_groups ADD UNIQUE KEY uq_chat_direct_key (direct_key);
-- ALTER TABLE chat_group_members ADD COLUMN nickname VARCHAR(100) DEFAULT NULL AFTER role_in_group;
--
-- ALTER TABLE chat_messages ADD COLUMN group_id BIGINT UNSIGNED DEFAULT NULL AFTER id;
-- ALTER TABLE chat_messages MODIFY receiver_id BIGINT UNSIGNED DEFAULT NULL;
-- ALTER TABLE chat_messages MODIFY message TEXT DEFAULT NULL;
-- ALTER TABLE chat_messages ADD COLUMN message_text TEXT DEFAULT NULL AFTER message;
-- ALTER TABLE chat_messages ADD COLUMN message_type VARCHAR(30) NOT NULL DEFAULT 'text' AFTER message_text;
-- ALTER TABLE chat_messages ADD COLUMN poll_id BIGINT UNSIGNED DEFAULT NULL AFTER message_type;
-- ALTER TABLE chat_messages ADD COLUMN attachment_id BIGINT UNSIGNED DEFAULT NULL AFTER message_type;
-- ALTER TABLE chat_messages ADD COLUMN is_deleted TINYINT(1) NOT NULL DEFAULT 0 AFTER created_at;
-- ALTER TABLE chat_messages ADD COLUMN deleted_by BIGINT UNSIGNED DEFAULT NULL AFTER is_deleted;
-- ALTER TABLE chat_messages ADD COLUMN deleted_at DATETIME DEFAULT NULL AFTER deleted_by;
-- ALTER TABLE chat_messages ADD KEY idx_chat_messages_group_created (group_id, created_at);
-- ALTER TABLE chat_messages ADD KEY idx_chat_messages_poll (poll_id);
-- ALTER TABLE chat_messages ADD KEY idx_chat_messages_attachment (attachment_id);
