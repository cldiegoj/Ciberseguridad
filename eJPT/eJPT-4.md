# Enumeración de servicios

Es el proceso de extraer información detallada de los servicios corriendo en los puertos abiertos que hemos identificado durante el scaneo.

La enumeración de servicios provee: 

- Versión del servicio
- Cuentas de usuario y grupos
- Recursos compartidos
- Configuración de red y topologia
- Detalles del sistema operativo 
- Configuraciones erroneas de seguridad
- Credenciales predeterminadas y contraseñas debiles
- Bases de datos accesibles y aplicaciones

## Enumeración especifica 

| Servicio | Puerto | Herramientas |
| :---: | :--- | :--- |
| SMB/SAMBA | 445,139 | enum4linux, smbclient, smbmap, crackmapexec |
| FTP | 21 | ftp, nmap scripts (ftp-anon, ftp-bounce) |
| SSH | 22 | ssh, hydra, nmap scripts (ssh-auth-service) |
| HTTP/HTTPS | 80,443 | gobuster, nikto, dirb, burp suite, curl |
| MySQL | 3306 | mysql client, nmap scripts (mysql-*) |
| RDP | 3389 | xfreerdp, rdesktop, nmap scripts |

