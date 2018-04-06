#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

def startSSHAudit(ipDomain):
	pathAndFileName = "/temp/sshaudit_" + ipDomain + ".json"

	#Delete file if exists
	if os.path.isfile(pathAndFileName):
		os.remove(pathAndFileName)

	#Execute SSH-Audit
	os.system("./scanners/ssh-audit.py --no-colors --batch --level=warn " + ipDomain + " > /temp/sshaudit_" + ipDomain + ".txt")
