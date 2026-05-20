# Tannhauser - Supermercado IoT

Versión ligera para GitHub. No incluye entorno virtual, cachés ni archivos generados.

## Ejecutar la app Flet

```bash
cd tannhauserfinal_Sprint/tannhauserfinal_con_comentarios
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
cd tannhauserfinal
copy .env.example .env
python main.py
```

En Linux/Mac cambia la activación por:

```bash
source .venv/bin/activate
cp .env.example .env
```

Edita `.env` con los datos reales de MySQL antes de iniciar la app.
