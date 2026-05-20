\# Tannhäuser - Proyecto de Informática II



Repositorio del proyecto Tannhäuser, desarrollado para el sistema de supermercado inteligente.



\## Descripción del proyecto



Tannhäuser es una aplicación de gestión y visualización de datos para un supermercado inteligente.



El sistema permite:



\- Gestionar usuarios.

\- Diferenciar roles de usuario.

\- Visualizar datos de sensores.

\- Gestionar alertas y umbrales.

\- Controlar secciones como sensores, luces, cámaras o neveras.

\- Almacenar lecturas procedentes de sensores en base de datos.

\- Consultar el estado actual del sistema desde la aplicación.



La aplicación principal se ejecuta con Python y Flet.



\## Rama del checkpoint



La funcionalidad específica del checkpoint se ha desarrollado en la rama:



feature/biodinario-miguel



\## Ejecución del proyecto



\### Requisitos previos



\- Python 3.x

\- XAMPP

\- Apache iniciado en XAMPP

\- Base de datos tannhauser disponible en phpMyAdmin

\- Visual Studio Code

\- Git



\### Instalación de dependencias



Crear un entorno virtual:



python -m venv .venv



Activar el entorno virtual en PowerShell:



.\\.venv\\Scripts\\Activate.ps1



Instalar dependencias:



pip install -r requirements.txt



\### Configuración de variables de entorno



Crear un archivo .env a partir de .env.example.



Ejemplo de .env.example:



DB\_HOST=localhost

DB\_PORT=3306

DB\_NAME=tannhauser

DB\_USER=usuario\_mysql

DB\_PASSWORD=contraseña\_mysql



El archivo .env real no se sube al repositorio.



\### Ejecución de la aplicación



Con Apache iniciado en XAMPP, ejecutar:



python main.py



\## Funcionalidad del checkpoint: sensor biodinario



Se ha añadido una funcionalidad específica para el examen/checkpoint.



El nuevo sensor biodinario recoge dos datos:



\- Un dato numérico.

\- Un dato alfanumérico.



\## Cambios realizados



Se han añadido los siguientes elementos:



\- database/update\_biodinario.sql

\- php/ingest\_biodinario.php

\- arduino/SketchBiodinario\_Tannhauser.ino

\- requirements.txt

\- .env.example

\- .gitignore



\## Base de datos



Para adaptar la base de datos al nuevo sensor, ejecutar en phpMyAdmin el archivo:



database/update\_biodinario.sql



Este script realiza las siguientes acciones:



1\. Crea la tabla biodinario\_readings.

2\. Añade el tipo de sensor BIODINARIO en sensor\_types.

3\. Añade el dispositivo biodinario\_01 en devices.



Consultas de comprobación:



SELECT \* FROM sensor\_types WHERE code = 'BIODINARIO';



SELECT \* FROM devices WHERE device\_code = 'biodinario\_01';



SELECT \* FROM biodinario\_readings ORDER BY id DESC LIMIT 5;



SELECT \* FROM current\_state WHERE state\_code = 'BIODINARIO';



\## Endpoint PHP



El endpoint creado para recibir datos del sensor es:



php/ingest\_biodinario.php



Para probarlo en XAMPP, copiarlo a:



C:\\xampp\\htdocs\\tannhauser\\ingest\_biodinario.php



Antes de ejecutarlo, configurar en el PHP los datos reales de conexión a la base de datos.



El endpoint recibe un JSON con este formato:



{

&#x20; "dato\_numerico": 42,

&#x20; "dato\_alfanumerico": "OK-42"

}



El PHP valida los datos e inserta la información en:



\- biodinario\_readings

\- readings

\- current\_state



\## Prueba del endpoint desde PowerShell



Ejecutar:



$body = @{

&#x20;   dato\_numerico = 42

&#x20;   dato\_alfanumerico = "OK-42"

} | ConvertTo-Json



Invoke-RestMethod -Uri "http://localhost/tannhauser/ingest\_biodinario.php" -Method Post -ContentType "application/json" -Body $body



Si funciona correctamente, devuelve un mensaje indicando que la lectura biodinaria se ha insertado correctamente.



\## Código Arduino



El código Arduino está en:



arduino/SketchBiodinario\_Tannhauser.ino



Incluye el método pedido en el examen:



DatabaseInsert(int datoNumerico, const char datoAlfanumerico\[])



Este método recibe el dato numérico y el dato alfanumérico del sensor, construye un JSON y lo envía mediante HTTP POST al endpoint PHP para almacenarlo en la base de datos.



En el código Arduino se han dejado como plantilla los siguientes valores:



\- TU\_WIFI

\- TU\_PASSWORD\_WIFI

\- IP\_DE\_TU\_PC



Estos valores deben modificarse en una prueba real con ESP32.



\## Método DatabaseInsert



El método DatabaseInsert realiza los siguientes pasos:



1\. Comprueba que la ESP32 tiene conexión WiFi.

2\. Construye un JSON con dato\_numerico y dato\_alfanumerico.

3\. Envía el JSON mediante HTTP POST a ingest\_biodinario.php.

4\. Muestra por monitor serie el código HTTP y la respuesta del servidor.



\## Archivos importantes



\- main.py: punto de entrada de la aplicación.

\- controllers/: controladores de la aplicación.

\- models/: modelos y acceso a datos.

\- views/: pantallas de la aplicación.

\- utils/: utilidades de navegación.

\- database/update\_biodinario.sql: modificación de base de datos para el checkpoint.

\- php/ingest\_biodinario.php: endpoint PHP para insertar datos del sensor biodinario.

\- arduino/SketchBiodinario\_Tannhauser.ino: código Arduino/ESP32 del checkpoint.

\- requirements.txt: dependencias necesarias.

\- .env.example: plantilla de configuración.



\## Notas de seguridad



No se debe subir al repositorio:



\- .env

\- .venv/

\- Contraseñas reales de base de datos.

\- Contraseña real del WiFi.



Por eso estos elementos están incluidos en .gitignore.

