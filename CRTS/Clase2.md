# CRTS Sesión 2

La carpeta proc es la carpeta vital del sistema
Esta la información de cada proceso que se está ejecutando en tu maquina Linux

```sh
grep -EHirn "accesskey|admin|aes|api_key|apikey|checkClientTrusted|crypt|http:|https:|password|pinning|secret|SHA256|SharedPreferences|superuser|token|X509TrustManager|insert into"
```

Archivos y ubicaciones críticas para Red Team:

```sh
C:\Windows\System32\config\SAM
C:\Windows\System32\config\System
HKLM\SAM y HKLM\SYSTEM
C:\Windows\[usuario]\NTUSER.DAT\SAM
C:\Windows\System32\winevt\Logs\
C:\Windows\[usuario]\AppData\Roaming\Microsoft\Windows\PowerShell
```

## Redes

7 Capas OSI

- Capa 7: Aplicación
- Capa 6: Presentación
- Capa 5: Sesión
- Capa 4: Transporte
- Capa 3: Red
- Capa 2: Enlace de datos
- Capa 1: Física

4 Capas TCP/IP

- Capa 4: Aplicación 
- Capa 3: Transporte (TCP/UDP)
- Capa 2: Internet (IP, ICMP)
- Capa 1: Acceso a Red (1 y 2 del OSI)

[linPEAS](https://github.com/peass-ng/PEASS-ng/tree/master/linPEAS)