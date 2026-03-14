# Ataques de Red

Wireshark es el estandar de la industria para el analisis de paquetes de red, permitiendote capturar e inspeccionar trafico de red en detalle

Capacidades:

- Captura en tiempo real
- Analisis de protocolos
- Filtros
- Troubleshooting
- Forense
- Analisis de seguridad
- Extracción de data

Por qué importa para eJPTv2

- Credenciales HTTP y cookies de sesión
- FTP/Telnet autenticación en texto plano
- Queries DNS revelando infraestructura interna
- SNMP community strings and OIDs
- SMB credenciales y transferencias de archivo

Filtros utiles:

```sh
tcp port 80
host 192.168.1.10
tcp port 22
tcp port 21
src host 192.168.1.10
dst host 8.8.8.8
tcp port 80 or tcp port 443
not icmp
```

Filtros de display:

```sh
http
dns
ftp 
smb 

ip.src == 192.168.1.10
ip.dst == 8.8.8.8

tcp.port == 22
tcp.dstport == 3306

tcp.port == 80 and http

!arp and !dns

http.request.uri contains "login"

(tcp.dstport == 80 or tcp.dstport == 443) and ip.src == 192.168.1.10
```

## Analisis de detalles del paquete

Estructura del paquete

1. Packet List
2. Packet Details
3. Packet Bytes

HTTP GET REQUEST BREAKDOWN:

- Frame: Capa Fisica
- Ethernet: Dirección MAC
- IP: Origen y destino IP
- TCP: Origen y destino puertos
- HTTP: Metodo de request, URL y headers

TCP Streams:

- Click derecho en paquete TCP 
- Selecciona "Follow -> TCP Stream" 
- Wireshark muestra cliente (azul) y servidor (rojo)
- Puede exportar conversación como archivo

Extraer data de capturas:

- File -> Export Objects -> HTTP
- Selecciona archivos
- Guardas en disco

También funciona para SMB y TFTP

Extracción de contraseñas: 

Muchos protocolos transmiten las credenciales en texto plano:

- HTTP 
- FTP 
- TELNET 
- IMAP/POP3

Capturando trafico HTTP: 

```sh
http.request.method == "POST"
```

Protocolos de red fundamentales: 

| Capa | OSI | TCP/IP | Protocolos | Wireshark |
| :---: | :--- | :--- | :--- | :--- |
| Aplicación | 5-7 | Aplicación | HTTP,HTTPS,FTP,SSH,SMTP,DNS | Decoded data, headers |
| Transporte | 4 | Transporte | TCP,UDP,SCTP | Port numbers, segments |
| Internet | 3 | Internet | IP,ICMP,IGMP | Direcciones IP, routing |
| Data Link | 2 | Link | Ethernet, ARP | Direcciones MAC , frames |
| Fisica | 1 | Fisica | Cables, señales | Data a nivel de bit |

## Enumeración de red 

- Network Discovery: Identify live hosts
- Port Scanning: Discover open services
- Service Identification: Determine service versions
- Vulnerability assessment: Identify weaknesses
- Documentation: Record findings

Host Discovery: 

```sh
#Usando ping
for i in {1...254}; do ping -c 1 192.168.1.$i | grep "bytes from"; done

#Usando nmap 
nmap -sn 192.168.1.0/24

#Identificar live hosts
nmap -sn 192.168.1.0/24 -oG - | grep "Up"

#Usando arp-scan 
arp-scan -l

#Usando netdiscover 
netdiscover -r 192.168.1.0/24

#Nmap con arp
nmap -sn 192.168.1.0/24 --send-eth
```

Escaneo de puertos y servicios:

```sh
nmap -sV 192.168.1.10

nmap -p- -sV 192.168.1.10

nmap -A -T4 192.168.1.10

nmap -O -sC 192.168.1.10

nmap -sU -p 53,123,161 192.168.1.10

nmap -A -T4 --traceroute 192.168.1.0/24

#Service detection
nmap -sV --version-intensity 9 192.168.1.10

#Probe open port only 
nmap -sV --version-light 192.168.1.10

#Combinado con script scanning
nmap -sV -sC 192.168.1.10
```

