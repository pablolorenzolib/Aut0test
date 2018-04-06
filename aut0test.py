#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
from reportGenerator import ReportGenerator
from scanners import TestSSLScript
from scanners import SSHAuditScript
from scanners import WhatWebScript
from scanners import DroopescanScript
from scanners import NiktoScript
from scanners import WPScanScript
from scanners import OpenVasScript
from parsers import TestSSLData4ReportScript
from parsers import WhatWebData4ReportScript
from parsers import DroopescanData4ReportScript
from parsers import NiktoData4ReportScript
from parsers import WPScanData4ReportScript
from parsers import OpenVasData4ReportScript

os.system("clear")
print ("")
print ("")
print ("")
print ("+---------------------------------------------------------------+")
print ("|\t_______       _________________            _____ \t|")
print ("|\t___    |___  ___  /__  __ \_  /______________  /_\t|")
print ("|\t__  /| |  / / /  __/  / / /  __/  _ \_  ___/  __/\t|")
print ("|\t_  ___ / /_/ // /_ / /_/ // /_ /  __/(__  )/ /_  \t|")
print ("|\t/_/  |_\__,_/ \__/ \____/ \__/ \___//____/ \__/  \t|")
print ("|\t                                                 \t|")
print ("+---------------------------------------------------------------+")
print ("")
ipDomain = input("Insert the target to scan: (IP or URL. EG: target.com or 123.123.123.123): ")
print ("")
print ("")
level = input("Select the level of scan from 1 to 3: (1: lowest, 2: medium 3: high): ")


#We need to start openvas at first, because take time to start the service.
os.system("openvas-start &")

#Here we start all the modules:
print(chr(27)+"[0;94m"+ "[-] Starting module TestSSL..." +chr(27)+"[0;m")
TestSSLScript.startTestSSL(ipDomain)
print (chr(27)+"[0;92m"+ "[+] Module TestSSL finished." +chr(27)+"[0;m")
print(chr(27)+"[0;94m"+ "[-] Starting module SSH-Audit..." +chr(27)+"[0;m")
SSHAuditScript.startSSHAudit(ipDomain)
print (chr(27)+"[0;92m"+ "[+] Module SSH-Audit finished." +chr(27)+"[0;m")
print(chr(27)+"[0;94m"+ "[-] Starting module WhatWeb..." +chr(27)+"[0;m")
WhatWebScript.startWhatWeb(ipDomain,level)
print (chr(27)+"[0;92m"+ "[+] Module WhatWeb finished." +chr(27)+"[0;m")
print(chr(27)+"[0;94m"+ "[-] Starting module Droopescan..." +chr(27)+"[0;m")
DroopescanScript.startDroopescan(ipDomain)
print (chr(27)+"[0;92m"+ "[+] Module Droopscan finished." +chr(27)+"[0;m")
print(chr(27)+"[0;94m"+ "[-] Starting module Nikto..." +chr(27)+"[0;m")
NiktoScript.startNikto(ipDomain,level)
print (chr(27)+"[0;92m"+ "[+] Module Nikto finished." +chr(27)+"[0;m")
print(chr(27)+"[0;94m"+ "[-] Starting module WPScan..." +chr(27)+"[0;m")
WPScanScript.startWPScan(ipDomain,level)
print (chr(27)+"[0;92m"+ "[+] Module WPScan finished." +chr(27)+"[0;m")
print(chr(27)+"[0;94m"+ "[-] Starting module OpenVAS..." +chr(27)+"[0;m")
OpenVasScript.startOpenVAS(ipDomain,level)
print (chr(27)+"[0;92m"+ "[+] Module OpenVAS finished." +chr(27)+"[0;m")

#Now we execute the parsers
print(chr(27)+"[0;94m"+ "[-] Parsing data from scans..." +chr(27)+"[0;m")
TestSSLData4ReportScript.startTestSSL(ipDomain)
WhatWebData4ReportScript.startWhatWeb(ipDomain,level)
DroopescanData4ReportScript.startDroopescan(ipDomain)
NiktoData4ReportScript.startNikto(ipDomain,level)
WPScanData4ReportScript.startWPScan(ipDomain,level)
OpenVasData4ReportScript.startOpenVAS(ipDomain,level)

#Now we generate the report
print(chr(27)+"[0;94m"+ "[-] Generating report..." +chr(27)+"[0;m")
ReportGenerator.startReport(ipDomain,level)
print (chr(27)+"[0;92m"+ "[+] Report generated." +chr(27)+"[0;m")

