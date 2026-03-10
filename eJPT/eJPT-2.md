# Capitulo 2

## Passive Information Gathering

### WHOIS LOOKUP 

La base de datos WHOIS contiene registros de información sobre dominios e IPs

Incluyendo data como:

- Detalles
- Fechas
- Servidores
- Información de contacto

```sh
$ whois securityeagle.com
```

### Enumeración de DNS

| Tipo de record | Proposito | Revelación de seguridad|
| :---: | :--- | :--- |
| A | Mapea dominios a IPv4 | Revela IPs de servidores web |
| AAAA | Mapea dominios a IPv6 | Revela infraestructura IPv6 |
| MX | Direcciones de servidor de correo | Muestra infraestructura de email, una potencial entrada |
| NS | Name servers de authoritative | Muestra la topologia de la infraestructura DNS |
| TXT | Records de texto | Puede filtrar politicas e información |
| CNAME | Alias de otro dominio | Revela relaciones de infraestructura |
| SOA | Zone authority information | Muestra servidores DNS primarios e información de zona |
| PTR | DNS reversa (IP a Dominio) | Ayuda a identificar la IP |

### Enumeración de Subdominios

Usando la web  crt.sh se puede enumerar los subdominios que se tienen registrados:

[CRT.SH](crt.sh)

También lo podemos visualizar en la linea de comandos: 

$ curl -s "https://crt.sh/?q=dominio.com&output=json" \ | jq -r '.[].name_value' | sort -u 

 ### Google Dorks
 
 Uso de operadores de busqueda avanzada para visualizar información que no debería ser de acceso publico
 
| Operador | Descripción | Ejemplo |
| :---: | :--- | :--- |
| site: | Limita resultados a un dominio | site:example.com |
| filetype: | Busca tipos de archivos especificos | filetype:pdf |
| ext: | Alternativa a filetype: | ext:xlsx |
| inurl: | Palabra aparece en la URL | inurl:admin |
| intitle: | Palabra en titulo de pagina | intitle:login |
| intext: | Palabra en contenido de pagina | intext:password |
| - | Excluye termino en resultados | -www |
| "quotes" | Match exacto de frases | "admin panel" |
| * | Wildcard character | admin* | 

### Recoleción de email y reconocimiento de empleados

Usando theHarvester para recolección de emails y subdominios

$ theharvester -d dominio.com -b all -f 500

$ theharvester -d dominio.com -b all -c 

$ theharvester -d dominio.com -b all -f report.html

## Recoleción de información activa

### DNS Zone Transfer Attack

Primer paso: 

$ host -t ns domain.com
domain.com name server ns1.domain.com
domain.com name server ns2.domain.com

Segundo paso:

$ dig axfr @ns1.domain.com domain.com
$ dig axfr @ns2.domain.com domain.com

### Port Scanning

$ nmap domain.com

Todos los puertos 

$ nmap -p- domain.com 

Puertos especificos

$ nmap -p 22,80,443,3306 domain.com

Scaneo agresivo (OS + Servicio)

$ nmap -A domain.com

### Detección de vulnerabilidades web 

$ nmap --script vuln domain.com

Methodos HTTP y opciones:

$ nmap --script http-methods domain.com

Vulnerabilidades de SSL/TLS:

$ nmap --script ssl-enum-ciphers -p 443 domain.com

Vulnerabilidades comunes: 

$ nmap --script http-title,http-headers,http-robots.txt \ domain.com

## Herramientas de reconocimiento pasivo

- whois 
- dig 
- nslookup 
- host 
- theHarvester
- Sublist3r
- Amass 
- crt.sh 
- Google Search
- Shodan