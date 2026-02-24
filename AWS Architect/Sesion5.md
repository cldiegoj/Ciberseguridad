## SQL Electron

[github:Sqlelectron](https://github.com/sqlectron/sqlectron/releases/tag/v1.39.0)

## Aurora and RDS

Puerto: 3306
admin

Contraseña con Mayus Min signos

Initial Database Name
mybd

Enpoint: database-1.c9wmoyc8k23m.us-west-1.rds.amazonaws.com

## Lambda

### Conceptos clave de los precios de AWS

- Pago por uso

Con el pago por uso, se puede adaptar a las necesidades cambiantes empresariales y reducir el riesgo de aprovisionar en exceso o sufrir una falta de capacidad

- Ahorro cuando se compromete

Para ciertos servicios, como servicios de computación de AWS, Savings Plans ofrece descuentos en comparación con los precios bajo demanda si se compromete a un plan de 1 o 3 años

- Más uso, menos dinero

Con AWS, se pueden obtener ahorros importantes a medida que aumenta su uso. Para algunos servicios, los precios son escalonados, .lo que significa que cuanto más se utilice, menos se pagará

### Factores determinantes del costo

Los precios varian en función de varios factores, como la categoría o el tipo de servicio.

Hay 3 aspectos fundamentales de costo con AWS

1. Computación 

Se paga por periodo de tiempo determinado, por ejemplo, hora o segundo. A menos que se haya hecho una reserva cuyo costo esté acordado de antemano, se pagará desde el momento en que se lance un recurso hasta el momento en que detenga la instacia

2. Almacenamiento

El precio depende en gran medida de la cantidad de almacenamiento que haya aprovisionado o de la cantidad que esté utilizando.
Para Amazon S3, el costo es escalonado, es decir, se puede optimizar los costos de almacenamiento en función de la frecuencia y rapidez con la que necesite acceder a los datos

- Precio de almacenamiento
- Precio de solicitud y recuperación de los datos
- Precio de transferencia de datos y aceleración de transferencia
- Precio de la administración y el análisis de datos
- Precio de replicación

3. Transferencia de datos

Mayoría de los casos, transferencias entrantes o entre servicios de AWS de la MISMA REGIÓN es gratuita. Existiendo algunas excepciones

La transferencia saliente de datos se suma entre distintos servicios y luego se cobra según la tarifa para transferencia saliente de datos. Cuantos más datos transfiera, menos pagará por gigabyte.

### Herramientas de AWS

#### Amazon Organizations

Proporciona administración y gobernanza centralizados de su entorno de AWS, se pueden crear agrupar y administar cuentas, como también aplicar politicas de seguridad a nivel de cuenta y consolidar la facturación con varias cuentas mediante un uníco metodo de pago

- Consolidar varias cuentas de AWS en una organización centralizados
- Implemente politicas en toda la organización

#### Panel de administración de facturación y costos de AWS

Panel de administración y costos de AWS centralizando la administración de costos y muestra los cargos actuales, el uso, las previsiones y los desgloses detallados.

- Utilice visualizaciones e informes de facturación utiles sobre el gasto mensual en AWS
- Configuire y administré metodos de pago

#### AWS Budgets

Establecer presupuestos personalizados y envía altertas cuando los costos, el uso o la cobertura o la utilización de Saving Plans y las Instancias reservadas (RI) superan los umbrales definidos

- Configurar alertas para cuando los costos proyectados superen los umbrales predefinidos
- Prevea los gastos futuros en función de las tendencias de uso actuales

#### Explorador de costos de AWS 

Ayuda a visualizar, analizar y administar los costos y el uso de AWS con gráficos, informes y pronosticos interativos, informando sobre patrones de gasto, tendencias y recomendaciones sobre instancias reservadas

- Analizar tendencias historicas de gasto para identificar oportunidades de ahorro de costos
- Prevea los costos futuros de AWS en función de los patrones de uso actuales para presupuestar de manera eficaz

#### Calculadora de precios AWS 

Crear estimaciones, ingresando configuraciones especificas, tipos de instancias, opciones de almacenamiento y volumenes de almancenamiento

- Calcular costos potenciales antes de la implementación
- Compare los costos de los diferentes servicios y configuraciones de AWS

