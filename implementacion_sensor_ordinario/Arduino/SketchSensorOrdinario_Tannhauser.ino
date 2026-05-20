#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>

// =======================================================
// PROYECTO TANNHÄUSER - SENSOR ORDINARIO
// El nuevo sensor devuelve 2 datos: int + char[]
// =======================================================

// Si la librería real del sensor ordinario existe, se incluiría aquí:
// #include <SensorOrdinario.h>

// =========================
// CONFIGURACIÓN DE PINES
// =========================
#define DHT_PIN 4
#define DHT_TYPE DHT11

#define MQ135_PIN 36
#define TRIG_PIN 5
#define ECHO_PIN 18

// Pines del nuevo sensor ordinario
#define ORDINARIO_RX_PIN 16
#define ORDINARIO_TX_PIN 17

// =========================
// CONFIGURACIÓN WIFI / API
// =========================
const char* ssid = "mikito";
const char* password = "xxxxxxx";

// Sustituir IP_DE_TU_PC por la IP real del ordenador donde corre FastAPI.
// Ejemplo: http://192.168.1.45:8000/ingest/ordinary
const char* ordinaryServerUrl = "http://IP_DE_TU_PC:8000/ingest/ordinary";

// Si mantienes el envío anterior de sensores, deja también tu endpoint anterior:
const char* serverUrl = "http://IP_DE_TU_PC:8000/ingest/readings/batch";

// =========================
// OBJETOS
// =========================
DHT dht(DHT_PIN, DHT_TYPE);

// =========================
// VARIABLES GLOBALES
// =========================
float temperatura = 0.0;
float humedad = 0.0;
int calidadAire = 0;
float distanciaCm = 0.0;

// La librería del enunciado indica que leerDatosOrdinarios()
// devuelve un array con 2 datos: int y char[].
// En Arduino/C++ se representa de forma segura con una estructura.
struct DatosOrdinarios {
  int valorNumerico;
  char valorAlfanumerico[50];
};

// =======================================================
// FUNCIONES DE LA LIBRERÍA DEL SENSOR ORDINARIO
// En el proyecto real estas funciones vendrían de la librería.
// Se dejan declaradas para reflejar exactamente el enunciado.
// =======================================================
void inicializarSensor(int pin_RX, int pin_TX);
bool comprobarDatosDisponibles();
DatosOrdinarios leerDatosOrdinarios();

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
// UTILIDAD PARA JSON
// =========================
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

// =======================================================
// MÉTODO PEDIDO EN EL ENUNCIADO
// Recibe los valores generados por el sensor ordinario y
// los envía a la BBDD del proyecto mediante la API.
// =======================================================
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

// =======================================================
// LECTURA DEL SENSOR ORDINARIO Y ALMACENAMIENTO EN BBDD
// Usa las funciones indicadas por el enunciado:
// - comprobarDatosDisponibles()
// - leerDatosOrdinarios()
// - DataBaseInsert(...)
// =======================================================
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

  long duracion = pulseIn(ECHO_PIN, HIGH, 30000);

  if (duracion == 0) {
    return false;
  }

  distanciaCm = duracion * 0.0343 / 2.0;
  return true;
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

  conectarWiFi();

  // Inicialización pedida por el enunciado para el sensor ordinario
  inicializarSensor(ORDINARIO_RX_PIN, ORDINARIO_TX_PIN);

  Serial.println("Sistema Tannhäuser iniciado correctamente");
}

// =========================
// LOOP
// =========================
void loop() {
  bool dhtOk = leerDHT11();
  leerMQ135();
  bool distOk = leerHCSR04();

  Serial.println("===== LECTURA DE SENSORES EXISTENTES =====");

  if (dhtOk) {
    Serial.print("Temperatura: ");
    Serial.print(temperatura, 2);
    Serial.println(" C");

    Serial.print("Humedad: ");
    Serial.print(humedad, 2);
    Serial.println(" %");
  } else {
    Serial.println("Temperatura/Humedad: error");
  }

  Serial.print("Calidad del aire: ");
  Serial.println(calidadAire);

  if (distOk) {
    Serial.print("Distancia HC-SR04: ");
    Serial.print(distanciaCm, 2);
    Serial.println(" cm");
  } else {
    Serial.println("Distancia HC-SR04: error");
  }

  // Parte nueva del ejercicio: lectura + inserción del sensor ordinario
  leerSensorOrdinarioYGuardar();

  Serial.println();
  delay(5000);
}
