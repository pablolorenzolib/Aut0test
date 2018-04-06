#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import json

def startWPScan(ipDomain,level):
	pathAndFileName = "/temp/wpscan_" + level + "_" + ipDomain + ".json"
	newPathAndFileName = "/temp/wpscan_f_" + level + "_" + ipDomain + ".json"

	#Delete file if exists
	if os.path.isfile(newPathAndFileName):
		os.remove(newPathAndFileName)

	try:
		f = open(pathAndFileName)
		s = f.read()
		jsonResults = json.loads(s)
		f.close()
	except:
		print ("There is not results for the WPScan.")
	else:
		if len(jsonResults) == 2:
			try:
				with open(newPathAndFileName, 'w') as outfile:
		    			json.dump(jsonResults['scan_aborted'], outfile)
			except:
				print ("Error parsing WPScan data.")
		#else:
			#Check the results
			#for num in range(len(jsonResults)):
				#aborted = jsonResults[1]['scan_aborted']
		
