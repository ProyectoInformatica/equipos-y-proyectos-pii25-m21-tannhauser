import json
from pathlib import Path

max_w = {
    'sensor_luz': 10.0,
    'sensor_nevera': 150.0,
    'sensor_puerta': 5.0,
    'sensor_temperatura': 2.0,
    'sensor_humedad': 2.0,
}

root = Path(__file__).resolve().parents[1]
files = {p for p in root.rglob('sensores/sensor_*.json')}
results = {}

for f in sorted(files):
    name = f.stem
    try:
        with f.open('r', encoding='utf-8') as fh:
            data = json.load(fh)
    except Exception as e:
        # skip unreadable files
        continue

    # normalize entries
    if isinstance(data, list):
        entries = data
    elif isinstance(data, dict) and isinstance(data.get('lecturas'), list):
        entries = data['lecturas']
    else:
        entries = []

    consumos = []
    for e in entries:
        if not isinstance(e, dict):
            continue
        if 'consumo_w' in e:
            try:
                consumos.append(float(e['consumo_w']))
            except Exception:
                continue
        elif 'valor' in e:
            m = max_w.get(name)
            if m is None:
                continue
            try:
                consumos.append((float(e['valor'])/100.0)*float(m))
            except Exception:
                continue

    if consumos:
        mean_w = round(sum(consumos)/len(consumos), 4)
        total_w = round(sum(consumos), 4)
        count = len(consumos)
    else:
        mean_w = 0.0
        total_w = 0.0
        count = 0

    results[name] = {'mean_w': mean_w, 'count': count, 'total_w': total_w}

# print results
print('Media de consumo por sensor (W):')
for k in sorted(results):
    v = results[k]
    print(f'- {k}: media={v["mean_w"]} W, lecturas={v["count"]}, suma={v["total_w"]} W')

# write CSV
outcsv = Path(__file__).resolve().parents[1] / 'tools' / 'consumo_medias.csv'
with outcsv.open('w', encoding='utf-8') as fh:
    fh.write('sensor,mean_w,count,total_w\n')
    for k in sorted(results):
        v = results[k]
        fh.write(f'{k},{v["mean_w"]},{v["count"]},{v["total_w"]}\n')

print('\nCSV generado en:', outcsv)
