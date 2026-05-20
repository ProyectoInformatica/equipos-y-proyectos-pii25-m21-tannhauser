# Respuesta final — Sensor ordinario para Proyecto Tannhäuser

## Qué se ha implementado

Se ha adaptado el proyecto para añadir un nuevo **sensor ordinario** que genera dos valores por lectura:

- `numeric_value`: dato numérico, por ejemplo `25`.
- `text_value`: dato alfanumérico, por ejemplo `ESTADO_OK`.

La solución cubre los 4 puntos del ejercicio:

1. Método Arduino `DataBaseInsert()` que recibe los dos valores del sensor y los envía a la BBDD mediante HTTP.
2. Adaptación de la base de datos para guardar una lectura mixta numérica + alfanumérica.
3. Endpoint de backend para recibir los datos y guardarlos.
4. Código Arduino que inicializa el sensor, comprueba si hay datos, los lee y llama a `DataBaseInsert()`.

---

# 1. Adaptación de la base de datos

Archivo incluido:

```text
BaseDeDatos/adaptacion_sensor_ordinario.sql
```

Cambios realizados:

```sql
ALTER TABLE readings
  ADD COLUMN text_value VARCHAR(100) NULL AFTER reading_value,
  ADD COLUMN reading_kind ENUM('numerico','texto','mixto') NOT NULL DEFAULT 'numerico' AFTER reading_unit;
```

Con esto, la tabla `readings` puede seguir guardando sensores antiguos y, además, guardar el sensor ordinario con los dos valores en la misma fila.

También se añade el tipo de sensor:

```sql
INSERT INTO sensor_types (code, name, unit, category, description)
SELECT 'ORDINARY_SENSOR',
       'Sensor ordinario',
       NULL,
       'otro',
       'Sensor ordinario que recoge un dato numérico y un dato alfanumérico'
WHERE NOT EXISTS (
  SELECT 1 FROM sensor_types WHERE code = 'ORDINARY_SENSOR'
);
```

Y el dispositivo físico:

```sql
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
  JSON_OBJECT('sensor_name', 'sensor_ordinario'),
  NOW()
FROM sensor_types st
WHERE st.code = 'ORDINARY_SENSOR'
  AND NOT EXISTS (
    SELECT 1 FROM devices WHERE device_code = 'ordinary_01'
  );
```

---

# 2. Método Arduino pedido: `DataBaseInsert()`

Archivo incluido:

```text
Arduino/SketchSensorOrdinario_Tannhauser.ino
```

Método principal:

```cpp
bool DataBaseInsert(int valorNumerico, const char valorAlfanumerico[]) {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi no conectado. Intentando reconectar...");
    conectarWiFi();
  }

  HTTPClient http;
  http.begin(ordinaryServerUrl);
  http.addHeader("Content-Type", "application/json");

  String json = "{";
  json += "\"numeric_value\":";
  json += String(valorNumerico);
  json += ",";
  json += "\"text_value\":\"";
  json += escaparJson(valorAlfanumerico);
  json += "\",";
  json += "\"source\":\"esp32\"";
  json += "}";

  Serial.println("Enviando lectura del sensor ordinario:");
  Serial.println(json);

  int httpCode = http.POST(json);
  Serial.print("Código HTTP: ");
  Serial.println(httpCode);

  bool insertado = false;

  if (httpCode > 0) {
    String respuesta = http.getString();
    Serial.println("Respuesta del servidor:");
    Serial.println(respuesta);

    insertado = (httpCode >= 200 && httpCode < 300);
  } else {
    Serial.println("Error al enviar la petición HTTP del sensor ordinario");
  }

  http.end();
  return insertado;
}
```

---

# 3. Código Arduino que lee el sensor ordinario y lo guarda

En `setup()` se inicializa el sensor:

```cpp
inicializarSensor(ORDINARIO_RX_PIN, ORDINARIO_TX_PIN);
```

En el `loop()` se llama a:

```cpp
leerSensorOrdinarioYGuardar();
```

La función hace exactamente lo que pide el enunciado:

```cpp
void leerSensorOrdinarioYGuardar() {
  if (!comprobarDatosDisponibles()) {
    Serial.println("Sensor ordinario: no hay datos disponibles");
    return;
  }

  DatosOrdinarios datos = leerDatosOrdinarios();

  Serial.println("===== LECTURA SENSOR ORDINARIO =====");
  Serial.print("Valor numérico: ");
  Serial.println(datos.valorNumerico);
  Serial.print("Valor alfanumérico: ");
  Serial.println(datos.valorAlfanumerico);

  bool ok = DataBaseInsert(datos.valorNumerico, datos.valorAlfanumerico);

  if (ok) {
    Serial.println("Sensor ordinario guardado correctamente en BBDD");
  } else {
    Serial.println("No se pudo guardar el sensor ordinario en BBDD");
  }
}
```

---

# 4. Backend FastAPI añadido al proyecto

Archivos incluidos:

```text
Backend/api.py
Backend/sensor_data_manager.py
```

Se ha añadido el modelo de entrada:

```python
class OrdinaryReadingIn(BaseModel):
    numeric_value: int | float
    text_value: str
    source: Optional[str] = "esp32"
```

Y el endpoint:

```python
@app.post("/ingest/ordinary")
def ingest_ordinary_reading(reading: OrdinaryReadingIn):
    try:
        sensor_manager.guardar_lectura_sensor_ordinario(
            valor_numerico=reading.numeric_value,
            valor_alfanumerico=reading.text_value,
            source=reading.source or "esp32"
        )

        return {
            "status": "ok",
            "message": "Lectura del sensor ordinario guardada correctamente",
            "data": {
                "sensor_name": "sensor_ordinario",
                "numeric_value": reading.numeric_value,
                "text_value": reading.text_value,
                "source": reading.source or "esp32"
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": "No se pudo guardar la lectura del sensor ordinario",
            "details": str(e)
        }
```

En `sensor_data_manager.py` se ha añadido el método:

```python
def guardar_lectura_sensor_ordinario(self, valor_numerico, valor_alfanumerico: str, source: str = "esp32"):
```

Este método:

1. Asegura que exista el sensor ordinario en `sensor_types` y `devices`.
2. Inserta la lectura mixta en `readings`.
3. Guarda el valor numérico en `reading_value`.
4. Guarda el valor alfanumérico en `text_value`.
5. Marca la lectura como `reading_kind = 'mixto'`.
6. Actualiza `current_state` con el último valor numérico y el último valor alfanumérico.

---

# 5. Alternativa PHP para XAMPP

También se incluye un endpoint opcional:

```text
Backend_PHP_XAMPP/ingest_ordinary.php
```

Se puede usar si se prefiere mantener la ruta estilo XAMPP/PHP del Arduino.

En ese caso, en Arduino habría que poner:

```cpp
const char* ordinaryServerUrl = "http://IP_DE_TU_PC/tannhauser/ingest_ordinary.php";
```

---

# 6. Qué tendría que entregar

Para entregar el ejercicio, lo importante es enseñar estos tres bloques:

1. `adaptacion_sensor_ordinario.sql`
2. `DataBaseInsert()` en Arduino
3. Lectura del sensor ordinario con:

```cpp
inicializarSensor(ORDINARIO_RX_PIN, ORDINARIO_TX_PIN);
comprobarDatosDisponibles();
leerDatosOrdinarios();
DataBaseInsert(datos.valorNumerico, datos.valorAlfanumerico);
```

Con eso queda cubierta la implementación completa pedida en el enunciado.
