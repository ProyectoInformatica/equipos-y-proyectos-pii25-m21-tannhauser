import json
import os
import traceback

from controllers.estadisticas_controller import EstadisticasController


def main():
    try:
        base_dir = os.path.dirname(__file__)
        os.chdir(base_dir)
        print(f"Working dir: {os.getcwd()}")

        ctrl = EstadisticasController()
        print("Calculando consumo últimas 24h...")
        consumo = ctrl.obtener_consumo_ultimas_24h()
        print("Consumo calculado:")
        print(json.dumps(consumo, indent=4, ensure_ascii=False))

        # Mostrar contenido de archivos JSON en data/sensores
        sensores_dir = ctrl.fm.SENSORES_DIR
        print(f"\nArchivos en: {sensores_dir}")
        if os.path.exists(sensores_dir):
            for f in sorted(os.listdir(sensores_dir)):
                if not f.endswith('.json'):
                    continue
                ruta = os.path.join(sensores_dir, f)
                print(f"\n--- {ruta} ---")
                try:
                    with open(ruta, 'r', encoding='utf-8') as fh:
                        data = json.load(fh)
                        print(json.dumps(data, indent=4, ensure_ascii=False)[:2000])
                except Exception as e:
                    print(f"Error leyendo {ruta}: {e}")
        else:
            print("No existe el directorio de sensores.")

    except Exception:
        traceback.print_exc()


if __name__ == '__main__':
    main()
