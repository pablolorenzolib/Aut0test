#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

def startWhatWeb(ipDomain, level):
	pathAndFileName = "/temp/whatweb_" + level + "_" + ipDomain + ".json"

	#Delete file if exists
	if os.path.isfile(pathAndFileName):
		os.remove(pathAndFileName)

	#High and medium level
	if level == "3" or level == "2":
		os.system("whatweb -a 3 -q --no-errors --log-json=" + pathAndFileName + " " + ipDomain)
	#Low level
	if level == "1":
		os.system("whatweb -a 1 -q --no-errors --log-json=" + pathAndFileName + " " + ipDomain)
