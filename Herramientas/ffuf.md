# Herramienta de enumeración y fuerza bruta

```sh
ffuf -u HOST/FUZZ -w LISTA.txt
```

## Parametros

```sh
-u es para especificar el host
-w es para especificar el diccionario/lista de palabras
```

### Matcher

Muestra en el output solo los que coincidan con el parametro

```sh
-mc Matchea codigos de status HTTP
-ml Matchea cantidad de lineas de respuesta
-mr Matchea regexp
-ms Matchea tamaño de respuesta HTTP
-mt Matchea numero de milisegundos de la respuesta: >100 o <100
-mw Matchea numero de palabras en la respuesta
```

Ejemplo:

```sh
ffuf -u http://google.com/FUZZ -w common.txt -mc 200

Solo mostrará resultados con código de respuesta HTTP 200
```

### Filter

Elimina del output los que coinciden con el parametro

```sh
-fc Filtra codigos status HTTP
-fl Cantidad de lineas de respuesta
-fr Filtra regexp
-fs Filtra tamaño de respuesta http
-ft Filtra numero de milisegundos de la respuesta: >100 o <100
-fw Filtra el numero de palabras en la respuesta
```

Ejemplo:

```sh
ffuf -u http://google.com/FUZZ -w common.txt -fs 12169

No mostrará resultados con tamaño de respuesta de 12169
```