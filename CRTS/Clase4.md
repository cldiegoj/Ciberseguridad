# Clase 4

## Herramientas para ejercicios de Red Team Físico

- RFID Cloners (Flipper Zero): Dispositivos para clonar tarjetas de acceso
- Lockpicking Sets: Ganzúas y herramientas para abrir cerraduras
- Raspberry Pi con WiFi Pineapple: Para crear puntos de acceso falsos y capturar credenciales
- USB Rubber Ducky: Dispositivo que emula un teclado para ejecutar payloads automáticamente al conectarse
- Bash Bunny: Herramienta de ataque USB multiprotocolo para exfiltración de datos y ejecución de scripts

### Herramientas de Reconocimiento Físico

- Cámaras ocultas
- Drones
- Dispositivos de escucha

### Herramientas de ingeniería social

- Credenciales falsas
- Dispositivos de tailgating

## Herramientas de Escaneo y reconocimiento

### Nmap: Técnicas Avanzadas de Evasión

1. Fragmentación de paquetes

```sh
# Fragmentación básica (divide paquetes en fragmentos de 8 bytes)
nmap -f 192.168.1.0/24

# Fragmentación con MTU personalizado
nmap --mtu 16 192.168.1.0/24

# MTU debe ser múltiplo de 8 (8, 16, 24, 32, etc.)
```

2. Señuelos

```sh
# Usar IPs señuelo para ofuscar origen real
nmap -D RND:10 192.168.1.100

# RND:10 genera 10 IPs aleatorias como señuelo
# Tu IP real estará mezclada entre los señuelos

# Especificar señuelos manualmente
nmap -D 10.10.10.5,10.10.10.6,ME,10.10.10.7 192.168.1.100

# ME representa tu IP real en la secuencia
```
3. Spoofing de Dirección de origen

```sh
# Spoofear IP de origen (requiere acceso a nivel de red)
nmap -S 10.10.10.50 -e eth0 192.168.1.100

# -S: IP spoofed
# -e: interfaz de red a usar
# Útil en segmentos de red compartidos

# Spoofear puerto de origen
nmap --source-port 53 192.168.1.0/24

# Puerto 53 (DNS) suele estar permitido en firewalls
```

4. Control de Timing (Evasión temporal)

```sh
# Templates de timing (-T0 a -T5)
# T0: Paranoid (extremadamente lento, evade IDS)
nmap -T0 192.168.1.100

# T1: Sneaky (muy lento, bajo perfil)
nmap -T1 192.168.1.100

# T2: Polite (reduce carga de red)
nmap -T2 192.168.1.0/24

# Personalización manual de timing
nmap --scan-delay 5s --max-rate 10 192.168.1.0/24

# --scan-delay: espera entre sondas
# --max-rate: paquetes máximos por segundo
```

5. Tecnicas de Escaneo Furtivo

```sh
# SYN Stealth Scan (no completa handshake TCP)
nmap -sS 192.168.1.0/24

# FIN Scan (envía paquetes FIN, evade algunos firewalls)
nmap -sF 192.168.1.100

# NULL Scan (sin flags TCP establecidos)
nmap -sN 192.168.1.100

# XMAS Scan (flags FIN, PSH, URG activos)
nmap -sX 192.168.1.100

# Idle/Zombie Scan (usa host zombi para escanear)
nmap -sI zombie_host:port target_host
```

El NULL (-sN) siempre se le va a retornar una respuesta del destino

6. Evasión de Firewalls e IDS

```sh
# Enviar paquetes con flags TCP inválidos
nmap --badsum 192.168.1.100

# Checksums incorrectos son descartados por hosts reales
# pero procesados por algunos firewalls/IDS

# Usar datos aleatorios en paquetes
nmap --data-length 25 192.168.1.100

# Añade datos adicionales para cambiar firma del paquete

# Combinar múltiples técnicas de evasión
nmap -f -T1 -D RND:10 --source-port 53 --data-length 20 192.168.1.0/24
```
Longitud del dato, hay que tener en cuenta

7. Evasión mediante proxies y redirección

```sh
# Escaneo a través de proxy HTTP/SOCKS
nmap --proxies http://proxy1:8080,http://proxy2:8080 192.168.1.100

# Cadena de proxies para mayor anonimato
nmap --proxies socks4://proxy:1080 -p 80,443 target.com
```

8. Scripts NSE para Evasión y Reconocimiento Avanzado

