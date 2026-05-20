USE tannhauser;

CREATE TABLE IF NOT EXISTS biodinario_readings (
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    device_id BIGINT UNSIGNED NOT NULL,
    dato_numerico INT NOT NULL,
    dato_alfanumerico VARCHAR(100) NOT NULL,
    recorded_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    source ENUM('simulado','esp32','manual','sistema','importado') NOT NULL DEFAULT 'esp32',
    payload JSON DEFAULT NULL,
    PRIMARY KEY (id),
    KEY idx_biodinario_recorded_at (recorded_at),
    KEY idx_biodinario_device (device_id),
    CONSTRAINT fk_biodinario_device
        FOREIGN KEY (device_id) REFERENCES devices(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO sensor_types (
    code,
    name,
    unit,
    category,
    description,
    created_at
)
SELECT
    'BIODINARIO',
    'Sensor biodinario',
    'num/text',
    'estado',
    'Sensor de checkpoint que recoge un dato numérico y otro alfanumérico',
    NOW()
WHERE NOT EXISTS (
    SELECT 1 FROM sensor_types WHERE code = 'BIODINARIO'
);

INSERT INTO devices (
    device_code,
    device_name,
    sensor_type_id,
    location_name,
    pin_or_channel,
    status,
    metadata,
    installed_at,
    is_active
)
SELECT
    'biodinario_01',
    'Sensor biodinario checkpoint',
    st.id,
    'Zona checkpoint',
    'RX/TX',
    'activo',
    JSON_OBJECT('origen', 'checkpoint', 'tipo', 'biodinario'),
    NOW(),
    1
FROM sensor_types st
WHERE st.code = 'BIODINARIO'
AND NOT EXISTS (
    SELECT 1 FROM devices WHERE device_code = 'biodinario_01'
);