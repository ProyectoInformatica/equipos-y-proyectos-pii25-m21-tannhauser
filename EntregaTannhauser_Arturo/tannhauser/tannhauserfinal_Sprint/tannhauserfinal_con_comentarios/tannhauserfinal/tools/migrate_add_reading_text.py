#!/usr/bin/env python3
"""
Script de migración para añadir `reading_text` y permitir NULL en `reading_value`.
Ejecutar desde la raíz del proyecto: `python tannhauserfinal/tools/migrate_add_reading_text.py`
"""
import sys
from pathlib import Path

# Añadir el proyecto al path para importar models.db
sys.path.append(str(Path(__file__).resolve().parents[1]))

from models.db import get_connection


def main():
    conn = get_connection()
    if not conn:
        print("No se pudo conectar a la base de datos. Revisa las variables de entorno.")
        return

    try:
        cursor = conn.cursor()
        # Obtener nombre de la base de datos activo
        cursor.execute("SELECT DATABASE();")
        db_row = cursor.fetchone()
        db_name = db_row[0] if db_row else None

        if not db_name:
            print("No se detectó la base de datos activa.")
            return

        # Comprobar existencia de la tabla `readings`
        cursor.execute(
            "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = %s AND table_name = 'readings'",
            (db_name,)
        )
        if cursor.fetchone()[0] == 0:
            print("La tabla 'readings' no existe en la base de datos especificada. Abortando.")
            return

        # Añadir columna reading_text si no existe
        cursor.execute(
            "SELECT COUNT(*) FROM information_schema.columns WHERE table_schema = %s AND table_name = 'readings' AND column_name = 'reading_text'",
            (db_name,)
        )
        if cursor.fetchone()[0] == 0:
            print("Añadiendo columna 'reading_text'... ")
            cursor.execute("ALTER TABLE readings ADD COLUMN reading_text VARCHAR(255) DEFAULT NULL;")
            print("Columna 'reading_text' añadida.")
        else:
            print("Columna 'reading_text' ya existe. Omitiendo.")

        # Verificar si reading_value admite NULL
        cursor.execute(
            "SELECT IS_NULLABLE, COLUMN_TYPE FROM information_schema.columns WHERE table_schema = %s AND table_name = 'readings' AND column_name = 'reading_value'",
            (db_name,)
        )
        row = cursor.fetchone()
        if row:
            is_nullable = row[0]
            if is_nullable == 'NO':
                print("Modificando 'reading_value' para permitir NULL... ")
                cursor.execute("ALTER TABLE readings MODIFY COLUMN reading_value DECIMAL(10,2) DEFAULT NULL;")
                print("'reading_value' modificado para permitir NULL.")
            else:
                print("'reading_value' ya permite NULL. Omitiendo.")
        else:
            print("No se encontró la columna 'reading_value' en 'readings'. Revisa el esquema.")

        conn.commit()
        print("Migración completada correctamente.")
    except Exception as e:
        print("Error durante la migración:", e)
        try:
            conn.rollback()
        except Exception:
            pass
    finally:
        try:
            cursor.close()
        except Exception:
            pass
        conn.close()


if __name__ == '__main__':
    main()