DNS Zone transfer:

```sh
dig @192.168.1.1 example.com axfr

#Usando nslookup 
nslookup
> server 192.168.1.10
> set type=NS 
> example.com
> set type=A 
> example.com

#Usando host command
host -t axfr example.com 192.168.1.10
```

DNS Record Enumeración

```sh
#A records (IPv4)
dig example.com A

#MX records (Mail Servers)
dig example.com MX

#NS records (nameservers)
dig example.com NS 

#TXT records
dig example.com TXT 

#Todos los records 
dig example.com ANY 

#REVERSE DNS LOOKUP
dig -x 8.8.8.8
```

SMB Enumeración

```sh
enum4linux 192.168.1.10 

enum4linux -a 192.168.1.10 # Todas las opciones 
enum4linux -U 192.168.1.10 # Enumeración de usuario
enum4linux -S 192.168.1.10 # Enumeración de compartidos
enum4linux -N 192.168.1.10 # NetBIOS names
enum4linux -P 192.168.1.10 # Password policy
```

NetBIOS Enumeración

```sh
nmblookup -A 192.168.1.10

nmblookup -B 192.168.1.255 \*
```

SNMP Enumeración

Simple Network Management Protocol es usado para gestionar dispositivos de red y monitorearlos

- PUERTO 161 UDP (Agente)
- PUERTO 162 UDP (trap)
- Version 1 , 2 y 3

| Tipo de información | Rango OID | Impacto de seguridad |
| :---: | :--- | :--- |
| System Description | 1.3.6.1.2.1.1.1 | Identifica OS, servicios y versiones |
| System Uptime | 1.3.6.1.2.1.1.3 | Ayuda a predecir status del parche |
| Network Interfaces | 1.3.6.1.2.1.2 | Revela la topologia de red |
| Running Processes | 1.3.6.1.2.1.25.4 | Identifica servicios |
| Network Routes | 1.3.6.1.2.1.4.21 | Detalles de la segmentación de red |
| TCP Connections | 1.3.6.1.2.1.6.13 | Servicios y conexiones activas |
| User Accounts | 1.3.6.1.4.1.77.1.2.25 | Enumeración de usuarios especificos Windows |

Herramientas de enumeración SNMP

```sh
snmpwalk -c public -v 1 192.168.1.100

snmpwalk -c public -v 1 192.168.1.100 1.3.6.1.2.1.1

snmpwalk -c public -v 1 192.168.1.100 1.3.6.1.2.1.1.1.0

snmpwalk -c public -v 1 192.168.1.100 1.3.6.1.2.1.1.2.0

snmpwalk -c public -v 1 192.168.1.100 1.3.6.1.2.1.2
```

SNMPGet 

```sh
# Get system name
snmpget -c public -v 1 192.168.1.1 1.3.6.1.2.1.1.5.0

# Get system uptime
snmpget -c public -v 1 192.168.1.1 1.3.6.1.2.1.1.3.0

# Get system description
snmpget -c public -v 1 192.168.1.1 1.3.6.1.2.1.1.1.0
```

OIDs comunes de SNMP

| OID | Descripción | Uso | 
| :---: | :--- | :--- |
| 1.3.6.1.2.1.1.1.0 | sysDescr | System description |
| 1.3.6.1.2.1.1.3.0 | sysUptime | Uptime information |
| 1.3.6.1.2.1.1.5.0 | sysName | Hostname |
| 1.3.6.1.2.1.1.6.0 | sysLocation | Physical location |
| 1.3.6.1.2.1.1.9   | sysServices | Services running |
| 1.3.6.1.2.1.25.1.1.0 | hrSystemUptime | Host resources uptime |
| 1.3.6.1.2.1.25.3.2 | hrDeviceDescr | Device descriptions |
| 1.3.6.1.2.1.25.4.2.1.2 | hrSWRunName | Running processes |

