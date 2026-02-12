## Malware

| Tipo de malware | Descripción | Objetivo principal | Ejemplos |
| :---: | :--- | :--- | :--- |
| Virus | Código malicioso que se adjunta a archivos legitimos y se propaga al ejecutarlos | Propagación y alternación de archivos |  Melissa, CIH |
| Gusanos | Se replica automáticamente a través de la red sin intervención del usuario | Propagación masiva y saturación de recursos | Conficker, WannaCry |
| Troyano | Se hace pasar por software legítimo para engañar al usuario | Acceso no autorizado al sistema | Zeus, Emotet |
| Infostealer | Roba información confidencial como contraseñas, cookies, historiales, etc | RedLine, Raccoon, Vidar | Robo de datos y venta en mercados ilegales |
| Ransomware | Cifra archivos y exige un pago para recuperarlos | Extorsión economica | WannaCry, LockBit, Ryuk |
| RAT - Remote Access Trojan | Permite control total del sistema infectado de forma remota | Espionaje y control | DarkComet, njRAT |
| Spyware | Espía actividades del usuario sin su conocimiento | Robo de información | Pegasus, FinFisher |
| Rootkit | Oculta procesos, archivos y registros maliciosos | Evasión y persistencia | ZeroAccess, TDL4 |
| Adware | Muestra publicidad no deseada y redirige tráfico web | Generación de ingresos publicitarios | Fireball, Gator |
| Keylogger | Registra pulsaciones del teclado | Robo de credenciales | Agent Tesla, HawkEye |
| Backdoor | Proporciona acceso remoto oculto al sistema | Persistencia y control remoto | Back Orifice, Poison Ivy |
| Dropper | Malware cuya función es instalar otros malwares | Entrega de payloads | Upatre, Smoke Loader |
| Logic Bomb | Se activa al cumplirse una condición específica | Sabotaje programado | Software interno |

### Top de Malware

* LockBit
* BlackCat
* Cl0p
* Conti
* RedLine Stealer
* Raccoon Stealer
* Vidar
* Lumma Stealer
* Emotet
* TrickBot
* Cobalt Strike
* Pegasus
* Mirai

### Vectores de infección

- Phishing
- Software pirata, cracks y mods
- Publicidad maliciosa
- Archivos adjuntos infectados

## Análisis de IoC

Son pruebas o pistas forenses que quedan en un sistema o red después que se ha producido una brecha de seguridad o un ciberataque.

### IoC de red

| Indicador | Descripción |
| :--- | :---: |
| Direcciones IP maliciosas | IPs conocidas por estar asociadas con servidores C2 |
| Tráfico de red anómalo | Picos inusuales de tráfico, patrones repetitivos o volúmenes que no coinciden con el uso normal |
| Dominios y URLs sospechosos | Nombres de dominios o direcciones web vinculados a phishing | 
| Conexiones salientes inesperadas | Equipos internos que inician conexiopnes hacia destinos externos desconocidos o no autorizados |
| Uso de puertos no estándar | Comuinicación a través de puertos poco comunes para evadir controles de seguridad |

### IoC de Host

| Indicador | Descripción |
| :--- | :---: |
| Procesos sospechosos | Ejecución de procesos desconocidos, sin firma digital o que imitan procesos legítimos |
| Consumo anómalo de recursos | Uso excesivo de CPU, memoria o disco |
| Persistencia no autorizada | Mecanismos que permiten la ejecución automatica de software malicioso al iniciar el sistema |
| Servicios o tareas sospechosas | Servicios creados sin autorización o con nombres engañosos |
| Inyección de procesos | Inserción de código malicioso dentro de procesos legítimos |

### IoC basado en archivos

| Indicador | Descripción |
| :--- | :---: |
| Archivos sospechosos | Presencia de archivos desconocidos |
| Cambios no autorizados en archivo | Modificaciones en archivos del sistema |
| Archivos ocultos o protegidos | Uso de atributos ocultos para evitar la detección |
| Ejecutables en ubicaciones inusuales | Programas ejecutandose desde carpetas temporales o de usuario |
| Archivos duplicados del sistema | Copias falsas de archivos legitimos usados para suplantación |

### IoC configuración y registros

| Indicador | Descripción |
| :--- | :---: |
| Cambios no autorizados en el registro | Alteraciones en claves del sistema relacionadas con inicio o seguridad |
| Desactivación de controles de seguridad | Modificación de configuraciones para deshabilitar antivirus o firewall |
| Configuraciones de red alteradas | Cambios en DNS, proxy o rutas que redirigen el tráfico |
| Politicas de seguridad modificadas | Ajustes que reducen el nivel de protección del sistema |
| Ejecución de codigo remoto | Descarga y ejecución de comandos o scripts desde Internet |
| Descarga de componentes adicionales | Obtención de módulos adicionales tras la infección inicial |
| Acceso no autorizado a información | Intentos de lectura o extracción de datos sensibles |
| Cifrado o destrucción de archivos | Modificación masiva de archivos |
| Intentos de evasión de seguridad | Acciones para ocultarse o desactivar mecanismos de detección |

### Virus total

Herramienta en línea que analiza archivos y URLs en busca de malware utilizando multiples motores antivirus.
Proporciona un informe detallado sobre posibles amenazas detectadas
Ampliamente utilizada por profesionales de seguridad

[VirusTotal](https://www.virustotal.com/gui/home/upload)
[Intelligence Search](https://www.talosintelligence.com/reputation_center)
[AbuseIP DB](https://www.abuseipdb.com/)

#### Sandbox

[Any Run](https://app.any.run/)
[VM Ray](https://www.vmray.com/)

#### Repositorios de Malware

[Malshare](https://malshare.com/)
[Malware Bazaar](https://bazaar.abuse.ch/browse)

## MITRE ATT&CK

La matriz MITRE ATT&CK es un marco de conocimiento que clasifica las tacticas, tecnicas y procedimientos TTPs utilizados por actores de amenazas en diferentes etapas de un ciberataque, ayudando a mejorar la detección y respuesta de seguridad.

### Analogía

Tactica -> Que se quiere lograr
Tecnica -> Como se hace
Procedimiento -> Pasos especificos que sigue

### Entendiendo el MITRE ATT&CK

- Táctica
	- Impact (TA0040) -> Cifrar archivos y exigir un rescate

- Tecnicas
	- Initial Access (TA0001) -> Phishing con documentos maliciosos
	- Execution (TA0002) -> Scripting usando macros en documentos Office
	- Persistence (TA0003) -> Scheduled Task para asegurar ejecución tras reinicios
	- Privilege Escalation (TA0004) -> Exploitation for Privilege Escalation para obtener permisos de administrador
	- Defense Evasion (TA0005) -> Disabling Security Tools desactivando antivirus y backups.

- Procedimiento
	- Phishing: Envían correos con documentos de Office infectados
	- Scripting: Macros ejecutan scripts que descargan TrickBot o Emotet
	- Credential Dumping: Uso de Mimikatz para robar credenciales
	- Remote Services: Movimiento lateral con PsExec o RDP
	- Disabling Security Tools: Desactivan antivirus y eliminan backups con vssadmin delete shadows

