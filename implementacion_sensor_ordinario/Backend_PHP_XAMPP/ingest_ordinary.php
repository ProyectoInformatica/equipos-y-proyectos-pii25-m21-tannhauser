<?php
/*
  Endpoint opcional para XAMPP/PHP.
  Recibe el JSON enviado por Arduino DataBaseInsert() y guarda
  el sensor ordinario en la BBDD tannhauser.

  URL ejemplo en Arduino:
  http://IP_DE_TU_PC/tannhauser/ingest_ordinary.php
*/

header('Content-Type: application/json; charset=utf-8');

$host = '127.0.0.1';
$db   = 'tannhauser';
$user = 'root';
$pass = '';
$charset = 'utf8mb4';

try {
    $pdo = new PDO(
        "mysql:host=$host;dbname=$db;charset=$charset",
        $user,
        $pass,
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
        ]
    );

    $raw = file_get_contents('php://input');
    $data = json_decode($raw, true);

    if (!is_array($data)) {
        throw new Exception('JSON no válido');
    }

    if (!isset($data['numeric_value']) || !isset($data['text_value'])) {
        throw new Exception('Faltan numeric_value o text_value');
    }

    $numericValue = (float)$data['numeric_value'];
    $textValue = substr(trim((string)$data['text_value']), 0, 100);
    $source = isset($data['source']) ? (string)$data['source'] : 'esp32';

    // La tabla readings solo acepta estos valores en el enum source.
    if (!in_array($source, ['simulado', 'esp32', 'manual', 'importado'], true)) {
        $source = 'esp32';
    }

    $pdo->beginTransaction();

    // 1) Asegurar tipo de sensor.
    $stmt = $pdo->prepare("SELECT id FROM sensor_types WHERE code = 'ORDINARY_SENSOR' LIMIT 1");
    $stmt->execute();
    $sensorType = $stmt->fetch();

    if (!$sensorType) {
        $stmt = $pdo->prepare("\n            INSERT INTO sensor_types (code, name, unit, category, description)\n            VALUES ('ORDINARY_SENSOR', 'Sensor ordinario', NULL, 'otro',\n                    'Sensor ordinario que recoge un dato numérico y un dato alfanumérico')\n        ");
        $stmt->execute();
        $sensorTypeId = (int)$pdo->lastInsertId();
    } else {
        $sensorTypeId = (int)$sensorType['id'];
    }

    // 2) Asegurar dispositivo.
    $stmt = $pdo->prepare("SELECT id FROM devices WHERE device_code = 'ordinary_01' LIMIT 1");
    $stmt->execute();
    $device = $stmt->fetch();

    if (!$device) {
        $stmt = $pdo->prepare("\n            INSERT INTO devices (\n                device_code, device_name, sensor_type_id, location_name,\n                pin_or_channel, status, metadata, installed_at\n            ) VALUES (\n                'ordinary_01', 'Sensor ordinario principal', :sensor_type_id, 'Zona general',\n                'RX/TX', 'activo', :metadata, NOW()\n            )\n        ");
        $stmt->execute([
            ':sensor_type_id' => $sensorTypeId,
            ':metadata' => json_encode(['sensor_name' => 'sensor_ordinario'], JSON_UNESCAPED_UNICODE)
        ]);
        $deviceId = (int)$pdo->lastInsertId();
    } else {
        $deviceId = (int)$device['id'];
    }

    $payload = json_encode([
        'sensor_name' => 'sensor_ordinario',
        'numeric_value' => $numericValue,
        'text_value' => $textValue
    ], JSON_UNESCAPED_UNICODE);

    // 3) Insertar la lectura mixta.
    $stmt = $pdo->prepare("\n        INSERT INTO readings (\n            device_id, sensor_type_id, reading_value, text_value, normalized_value,\n            consumption_w, reading_unit, reading_kind, recorded_at, source, payload\n        ) VALUES (\n            :device_id, :sensor_type_id, :reading_value, :text_value, :normalized_value,\n            NULL, NULL, 'mixto', NOW(6), :source, :payload\n        )\n    ");
    $stmt->execute([
        ':device_id' => $deviceId,
        ':sensor_type_id' => $sensorTypeId,
        ':reading_value' => $numericValue,
        ':text_value' => $textValue,
        ':normalized_value' => $numericValue,
        ':source' => $source,
        ':payload' => $payload
    ]);

    // 4) Actualizar estado actual numérico.
    $stmt = $pdo->prepare("\n        INSERT INTO current_state (device_id, state_code, state_value, numeric_value, updated_at, source, payload)\n        VALUES (:device_id, 'ordinario_num', :state_value, :numeric_value, NOW(6), :source, :payload)\n        ON DUPLICATE KEY UPDATE\n            state_value = VALUES(state_value),\n            numeric_value = VALUES(numeric_value),\n            updated_at = VALUES(updated_at),\n            source = VALUES(source),\n            payload = VALUES(payload)\n    ");
    $stmt->execute([
        ':device_id' => $deviceId,
        ':state_value' => (string)$numericValue,
        ':numeric_value' => $numericValue,
        ':source' => $source,
        ':payload' => $payload
    ]);

    // 5) Actualizar estado actual alfanumérico.
    $stmt = $pdo->prepare("\n        INSERT INTO current_state (device_id, state_code, state_value, numeric_value, updated_at, source, payload)\n        VALUES (:device_id, 'ordinario_txt', :state_value, NULL, NOW(6), :source, :payload)\n        ON DUPLICATE KEY UPDATE\n            state_value = VALUES(state_value),\n            numeric_value = VALUES(numeric_value),\n            updated_at = VALUES(updated_at),\n            source = VALUES(source),\n            payload = VALUES(payload)\n    ");
    $stmt->execute([
        ':device_id' => $deviceId,
        ':state_value' => $textValue,
        ':source' => $source,
        ':payload' => $payload
    ]);

    $pdo->commit();

    echo json_encode([
        'status' => 'ok',
        'message' => 'Lectura del sensor ordinario guardada correctamente',
        'numeric_value' => $numericValue,
        'text_value' => $textValue
    ], JSON_UNESCAPED_UNICODE);

} catch (Throwable $e) {
    if (isset($pdo) && $pdo->inTransaction()) {
        $pdo->rollBack();
    }

    http_response_code(500);
    echo json_encode([
        'status' => 'error',
        'message' => 'No se pudo guardar la lectura del sensor ordinario',
        'details' => $e->getMessage()
    ], JSON_UNESCAPED_UNICODE);
}
