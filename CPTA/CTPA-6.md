# Clase 6

```sh
schtasks /query /fo LIST /v
```

Lista todos los servicios que se están ejecutando

```sh
.\accesschk.exe /accepeula -quvw cfc.user C:\DevTools\CleanUp.ps1
```

Comando en PowerShell para revisar permisos 

```sh
tasklist /v

tasklist /V | findstr mspaint.exe
```

Hay una vulnerabilidad en la cual el acceso directo ejecuta la aplicación como ADMIN y en caso nos deje abrir archivos como el caso de PAINT.exe podemos abrir servicios

```sh
C:\Windows\System32\cmd.exe
```

y el CMD estará bajo el usuario que es propietario del proceso PAINT.exe, que en este caso sería ADMIN

Para por ejemplo RemoteMouse.exe se puede ejectuar con el "Path" del cmd una shell con Autority/System, porque RemoteMouse es una aplicación instalada bajo ese perfil