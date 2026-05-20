#!/usr/bin/env python3
"""
Simulador sencillo para `sensor_ordinario`.
Envía lecturas compuestas (value_num + value_text) al endpoint de ingestión.
"""
import time
import random
import argparse
import requests


def run(url: str, sensor_name: str, interval: float):
    print(f"Simulador sensor '{sensor_name}' -> POST {url} cada {interval}s")
    while True:
        num = random.randint(0, 1000)
        text = f"ID-{random.randint(100,999)}"
        payload = {
            "sensor_name": sensor_name,
            "value_num": num,
            "value_text": text,
            "source": "simulado"
        }

        try:
            resp = requests.post(url, json=payload, timeout=5)
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} -> {resp.status_code} {resp.text}")
        except Exception as e:
            print(f"Error enviando lectura: {e}")

        time.sleep(interval)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Simulador sensor_ordinario')
    p.add_argument('--url', default='http://127.0.0.1:8000/ingest/readings', help='Endpoint ingest')
    p.add_argument('--sensor', default='sensor_ordinario', help='Nombre del sensor')
    p.add_argument('--interval', type=float, default=5.0, help='Intervalo en segundos entre envíos')
    args = p.parse_args()

    run(args.url, args.sensor, args.interval)
