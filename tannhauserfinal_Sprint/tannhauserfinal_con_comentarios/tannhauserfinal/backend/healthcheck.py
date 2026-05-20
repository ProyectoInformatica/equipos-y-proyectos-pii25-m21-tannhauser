import sys
from pathlib import Path

# Añadir la raíz del proyecto al path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from models.db import get_connection


def run_healthcheck():
    resultado = {
        "status": "error",
        "database": "down",
        "details": ""
    }

    conn = get_connection()

    if not conn:
        resultado["details"] = "No se pudo crear la conexión con MySQL."
        return resultado

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE();")
        db = cursor.fetchone()

        resultado["status"] = "ok"
        resultado["database"] = "ok"
        resultado["details"] = f"Conexión correcta con la base de datos: {db[0]}"

        cursor.close()
        conn.close()
        return resultado

    except Exception as e:
        resultado["details"] = f"Error al consultar la base de datos: {e}"
        try:
            conn.close()
        except Exception:
            pass
        return resultado


if __name__ == "__main__":
    resultado = run_healthcheck()
    print("HEALTHCHECK")
    print(resultado)