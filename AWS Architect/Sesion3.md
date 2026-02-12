## Preguntas - Recursos

- Tendencia multiple - Varios usuarios comparten los recursos de un servidor
- HOST DEDICADO - Tener todos los recursos de un servidor
- Instancias SPOT - Son instancias que AWS ofrece y que son muy baratas, pero AWS en cualquier momento te las puede quitar


## Escalabilidad 

Capacidad de un sistema para manejar un aumento de carga mediante la incorporación de Recursos

* Escalamiento vertical: Agregar más potencia a las maquinas existentes
* Escalamiento horizontal: Se centra en la planificación de la capacidad a largo plazo para garantizar que el sistema pueda crecer y adaptarse a más usuarios o cargas de trabajo según sea necesario

### Tipos de instancias EC2

1. De uso general
2. Optimizadas para la computación
3. Optimizadas para memoria
4. De computación acelerada
5. Optimizadas para el almacenamiento

## Elasticidad

Capacidad de ajustar automaticamente los recursos de la nube, aumentando o reduciendo su capacidad en función de la demanda en tiempo real. De este modo, un sistema puede escalar horizontalmente cuando la carga es alta y reducir recursos cuando la demanda disminuye.

Permitiendo reducir costos y garantizar un uso eficiente de los recursos.

## Responsabilidades

### Cliente 

- Datos del Cliente
- Cifrado de Datos
- Cifrado del servidor
- Protección del tráfico de red
- Administración de la plataforma y aplicaciones
- Configuración de SO, red y firewall

### AWS

- Software para computación, almacenamiento, BD y redes
- Hardware e infraestructura global

## Amazon Virtual Private Cloud (VPC)

Permite aprovisionar una sección aislada de forma lógica de la nube de AWS, donde puede lanzar recursos de AWS en una red virtual que usted defina

### Subred

Se utiliza para organizar los recursos y pueden ser de acceso público o privado, se contiene recursos como BDs 

### Amazon Virtual Private Cloud

VPC utiliza para establecer límites en sus recursos de AWS
Virtual Private Gateway (VGW), es una puerta de enlace privada virtual que permite el trafico de internet protegido entre en la VPC
VPN cira el tráfico de internet, protegiendolo de cualquier persona que intente interceptarlo o supervisarlo

## Amazon Elastic Block Store

- Una unidad de red que puede adjuntar a las instancias mientras se ejecutan
- Permite que las instancias persistan los datos
- Solo pueden montarse en una instancia a la vez
- Están vinculados a una zona de disponibilidad específica
- Para trasladar volumen, primero hay que hacer una snapshot del mismo
- Tener una capacidad provisionada, se facturará toda la capacidad aprovisionada y se puede aumentar la capacidad de la unidad con el tiempo

### Casos de uso

1. Alojamiento de base de Datos
2. Almacenamiento de copias de seguridad para aplicaciones

### Beneficios

1. Migración de datos
2. Cambios en los tipos de instancia
3. Recuperación de desastres
4. Optimización de costos
5. Ajuste del rendimiento

## Amazon EFS (Elastic File System)

- NFS gestionado
- EFS funciona con instancias EC2 en multi-AZ
- Alta disponibilidad, escalable, caro, pago por uso