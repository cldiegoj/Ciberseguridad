# Herramienta de enumeración y fuerza bruta

gobuster tiene varios apartados para distintas cosas

```sh
dir		enumeracion de archivos/directorios
vhost	enumeracion de vhost
dns		enumeracion de subdominios dns
fuzz	activa el modo de "fuzzeo", reemplaza la palabra FUZZ en el URL
tftp	enumeracion de tftp
s3		enumeracion de aws bucket
gcs		enumeracion de gcs bucket
```

## dir

Como parametros obligatorios necesita "URL" y "Wordlist"

Ejemplo:

```sh
gobuster -u 10.10.10.10 -w list.txt
```

Nota: Si queremos buscar con extensiones de archivo se utiliza el parametro -x

```
-x .php
```

## dns

Del mismo modo que dir se necesita "domain" y "Wordlist", adicionalmente también se le añade el parametro --wildcard

Ejemplo: 

```sh
gobuster dns example.com -w list.txt --wildcard 
```

# vhost

Un host virtual es un servidor usado para tener multiples dominios que apuntan al mismo servidor, usando vhost el servidor es capaz de distingir las peticiones de distintos dominios

```sh
gobuster vhost -w list.txt -u example.com
```