# Sesión 3

## FlareVM

```sh
### En CMD
cmd > sha256sum.exe .\Malware.Unknown.exe
cmd > md5sum.exe .\Malware.Unknown.exe

### En Powershell
PS > Get-FileHash -Algorithm MD5 .\Malware.Unknown.exe
PS > Get-FileHash -Algorithm SHA256 .\Malware.Unknown.exe

### Uso de FLOSS para extraer Strings
FLOOS.exe .\Malware.Unknown.exe
FLOOS.exe -n 20 malware.exe
```

## DLL (Dynamic Link Library) y Windows API

Es una biblioteca que contiene código y datos reutilizables que pueden ser cargados por múltiples programas al mismo tiempo. En lugar de incluir todo en el código, se delegan a DLLs del sistema, reduciendo el tamaño de los binarios y centralizando funciones críticas. 

Los DLLs son importantes porque todo programa en Windows necesita interactuar con ellas para realizar acciones sobre el sistema operativo.

Windows API son el conjunto de funciones expuestas por estas DLLs para permitir que el software interactue con el nucleo del sistema.

### Liberias comunes

- KERNEL32.dll 	-> Creación de archivos, inyectar memoria ejecutable, controlar procesos. Normalmente usado por loaders, malware avanzado, ransomware
- ADVAPI32.dll 	-> Creación/Modificación de servicios, gestionar permisos y utilizar funciones criptograficas. Esta DLL es crítica porque permite establecer persistencia, creando servicios que se inician al arrancar el sistema o modificando claves del registro
- USER32.dll   	-> Interacción con el usuario e interfaz gráfica. 
- WININET.dll  	-> Proporciona comunicaciones HTTP/HTTPS, es un indicador que tiene la capacidad de comunicarse con servidores remotos, descargar archivos o enviar información. En malware suele asociarse con comunicaciones con servidores de comando y control (C2)
- URLMON.dll   	-> Descarga de recursos de Internet mediante protocolos HTTP/HTTPS/FTP. Permite descargar directamente archivos, almacenarlos con una sola llamada, sin necesidad de implementar lógica de red compleja ni manejar sesiones.
- MSVCRT.dll   	-> Herramientas básicas de gestión de memoria, manipulación de cadenas, etc. Para malware escrito en C o C++
- CRUNTIME140.dll	-> Binarios compilado en versiones modernas de Visual C++. Esto sugiere que esta diseñado para sistemas actuales y no para legacy

[Link](https://learn.microsoft.com/en-us/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775123(v=vs.85))
[Malapi.io](https://malapi.io/)

## IAT (Import Address Table)

Dentro de un .exe, la IAT es un diccionario de librerias y funciones que son esenciales para el funcionamiento del programa.

Ejemplo: 

```sh
kernel32.dll
	CreateFileA
	WriteFile
	CloseHandle
```