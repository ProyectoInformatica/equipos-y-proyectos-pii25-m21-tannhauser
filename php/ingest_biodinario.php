<?php
header('Content-Type: application/json; charset=utf-8');

$host = '127.0.0.1';
$dbname = 'tannhauser';
$user = 'miguelapp';
$pass = 'TuClave1234!';

function responder($ok, $mensaje, $extra = []) {
    echo json_encode(array_merge([
        'ok' => $ok,
        'mensaje' => $mensaje
    ], $extra), JSON_UNESCAPED_UNICODE);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    responder(false, 'Método no permitido. Usa POST.');
}

$raw = file_get_contents('php://input');
$data = json_decode($raw, true);

if (!$data) {
    responder(false, 'JSON no válido o cuerpo vacío.');
}

$datoNumerico = $data['dato_numerico'] ?? null;
$datoAlfanumerico = $data['dato_alfanumerico'] ?? null;

if ($datoNumerico === null || !is_numeric($datoNumerico)) {
    responder(false, 'Falta dato_numerico o no es numérico.');
}

if ($datoAlfanumerico === null || trim($datoAlfanumerico) === '') {
    responder(false, 'Falta dato_alfanumerico.');
}

$datoNumerico = (int)$datoNumerico;
$datoAlfanumerico = trim((string)$datoAlfanumerico);

try {
    $pdo = new PDO(
        "mysql:host=$host;dbname=$dbname;charset=utf8mb4",
        $user,
        $pass,
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION]
    );

    $stmtDevice = $pdo->prepare("
        SELECT id
        FROM devices
        WHERE device_code = 'biodinario_01'
        LIMIT 1
    ");
    $stmtDevice->execute();
    $device = $stmtDevice->fetch(PDO::FETCH_ASSOC);

    if (!$device) {
        responder(false, 'No existe biodinario_01. Ejecuta primero update_biodinario.sql.');
    }

    $stmtSensor = $pdo->prepare("
        SELECT id
        FROM sensor_types
        WHERE code = 'BIODINARIO'
        LIMIT 1
    ");
    $stmtSensor->execute();
    $sensor = $stmtSensor->fetch(PDO::FETCH_ASSOC);

    if (!$sensor) {
        responder(false, 'No existe BIODINARIO. Ejecuta primero update_biodinario.sql.');
    }

    $payload = json_encode([
        'device_code' => 'biodinario_01',
        'dato_numerico' => $datoNumerico,
        'dato_alfanumerico' => $datoAlfanumerico
    ], JSON_UNESCAPED_UNICODE);

    $insertBiodinario = $pdo->prepare("
        INSERT INTO biodinario_readings (
            device_id,
            dato_numerico,
            dato_alfanumerico,
            recorded_at,
            source,
            payload
        ) VALUES (
            :device_id,
            :dato_numerico,
            :dato_alfanumerico,
            NOW(6),
            'esp32',
            :payload
        )
    ");

    $insertBiodinario->execute([
        'device_id' => $device['id'],
        'dato_numerico' => $datoNumerico,
        'dato_alfanumerico' => $datoAlfanumerico,
        'payload' => $payload
    ]);

    $insertReading = $pdo->prepare("
        INSERT INTO readings (
            device_id,
            sensor_type_id,
            reading_value,
            normalized_value,
            consumption_w,
            reading_unit,
            recorded_at,
            source,
            payload
        ) VALUES (
            :device_id,
            :sensor_type_id,
            :reading_value,
            NULL,
            NULL,
            'num',
            NOW(6),
            'esp32',
            :payload
        )
    ");

    $insertReading->execute([
        'device_id' => $device['id'],
        'sensor_type_id' => $sensor['id'],
        'reading_value' => $datoNumerico,
        'payload' => $payload
    ]);

    $upsertState = $pdo->prepare("
        INSERT INTO current_state (
            device_id,
            state_code,
            state_value,
            numeric_value,
            updated_at,
            source,
            payload
        ) VALUES (
            :device_id,
            'BIODINARIO',
            :state_value,
            :numeric_value,
            NOW(6),
            'esp32',
            :payload
        )
        ON DUPLICATE KEY UPDATE
            state_value = VALUES(state_value),
            numeric_value = VALUES(numeric_value),
            updated_at = NOW(6),
            source = VALUES(source),
            payload = VALUES(payload)
    ");

    $upsertState->execute([
        'device_id' => $device['id'],
        'state_value' => $datoAlfanumerico,
        'numeric_value' => $datoNumerico,
        'payload' => $payload
    ]);

    responder(true, 'Lectura biodinaria insertada correctamente.', [
        'dato_numerico' => $datoNumerico,
        'dato_alfanumerico' => $datoAlfanumerico
    ]);

} catch (PDOException $e) {
    responder(false, 'Error de base de datos.', [
        'error' => $e->getMessage()
    ]);
}
?>