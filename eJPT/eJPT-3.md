# Host Discovery

Hay 4 metodos para hacer descubrimiento de hosts:

ICMP
ARP
TCP
UDP

El metodo depende de la topologia de red, configuración del firewall y accesibilidad del objetivo

## ICMP

```sh
ping 192.168.1.1
nmap -sn 192.168.1.0/24
```

Es rapido pero normalmente está bloqueado por firewalls, ideal para una vista rapida de la red

## ARP Scanning

```sh
nmap -sn -PR 192.168.1.0/24 
```

No puede bloquearse, opera en capa 2. Sin embargo, solo funciona en red local.

## TCP Port Scan 

```sh
nmap -sn -PS80,443,22 192.168.1.0/24
```

Funciona a traves de redes, pasa fitltro ICMP. Pero también es más lento y detectable, normalmente se usa cuando ICMP está bloqueado para redes remotas.

## Entender Output

- Host is up: Objetivo respondió al request
- latency: tiempo de respuesta
- 0.0023s: respuesta rapida, local
- 0.05+: respuesta lenta, red remota

## Puertos comunes

- 80: HTTP
- 443: HTTPS
- 22: SSH 
- 445: SMB
- 3389: RDP

## Comandos NMAP 

- sn: Ping Scan
- PS: TCP SYN ping
- PA: TCP ACK ping
- PR: ARP ping
- PU: UDP ping
- n: skip dns resolution
- oN: Output formato normal
- oX: Output formato XML
- oG: Output grepeable
- oA: Output todos los formatos

# Escaneo de puertos con nmap 

## Estados de Puerto

| Estado | Significado | Acción |
| :---: | :--- | :--- |
| Open | Servicio en escucha, aceptando conexiones | Vector de ataque |
| Closed | Puerto accesible pero no en estado de escucha | Usualmente se ignora |
| Filtered | Puerto bloqueado por un firewall, no se puede determinar un estado | Puede ser un honeypot | 
| Unfiltered | Puerto accesible pero estado desconocido | Necesita más investigación |
| Open-Filtered | No se puede determinar si está abierto o filtrado | Seguramente protegido por un firewall |

## Tipos de escaneo

- TCP Connect Scan (sT): Completa el 3-way handshake de TCP
- TCP SYN Scan (sS): Mejor conocido como stealth scan, no completa el handshake
- UDP Scan (sU): Testea puertos UDP

## Rango de puertos

Por default scanea los primeros 1000 puertos: 

```sh
nmap 192.168.1.10
```

Especificar puertos: 

```sh
nmap -p 22,80,443 192.168.1.10
```

Rango de puertos: 

```sh
nmap -p 1-1000 192.168.1.10
```

Scanea todos los puertos (65535): 

```sh
nmap -p- 192.168.1.10
```

Scanea solo puertos comunes: 

```sh
nmap --top-ports 100 192.168.1.10
```

## Nmap NSE

NSE es un framework en nmap que permite:

- Network Discovery
- Vulnerability detection
- Service enumeration
- Version detection enhancement
- Authentication testing

### Categorias

| Categoria | Proposito |
| :---: | :--- |
| auth | Descubrimiento de mecanismos de autenticación y probar credenciales predeterminadas |
| broadcast | Mandar paquetes de broadcast para descubrir hosts y servicios |
| brute | Uso de fuerza bruta en servicios | 
| default | Scripts seguros | 
| discovery | Descubrimiento de red y enumeración |
| dos | Detecta vulnerabilidades de DoS |
| exploit | Explotación de scripts |
| external | ejecuta servicios externos |
| fuzzer | Scripts de fuzzing para identificar comportamientos anomalos |
| intrusive | Puede crashear servicios o activar alertas |
| malware | Detecta firmas de malware |
| safe | Scripts no intrusivos |
| version | Activa precisión de detección de versión |
| vuln | Revisa por CVEs y vulnerabilidades conocidas |

Sintaxis:

```sh
nmap --script [categoria] 192.168.1.10
```

## Evasión de Firewall e IDS

Varios firewalls confian en trafico de puertos especificos (DNS, DHCP, HTTP)

Eso se vería de la siguiente manera: 

```sh
sudo nmap -g 53 192.168.1.10
```

Fragmentar paquetes para bypassear inspección de paquetes


*8-byte*

```sh
sudo nmap -f 192.168.1.10
```

Fragmentación más agresiva: 

*16-byte*

```sh
sudo nmap -ff 192.168.1.10
```

Decoy Scanning

Hacer que el scaneo provenga de multiples IPs al enviar paquetes señuelos

```sh
sudo nmap -D 192.168.1.1,192.168.1.2 192.168.1.10

#Random IPs
sudo nmap -D RND:5 192.168.1.10
```

Idle Zombie Scan

Manda paquetes de una tercera parte "zombie" IP para encubrir tu IP actual

```sh
sudo nmap -sl 192.168.1.5 192.168.1.10
```

Para evasión de IDS: 

Timing Options 

Relantiza los escaneos:

```sh
sudo nmap -T0 192.168.1.10
sudo nmap -T1 --scan-delay 15s 192.168.1.10
sudo nmap -T2 --max-rtt-timeout 2000 192.168.1.10
```

Randomizar escaneo de hosts:

```sh
nmap --randomize-hosts 192.168.1.0/24
```

Data Padding

Añade data a los paquetes para bypassear la detección por firmas 

```sh
sudo nmap --data-length 120 192.168.1.10
```

