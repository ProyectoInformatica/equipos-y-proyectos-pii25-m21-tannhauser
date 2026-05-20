import json
from pathlib import Path
from datetime import datetime

max_w = {
    'sensor_luz': 10.0,
    'sensor_nevera': 150.0,
    'sensor_puerta': 5.0,
    'sensor_temperatura': 2.0,
    'sensor_humedad': 2.0,
}

root = Path(__file__).resolve().parents[1]
files = sorted(root.rglob('sensores/sensor_*.json'))

def parse_entries(data, name):
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get('lecturas'), list):
        return data['lecturas']
    return []

# resultados
totals = {}
hourly = []  # tuples (sensor, hour_iso, wh)

for f in files:
    name = f.stem
    try:
        with f.open('r', encoding='utf-8') as fh:
            data = json.load(fh)
    except Exception:
        continue
    entries = parse_entries(data, name)
    rows = []
    for e in entries:
        if not isinstance(e, dict):
            continue
        ts = e.get('timestamp')
        if ts is None:
            continue
        try:
            dt = datetime.fromisoformat(ts)
        except Exception:
            continue
        if 'consumo_w' in e:
            try:
                p = float(e['consumo_w'])
            except Exception:
                continue
        elif 'valor' in e:
            m = max_w.get(name)
            if m is None:
                continue
            try:
                p = (float(e['valor'])/100.0)*float(m)
            except Exception:
                continue
        else:
            continue
        rows.append((dt, p))
    if not rows:
        totals[name] = {'total_wh': 0.0, 'count': 0}
        continue
    # ordenar por tiempo
    rows.sort(key=lambda x: x[0])
    total_wh = 0.0
    for i in range(len(rows)-1):
        t0, p0 = rows[i]
        t1, _ = rows[i+1]
        delta = (t1 - t0).total_seconds()
        if delta <= 0:
            continue
        wh = p0 * (delta/3600.0)
        total_wh += wh
        hour_iso = t0.replace(minute=0, second=0, microsecond=0).isoformat()
        hourly.append((name, hour_iso, wh))
    # for the last measurement we can't know duration; ignore or assume small interval; we'll ignore
    totals[name] = {'total_wh': round(total_wh, 4), 'count': len(rows), 'total_kwh': round(total_wh/1000.0, 6)}

# write totals CSV
out_totals = Path(__file__).resolve().parents[1] / 'tools' / 'consumo_kwh.csv'
with out_totals.open('w', encoding='utf-8') as fh:
    fh.write('sensor,total_wh,total_kwh,count\n')
    for k in sorted(totals):
        v = totals[k]
        fh.write(f'{k},{v.get("total_wh",0.0)},{v.get("total_kwh",0.0)},{v.get("count",0)}\n')

# write hourly CSV
out_hourly = Path(__file__).resolve().parents[1] / 'tools' / 'consumo_kwh_hourly.csv'
with out_hourly.open('w', encoding='utf-8') as fh:
    fh.write('sensor,hour_iso,wh,kwh\n')
    for s, h, wh in hourly:
        fh.write(f'{s},{h},{round(wh,4)},{round(wh/1000.0,6)}\n')

print('Generado:', out_totals)
print('Generado:', out_hourly)
