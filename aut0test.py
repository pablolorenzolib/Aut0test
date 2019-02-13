#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import socket
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

ip=''
level=1

def checkTarget():
	target =''
	try:
		target = input("Insert the target to scan: (IP or URL. Eg: www.target.com or target.com or 123.123.123.123): ")
		if target == '':
			return False
	except:
		print ("")
		print(chr(27)+"[0;91m"+ "Incorrect URL/IP format, try to write one of the following formats: www.domain.extension or domain.extension or 123.123.123.123" +chr(27)+"[0;m")
		print ("")
		return False

	#Checking if it is a valid IP.
	global ip
	
	try:
		socket.inet_aton(target)
		validIP=True
		ip=target
	except socket.error:
		validIP=False

	#If it is not a valid IP we will check if it is a valid URL.
	if not validIP:
		try:
			ip=socket.gethostbyname(target)
		except:
			print ("")
			print(chr(27)+"[0;91m"+ "Incorrect URL/IP format, try to write one of the following formats: www.domain.extension or domain.extension or 123.123.123.123" +chr(27)+"[0;m")
			print ("")
			return False

	return True


def checkLevel():
	global level
	level = input("Select the intensity level of scan from 1 to 3 (1: low, 2: medium 3: high): ")

	try:
		val = int(level)
	except ValueError:
		print ("")
		print(chr(27)+"[0;91m"+ "Incorrect number, try to write 1 or 2 or 3" +chr(27)+"[0;m")
		print ("")
		return False

	if val < 1:
		print ("")
		print(chr(27)+"[0;91m"+ "Incorrect number, try to write 1 or 2 or 3" +chr(27)+"[0;m")
		print ("")
		return False
	if val > 3:
		print ("")
		print(chr(27)+"[0;91m"+ "Incorrect number, try to write 1 or 2 or 3" +chr(27)+"[0;m")
		print ("")
		return False

	print ("")
	return True

#We need to start openvas at first, because take time to start the service.
#os.system("openvas-start &")

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

fail = checkTarget()
while not fail:
	fail = checkTarget()

fail = checkLevel()
while not fail:
	fail = checkLevel()

#Here we start all the modules:
print ("")
print(chr(27)+"[0;94m"+ "[-] Starting module TestSSL..." +chr(27)+"[0;m")
TestSSLScript.startTestSSL(ip)
print (chr(27)+"[0;92m"+ "[+] Module TestSSL finished." +chr(27)+"[0;m")

print ("")
print(chr(27)+"[0;94m"+ "[-] Starting module SSH-Audit..." +chr(27)+"[0;m")
SSHAuditScript.startSSHAudit(ip)
print (chr(27)+"[0;92m"+ "[+] Module SSH-Audit finished." +chr(27)+"[0;m")

print ("")
print(chr(27)+"[0;94m"+ "[-] Starting module WhatWeb..." +chr(27)+"[0;m")
WhatWebScript.startWhatWeb(ip,str(level))
print (chr(27)+"[0;92m"+ "[+] Module WhatWeb finished." +chr(27)+"[0;m")

print ("")
print(chr(27)+"[0;94m"+ "[-] Starting module Droopescan..." +chr(27)+"[0;m")
DroopescanScript.startDroopescan(ip)
print (chr(27)+"[0;92m"+ "[+] Module Droopscan finished." +chr(27)+"[0;m")

print ("")
print(chr(27)+"[0;94m"+ "[-] Starting module Nikto..." +chr(27)+"[0;m")
NiktoScript.startNikto(ip,str(level))
print (chr(27)+"[0;92m"+ "[+] Module Nikto finished." +chr(27)+"[0;m")

print ("")
print(chr(27)+"[0;94m"+ "[-] Starting module WPScan..." +chr(27)+"[0;m")
WPScanScript.startWPScan(target,str(level))
print (chr(27)+"[0;92m"+ "[+] Module WPScan finished." +chr(27)+"[0;m")

print ("")
print(chr(27)+"[0;94m"+ "[-] Starting module OpenVAS..." +chr(27)+"[0;m")
#OpenVasScript.startOpenVAS(ip,str(level))
print (chr(27)+"[0;92m"+ "[+] Module OpenVAS finished." +chr(27)+"[0;m")

#Now we execute the parsers
print ("")
print(chr(27)+"[0;94m"+ "[-] Parsing data from scans..." +chr(27)+"[0;m")
TestSSLData4ReportScript.startTestSSL(ip)
WhatWebData4ReportScript.startWhatWeb(ip,str(level))
DroopescanData4ReportScript.startDroopescan(ip)
NiktoData4ReportScript.startNikto(ip,str(level))
WPScanData4ReportScript.startWPScan(ip,str(level))
OpenVasData4ReportScript.startOpenVAS(ip,str(level))
print (chr(27)+"[0;92m"+ "[+] Data parsed." +chr(27)+"[0;m")

#Now we generate the report
print ("")
print(chr(27)+"[0;94m"+ "[-] Generating report..." +chr(27)+"[0;m")
ReportGenerator.startReport(ip,str(level))
print (chr(27)+"[0;92m"+ "[+] Report generated." +chr(27)+"[0;m")
