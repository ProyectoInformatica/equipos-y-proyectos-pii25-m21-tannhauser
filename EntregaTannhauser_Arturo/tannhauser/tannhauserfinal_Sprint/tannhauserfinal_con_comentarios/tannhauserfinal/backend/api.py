import sys
from pathlib import Path
from typing import Optional, List

from fastapi import FastAPI
from pydantic import BaseModel

# Añadir la raíz del proyecto al path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from models.db import get_connection
from models.sensor_data_manager import SensorDataManager

app = FastAPI(title="Tannhäuser API", version="1.0.0")

sensor_manager = SensorDataManager()


class ReadingIn(BaseModel):
    sensor_name: str
    # valor tradicional en `value`, o bien enviar `value_num`/`value_text` para lecturas compuestas
    value: Optional[str | float | int] = None
    value_num: Optional[float] = None
    value_text: Optional[str] = None
    source: Optional[str] = "esp32"


class BatchReadingItem(BaseModel):
    sensor_name: str
    value: str | float | int


class BatchReadingsIn(BaseModel):
    source: Optional[str] = "esp32"
    readings: List[BatchReadingItem]


@app.get("/")
def root():
    return {"message": "Tannhäuser API funcionando"}


@app.get("/health")
def health():
    conn = get_connection()

    if not conn:
        return {
            "status": "error",
            "database": "down",
            "details": "No se pudo conectar con MySQL"
        }

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db = cursor.fetchone()
        cursor.close()
        conn.close()

        return {
            "status": "ok",
            "database": "ok",
            "details": f"Conexión correcta con la base de datos: {db[0]}"
        }
    except Exception as e:
        try:
            conn.close()
        except Exception:
            pass

        return {
            "status": "error",
            "database": "down",
            "details": str(e)
        }


@app.post("/ingest/readings")
def ingest_reading(reading: ReadingIn):
    try:
        # Construir `valor` según el payload recibido
        if reading.value_num is not None or reading.value_text is not None:
            valor = {"num": reading.value_num, "text": reading.value_text}
        else:
            valor = reading.value

        sensor_manager.guardar_lectura_sensor(
            nombre_sensor=reading.sensor_name,
            valor=valor,
            source=reading.source or "esp32"
        )

        return {
            "status": "ok",
            "message": "Lectura recibida y guardada correctamente",
            "data": {
                "sensor_name": reading.sensor_name,
                "value": reading.value,
                "source": reading.source or "esp32"
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "message": "No se pudo guardar la lectura",
            "details": str(e)
        }


@app.post("/ingest/readings/batch")
def ingest_readings_batch(batch: BatchReadingsIn):
    try:
        for item in batch.readings:
            sensor_manager.guardar_lectura_sensor(
                nombre_sensor=item.sensor_name,
                valor=item.value,
                source=batch.source or "esp32"
            )

        return {
            "status": "ok",
            "message": "Lecturas por lote guardadas correctamente",
            "total": len(batch.readings),
            "source": batch.source or "esp32"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": "No se pudieron guardar las lecturas por lote",
            "details": str(e)
        }