#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import json

def startWhatWeb(ipDomain,level):
	pathAndFileName = "/temp/whatweb_" + level + "_" + ipDomain + ".json"
	newPathAndFileName = "/temp/whatweb_f_" + level + "_" + ipDomain + ".json"

	#Delete file if exists
	if os.path.isfile(newPathAndFileName):
		os.remove(newPathAndFileName)

	try:
		f = open(pathAndFileName)
		s = f.read()
		jsonResults = json.loads(s)
		f.close()
	except:
		print ("There is not results for the WhatWeb scanner.")
	else:
		if len(jsonResults) == 3:
			try:
				with open(newPathAndFileName, 'w') as outfile:
		    			json.dump(jsonResults[1]['plugins'], outfile)
			except:
				print ("Error parsing WhatWeb data.")
