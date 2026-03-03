# Capitulo 1

## Pentesting 

### Tipos de pruebas de penetración

- Caja negra: Sin conocimientos del sistema, simula una perspectiva de un atacante externom y consume más tiempo pero es el más realista
- Caja blanca: El testeador tiene total conocimiento sobre el sistema/infraestructura, se tiene acceso al código fuente, diagramas, credenciales, etc; y cubre más pero es menos realista
- Caja Gris: El testeador tiene conocimiento medio, por ejemplo acceso a nivel de usuario, balancea realismo con eficiencia y es el más común en escenarios de la vida real.

### Fases de la metodología

1. Planeamiento y reconocimiento: 
2. Escaneo y enumeración
3. Evaluación de vulnerabilidades
4. Explotación
5. Post-Explotación
6. Reporting

### Consideraciones Eticas y Legales

- Siempre obtener autorización escrita antes de testear algun sistema
- Mantenerse dentro del alcance definido
- Evitar dañar o inhabilitar servicios
- Mantener confidencialidad de la información descubierta

## Conceptos básicos de redes

### Modelo OSI

1. Capa fisica
2. Capa de enlace de datos
3. Capa de red
4. Capa de transporte
5. Capa de sesión
6. Capa de presentación
7. Capa de aplicación

### TCP/UDP 

- TCP

SYN -> SYN-ACK -> ACK

3-Way Handshake

- UDP 

Mnada los datos y espera que lleguen ahí, no hay confirmación

### Puertos

80 	-> HTTP
22 	-> SSH
445	-> SMB


### DNS

Domain Name System

Las computadoras se comunican con IPs, por eso existe el DNS para que las personas no tengan que memorizar todas las IPs que utilizan, solo el nombre. Ejm: google.com

### Estructura de archivos Linux

- /home/[username]: Archivos personales y espacio de trabajo (Normalmente se señaliza con "~")
- /root: Directorio del usuario root
- /etc: Archivos de configuración del sistema
- /tmp: Archivos temporales
- /var: Data variable
- /usr/bin: Programas de usuario y aplicaciones
- /opt: Paquetes de software opcionales

### Comandos de navegación

- pwd
- ls
	- ls -l: Detallado
	- ls -la: Incluye archivos ocultos
	- ls -lh: "Human-readable file sizes"
- cd
- mkdir 
	- mkdir -p notes/recon/nmap: Crea directorios anidados
- touch
- cp [file.txt] [file2.txt]
	- cp -r [folder1] [folder2]

- mv [oldname.txt] [newname.txt]
	- mv [file.txt] /tmp/ 
- rm 
	- rm -r folder/: Borrar un directorio de forma recursiva
	- rm -rf folder/: Fuerza borrar
- cat
- less: Visualizar un archivo una pagina a la vez
- head: Primeras lineas
- tail: Ultimas lineas

### Permisos de archivos

```sh
-rwxr-xr-x 1 kali kali 4096 Dec 10 10:30 script.sh
```

"-" Tipo de archivo ("-" Archivo "=" Directorio)

rwx Permisos de propietario
r-x Permisos de grupo
r-x Permisos de otros

```sh
chmod +x script.sh 	- Hace el archivo ejecutable
chmod 755 script.sh - rwxr-xr-x
chmod 644 file.txt  - rw-r-r-
```
Numeros de Permisos

- 777 -- rwxrwxrwx (Todos pueden hacer todo)
- 755 -- rwxr-xr-x (Owner full, otros read/execute)
- 644 -- rw-r-r-   (Owner read/write, Otros solo read)
- 600 -- rw------- (Solo el Owner puede read/write)

### Busqueda de Strings

grep

Busca patrones en archivos

```sh
grep "admin" users.txt — Find lines containing "admin"
grep-i "password" file.txt — Case-insensitive search
grep-r "config" /etc/ — Search recursively in directory
grep-v "comment" file.txt — Show lines NOT containing "comment"
```

find 

Busca archivos por nombre, peso, permisos, etc

```sh
find /-name "password.txt" 2>/dev/null — Find file by name
find /home-type f-size +10M — Files larger than 10MB
find /-perm-4000 2>/dev/null — Find SUID files (privilege escalation)
```

cut

Extrae columnas especificas del texto

```sh
cat users.txt | cut-d:-f1 — Extract first field (delimiter: colon)
```

sort y uniq

Organiza la data

```sh
sort users.txt — Sort alphabetically
sort-u users.txt — Sort and remove duplicates
cat data.txt | sort | uniq — Remove duplicates
```

### I&O Redirecciones

- ">" Sobreescribe el archivo
- ">>" Añade al archivo
- "<" Redirecciona el input del archivo
- "|" Manda el output a otro Comandos
- "2>" Redirecciona errores
- "2>/dev/null Descarta errores

### Comandos de información del sistema

- whoami
- id: User ID
- uname: Show system information
- ifconfig/ip

### Comandos de red

- ping
- netstat: Conexiones de red
- wget and curl: Descarga de archivos desde la red

### Gestión de procesos

- ps: ver procesos activos
- kill