```sh
# Detectar reglas de firewall
nmap --script firewall-bypass 192.168.1.100

# Evasión de detección de versión
nmap -sV --version-intensity 0 192.168.1.0/24

# Enumeración de subdominios DNS
nmap --script dns-brute target.com

# Detectar WAF (Web Application Firewall)
nmap -p 80,443 --script http-waf-detect target.com

# Fingerprinting avanzado del OS
nmap -O --osscan-guess --max-os-tries 1 192.168.1.100
```

9. Ejemplo de escaneo completo con máxima evasión

```sh
nmap -sS -T1 -f --mtu 24 -D RND:15 --source-port 53 \
     --data-length 30 --scan-delay 3s --max-rate 5 \
     --badsum --randomize-hosts -p- -vvv \
     -oN resultado_evasivo.txt 192.168.1.0/24

# Explicación:
# -sS: SYN stealth scan
# -T1: timing sneaky
# -f --mtu 24: fragmentación
# -D RND:15: 15 señuelos aleatorios
# --source-port 53: puerto origen DNS
# --data-length 30: datos adicionales
# --scan-delay 3s: 3 segundos entre sondas
# --max-rate 5: máximo 5 paquetes/seg
# --badsum: checksums inválidos
# --randomize-hosts: aleatorizar orden de hosts
# -p-: todos los puertos
# -v: verbose
# -oN: guardar resultado

```

10. Bypass de Filtros Específicos

```sh
# Bypass de filtros por tamaño de paquete
nmap --mtu 8 --data-length 0 target.com

# Bypass usando IPv6 (si el firewall solo filtra IPv4)
nmap -6 fe80::1%eth0

# Escaneo de puertos específicos en orden aleatorio
nmap -p 80,443,8080,8443 --randomize-hosts -T2 targets.txt

# Escaneo con exclusion de puertos especificos
nmap -p- --exclude-port 22 --randomize-hosts -T2 targets.txt

# Evasión de rate limiting
nmap --max-retries 0 --host-timeout 5m target.com
```

### Wireshark

1. Filtros de tráfico HTTP/HTTPS

```sh
# Filtrar credenciales en texto plano (POST HTTP)
http.request.method == "POST" && http contains "password"

# Detectar autenticación básica HTTP
http.authbasic

# Extraer tokens de sesión
http.cookie contains "session" || http.cookie contains "token"

# Filtrar User-Agents sospechosos
http.user_agent contains "sqlmap" || http.user_agent contains "nikto"

# Detectar exfiltración de datos por HTTP
http.content_length > 10000 && http.request.method == "POST"

# Filtrar tráfico hacia dominios específicos
http.host == "malicious-c2.com"
```

2. Filtros de tráfico DNS

```sh
# Detectar túneles DNS (consultas inusuales)
dns.qry.name.len > 50

# Filtrar respuestas DNS con múltiples IPs (Fast Flux)
dns.count.answers > 5

# Detectar consultas DNS a dominios sospechosos
dns.qry.name contains ".tk" || dns.qry.name contains ".ml"

# Identificar DNS tunneling por tipo de registro
dns.qry.type == 16  # TXT records usados para exfiltración

# Consultas DNS sin respuesta (posible C2)
dns.flags.response == 0 && dns.count.answers == 0
```

3. Filtros de tráfico de C2

```sh
# Detectar beacons periódicos (comunicación C2)
# Usar Statistics > Conversations, buscar intervalos regulares

# Filtrar tráfico TLS con certificados autofirmados
tls.handshake.certificate && x509ce.is_self_signed

# Detectar conexiones a IPs sin DNS previo
!(dns) && tcp.flags.syn == 1 && tcp.flags.ack == 0

# Identificar tráfico cifrado no estándar
tcp.port > 49152 && tcp.len > 100 && !(tls || ssh)

# Detectar JA3 hash (fingerprinting TLS)
# Requiere plugin tls.ja3
tls.handshake.type == 1
```

4. Filtros para Detección de Exploits

```sh
# Detectar shellcode común (NOPs)
tcp.payload contains 90:90:90:90

# Identificar ataques de inyección SQL
http.request.uri contains "union" || http.request.uri contains "select"

# Detectar payloads de Metasploit
tcp.payload contains "metasploit" || tcp.payload contains "meterpreter"

# Filtrar intentos de RCE
http.request.uri contains "cmd" || http.request.uri contains "exec"

# Detectar escaneos de vulnerabilidades
tcp.flags.syn == 1 && tcp.flags.ack == 0 && tcp.window_size_value < 1024
```

5. Filtros para Análisis de Credenciales

