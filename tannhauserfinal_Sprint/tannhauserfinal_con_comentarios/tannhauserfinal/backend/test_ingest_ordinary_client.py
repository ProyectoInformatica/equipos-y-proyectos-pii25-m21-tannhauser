import requests

url = "http://127.0.0.1:8000/ingest/ordinary"

lectura = {
    "numeric_value": 25,
    "text_value": "ESTADO_OK",
    "source": "esp32"
}

respuesta = requests.post(url, json=lectura)
print("Enviado:", lectura)
print("Codigo HTTP:", respuesta.status_code)
print("Respuesta:", respuesta.json())
