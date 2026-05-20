-- Migracion para integrar el sensor ordinario en una base de datos Tannhäuser ya creada.
-- Ejecutar en phpMyAdmin o MySQL Workbench sobre la BBDD tannhauser.

ALTER TABLE readings
  ADD COLUMN text_value VARCHAR(100) NULL AFTER reading_value,
  ADD COLUMN reading_kind ENUM('numerico','texto','mixto') NOT NULL DEFAULT 'numerico' AFTER reading_unit;

INSERT INTO sensor_types (code, name, unit, category, description)
SELECT 'ORDINARY_SENSOR',
       'Sensor ordinario',
       NULL,
       'otro',
       'Sensor ordinario que recoge un dato numerico y un dato alfanumerico'
WHERE NOT EXISTS (
  SELECT 1 FROM sensor_types WHERE code = 'ORDINARY_SENSOR'
);

INSERT INTO devices (
  device_code, device_name, sensor_type_id, location_name,
  pin_or_channel, status, metadata, installed_at
)
SELECT
  'ordinary_01',
  'Sensor ordinario principal',
  st.id,
  'Zona general',
  'RX/TX',
  'activo',
  JSON_OBJECT('sensor_name', 'sensor_ordinario'),
  NOW()
FROM sensor_types st
WHERE st.code = 'ORDINARY_SENSOR'
  AND NOT EXISTS (
    SELECT 1 FROM devices WHERE device_code = 'ordinary_01'
  );
