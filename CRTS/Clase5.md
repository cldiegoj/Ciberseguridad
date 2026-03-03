# Clase 5

## Shodan 

[Shodan](https://www.shodan.io/dashboard)

Ejemplos de Dorks:

```
country:es os:Windows city:Lima hostname:nextnet.com.pe org:"VIETTEL PERÚ S.A.C. " country:pe port:22

port:22 "default password"

city:Lima

webcam country:pe
```

## Censys

[Censys](https://platform.censys.io/home?_cb=cc2115)

Ejemplos de Dorks:

```
host.services.cert.names:"rimac.com"
```

## CRT.sh

[CRT.SH](crt.sh)

Busqueda de certificados en base a un dominio, para saber si podemos saber o descargar el cerficado de un dominio publico

```sh
psql -h crt.sh -p 5432 -U guest certwatch


```


## Amas

Herramienta global 

```sh
amass enum -d rimac.com -active -brute -w /usr/share/seclists/Discovery/DNS/dns-Jhaddix.txt -o amass_result.txt
```

## Subfinder

Más rapido que amass, naturalmente por la volumetría de la lista que se pasa en amass y no en subfinder

```sh
subfinder -d rimac.com -all -recursive -o subfinder_results.txt

cloud_enum -k rimac.com --disable-aws --disable-gcp 
```

## Acceso Inicial

Estrategia de entregar un payload u obtener credenciales que den un punto de apoyo dentro del entorno objetivo, sin activar detección

- No solo concentrarse en obtener solo 1 usuario valido
- Distintas tecnicas/tacticas especificas
- Casi todo es phishing

-> MITRE ATT&CK TA0001

-> APTs documentados
	- APT29
	- Araña dispersa
	- Grupo Lazaro
	- Ventisca de medianoche
	- Ventista estelar 
	- ALPHV/Gato Negro
	- Cl0p
	- FIN7
	
## Phishing y Spearphishing

### Pretexto 

Determina el exito o fracaso del compromiso...

- Tiene que tener concordancia
- Generar urgencia
- Imitar a remitente confiable
- No pedir demasiado

### Herramientas

TeamsPhisher -- Enviar mensajes de phishing a inquilinos externos de Teams
GoPish 		 -- Administra todo el ciclo de vida de 