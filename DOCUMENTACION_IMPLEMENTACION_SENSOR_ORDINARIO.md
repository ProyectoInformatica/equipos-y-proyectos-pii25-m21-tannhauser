# Documentación de implementación — Sensor ordinario

## Objetivo

Se ha integrado en el proyecto Tannhäuser un nuevo sensor ordinario que devuelve dos datos por lectura: un dato numérico y un dato alfanumérico. La implementación permite leer esos valores desde Arduino/ESP32, enviarlos al backend y almacenarlos en la base de datos MySQL.

## Archivos principales modificados

- `SketchSensoresyWIfi_copy_20260430180503/SketchSensoresyWIfi_copy_20260430180503.ino`
- `tannhauserfinal_Sprint/tannhauserfinal_con_comentarios/tannhauserfinal/backend/api.py`
- `tannhauserfinal_Sprint/tannhauserfinal_con_comentarios/tannhauserfinal/models/sensor_data_manager.py`
- `tannhauser.sql`

## Base de datos

La tabla `readings` se ha ampliado con dos campos nuevos:

```sql
text_value VARCHAR(100) NULL
reading_kind ENUM('numerico','texto','mixto') NOT NULL DEFAULT 'numerico'
```

Con esto se pueden guardar lecturas mixtas, manteniendo compatibilidad con los sensores antiguos.

También se ha registrado el tipo de sensor `ORDINARY_SENSOR` y el dispositivo `ordinary_01`.

## Arduino

Se ha añadido el método pedido en el enunciado:

```cpp
bool DataBaseInsert(int valorNumerico, const char valorAlfanumerico[])
```

Este método construye un JSON con `numeric_value` y `text_value` y lo envía al endpoint `/ingest/ordinary`.

También se usan las funciones solicitadas:

```cpp
inicializarSensor(ORDINARIO_RX_PIN, ORDINARIO_TX_PIN);
comprobarDatosDisponibles();
leerDatosOrdinarios();
```

## Backend

Se ha añadido el endpoint:

```text
POST /ingest/ordinary
```

Ejemplo de JSON recibido:

```json
{
  "numeric_value": 25,
  "text_value": "ESTADO_OK",
  "source": "esp32"
}
```

El backend llama al método `guardar_lectura_sensor_ordinario()`, que inserta la lectura en `readings` y actualiza `current_state`.

## Comprobación rápida

Con la API ejecutándose, se puede probar con:

```bash
python tannhauserfinal_Sprint/tannhauserfinal_con_comentarios/tannhauserfinal/backend/test_ingest_ordinary_client.py
```

La respuesta esperada es un JSON con `status: ok`.
