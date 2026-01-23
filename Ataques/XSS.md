## Descripción

Cross Site Scripting consiste en "inyectar" código malicioso, generalmente en JavaScript, donde se ejecutan sentencias de código que permiten robar datos como cookies, token de sesión, defacement, etc.

### XSS Reflejado
El script malicioso se refleja en la respuesta HTTP actual (ej. en un enlace de búsqueda)

### XSS Almacenado 
El script se guarda en el servidor (base de datos) y se sirve a múltiples usuarios

### XXS Basado en DOM
La vulnerabilidad reside en el código del lado del cliente, manipulando el DOM (Modelo de Objetos del Documento)