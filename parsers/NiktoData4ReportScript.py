#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import csv
import json

def startNikto(ipDomain,level):
	pathAndFileName = "/temp/niktoscan_" + level + "_" + ipDomain + ".csv"
	newPathAndFileName = "/temp/niktoscan_f_" + level + "_" + ipDomain + ".json"

	#Delete file if exists
	if os.path.isfile(newPathAndFileName):
		os.remove(newPathAndFileName)

	jsonData = {}
	dataJsonObj = []

	try:
		with open(pathAndFileName) as csvFile:
			csvData = csv.reader(csvFile, delimiter=',')

			for row in csvData:
				if len(row) > 3:
					if 'OSVDB' in row[3]:
						dataRow = {}
						dataRow['id'] = row[3]
						dataRow['tittle'] = row[6]
						dataRow['port'] = row[2]
						dataRow['petitionType'] = row[4]
						dataRow['url'] = row[5]
						dataJsonObj.append(dataRow)

		jsonData = dataJsonObj
	except:
		print ("There is not results for the Nikto scanner.")
	else:
		try:
			with open(newPathAndFileName, "w") as outfile:
			    json.dump(jsonData, outfile)
		except:
			print ("Error parsing Nikto data.")
