# Aut0test
Framework to automatize vulnerability and gathering scans


Tools/scripts used by Aut0test
--------------------------
Droopscan - https://github.com/droope/droopescan

Nikto     - https://github.com/sullo/nikto

OpenVAS   - http://www.openvas.org

SSH-Audit - https://github.com/arthepsy/ssh-audit

TestSSL   - https://testssl.sh/

WhatWeb   - https://github.com/urbanadventurer/WhatWeb

WPScan v3 - https://github.com/wpscanteam/wpscan-v3


Installation guide
-------------------
Use a Kali OS or any other linux enviroment pre-installing all tools that Aut0test use.

Create the "temp" folder in the root of the file directory.

Create the "pentestTools" folder in the "/root" directory and clone there https://github.com/wpscanteam/wpscan-v3

Start OpenVAS services before execute the tool.

In OpenVAS, create the user "admin" with password "admin" or change the user and password on the scripts.



User guide
-------------------
To start the tool, execute the Aut0test.py file and select the IP and level of scan (1 to 3).
