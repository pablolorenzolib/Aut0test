#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import json

def startTestSSL(ipDomain):
	pathAndFileName = "/temp/testssl_" + ipDomain + ".json"
	newPathAndFileName = "/temp/testssl_f_" + ipDomain + ".json"

	#Delete file if exists
	if os.path.isfile(newPathAndFileName):
		os.remove(newPathAndFileName)

	try:
		f = open(pathAndFileName)
		s = f.read()
		jsonResults = json.loads(s)
		f.close()
	except:
		print ("There is not results for the TestSSL scanner.")
	else:
		#Parsing vulnerabilities here
		vulns = []

		for num in range(len(jsonResults)):
			severity = jsonResults[num]['severity']

			if severity == "NOT ok":
				vulns.append(jsonResults[num])
			if severity == "WARN":
				vulns.append(jsonResults[num])
			if severity == "MEDIUM":
				vulns.append(jsonResults[num])
			if severity == "CRITICAL":
				vulns.append(jsonResults[num])

		try:
			with open(newPathAndFileName, 'w') as outfile:
	    			json.dump(vulns, outfile)
		except:
			print ("Error parsing TestSSL data.")
