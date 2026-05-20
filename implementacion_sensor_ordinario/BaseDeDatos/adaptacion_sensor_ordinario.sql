/*
  ADAPTACIÓN BBDD - SENSOR ORDINARIO
  Proyecto Tannhäuser

  Objetivo:
  Permitir registrar en una misma lectura los 2 datos del nuevo sensor ordinario:
  1) dato numérico
  2) dato alfanumérico
*/

USE tannhauser;

/* 1) La tabla readings ya almacena lecturas numéricas.
      Se amplía para guardar también el dato alfanumérico y marcar que la lectura es mixta. */
ALTER TABLE readings
  ADD COLUMN text_value VARCHAR(100) NULL AFTER reading_value,
  ADD COLUMN reading_kind ENUM('numerico','texto','mixto') NOT NULL DEFAULT 'numerico' AFTER reading_unit;

/* 2) Se registra el nuevo tipo de sensor dentro del catálogo general del sistema. */
INSERT INTO sensor_types (code, name, unit, category, description)
SELECT 'ORDINARY_SENSOR',
       'Sensor ordinario',
       NULL,
       'otro',
       'Sensor ordinario que recoge un dato numérico y un dato alfanumérico'
WHERE NOT EXISTS (
  SELECT 1 FROM sensor_types WHERE code = 'ORDINARY_SENSOR'
);

/* 3) Se registra el dispositivo físico asociado al nuevo sensor. */
INSERT INTO devices (
  device_code,
  device_name,
  sensor_type_id,
  location_name,
  pin_or_channel,
  status,
  metadata,
  installed_at
)
SELECT
  'ordinary_01',
  'Sensor ordinario principal',
  st.id,
  'Zona general',
  'RX/TX',
  'activo',
  JSON_OBJECT('sensor_name', 'sensor_ordinario', 'descripcion', 'Sensor mixto numérico/alfanumérico'),
  NOW()
FROM sensor_types st
WHERE st.code = 'ORDINARY_SENSOR'
  AND NOT EXISTS (
    SELECT 1 FROM devices WHERE device_code = 'ordinary_01'
  );

/* 4) Prueba opcional de inserción directa en BBDD.
      Se puede ejecutar para comprobar que la estructura acepta los 2 valores. */
INSERT INTO readings (
  device_id,
  sensor_type_id,
  reading_value,
  text_value,
  normalized_value,
  consumption_w,
  reading_unit,
  reading_kind,
  recorded_at,
  source,
  payload
)
SELECT
  d.id,
  st.id,
  25,
  'ESTADO_OK',
  25,
  NULL,
  NULL,
  'mixto',
  NOW(6),
  'esp32',
  JSON_OBJECT('sensor_name', 'sensor_ordinario', 'origen', 'prueba_sql')
FROM devices d
JOIN sensor_types st ON st.id = d.sensor_type_id
WHERE d.device_code = 'ordinary_01'
LIMIT 1;
