#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

// =========================
// CONFIGURA TUS PINES
// =========================
#define DHT_PIN 4
#define DHT_TYPE DHT11

#define MQ135_PIN 36      // VP / GPIO36
#define TRIG_PIN 5
#define ECHO_PIN 18

// Pines RX/TX del nuevo sensor ordinario pedido en el ejercicio
#define ORDINARIO_RX_PIN 16
#define ORDINARIO_TX_PIN 17

// =========================
// CONFIGURA TU WIFI
// =========================
const char* ssid = "mikito";
const char* password = "xxxxxxx";

// IP DE TU PC, NO localhost
const char* serverUrl = "http://ippc/tannhauser/ingest_readings.php";

// Endpoint integrado en el backend FastAPI del proyecto para el sensor ordinario.
// Cambia IP_DE_TU_PC por la IP del ordenador donde se ejecute la API.
const char* ordinaryServerUrl = "http://IP_DE_TU_PC:8000/ingest/ordinary";

// =========================
// OBJETOS
// =========================
DHT dht(DHT_PIN, DHT_TYPE);
HardwareSerial SensorOrdinarioSerial(2);

// =========================
// VARIABLES GLOBALES
// =========================
float temperatura = 0.0;
float humedad = 0.0;
int calidadAire = 0;
float distanciaCm = 0.0;

// El sensor ordinario devuelve dos datos por lectura:
// 1) un valor numerico entero
// 2) un valor alfanumerico en formato char[]
struct DatosOrdinarios {
  int valorNumerico;
  char valorAlfanumerico[50];
};

// =========================
// WIFI
// =========================
void conectarWiFi() {
  Serial.println("======================================");
  Serial.println("Conectando la ESP32 a la red WiFi...");
  Serial.print("SSID: ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  int intentos = 0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    intentos++;

    if (intentos >= 40) {
      Serial.println();
      Serial.println("No se pudo conectar al WiFi. Reintentando...");
      WiFi.disconnect();
      delay(1000);
      WiFi.begin(ssid, password);
      intentos = 0;
    }
  }

  Serial.println();
  Serial.println("WiFi conectado correctamente");
  Serial.print("IP de la ESP32: ");
  Serial.println(WiFi.localIP());
  Serial.println("======================================");
}


// =========================
// SENSOR ORDINARIO
// =========================
void inicializarSensor(int pin_RX, int pin_TX) {
  // En una libreria real, esta funcion vendria implementada por el fabricante.
  // Para que el proyecto sea verificable y compilable, se inicializa el puerto
  // serie del sensor usando los pines RX/TX indicados en el enunciado.
  SensorOrdinarioSerial.begin(9600, SERIAL_8N1, pin_RX, pin_TX);
  Serial.print("Sensor ordinario inicializado. RX=");
  Serial.print(pin_RX);
  Serial.print(" TX=");
  Serial.println(pin_TX);
}

bool comprobarDatosDisponibles() {
  // Devuelve true cuando el sensor ha enviado datos por el puerto serie.
  return SensorOrdinarioSerial.available() > 0;
}

DatosOrdinarios leerDatosOrdinarios() {
  DatosOrdinarios datos;
  datos.valorNumerico = 0;
  strcpy(datos.valorAlfanumerico, "SIN_DATO");

  String trama = SensorOrdinarioSerial.readStringUntil('\n');
  trama.trim();

  // Formato esperado de trama: numero,texto
  // Ejemplo: 25,ESTADO_OK
  int separador = trama.indexOf(',');

  if (separador >= 0) {
    datos.valorNumerico = trama.substring(0, separador).toInt();
    String texto = trama.substring(separador + 1);
    texto.trim();
    texto.toCharArray(datos.valorAlfanumerico, sizeof(datos.valorAlfanumerico));
  } else if (trama.length() > 0) {
    // Si el sensor solo enviase texto, se guarda como dato alfanumerico
    // y el valor numerico queda a 0.
    trama.toCharArray(datos.valorAlfanumerico, sizeof(datos.valorAlfanumerico));
  }

  return datos;
}

String escaparJson(const char* texto) {
  String salida = "";

  for (int i = 0; texto[i] != '\0'; i++) {
    char c = texto[i];

    if (c == '\"') {
      salida += "\\\"";
    } else if (c == '\\') {
      salida += "\\\\";
    } else if (c == '\n') {
      salida += "\\n";
    } else if (c == '\r') {
      salida += "\\r";
    } else {
      salida += c;
    }
  }

  return salida;
}

