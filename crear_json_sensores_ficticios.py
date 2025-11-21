def crear_json_sensores_ficticios(self):
    """
    Crea un JSON aparte con sensores ficticios que simulan
    sensores aún no instalados para probar el sistema.
    """
    ruta = os.path.join(os.path.dirname(self.db.path), "sensores_ficticios.json")

    datos_ficticios = {
        "sensores_ficticios": [
            {
                "id": "temp_virtual_01",
                "tipo": "DHT",
                "zona": "pasillo-virtual-1",
                "valor": round(random.uniform(3.0, 12.0), 1)
            },
            {
                "id": "hum_virtual_01",
                "tipo": "DHT",
                "zona": "bebidas-virtual",
                "valor": random.randint(35, 95)
            },
            {
                "id": "mov_virtual_01",
                "tipo": "PIR",
                "zona": "entrada-virtual",
                "activo": random.choice([True, False])
            },
            {
                "id": "lux_virtual_01",
                "tipo": "LDR",
                "zona": "iluminacion-virtual",
                "valor": random.randint(10, 2200)
            },
            {
                "id": "cam_virtual_01",
                "tipo": "CAM",
                "zona": "seguridad-virtual",
                "activo": random.choice([True, False])
            }
        ]
    }

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos_ficticios, f, indent=4, ensure_ascii=False)

    self.anotar_actividad("sistema", "crear_json_ficticio_sensores", "sensores_ficticios.json generado")

    print(f"📁 Archivo creado: {ruta}")
    print("📡 Sensores ficticios generados correctamente.\n")


#Y añadido al menú del superusuario:

print("10) Generar JSON de sensores ficticios") 
elif op == "10":
    self.admin.crear_json_sensores_ficticios()