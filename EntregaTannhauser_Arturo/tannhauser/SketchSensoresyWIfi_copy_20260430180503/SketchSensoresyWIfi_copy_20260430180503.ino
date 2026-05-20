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

// =========================
// CONFIGURA TU WIFI
// =========================
const char* ssid = "mikito";
const char* password = "xxxxxxx";

// IP DE TU PC y puerto del backend (FastAPI por defecto usa 8000)
// Ejemplo: "http://192.168.1.100:8000/ingest/readings"
const char* serverUrl = "http://IP_DE_TU_PC:8000/ingest/readings";

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

  // Inicializar sensor ordinario (ejemplo RX=16, TX=17)
  initializeSensor(16, 17);

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

  enviarDatos(dhtOk, distOk);

  // Comprobar y leer sensor ordinario
  if (comprobarDatosDisponibles()) {
    int valorNumerico = 0;
    String valorTexto = "";
    leerDatosOrdinarios(valorNumerico, valorTexto);
    Serial.println("Sensor ordinario: leyendo datos disponibles...");
    Serial.print("Num: "); Serial.println(valorNumerico);
    Serial.print("Text: "); Serial.println(valorTexto);
    DatabaseInsert(valorNumerico, valorTexto);
  }

  Serial.println();
  delay(5000); // cada 5 segundos
}

// -------------------------
// Implementación sensor ordinario (simulación / wrapper)
// -------------------------
int ORD_RX_PIN = 16;
int ORD_TX_PIN = 17;

void initializeSensor(int pin_RX, int pin_TX) {
  ORD_RX_PIN = pin_RX;
  ORD_TX_PIN = pin_TX;
  // Aquí se podría inicializar Serial1 o la librería real del sensor
  Serial.printf("Sensor ordinario inicializado RX=%d TX=%d\n", pin_RX, pin_TX);
}

bool comprobarDatosDisponibles() {
  // Implementar chequeo real según la librería del sensor.
  // Por ahora simulamos que rara vez hay datos para no saturar el servidor.
  // Puedes reemplazar por: return Serial1.available() > 0; según hardware.
  static unsigned long lastMillis = 0;
  if (millis() - lastMillis > 15000) { // cada 15s
    lastMillis = millis();
    return true;
  }
  return false;
}

void leerDatosOrdinarios(int &numero, String &texto) {
  // Reemplazar por la llamada real a la librería del sensor.
  // Debe devolver un entero y una cadena (alfanumérica).
  numero = random(0, 1000); // simulación
  texto = "ID-" + String(random(100,999));
}

void DatabaseInsert(int numericValue, String textValue) {
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("WiFi no conectado. Intentando reconectar...");
    conectarWiFi();
  }

  HTTPClient http;
  http.begin(serverUrl);
  http.addHeader("Content-Type", "application/json");

  String json = "{";
  json += "\"sensor_name\":\"sensor_ordinario\",";
  json += "\"value_num\":" + String(numericValue);
  json += ",\"value_text\":\"" + textValue + "\"";
  json += "}";

  Serial.println("Enviando (DatabaseInsert) JSON al servidor:");
  Serial.println(json);

  int httpCode = http.POST(json);

  Serial.print("Codigo HTTP: ");
  Serial.println(httpCode);

  if (httpCode > 0) {
    String respuesta = http.getString();
    Serial.println("Respuesta del servidor:");
    Serial.println(respuesta);
  } else {
    Serial.println("Error al enviar la petición HTTP (DatabaseInsert)");
  }

  http.end();
}