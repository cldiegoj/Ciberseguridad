# Evaluación de vulnerabilidades

Una vulnerabilidad es una debilidad en un sistema de información, procedimientos de seguridad, controles internos o implementaciones que pueden ser explotados por un agente maligno

- Vulnerabilidad: La debilidad en sí
- Exploit: El metodo o codigo usado para aprovechar la vulnerabilidad
- Payload: El resultado de la ejecución del código malicioso

## Clasificación de vulnerabilidades

Por Severidad: 

- Critico: Compromete todo el sistema 
- Alto: Impacto significativo en confidencialidad, integridad, disponibilidad
- Medio: Impacto moderado, requiere condiciones especificas
- Bajo: Impacto minimo, requiere acceso local o interacción de usuario

Por Tipo:

- Defectos de diseño
- Implementación de bugs
- Problemas de configuración
- Falta de parches de seguridad

## CVSS Scoring System

CVSS v3.1: 

| Metrica | Descripción |
| :---: | :--- |
| Vector de ataque | Red, Adyacente, Local o Fisico |
| Complejidad del ataque | Alta o baja |
| Privilegios requeridos | Ninguno, Bajos o altos |
| Interacción de usuario | Ninguno o requerido |
| Alcance | Cambiado o Igual |
| Confidencialidad | Ninguno, Bajo o Alto |
| Integridad | Ninguno, Bajo o Alto |
| Disponibilidad | Ninguno, Bajo o Alto |

Rangos de puntaje: 

- 0.0: Ninguno
- 0.1 a 3.9: Bajo
- 4.0 a 6.9: Medio
- 7.0 a 8.9: Alto
- 9.0 a 10.0: Critico

[Calculadora de CVSS](https://www.first.org/cvss/calculator/3.1)

## Bases de datos de vulnerabilidades

### Bases primarias

- CVE (Common Vulnerabilities and Exposures)

Provee identificadores unicos para vulnerabilidades conocidas

	* Formato: CVE-YEAR-NUMBER
	* Ejemplo: CVE-2021-44228 (Log4Shell)

- NVD (National Vulnerability Database)

Base de datos de vulnerabilidades de NIST que mejora las entradas de CVE

	* CVSS v2 y v3
	* CPE 
	* CWE
	* Informacion de parches y referencias
	* Disponibilidad de exploits e indicadores

[NIST NVD](https://nvd.nist.gov/)

- Exploit-DB 

Contiene pruebas de concepto de exploits

	* Codigos de exploit verificados y no-verificados
	* Ejemplos de Shellcode
	* Documentación
	* Google Hacking Database (GHDB)
	
[Exploit-DB](https://www.exploit-db.com/)

### Bases secundarias

- CWE (Common Weakness Enumeration)

Categoriza la causa raíz de las vulnerabilidades

	* CWE-79: XXS 
	* CWE-89: SQLi
	* CWE-119: Buffer Overflow
	* CEW-200: Information Exposure
	* CWE-287: Improper Authentication
	
Otros recursos:

- Packet Storm
- SecurityFocus
- VulnDB
- GitHub Security Advisories

## Uso de searchsploit

searchsploit es el CLI de la base de datos de exploits, provee acceso offline para miles de exploits


Uso basico:

```sh
searchsploit <search term>
```

Flags esenciales:

| Flag | Funcion | Descripción |
| :---: | :--- | :--- |
| -t | Buscar titulo | Buscar solo es titulos de exploit |
| -e | Busqueda exacta | Requerir una busqueda exacta de frase |
| -m ID | Mirror | Copiar el exploit en el directorio actual |
| -x ID | Examinar | Ver el codigo del exploit |
| -p ID | Path | Muestra el path |
| -w ID | Web | Muestra el URL del Exploit |
| -c | Case sensitive | Habilita el case-sensitive search |
| -nmap file | Integración con nmap | Busca desde nmap xml output |
| -u | update | Update local database |

Mantenimiento de database:

```sh
sudo searchsploit -u

searchsploit --version

ls -lh /usr/share/exploitdb/
```

## Escaneo de vulnerabilidades automatizado

Metodologías de escaneo:

| Aspecto | No-Autenticado | Autenticado |
| :---: | :--- | :--- |
| Perspectiva | Atacante externo | Vista interna/privilegiada |
| Credenciales | Ninguna | Credenciales validas siministradas |
| Detección | Servicios de red solo | Acceso completo al sistema |
| Verificación de parches | Banner version | Direct Path check |
| Falsos positivos | Alto 30-40% | Bajo 5-10% |
| Casos de uso | Pentesting externo | Auditoría interna, cumplimiento |

Flujo de trabajo del assessment de vulnerabilidades 

1. Discovery de assets
2. Escaneo de vulnerabilidades
3. Analisis y validación
4. Risk Assessment
5. Reporting 
6. Remediación 
7. Verificación 
8. Monitoreo continuo

Herramientas populares de escaneo: 

- Nessus

CLI SCAN: 

```sh
/opt/nessus/bin/nessuscli policy list

# START SCAN 
/opt/nessus/bin/nessuscli scan new \
	--name="Network Scan" \
	--targets="192.168.1.0/24" \
	--policy="Basic Network Scan"
```

	Web Interface: 

	- Scan Status
	- Policy Type
	- Severity Base
	- Vulnerability Bar
	- Percentage Complete
	- Host Count

	Reporte de Nessus: 

	- Sev (Severity)
	- CVSS
	- VPR
	- EPSS 
	- Name 
	- Family
	- Count 

- OpenVAS

Marco de trabajo 

| Risk Level | Caracteristicas | SLA | Acción |
| :---: | :--- | :--- | :--- |
| Critico | Gran impacto | 24-48 horas | Parche inmediato |
| Alto | Alto impacto | 1-2 semanas | Priorizar remediación |
| Medio | Medio impacto | 1-3 meses | Planificar remediación |
| Bajo | Bajo impacto | 3-6 meses | Revisar y planificar |
| Informativo | Sin riesgo directo | Monitorear | Documentar |

CLI SCAN: 

```sh
omp --username admin --password admin \
	--xml="<create_target>
	<name>Internal Network</name>
	<hosts>192.168.1.0/24</hosts>
	</create_target>"
	
# START SCAN
omp --username admin --password admin \
	--xml="<create_task>
	<name>Full Scan</name>
	<target id='target-uuid'/>
	<config id='full-and-fast'/>
	</create_task>"
```

- Nikto

Escanner de vulnerabilidades web 

```sh
nikto -h http://target.com

nikto -h http://target.com -p 8080

nikto -h http://target.com -o scan_results.html -Format html

nikto -h hosts.txt
```

- Nmap NSE Scripts 

```sh
nmap --script vuln target.com

nmap --script smb-vuln-ms17-010 192.168.1.0/24

nmap --script http-vuln-* target.com

nmap --script ssl-* -p 443 target.com
```

