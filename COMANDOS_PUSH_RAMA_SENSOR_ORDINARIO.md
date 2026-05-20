# Comandos para subir la versión integrada a una rama nueva

Ejecutar desde la carpeta local del repositorio clonado, por ejemplo:

```bash
cd C:\Users\alvar\Desktop\tannhauser_github
```

Actualizar `main`:

```bash
git checkout main
git pull
```

Crear la rama de entrega:

```bash
git checkout -b sensor-ordinario-integrado
```

Copiar encima los archivos de este ZIP integrado dentro de `tannhauser_github`. Después comprobar cambios:

```bash
git status
```

Guardar y subir:

```bash
git add .
git commit -m "Integra sensor ordinario en proyecto completo"
git push -u origin sensor-ordinario-integrado
```

Enlace de la rama para entregar:

```text
https://github.com/ProyectoInformatica/equipos-y-proyectos-pii25-m21-tannhauser/tree/sensor-ordinario-integrado
```
