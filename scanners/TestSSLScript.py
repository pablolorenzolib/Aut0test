#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

def startTestSSL(ipDomain):
	pathAndFileName = "/temp/testssl_" + ipDomain + ".json"

	#Delete file if exists
	if os.path.isfile(pathAndFileName):
		os.remove(pathAndFileName)

	#Execute TestSSL
	os.system("./scanners/testssl.sh -U --quiet --warnings batch --color 0 --jsonfile " + pathAndFileName + " " + ipDomain)
