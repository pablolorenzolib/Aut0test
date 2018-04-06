#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import csv
import json

def startOpenVAS(ipDomain,level):
	pathAndFileName = "/temp/openvas_" + level + "_" + ipDomain + ".csv"
	newPathAndFileName = "/temp/openvas_f_" + level + "_" + ipDomain + ".json"

	#Delete file if exists
	if os.path.isfile(newPathAndFileName):
		os.remove(newPathAndFileName)

	jsonData = {}
	dataJsonObj = []

	try:
		with open(pathAndFileName) as csvFile:
			csvData = csv.reader(csvFile, delimiter=',')

			for row in csvData:
				if not 'NOCVE' in row[11]:
					if not 'Port' in row[2]:
						dataRow = {}
						dataRow['cve'] = row[11]
						dataRow['tittle'] = row[7]
						dataRow['port'] = row[2]
						dataRow['protocol'] = row[3]
						dataRow['severity'] = row[5]
						dataRow['cvss'] = row[4]
						dataRow['description'] = row[8]
						dataRow['impact'] = row[16]
						dataRow['solution'] = row[17]
						dataJsonObj.append(dataRow)

		jsonData = dataJsonObj
	except:
		print ("There is not results for the OpenVAS scanner.")
	else:
		try:
			with open(newPathAndFileName, "w") as outfile:
			    json.dump(jsonData, outfile)
		except:
			print ("Error parsing OpenVAS data.")
