import mysql.connector
from models.db import get_connection

TABLAS_REQUERIDAS = [
    "roles",
    "users",
    "sensor_types",
    "devices",
    "readings",
    "current_state",
    "state_history",
    "products",
    "events",
    "camera_events",
    "media_assets",
    "activity_log",
    "comments",
    "chat_messages",
]


def comprobar_tablas(cursor):
    print("\n[1] Comprobación de tablas")
    print("-" * 50)
    ok = True

    for tabla in TABLAS_REQUERIDAS:
        try:
            cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
            total = cursor.fetchone()[0]
            print(f"✓ {tabla}: {total} registros")
        except Exception as e:
            print(f"✗ {tabla}: {e}")
            ok = False

    return ok


def comprobar_login_sql(cursor):
    print("\n[2] Comprobación de login SQL")
    print("-" * 50)

    try:
        query = """
            SELECT u.id, u.email, r.name
            FROM users u
            JOIN roles r ON u.role_id = r.id
            WHERE LOWER(u.email) = %s
              AND u.password_hash = SHA2(%s, 256)
              AND u.is_active = 1
            LIMIT 1
        """
        cursor.execute(query, ("admin@supermercado.com", "admin123"))
        row = cursor.fetchone()

        if row:
            print("✓ Login SQL correcto")
            return True
        else:
            print("✗ Login SQL incorrecto")
            return False

    except Exception as e:
        print(f"✗ Error en login SQL: {e}")
        return False


def comprobar_hashes(cursor):
    print("\n[3] Comprobación de hashes")
    print("-" * 50)

    try:
        cursor.execute("SELECT email, password_hash FROM users ORDER BY id")
        rows = cursor.fetchall()
        ok = True

        for email, password_hash in rows:
            if password_hash and len(str(password_hash)) >= 64:
                print(f"✓ {email}: hash correcto")
            else:
                print(f"✗ {email}: hash no válido")
                ok = False

        return ok

    except Exception as e:
        print(f"✗ Error comprobando hashes: {e}")
        return False


def comprobar_baja_logica(cursor, conn):
    print("\n[4] Comprobación de baja lógica")
    print("-" * 50)

    try:
        cursor.execute("""
            UPDATE users
            SET is_active = 0,
                deactivated_at = NOW(),
                updated_at = NOW()
            WHERE email = %s
        """, ("cliente@supermercado.com",))
        conn.commit()

        cursor.execute("""
            SELECT is_active, deactivated_at
            FROM users
            WHERE email = %s
        """, ("cliente@supermercado.com",))
        row = cursor.fetchone()

        cursor.execute("""
            UPDATE users
            SET is_active = 1,
                deactivated_at = NULL,
                updated_at = NOW()
            WHERE email = %s
        """, ("cliente@supermercado.com",))
        conn.commit()

        if row and row[0] == 0 and row[1] is not None:
            print("✓ Baja lógica correcta")
            return True

        print("✗ Baja lógica incorrecta")
        return False

    except Exception as e:
        print(f"✗ Error en baja lógica: {e}")
        return False


def comprobar_binarios(cursor):
    print("\n[5] Comprobación de binarios")
    print("-" * 50)

    try:
        cursor.execute("SELECT COUNT(*) FROM media_assets")
        total = cursor.fetchone()[0]

        if total > 0:
            print(f"✓ Hay {total} registro(s) binarios")
            return True
        else:
            print("✗ No hay binarios")
            return False

    except Exception as e:
        print(f"✗ Error en binarios: {e}")
        return False


def comprobar_fechas(cursor):
    print("\n[6] Comprobación de fechas")
    print("-" * 50)

    consultas = {
        "users.created_at": "SELECT COUNT(*) FROM users WHERE created_at IS NOT NULL",
        "readings.recorded_at": "SELECT COUNT(*) FROM readings WHERE recorded_at IS NOT NULL",
        "current_state.updated_at": "SELECT COUNT(*) FROM current_state WHERE updated_at IS NOT NULL",
        "state_history.changed_at": "SELECT COUNT(*) FROM state_history WHERE changed_at IS NOT NULL",
        "events.event_time": "SELECT COUNT(*) FROM events WHERE event_time IS NOT NULL",
        "activity_log.logged_at": "SELECT COUNT(*) FROM activity_log WHERE logged_at IS NOT NULL",
        "comments.created_at": "SELECT COUNT(*) FROM comments WHERE created_at IS NOT NULL",
    }

    ok = True

    try:
        for nombre, query in consultas.items():
            cursor.execute(query)
            total = cursor.fetchone()[0]
            if total > 0:
                print(f"✓ {nombre}: OK ({total})")
            else:
                print(f"✗ {nombre}: sin datos")
                ok = False

        return ok

    except Exception as e:
        print(f"✗ Error comprobando fechas: {e}")
        return False


def comprobar_foreign_keys(cursor):
    print("\n[7] Comprobación de foreign keys")
    print("-" * 50)

    try:
        cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.referential_constraints
            WHERE constraint_schema = DATABASE()
        """)
        total = cursor.fetchone()[0]

        if total > 0:
            print(f"✓ Foreign keys detectadas: {total}")
            return True
        else:
            print("✗ No se detectaron foreign keys")
            return False

    except Exception as e:
        print(f"✗ Error comprobando foreign keys: {e}")
        return False


def main():
    print("=" * 60)
    print("VERIFICACIÓN DEL SISTEMA TANNHÄUSER")
    print("=" * 60)

    try:
        conn = get_connection()
        if not conn:
            print("✗ No se pudo conectar a MySQL")
            return 1

        cursor = conn.cursor()

        resultados = [
            comprobar_tablas(cursor),
            comprobar_login_sql(cursor),
            comprobar_hashes(cursor),
            comprobar_baja_logica(cursor, conn),
            comprobar_binarios(cursor),
            comprobar_fechas(cursor),
            comprobar_foreign_keys(cursor),
        ]

        print("\n" + "=" * 60)
        print("RESUMEN FINAL")
        print("=" * 60)

        total_ok = sum(1 for r in resultados if r)
        total = len(resultados)

        print(f"Pruebas superadas: {total_ok}/{total}")

        if total_ok == total:
            print("✓✓✓ TODO CORRECTO")
            return 0
        else:
            print("⚠ Hay apartados pendientes")
            return 1

    except Exception as e:
        print(f"✗ Error general: {e}")
        return 1

    finally:
        try:
            conn.close()
        except:
            pass


if __name__ == "__main__":
    raise SystemExit(main())