// Metodo pedido por el enunciado.
// Recibe los dos valores del sensor ordinario y los manda al backend para
// insertarlos en la base de datos del proyecto.
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

  Serial.print("Codigo HTTP sensor ordinario: ");
  Serial.println(httpCode);

  bool insertado = false;

  if (httpCode > 0) {
    String respuesta = http.getString();
    Serial.println("Respuesta del servidor:");
    Serial.println(respuesta);
    insertado = (httpCode >= 200 && httpCode < 300);
  } else {
    Serial.println("Error al enviar la lectura del sensor ordinario");
  }

  http.end();
  return insertado;
}

void leerSensorOrdinarioYGuardar() {
  if (!comprobarDatosDisponibles()) {
    Serial.println("Sensor ordinario: no hay datos disponibles");
    return;
  }

  DatosOrdinarios datos = leerDatosOrdinarios();

  Serial.println("===== LECTURA SENSOR ORDINARIO =====");
  Serial.print("Valor numerico: ");
  Serial.println(datos.valorNumerico);
  Serial.print("Valor alfanumerico: ");
  Serial.println(datos.valorAlfanumerico);

  if (DataBaseInsert(datos.valorNumerico, datos.valorAlfanumerico)) {
    Serial.println("Sensor ordinario guardado correctamente en BBDD");
  } else {
    Serial.println("No se pudo guardar el sensor ordinario en BBDD");
  }
}

// =========================
// LECTURA DHT11
// =========================
bool leerDHT11() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();

  if (isnan(t) || isnan(h)) {
    return false;
  }

  temperatura = t;
  humedad = h;
  return true;
}

// =========================
// LECTURA MQ-135
// =========================
void leerMQ135() {
  calidadAire = analogRead(MQ135_PIN);
}

// =========================
// LECTURA HC-SR04
// =========================
bool leerHCSR04() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duracion = pulseIn(ECHO_PIN, HIGH, 30000); // timeout 30ms

  if (duracion == 0) {
    return false;
  }

  distanciaCm = duracion * 0.0343 / 2.0;
  return true;
}

// =========================
// ENVÍO HTTP A PHP
// =========================
void enviarDatos(bool dhtOk, bool distOk) {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi no conectado. Intentando reconectar...");
    conectarWiFi();
  }

  HTTPClient http;
  http.begin(serverUrl);
  http.addHeader("Content-Type", "application/json");

  String json = "{";
  json += "\"temperatura\":";
  json += dhtOk ? String(temperatura, 2) : "null";
  json += ",";
  json += "\"humedad\":";
  json += dhtOk ? String(humedad, 2) : "null";
  json += ",";
  json += "\"calidad_aire\":";
  json += String(calidadAire);
  json += ",";
  json += "\"distancia_cm\":";
  json += distOk ? String(distanciaCm, 2) : "null";
  json += "}";

  Serial.println("Enviando JSON al servidor:");
  Serial.println(json);

  int httpCode = http.POST(json);

  Serial.print("Codigo HTTP: ");
  Serial.println(httpCode);

  if (httpCode > 0) {
    String respuesta = http.getString();
    Serial.println("Respuesta del servidor:");
    Serial.println(respuesta);
  } else {
    Serial.println("Error al enviar la petición HTTP");
  }

  http.end();
}

// =========================
// SETUP
// =========================
void setup() {
  Serial.begin(115200);
  delay(1000);

  dht.begin();

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  inicializarSensor(ORDINARIO_RX_PIN, ORDINARIO_TX_PIN);

  conectarWiFi();

  Serial.println("Sistema iniciado correctamente");
}

// =========================
// LOOP
// =========================
void loop() {
  bool dhtOk = leerDHT11();
  leerMQ135();
  bool distOk = leerHCSR04();

  Serial.println("===== LECTURA DE SENSORES =====");

  if (dhtOk) {
    Serial.print("Temperatura: ");
    Serial.print(temperatura, 2);
    Serial.println(" C");

    Serial.print("Humedad: ");
    Serial.print(humedad, 2);
    Serial.println(" %");
  } else {
    Serial.println("Temperatura: error");
    Serial.println("Humedad: error");
  }

  Serial.print("Calidad del aire (valor analógico): ");
  Serial.println(calidadAire);

  if (distOk) {
    Serial.print("Distancia HC-SR04: ");
    Serial.print(distanciaCm, 2);
    Serial.println(" cm");
  } else {
    Serial.println("Distancia HC-SR04: error");
  }

  leerSensorOrdinarioYGuardar();

  enviarDatos(dhtOk, distOk);

  Serial.println();
  delay(5000); // cada 5 segundos
}