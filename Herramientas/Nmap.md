## Identificar puertos abeirtos
```sh
nmap -sS -p- --open -min-rate 5000 -n -vvv -Pn -oG allPorts
```
-oG se guarda en formato grepeable para poder extraer los puertos con extractports \
-sS escaneo sigiloso \
-p- escanea todos los puertos --open \
-min-rate 5000 Intenta enviar al menos 5000 paquetes por segundo \
-n No realiza resolución DNS \
-vvv Muestra resultados muy detallados \
-Pn Desactiva la detección de hosts

-O  Sistema Operativo del host
-sV Versiones de los servicios
-A  Modo agresivo
-sT TCP SCAN



Si la conexión no existe (CLOSED), al enviar un paquete TCP SYN el servidor retornará un TCP RST

Pero si un firewall está filtrando/dropeando los paquetes recibidos, la herramienta Nmap enviará un TCP SYN y no recibirá nada de regreso. 

```sh
iptables -I INPUT -p tcp --dport <port> -j REJECT --reject-with tcp-reset
```

Configuración de firewall para responder con un TCP RST...

-sS "Half Open SCAN" : Escaneo que retorna al servidor un RST TCP después de recibir un SYN/ACK para prevenir que el servidor haga más requests

Nmap usa TCP SCAN por default, con root/sudo usa SYN SCAN por default

-sU UDP SCAN, Nmap manda paquetes y si no tienen respuesta lo taggean como abierto/filtrado. También mandan un "doble check" de paquete para asegurar que esté abierto. Si recibe una respuesta [Lo cual no es usual] se marca como abierto, Si recibe un ICMP (ping) significa que el puerto está cerrado.

-sN TCP NULL SCAN
-sF TCP FIN SCAN
-sX TCP Xmas SCAN

Todos son utilizados para evadir la detección de firewalls y funcionan de manera similar a un UDP SCAN

-sn ICMP SCAN (Ping SCAN)

Nmap Scripting Engine (NSE) tiene 7 categorias

```sh
safe
intrusive
vuln
exploit
auth
brute
discovery
```

Script en Nmap

```sh
--script=<script-name> 
--script=http-fileupload-exploiter
--script=smb-enum-users,smb-enum-shares
```

Cuando el script requiere parametros se usa de esta manera:

```sh
nmap -p 80 --script http-put --script-args http-put.url='/dav/shell.php',http-put.file='./shell.php'

Todos los scripts están en la ruta: /usr/share/nmap/scripts/script.db

```

-Pn Le dice a Nmap que no se moleste en hacer un ping (ICMP) al host antes de escanearlo

-f Fragmenta los paquetes, haciendo que sea menos suseptible a ser detectado por firewall o IDS

--mtu <num> acepta un maximo de unidades de transacción (num debe ser multiplo de 8)

--scan-delay <time ms> Añade un delay a los paquetes enviados para el scaneo, util si la red es inestable

--basum Usado para generar un checksum invalido para los paquetes, un TCP/IP lo dropearía, pero un IDS o firewall lo respondería automaticamente sin revisar el checksum del paquete, usado para detectar la presencia de firewall/IDS

