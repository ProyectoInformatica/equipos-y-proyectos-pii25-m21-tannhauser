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

// IP DE TU PC, NO localhost
const char* serverUrl = "http://ippc/tannhauser/ingest_readings.php";

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

  Serial.println();
  delay(5000); // cada 5 segundos
}