```sh
# Extraer credenciales FTP
ftp.request.command == "USER" || ftp.request.command == "PASS"

# Capturar autenticación SMTP
smtp.req.command == "AUTH"

# Detectar autenticación Telnet
tcp.port == 23 && tcp.payload contains "login"

# Filtrar hashes NTLM (SMB)
ntlmssp.auth.username

# Capturar credenciales Kerberos
kerberos.CNameString
```

6. Filtros de movimiento lateral

```sh
# Detectar conexiones SMB/CIFS
smb2 || smb

# Filtrar ejecución remota (WMI, PSExec)
tcp.port == 135 || tcp.port == 445

# Identificar RDP (Remote Desktop)
tcp.port == 3389

# Detectar WinRM (PowerShell remoto)
tcp.port == 5985 || tcp.port == 5986

# Filtrar uso de PsExec
smb2.cmd == 5 && smb2.filename contains "PSEXESVC"
```
7. Filtros para exfiltración de datos

```sh
# Detectar transferencias grandes
tcp.len > 1000 == tcp.port != 80 && tcp.port != 443

# Filtrar tráfico ICMP inusual (túneles ICMP)
icmp.type == 8 && data.len &gt; 64

# Detectar transferencias por protocolos no estándar
tcp.port > 10000 && !(http || tls || ssh)

# Identificar uso de servicios de transferencia (Dropbox, Drive)
http.host contains "dropbox" || http.host contains "drive.google"

# Detectar exfiltración por DNS
dns.qry.type == 16 == dns.qry.name.len > 100
```

8. Filtros Combinados para Escenarios de Red Team 

```sh
# Detectar pivoting (host interno accediendo a múltiples IPs)
ip.src == 192.168.1.50 &amp;&amp; (tcp.flags.syn == 1) &amp;&amp; (ip.dst != 192.168.1.0/24)

# Identificar escaneo de puertos internos
tcp.flags.syn == 1 &amp;&amp; tcp.flags.ack == 0 &amp;&amp; ip.dst == 192.168.1.0/24

# Detectar uso de proxies internos
tcp.port == 8080 || tcp.port == 3128 || tcp.port == 1080

# Filtrar tráfico de herramientas de Red Team
http.user_agent contains "curl" || http.user_agent contains "python-requests"

# Identificar tráfico TOR
tcp.port == 9050 || tcp.port == 9150
```

9. Uso de Estadisticas para Análisis de Red Team

```sh
# Statistics &gt; Conversations
# Buscar: 
# - Conexiones de larga duración
# - Tráfico periódico (beacons cada X segundos)
# - Volumen anómalo de datos

# Identificar protocolos inusuales o no esperados
# Statistics > Protocol Hierarchy

# Detectar IPs que se comunican con múltiples hosts
# Statistics > Endpoints
```

10. Explotación y análisis de datos capturados

```sh
# Exportar objetos HTTP (archivos descargados)
# File > Export Objects > HTTP

# Extraer credenciales automáticamente
# Analyze > Expert Information (buscar warnings de autenticación)

# Filtrar y exportar conversaciones específicas
# Click derecho en paquete > Follow > TCP Stream

# Guardar filtros personalizados
# Analyze > Display Filters > Save

# Exportar paquetes filtrados
# File > Export Specified Packets > Use displayed packets
```

11. Detección de técnicas de evasión en Wireshark

```sh
# Detectar fragmentación IP (evasión de IDS)
ip.flags.mf == 1

# Identificar paquetes con TTL bajo (posible spoofing)
ip.ttl &lt; 10

# Detectar paquetes con flags TCP inválidos
tcp.flags == 0x00 || tcp.flags == 0x3f

# Filtrar checksums inválidos (técnica de evasión)
ip.checksum_bad == 1 || tcp.checksum_bad == 1

# Detectar padding excesivo (ofuscación)
tcp.len &gt; tcp.payload.len
```

12. Tshark para análisis automatizado

```sh
# Captura en vivo con filtro
tshark -i eth0 -f "tcp port 80" -w captura.pcap

# Análisis de PCAP con filtro de visualización
tshark -r captura.pcap -Y "http.request.method == POST"

# Extraer campos específicos (credenciales)
tshark -r captura.pcap -Y "http.request.method == POST" \
       -T fields -e http.request.uri -e http.file_data

# Estadísticas de conversaciones
tshark -r captura.pcap -q -z conv,tcp

# Detectar beacons (conexiones periódicas)
tshark -r captura.pcap -T fields -e frame.time_relative \
       -e ip.src -e ip.dst -e tcp.dstport

# Buscar strings específicos en payloads
tshark -r captura.pcap -Y "tcp.payload contains \"password\""
```