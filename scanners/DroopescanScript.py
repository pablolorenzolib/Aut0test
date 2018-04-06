#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

def startDroopescan(ipDomain):
	pathAndFileName = "/temp/droopscan_" + ipDomain + ".json"

	#Delete file if exists
	if os.path.isfile(pathAndFileName):
		os.remove(pathAndFileName)

	#Execute Droopescan
	os.system("droopescan scan -u " + ipDomain + " --output json > " + pathAndFileName)
