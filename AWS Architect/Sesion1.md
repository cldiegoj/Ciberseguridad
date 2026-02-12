# Curso AWS Architect PIT UNI

## ¿Qué es computación en la nube?

Entrega bajo demanda de recursos de TI a través de internet con precio de pago por uso

## Tipos de implementación en la nube

- En las instalaciones
- Basada en la nube
- Híbrida

## Principales beneficios

- Operar con gastos variables en lugar de gastos fijos
- Aprovechar las economías de escala masivas
- Dejar de hacer suposiciones sobre la capacidad
- Aumentar la velocidad y agilidad
- Dejar de gastar dinero en la ejecución y el mantenimiento de centros de datos
- Convertirse en una empresa global en minutos

## CAPEX Y OPEX - TCO



## Tipos de servicios

- Infraestructura como servicio (IaaS)
	Proporciona bloques de construcción para las IT en el cloud
	Proporciona redes, ordenadores y espacio de almacenamiento de datos
	Máximo nivel de flexibilidad
	Facil paralelismo con la IT tradicional
- Plataforma como servicio (PaaS)
	Proporciona bloques de construcción para las IT en el cloud
	Proporciona redes, ordenadores y espacio de almacenamiento de datos
- Software como servicio (SaaS)
	Producto completo que es ejecutado y gestionado por el proveedor de servicios

## Regiones de AWS

- Una región se compone de multiples zonas
- La mayoría de los servicios de AWS son de ambito regional

### ¿Qué se debe tener en cuenta para escoger una región?

- Cumplimiento
- Proximidad a los clientes
- Servicios disponibles
- Precios

## Zonas de disponibilidad de AWS

- Una región tiene al menos 3 AZ y puede llegar hasta 6 AZ
- Cada AZ esta compuesta por una o más centros de datos físicos, diseñados para operar de forma independiente
- Las AZ están fisicamente separadas entre sí, de manera que se encuentran aisladas ante fallas o desastres a nivel de zonas
- Estan conectadas con redes de alto ancho de banda y latencia ultrabaja
- Las AZ dentro de una región están interconectadas mediante enlaces de red privados de alto ancho de banda y latencia ultrabaja, lo que permite la replicación rápida y seguira de datos.

## Responsabilidades

- Responsabilidad del cliente 

```sh
Datos del cliente
Cifrado de datos del cliente
```

- Responsabilidad del cliente o de AWS

```sh
Cifrado del servidor
Protección del tráfico de red
Administración de plataforma y aplicaciones
Configuración de SO, red y firewall
```

- Responsabilidad del AWS 

```sh
Software para computación, almacenamiento, base de datos y redes
Hardware, Infraestructura global de AWS
```