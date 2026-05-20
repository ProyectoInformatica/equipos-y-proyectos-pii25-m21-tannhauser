PROYECTO TANNHÄUSER - ACTIVIDAD 10
Sistema con Arduino, Base de Datos remota y Optimización

============================================================
1. DESCRIPCIÓN GENERAL DEL PROYECTO
============================================================

Este proyecto corresponde a la Actividad 10 del sistema Tannhäuser, basado en un supermercado inteligente con sensores conectados mediante Arduino/ESP32, almacenamiento de datos en base de datos y visualización de la información desde una aplicación de escritorio.

El sistema permite registrar usuarios, gestionar distintos roles, almacenar relaciones entre usuarios y guardar lecturas procedentes de sensores. La aplicación consulta la base de datos para mostrar la información registrada y comprobar el funcionamiento del sistema.

La entrega incluye:

- Proyecto completo de la aplicación.
- Código Arduino utilizado para la lectura y envío de datos.
- Backup de la base de datos en formato SQL.
- Datos de prueba para comprobar las funcionalidades.
- Archivo de instrucciones de ejecución.

============================================================
2. CONTENIDO DE LA ENTREGA
============================================================

La carpeta de entrega contiene los siguientes elementos:

1. Proyecto/
   Contiene el proyecto completo desarrollado en Visual Studio Code.

2. Arduino/
   Contiene el último código cargado en la placa Arduino/ESP32 para leer los sensores y enviar los datos.

3. BaseDeDatos/
   Contiene el archivo SQL exportado desde phpMyAdmin con la estructura y los datos de la base de datos.

4. README.txt
   Documento actual con la explicación del proyecto y las instrucciones de uso.

5. enlace_github.txt
   Archivo donde se debe incluir el enlace al repositorio de GitHub cuando el proyecto haya sido subido.

============================================================
3. BASE DE DATOS
============================================================

La base de datos se ha exportado desde phpMyAdmin en formato .sql.

El archivo SQL contiene:

- Estructura de las tablas.
- Registros de usuarios.
- Roles del sistema.
- Relaciones entre usuarios.
- Lecturas de sensores.
- Datos de prueba necesarios para validar el funcionamiento.

Para importar la base de datos:

1. Abrir XAMPP.
2. Iniciar Apache y MySQL.
3. Entrar en phpMyAdmin desde:
   http://localhost/phpmyadmin
4. Crear una base de datos nueva con el nombre utilizado por el proyecto.
   Por ejemplo:
   tannhauser
5. Seleccionar la base de datos creada.
6. Pulsar en la pestaña "Importar".
7. Seleccionar el archivo .sql incluido en la carpeta BaseDeDatos.
8. Pulsar en "Continuar".
9. Comprobar que las tablas y los registros se han importado correctamente.

============================================================
4. EJECUCIÓN DEL PROYECTO
============================================================

Para ejecutar la aplicación:

1. Abrir Visual Studio Code.
2. Abrir la carpeta del proyecto.
3. Comprobar que la base de datos está importada y que MySQL está iniciado.
4. Revisar el archivo de configuración de conexión a la base de datos.
5. Ejecutar la aplicación desde Visual Studio Code.

Es importante que los datos de conexión coincidan con la configuración local o remota utilizada:

- Host
- Puerto
- Nombre de la base de datos
- Usuario
- Contraseña

Ejemplo habitual en entorno local con XAMPP:

Host: localhost
Puerto: 3306
Base de datos: tannhauser
Usuario: root
Contraseña: vacía o la configurada en MySQL

============================================================
5. CÓDIGO ARDUINO
============================================================

La carpeta Arduino contiene el último programa cargado en la placa.

Este código se encarga de:

- Leer los valores de los sensores conectados.
- Procesar las señales obtenidas.
- Enviar los datos para su almacenamiento en la base de datos.
- Permitir la comunicación entre el microcontrolador y el sistema.

Para utilizarlo:

1. Abrir Arduino IDE.
2. Cargar el archivo .ino incluido en la carpeta Arduino.
3. Seleccionar la placa correspondiente.
4. Seleccionar el puerto correcto.
5. Subir el programa a la placa.
6. Abrir el monitor serie para comprobar las lecturas.

============================================================
6. FUNCIONALIDADES IMPLEMENTADAS
============================================================

El proyecto incluye las siguientes funcionalidades principales:

- Gestión de usuarios.
- Diferenciación de roles.
- Registro de relaciones entre usuarios.
- Lectura y almacenamiento de datos de sensores.
- Consulta de información desde la aplicación.
- Visualización de datos almacenados en la base de datos.
- Comunicación entre el microcontrolador y la base de datos.
- Datos de prueba suficientes para validar el sistema.

También se incluye una mejora del sistema mediante la funcionalidad implementada en el proyecto, como lectura periódica de sensores, mensajería, concurrencia o sistema de optimización, según la versión final entregada.

============================================================
7. DATOS DE PRUEBA
============================================================

La base de datos incluye registros de prueba para poder comprobar las funcionalidades solicitadas en la actividad.

Se han incluido datos como:

- Usuarios con distintos roles.
- Usuarios principales.
- Usuarios secundarios.
- Relaciones entre usuarios.
- Lecturas de sensores asociadas a usuarios.
- Varios registros de sensores para validar la visualización.
- Mensajes entre usuarios si la funcionalidad está incluida en el proyecto.

Estos datos permiten que el profesor pueda probar el sistema sin tener que introducir manualmente toda la información desde cero.

============================================================
8. GITHUB
============================================================

El proyecto debe subirse a GitHub antes de la entrega final.

Cuando esté subido, se debe crear o modificar el archivo:

enlace_github.txt

Y escribir dentro el enlace al repositorio, por ejemplo:

https://github.com/usuario/nombre-del-repositorio

En el momento de preparar este README, el repositorio todavía puede estar pendiente de subida.

============================================================
9. COMPROBACIONES ANTES DE ENTREGAR
============================================================

Antes de comprimir la carpeta final en formato .zip, se recomienda comprobar lo siguiente:

1. El proyecto se abre correctamente en Visual Studio Code.
2. El código Arduino está incluido en formato .ino.
3. El archivo SQL está dentro de la carpeta BaseDeDatos.
4. El archivo SQL contiene tanto CREATE TABLE como INSERT INTO.
5. La base de datos puede importarse correctamente en phpMyAdmin.
6. La aplicación conecta correctamente con la base de datos.
7. Existen datos de prueba suficientes para usuarios, roles, sensores y relaciones.
8. El archivo enlace_github.txt contiene el enlace al repositorio o queda preparado para añadirlo.
9. Todo el contenido está comprimido en un único archivo .zip.

============================================================
10. NOMBRE RECOMENDADO DEL ZIP
============================================================

Se recomienda entregar el archivo comprimido con un nombre claro, por ejemplo:

Actividad10_Tannhauser.zip

o

Actividad10_Tannhauser_Miguel_Alvaro_Alejandro.zip

============================================================
FIN DEL DOCUMENTO
============================================================
