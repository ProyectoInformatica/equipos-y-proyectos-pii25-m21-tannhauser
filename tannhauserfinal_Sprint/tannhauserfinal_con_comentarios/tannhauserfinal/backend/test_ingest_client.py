import requests

url = "http://127.0.0.1:8000/ingest/readings"

datos = [
    {"sensor_name": "sensor_temperatura", "value": 26.1, "source": "esp32"},
    {"sensor_name": "sensor_humedad", "value": 61, "source": "esp32"},
    {"sensor_name": "sensor_luz", "value": 82, "source": "esp32"},
    {"sensor_name": "sensor_nevera", "value": 3.8, "source": "esp32"},
    {"sensor_name": "sensor_puerta", "value": "abierta", "source": "esp32"},
]

for lectura in datos:
    respuesta = requests.post(url, json=lectura)
    print("Enviado:", lectura)
    print("Respuesta:", respuesta.status_code, respuesta.json())
    print("-" * 50)