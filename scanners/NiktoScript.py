#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

def startNikto(ipDomain,level):
	pathAndFileName = "/temp/niktoscan_" + level + "_" + ipDomain

	#Delete file if exists
	if os.path.isfile(pathAndFileName):
		os.remove(pathAndFileName)

	#High level
	if level == "3":
		os.system("nikto -ask no -Cgidirs all -maxtime 3h -Format csv -output " + pathAndFileName + ".csv -host " + ipDomain)
	#Medium level
	if level == "2":
		os.system("nikto -ask no -Cgidirs all -maxtime 2h -Format csv -output " + pathAndFileName + ".csv -host " + ipDomain)
	#Low level
	if level == "1":
		os.system("nikto -ask no -Cgidirs all -maxtime 1h -Format csv -output " + pathAndFileName + ".csv -host " + ipDomain)
