-- Tannhäuser - Sprint 1
-- Base de datos MySQL 8.0
-- Diseñada a partir del proyecto actual en JSON/Flet y del nuevo backlog

DROP DATABASE IF EXISTS tannhauser;
CREATE DATABASE tannhauser CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE tannhauser;

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS camera_events;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS state_history;
DROP TABLE IF EXISTS current_state;
DROP TABLE IF EXISTS readings;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS activity_log;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS devices;
DROP TABLE IF EXISTS sensor_types;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS roles;

SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE roles (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(30) NOT NULL UNIQUE,
    name VARCHAR(60) NOT NULL,
    description VARCHAR(255) NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE users (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    role_id BIGINT UNSIGNED NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_users_role FOREIGN KEY (role_id) REFERENCES roles(id)
) ENGINE=InnoDB;

CREATE TABLE sensor_types (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(40) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    unit VARCHAR(20) NULL,
    category ENUM('ambiental','seguridad','consumo','estado','camara','otro') NOT NULL DEFAULT 'otro',
    description VARCHAR(255) NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE devices (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    device_code VARCHAR(50) NOT NULL UNIQUE,
    device_name VARCHAR(120) NOT NULL,
    sensor_type_id BIGINT UNSIGNED NULL,
    location_name VARCHAR(120) NULL,
    pin_or_channel VARCHAR(40) NULL,
    status ENUM('activo','mantenimiento','inactivo') NOT NULL DEFAULT 'activo',
    metadata JSON NULL,
    installed_at DATETIME NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_devices_sensor_type FOREIGN KEY (sensor_type_id) REFERENCES sensor_types(id)
) ENGINE=InnoDB;

CREATE TABLE readings (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    device_id BIGINT UNSIGNED NOT NULL,
    sensor_type_id BIGINT UNSIGNED NOT NULL,
    reading_value DECIMAL(10,2) NOT NULL,
    normalized_value DECIMAL(10,2) NULL,
    consumption_w DECIMAL(10,4) NULL,
    reading_unit VARCHAR(20) NULL,
    recorded_at DATETIME(6) NOT NULL,
    source ENUM('simulado','esp32','manual','importado') NOT NULL DEFAULT 'simulado',
    payload JSON NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_readings_device FOREIGN KEY (device_id) REFERENCES devices(id),
    CONSTRAINT fk_readings_sensor_type FOREIGN KEY (sensor_type_id) REFERENCES sensor_types(id),
    INDEX idx_readings_recorded_at (recorded_at),
    INDEX idx_readings_device_recorded_at (device_id, recorded_at),
    INDEX idx_readings_sensor_recorded_at (sensor_type_id, recorded_at)
) ENGINE=InnoDB;

CREATE TABLE current_state (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    device_id BIGINT UNSIGNED NOT NULL,
    state_code VARCHAR(50) NOT NULL,
    state_value VARCHAR(100) NOT NULL,
    numeric_value DECIMAL(10,2) NULL,
    updated_at DATETIME(6) NOT NULL,
    source ENUM('simulado','esp32','manual','sistema','importado') NOT NULL DEFAULT 'simulado',
    payload JSON NULL,
    CONSTRAINT fk_current_state_device FOREIGN KEY (device_id) REFERENCES devices(id),
    UNIQUE KEY uq_current_state_device_state (device_id, state_code),
    INDEX idx_current_state_updated_at (updated_at)
) ENGINE=InnoDB;

CREATE TABLE state_history (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    device_id BIGINT UNSIGNED NOT NULL,
    state_code VARCHAR(50) NOT NULL,
    old_value VARCHAR(100) NULL,
    new_value VARCHAR(100) NOT NULL,
    changed_at DATETIME(6) NOT NULL,
    event_type VARCHAR(50) NULL,
    source ENUM('simulado','esp32','manual','sistema','importado') NOT NULL DEFAULT 'simulado',
    payload JSON NULL,
    CONSTRAINT fk_state_history_device FOREIGN KEY (device_id) REFERENCES devices(id),
    INDEX idx_state_history_changed_at (changed_at),
    INDEX idx_state_history_device_changed_at (device_id, changed_at)
) ENGINE=InnoDB;

CREATE TABLE events (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NULL,
    device_id BIGINT UNSIGNED NULL,
    event_type VARCHAR(60) NOT NULL,
    severity ENUM('info','warning','critical') NOT NULL DEFAULT 'info',
    title VARCHAR(150) NOT NULL,
    description TEXT NULL,
    event_time DATETIME(6) NOT NULL,
    payload JSON NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_events_user FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_events_device FOREIGN KEY (device_id) REFERENCES devices(id),
    INDEX idx_events_time (event_time),
    INDEX idx_events_type_time (event_type, event_time)
) ENGINE=InnoDB;

CREATE TABLE camera_events (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    device_id BIGINT UNSIGNED NOT NULL,
    event_type VARCHAR(60) NOT NULL,
    file_path VARCHAR(255) NULL,
    mime_type VARCHAR(100) NULL,
    captured_at DATETIME(6) NOT NULL,
    notes VARCHAR(255) NULL,
    metadata JSON NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_camera_events_device FOREIGN KEY (device_id) REFERENCES devices(id),
    INDEX idx_camera_events_captured_at (captured_at),
    INDEX idx_camera_events_device_captured_at (device_id, captured_at)
) ENGINE=InnoDB;

CREATE TABLE products (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    sku VARCHAR(50) NULL UNIQUE,
    nombre VARCHAR(150) NOT NULL,
    cantidad INT NOT NULL DEFAULT 0,
    precio DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    is_active TINYINT(1) NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB;

CREATE TABLE activity_log (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NULL,
    log_level ENUM('INFO','WARNING','ERROR') NOT NULL DEFAULT 'INFO',
    action VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    logged_at DATETIME(6) NOT NULL,
    metadata JSON NULL,
    CONSTRAINT fk_activity_log_user FOREIGN KEY (user_id) REFERENCES users(id),
    INDEX idx_activity_log_logged_at (logged_at),
    INDEX idx_activity_log_action_logged_at (action, logged_at)
) ENGINE=InnoDB;

CREATE TABLE comments (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT UNSIGNED NULL,
    usuario_alias VARCHAR(100) NOT NULL,
    texto TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    CONSTRAINT fk_comments_user FOREIGN KEY (user_id) REFERENCES users(id),
    INDEX idx_comments_created_at (created_at)
) ENGINE=InnoDB;

-- ==============================
-- DATOS BASE DEL PROYECTO ACTUAL
-- ==============================

INSERT INTO roles (id, code, name, description) VALUES
(1, 'superusuario', 'Superusuario', 'Acceso total al sistema'),
(2, 'administrador', 'Administrador', 'Gestión operativa y administrativa'),
(3, 'cliente', 'Cliente', 'Usuario final del supermercado'),
(4, 'empleado', 'Empleado', 'Operación diaria e inventario');

INSERT INTO users (id, role_id, nombre, email, password_hash, is_active) VALUES
(1, 1, 'Superusuario', 'root@supermercado.com', 'root123', 1),
(2, 2, 'Administrador', 'admin@supermercado.com', 'admin123', 1),
(3, 3, 'Cliente', 'cliente@supermercado.com', 'cliente123', 1),
(5, 3, 'Arturo', 'arturo@clubpenguin.com', '123456', 1),
(6, 3, 'jesus', 'jesus@panda.com', 'panda1234', 1),
(7, 4, 'empleado', 'empleado@supermercado.com', 'empleado1', 1);

INSERT INTO sensor_types (id, code, name, unit, category, description) VALUES
(1, 'TEMP_AIR', 'Temperatura ambiente', 'C', 'ambiental', 'Lectura de temperatura del supermercado'),
(2, 'HUM_AIR', 'Humedad ambiente', '%', 'ambiental', 'Lectura de humedad relativa'),
(3, 'LIGHT_STATE', 'Estado de luz', 'ON/OFF', 'estado', 'Estado de iluminación'),
(4, 'FRIDGE_TEMP', 'Temperatura de nevera', 'C', 'ambiental', 'Temperatura en cámara frigorífica'),
(5, 'DOOR_STATE', 'Estado de puerta', 'abierta/cerrada', 'estado', 'Estado de la puerta de acceso'),
(6, 'MQ135_AIR', 'Calidad de aire MQ-135', 'indice', 'ambiental', 'Índice de calidad de aire'),
(7, 'CAM_EVENT', 'Evento de cámara', NULL, 'camara', 'Captura y eventos de cámara');

INSERT INTO devices (id, device_code, device_name, sensor_type_id, location_name, pin_or_channel, status, metadata) VALUES
(1, 'temp_01', 'Sensor temperatura principal', 1, 'Zona general', 'GPIO-DHT', 'activo', JSON_OBJECT('origen', 'json_actual')),
(2, 'hum_01', 'Sensor humedad principal', 2, 'Zona general', 'GPIO-DHT', 'activo', JSON_OBJECT('origen', 'json_actual')),
(3, 'light_01', 'Control de luces', 3, 'Tienda', 'GPIO-LDR', 'activo', JSON_OBJECT('origen', 'json_actual')),
(4, 'fridge_01', 'Sensor nevera', 4, 'Cámara frigorífica', 'GPIO-DHT22', 'activo', JSON_OBJECT('origen', 'json_actual')),
(5, 'door_01', 'Sensor puerta acceso', 5, 'Entrada principal', 'GPIO-HCSR04', 'activo', JSON_OBJECT('origen', 'json_actual')),
(6, 'mq135_01', 'Sensor calidad de aire', 6, 'Zona clientes', 'ADC1', 'activo', JSON_OBJECT('previsto_en_backlog', true)),
(7, 'cam_01', 'ESP32-CAM vigilancia', 7, 'Entrada principal', 'CAM', 'activo', JSON_OBJECT('previsto_en_backlog', true));

INSERT INTO products (id, sku, nombre, cantidad, precio) VALUES
(1, 'PROD-001', 'Leche Entera 1L', 30, 1.25),
(2, 'PROD-002', 'Pan Integral', 35, 0.90),
(3, 'PROD-003', 'Huevos (docena)', 10, 2.50);

INSERT INTO comments (user_id, usuario_alias, texto, created_at) VALUES
(NULL, 'Anónimo', 'Tetsed', '2026-01-09 14:04:00');

-- Lecturas reales importadas del proyecto actual (muestra útil para arrancar Sprint 1)
INSERT INTO readings (device_id, sensor_type_id, reading_value, normalized_value, consumption_w, reading_unit, recorded_at, source, payload) VALUES
(1, 1, 20.18, NULL, 0.4036, 'C', '2025-12-01 19:28:35.432192', 'importado', JSON_OBJECT('archivo', 'sensor_temperatura.json')),
(1, 1, 25.00, NULL, 0.5000, 'C', '2025-12-01 19:28:38.164948', 'importado', JSON_OBJECT('archivo', 'sensor_temperatura.json')),
(1, 1, 25.50, NULL, 0.5100, 'C', '2026-01-09 13:18:02.735684', 'importado', JSON_OBJECT('archivo', 'sensor_temperatura.json')),
(2, 2, 55.00, NULL, 1.1000, '%', '2025-11-29 11:04:15.393884', 'importado', JSON_OBJECT('archivo', 'sensor_humedad.json')),
(2, 2, 40.00, NULL, 0.8000, '%', '2025-11-29 11:04:20.446125', 'importado', JSON_OBJECT('archivo', 'sensor_humedad.json')),
(2, 2, 78.00, NULL, 1.5600, '%', '2025-11-29 11:04:25.517253', 'importado', JSON_OBJECT('archivo', 'sensor_humedad.json')),
(4, 4, -18.00, NULL, 1.8000, 'C', '2025-12-01 19:28:35.000000', 'simulado', JSON_OBJECT('archivo', 'sensor_nevera.json')),
(6, 6, 63.00, 63.00, NULL, 'indice', '2026-01-09 13:20:00.000000', 'simulado', JSON_OBJECT('nota', 'dato de arranque para Sprint 2'));

INSERT INTO current_state (device_id, state_code, state_value, numeric_value, updated_at, source, payload) VALUES
(3, 'light_power', 'ON', 1, '2026-01-09 13:18:00.000000', 'simulado', JSON_OBJECT('archivo', 'sensor_luz.json')),
(5, 'door_state', 'abierta', NULL, '2025-12-01 19:28:38.295094', 'importado', JSON_OBJECT('archivo', 'sensor_puerta.json'));

INSERT INTO state_history (device_id, state_code, old_value, new_value, changed_at, event_type, source, payload) VALUES
(5, 'door_state', 'cerrada', 'abierta', '2025-12-01 18:57:22.533696', 'entrada', 'importado', JSON_OBJECT('archivo', 'sensor_puerta.json')),
(5, 'door_state', 'abierta', 'cerrada', '2025-12-01 18:57:23.680742', 'salida', 'importado', JSON_OBJECT('archivo', 'sensor_puerta.json')),
(5, 'door_state', 'cerrada', 'abierta', '2025-12-01 19:28:35.545664', 'entrada', 'importado', JSON_OBJECT('archivo', 'sensor_puerta.json'));

INSERT INTO events (user_id, device_id, event_type, severity, title, description, event_time, payload) VALUES
(2, NULL, 'login_demo', 'info', 'Acceso de administrador', 'Evento de ejemplo alineado con la UI actual.', '2026-01-09 13:00:00.000000', JSON_OBJECT('origen', 'actividad.log')),
(NULL, 5, 'door_event', 'info', 'Movimiento en puerta', 'Apertura/cierre detectado desde sensor de puerta.', '2025-12-01 18:57:22.533696', JSON_OBJECT('evento', 'entrada'));

INSERT INTO activity_log (user_id, log_level, action, message, logged_at, metadata) VALUES
(2, 'INFO', 'login', 'Inicio de sesión correcto del administrador.', '2026-01-09 13:00:00.000000', JSON_OBJECT('archivo', 'actividad.log')),
(7, 'INFO', 'inventario', 'Consulta del inventario desde la aplicación.', '2026-01-09 13:05:00.000000', JSON_OBJECT('modulo', 'inventario'));

-- =====================
-- VISTAS ÚTILES SPRINT 1
-- =====================

CREATE OR REPLACE VIEW vw_ultimas_lecturas AS
SELECT
    d.device_code,
    d.device_name,
    st.code AS sensor_code,
    st.name AS sensor_name,
    r.reading_value,
    r.reading_unit,
    r.consumption_w,
    r.recorded_at
FROM readings r
JOIN devices d ON d.id = r.device_id
JOIN sensor_types st ON st.id = r.sensor_type_id
JOIN (
    SELECT device_id, MAX(recorded_at) AS max_recorded_at
    FROM readings
    GROUP BY device_id
) last_r ON last_r.device_id = r.device_id AND last_r.max_recorded_at = r.recorded_at;

CREATE OR REPLACE VIEW vw_estado_actual AS
SELECT
    d.device_code,
    d.device_name,
    cs.state_code,
    cs.state_value,
    cs.numeric_value,
    cs.updated_at
FROM current_state cs
JOIN devices d ON d.id = cs.device_id;

-- =============================
-- CONSULTAS DE COMPROBACIÓN RÁPIDA
-- =============================
-- SELECT * FROM vw_ultimas_lecturas;
-- SELECT * FROM vw_estado_actual;
-- SELECT nombre, email FROM users;
-- SELECT nombre, cantidad, precio FROM products;
-- SELECT event_type, title, event_time FROM events ORDER BY event_time DESC;

