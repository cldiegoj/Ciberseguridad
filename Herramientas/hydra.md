# Herramienta de fuerza bruta

Ejemplo de Sintaxis: 

```sh
hydra -l admin -P /usr/share/wordlists/rockyou.txt ftp://172.17.0.2
```

Donde: 

Se comienza con hydra (comando)
Sigue definir el "usuario", donde "-l" en minuscula es cuando se define un usuario especifico, "-L" es cuando se tiene un archivo con distintos usuarios para el login

Del mismo modo se utiliza para la contraseña, "-p" para definir una contraseña especifica y "-P" para pasar un archivo listado de contraseñas a probar

También cuando se quieren atacar varias IPs o servidores se utiliza el parametro "-M"