## IAM en AWS

Contraseña: PassCldiego2611

A un usuario se le pueden aplicar politicas de usuario, a que recursos, que acciones van a tomar.
Las politicas por detrás son un JSON, 

Atributos: 

- Version
- Statement
- Sid
- Effect
- Action
- Resource

Ajustar solo las politicas justas y necesarias: Minimo privilegio

## Hipervisores

Utilizar bastantes Sistemas Operativos dentro de un mismo hardware

### Tipo 1

Cuando se instala el supervisor directamente al hardware, permitiendo tener varios sistemas operativos sin necesidad de tener un SO base.

### Tipo 2

Al instalar un SO base como Windows 11, se puede instalar un supervisor de tipo 2 que segmenta los recursos para el W11 para otros sistemas operativos.

## Capacidad de computo

- Se refiere a la potencia de procesamiento necesaria para ejecutar aplicaciones, administrar datos y realizar calculos
- En nube está disponible bajo demanda
- Es posible acceder a ella de forma remota sin tener que poseer ni mantener un hardware
- Basicamente es poder tener maquinas virtuales con un proveedor para ejecutar aplicaciones y tareas a través de internet.

## Amazon EC2 (Elastic Compute Cloud)

- Es una maquina virtual
- SO: Linux, Windows o Mac OS
- Potencia de calculo y nucleos
- Memoria de acceso aleatorio
- Espacio de almacenamiento
- Tarjeta de red
- Reglas de firewall
- Script de arranque

### Pasos

Al lanzar una instancia de EC2, se comienza por seleccionar una imagen de maquina de Amazon (AMI), que define el SO y puede incluir software adicional. También se puede seleccionar el tipo de instancia, que determina los recursos de hardware subyacentes, como el CPU memoria y red.