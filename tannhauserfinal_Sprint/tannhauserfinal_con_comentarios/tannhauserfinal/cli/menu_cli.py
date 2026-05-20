import sys
from pathlib import Path

# Añadir la raíz del proyecto al path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from models.db import get_connection


def listar_dispositivos():
    conn = get_connection()
    if not conn:
        print("No se pudo conectar a la base de datos.")
        return

    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT id, device_code, device_name, location_name, status
        FROM devices
        ORDER BY id
    """)
    filas = cursor.fetchall()

    print("\nDISPOSITIVOS")
    if not filas:
        print("No hay dispositivos.")
    else:
        for d in filas:
            print(f"[{d['id']}] {d['device_code']} - {d['device_name']} - {d['location_name']} - {d['status']}")

    cursor.close()
    conn.close()


def ver_estado_actual():
    conn = get_connection()
    if not conn:
        print("No se pudo conectar a la base de datos.")
        return

    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT cs.id, d.device_name, cs.state_code, cs.state_value, cs.numeric_value, cs.updated_at
        FROM current_state cs
        JOIN devices d ON cs.device_id = d.id
        ORDER BY cs.updated_at DESC
    """)
    filas = cursor.fetchall()

    print("\nESTADO ACTUAL")
    if not filas:
        print("No hay estados registrados.")
    else:
        for e in filas:
            print(f"[{e['id']}] {e['device_name']} | {e['state_code']} | {e['state_value']} | {e['numeric_value']} | {e['updated_at']}")

    cursor.close()
    conn.close()


def ver_ultimas_lecturas():
    conn = get_connection()
    if not conn:
        print("No se pudo conectar a la base de datos.")
        return

    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT r.id, d.device_name, r.reading_value, r.reading_unit, r.recorded_at, r.source
        FROM readings r
        JOIN devices d ON r.device_id = d.id
        ORDER BY r.recorded_at DESC, r.id DESC
        LIMIT 10
    """)
    filas = cursor.fetchall()

    print("\nÚLTIMAS LECTURAS")
    if not filas:
        print("No hay lecturas registradas.")
    else:
        for r in filas:
            print(f"[{r['id']}] {r['device_name']} | {r['reading_value']} {r['reading_unit']} | {r['recorded_at']} | {r['source']}")

    cursor.close()
    conn.close()


def main():
    while True:
        print("\n=== TANNHÄUSER CLI ===")
        print("1. Listar dispositivos")
        print("2. Ver estado actual")
        print("3. Ver últimas lecturas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            listar_dispositivos()
        elif opcion == "2":
            ver_estado_actual()
        elif opcion == "3":
            ver_ultimas_lecturas()
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()