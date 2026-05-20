<?php
header('Content-Type: application/json; charset=utf-8');

$host = '127.0.0.1';
$db   = 'tannhauser';
$user = 'root';
$pass = '';

$raw = file_get_contents('php://input');
$data = json_decode($raw, true);

if (!is_array($data)) {
    http_response_code(400);
    echo json_encode(['status' => 'error', 'message' => 'JSON no valido']);
    exit;
}

$numericValue = $data['numeric_value'] ?? null;
$textValue = $data['text_value'] ?? null;
$source = $data['source'] ?? 'esp32';

if (!is_numeric($numericValue) || $textValue === null) {
    http_response_code(400);
    echo json_encode(['status' => 'error', 'message' => 'Faltan numeric_value o text_value']);
    exit;
}

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8mb4", $user, $pass, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);

    $pdo->beginTransaction();

    $stmt = $pdo->prepare("SELECT id FROM sensor_types WHERE code = 'ORDINARY_SENSOR' LIMIT 1");
    $stmt->execute();
    $sensorType = $stmt->fetch();

    if (!$sensorType) {
        $stmt = $pdo->prepare("
            INSERT INTO sensor_types (code, name, unit, category, description)
            VALUES ('ORDINARY_SENSOR', 'Sensor ordinario', NULL, 'otro',
                    'Sensor ordinario que recoge un dato numerico y un dato alfanumerico')
        ");
        $stmt->execute();
        $sensorTypeId = (int)$pdo->lastInsertId();
    } else {
        $sensorTypeId = (int)$sensorType['id'];
    }

    $stmt = $pdo->prepare("SELECT id FROM devices WHERE device_code = 'ordinary_01' LIMIT 1");
    $stmt->execute();
    $device = $stmt->fetch();

    if (!$device) {
        $stmt = $pdo->prepare("
            INSERT INTO devices (
                device_code, device_name, sensor_type_id, location_name,
                pin_or_channel, status, metadata, installed_at
            ) VALUES (
                'ordinary_01', 'Sensor ordinario principal', :sensor_type_id, 'Zona general',
                'RX/TX', 'activo', :metadata, NOW()
            )
        ");
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
        'numeric_value' => (float)$numericValue,
        'text_value' => (string)$textValue
    ], JSON_UNESCAPED_UNICODE);

    $stmt = $pdo->prepare("
        INSERT INTO readings (
            device_id, sensor_type_id, reading_value, text_value, normalized_value,
            consumption_w, reading_unit, reading_kind, recorded_at, source, payload
        ) VALUES (
            :device_id, :sensor_type_id, :reading_value, :text_value, :normalized_value,
            NULL, NULL, 'mixto', NOW(6), :source, :payload
        )
    ");
    $stmt->execute([
        ':device_id' => $deviceId,
        ':sensor_type_id' => $sensorTypeId,
        ':reading_value' => (float)$numericValue,
        ':text_value' => (string)$textValue,
        ':normalized_value' => (float)$numericValue,
        ':source' => $source,
        ':payload' => $payload
    ]);

    $stmt = $pdo->prepare("
        INSERT INTO current_state (device_id, state_code, state_value, numeric_value, updated_at, source, payload)
        VALUES (:device_id, 'ordinario_num', :state_value, :numeric_value, NOW(6), :source, :payload)
        ON DUPLICATE KEY UPDATE
            state_value = VALUES(state_value),
            numeric_value = VALUES(numeric_value),
            updated_at = VALUES(updated_at),
            source = VALUES(source),
            payload = VALUES(payload)
    ");
    $stmt->execute([
        ':device_id' => $deviceId,
        ':state_value' => (string)$numericValue,
        ':numeric_value' => (float)$numericValue,
        ':source' => $source,
        ':payload' => $payload
    ]);

    $stmt = $pdo->prepare("
        INSERT INTO current_state (device_id, state_code, state_value, numeric_value, updated_at, source, payload)
        VALUES (:device_id, 'ordinario_txt', :state_value, NULL, NOW(6), :source, :payload)
        ON DUPLICATE KEY UPDATE
            state_value = VALUES(state_value),
            numeric_value = VALUES(numeric_value),
            updated_at = VALUES(updated_at),
            source = VALUES(source),
            payload = VALUES(payload)
    ");
    $stmt->execute([
        ':device_id' => $deviceId,
        ':state_value' => (string)$textValue,
        ':source' => $source,
        ':payload' => $payload
    ]);

    $pdo->commit();

    echo json_encode([
        'status' => 'ok',
        'message' => 'Lectura del sensor ordinario guardada correctamente',
        'numeric_value' => (float)$numericValue,
        'text_value' => (string)$textValue
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
?>
