#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import json
_jsonResults = ""

def startDroopescan(ipDomain):
	pathAndFileName = "/temp/droopscan_" + ipDomain + ".json"
	newPathAndFileName = "/temp/droopscan_f_" + ipDomain + ".json"

	#Delete file if exists
	if os.path.isfile(newPathAndFileName):
		os.remove(newPathAndFileName)

	try:
		f = open(pathAndFileName)
		s = f.read()
		if "not identified as a supported CMS." not in s:
			_jsonResults = json.loads(s)
		else:
			_jsonResults = "There is not identified CMS in the selected target."

		f.close()
	except:
		print ("There is not results for the Droopescan scanner.")
	else:
		#We will generate the new json
		try:
			with open(newPathAndFileName, 'w') as outfile:
	    			json.dump(_jsonResults, outfile)
		except:
			print ("Error parsing Droopscan data.")
