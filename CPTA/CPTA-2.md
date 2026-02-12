# Conceptos básicos

## Punto de partida
En cualquier ataque informatico exitoso hay un momento clave en el que todo cambia, donde el atacante deja de ser un usuario más y pasa a tener control total. Ese momento se llama elevación de privilegios.

## Privilegios

Separan a los usuarios normales de los administradores
Administradores de System o root
Procesos confiables de procesos limitados

La elevación de privilegios es consecuencia de:
- Errores de configuración
- Software vulnerable
- Permisos mal asignados
- Suposiciones incorrectas por parte de administradores

## Objetivos
Cuando uno logra escalar privilegios, puede:
* Desactivar antivirus y EDR
* Leer archivos sensibles
* Crear usuarios persistentes
* Manipular servicios y tareas programadas
* Pivotar hacia otros sistemas
* Borrar rastros del ataque
* Entre otros...

## Cyber Kill Chain

Recon -> Weaponize -> Deliver -> Exploit -> Install -> C&C -> Action

# Compartir archivos

```
python3 -m http.server 8080 
```