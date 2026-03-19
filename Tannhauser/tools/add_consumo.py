import json
from pathlib import Path

# Mapa de máximos por sensor
max_w = {
    'sensor_luz': 10.0,
    'sensor_nevera': 150.0,
    'sensor_puerta': 5.0,
    'sensor_temperatura': 2.0,
    'sensor_humedad': 2.0,
}

# Buscar archivos sensor_*.json en el workspace (carpeta padre de este script)
root = Path(__file__).resolve().parents[1]
patterns = [
    'data/sensores/sensor_*.json',
    'tannhauserfinal/data/sensores/sensor_*.json',
    'data/**/sensores/sensor_*.json',
]

files = set()
for p in patterns:
    for f in (root / p).parents[0].glob((root / p).name):
        files.add(str(f))
# Fallback: glob recursively from root
files |= {str(p) for p in root.rglob('sensores/sensor_*.json')}

if not files:
    print('No se encontraron archivos de sensores.')
else:
    print(f'Archivos encontrados: {len(files)}')

for filepath in sorted(files):
    p = Path(filepath)
    name = p.stem  # sensor_luz
    m = max_w.get(name, None)
    try:
        with p.open('r', encoding='utf-8') as fh:
            data = json.load(fh)
    except Exception as e:
        print(f'Error leyendo {p}: {e}')
        continue

    # detectar formato: lista directa o dict con clave 'lecturas'
    entries = None
    container_type = None
    if isinstance(data, list):
        entries = data
        container_type = 'list'
    elif isinstance(data, dict) and isinstance(data.get('lecturas'), list):
        entries = data['lecturas']
        container_type = 'dict_lecturas'
    else:
        print(f'Omitido {p}: formato no es lista ni dict con "lecturas"')
        continue

    # crear copia de seguridad
    bak = p.with_suffix(p.suffix + '.bak')
    try:
        with bak.open('w', encoding='utf-8') as fh:
            json.dump(data, fh, ensure_ascii=False, indent=4)
    except Exception:
        pass

    changed = False
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        if 'consumo_w' in entry:
            continue
        valor = entry.get('valor')
        if valor is None or m is None:
            continue
        try:
            consumo = round((float(valor) / 100.0) * float(m), 4)
        except Exception:
            continue
        entry['consumo_w'] = consumo
        changed = True

    if changed:
        # volver a insertar según tipo de contenedor
        try:
            if container_type == 'list':
                out = entries
            else:
                data['lecturas'] = entries
                out = data
            with p.open('w', encoding='utf-8') as fh:
                json.dump(out, fh, ensure_ascii=False, indent=4)
            # contar lecturas para el log
            count = len(entries) if entries is not None else 0
            print(f'Actualizado {p} ({count} lecturas)')
        except Exception as e:
            print(f'Error escribiendo {p}: {e}')
    else:
        print(f'No cambios en {p}')
