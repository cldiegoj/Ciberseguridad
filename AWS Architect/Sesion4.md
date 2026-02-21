## EFS - Clases de almacenamiento

- Niveles de almacenamiento
	- Estandar (Archivos de acceso frecuente)
	- Acceso infrecuente (Menor precio de almacenamiento)
- Disponibilidad
	- Estándar (Multi AZ)
	- Una zona (Una AZ)
	
## Amazon Simple Storage Service (Amazon S3)

Servicio de almacenamiento de objetos de alta disponibilidad y completamente administrado para almacenar y recuperar cualquier cantidad de datos como objetos. Durabilidad del 99,9%, lo que significaría que los datos cuentan con una alta protección contra las perdidas y optimización de costos, control de versiones y administración de ciclo de vida y clases de almacenamiento.

### Elementos

- Objetos de S3
	Pueden ser de cualquier tipo de archivo, poseen identificador de versión
- Buckets de S3
	Tienen un nombre único a nivel global de todo AWS
	Se debe especificar la región en la que residirá

- Los valores de los objetos son el contenido del cuerpo
	- Max tamaño del objeto es 5TB
	- Si subes más de 5GB debe utilizar subida multiparte
	
## Amazon Relational Database Service (Amazon RDS)

Servicio de bases de datos relacionales administrado que gestiona tareas rutinarias de las BD, copias de seguridad, parches, aprovisionamiento de hardware.
Admite varios tipos de clases de instancias de bases de datos que optimizan la memoria, rendimiento e I/O
Para resiliencia se ofrece multi-AZ, copias de seguridad automatizadas, pero también puede crear copias de seguridad manualmente mediante instantaneas de BD, RDS ofrece carateristicas de seguridad que incluyen el aislamiento de la red, el cifrado en tránsito y cifrado en reposo.

* Motores de base de datos compatibles
	* Amazon Aurora
	* MySQL
	* PostgreSQL
	* MSSQL Server
	* Maria DB
	* Oracle Database

KMS Servicio de administración de llaves

### Beneficios

* Optimización de costos: Solo se debe pagar por los recursos de computación y almacenamiento que consume mediante un modelo flexible de pago por uso.

* Implementación multi-AZ: Mejora la fiabilidad de las BDs mediante Implementaciones multi-AZ. Replicando automaticamente los datos en una instancia en espera en una zona de disponibilidad diferente. RDS realiza automaticamente la conmutación por error a la instancia en espera, sin intervención manual.

* Optimización de rendimiento: Mejora el rendimiento mediante la administración automatizada de las tareas de asignación, supervisión y optimización de recursos

* Controles de seguridad: Mediante varias capas de protección incluido el aislamiento de VPC y el cifrado. Aprovecha copias de seguridad automatizadas y ofrece implementaciones multi-AZ para brindar resiliencia frente a posibles errores del sistema