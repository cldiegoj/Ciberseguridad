# Clase 3

El red team solo tiene 2 marcos de referencia

## MITRE ATT&CK 

[Link](https://attack.mitre.org/)
[Navigator](https://mitre-attack.github.io/attack-navigator/)
Standar Americano

Matrices principales: 
- Enterprise
- Mobile
- ICS

### 14 Tácticas

1. Reconnaissance
2. Resource Development
3. Initial Access
4. Execution
5. Persistence
6. Privilege Escalation
7. Defense Evasion
8. Credential Access
9. Discovery
10. Lateral Movement
11. Colection
12. Command and Control
13. Exfiltration
14. Impact

### Aplicación Práctica de MITRE

En operaciones Red Team 

- Planificar escenarios de ataques basados en adversarios reales
- Mapear las técnicas utilizadas durante las operaciones
- Documentar gaps de detección en el Blue Team
- Crear informes estructurados y comparables

## TIBER-EU 

Desarrollado por el Banco Central Europeo para realizar pruebas controladas de ciberataques contra entidades del sector financiero

### Caracteristicas

- Basado en inteligencia de amenazas
- Enfoque holístico
- Supervisión regulatoria
- Confidencialidad

### Fases de TIBER-EU

- Identification
- Preparation
- Testing
- Closure

## Comando y Control (C2)

Infraestructura centralizada que permite a los operadores mantener comunicación con los sistemas comprometidos, ejecutar comandos, exflitrar datos y gestionar operaciones de post explotación

### Por qué instalar C2 en un servidor externo?

Se instala en servidores externos en lugar de red locales por lo siguiente:

- Separación de Infraestructura: Proteger la red interna de posibles contramedidas o investigaciones forenses del blue team
- OPSEC: Evitar exponer tu IP real y ubicación fisica
- Disponibilidad: Los servidores externos tienen mejor uptime y conectividad desde redes objetivo
- Evasión: Permite usar dominios legítimos, certificados SSL válidos y tecnicas de domain fronting
- Escalabilidad: Facilita el despliegue de multiples servidores de redirección para ofuscar la Infraestructura real

### Componentes de un C2

- Servidor C2 Principal: Nucleo que gestiona operadores, agentes y datos. Debe estar oculto detrás de redirectors
- Redirectors: Servidores intermedios que redirigen tráfico al C2 principal, protegiendo su ubicación real.
- Agentes/Beacons: Malware instalado en sistemas objetivo que se comunica con el C2.
- Listeners: Servicios en el C2 que esperan conexiones de agentes
- Perfil de C2: Configuración que define como se comunican los agentes, imitando tráfico legítimo
- Infraestructura de dominio: Dominios categorizados y con buena reputación para evasión

### Arquitectura C2 Recomendada

1. Dominio con certificado SSL válido
2. Servidor Redirector
3. Servidor C2 Principal
4. VPN o SSH tunnel entre redirector y C2 principal
5. Loggin centralizado para análisis forense interno

