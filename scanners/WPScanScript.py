#!/usr/bin/python3
# -*- coding: utf-8 -*-
#WPScan Beta V3 - The script works when we execute wpscan v3 from the original path.

import sys
import os

def startWPScan(ipDomain,level):
	pathAndFileName = "/temp/wpscan_" + level + "_" + ipDomain + ".json"

	#Delete file if exists
	if os.path.isfile(pathAndFileName):
		os.remove(pathAndFileName)

	#update the database of WPScan
	os.system("wpscan --update")

	#[It has redirections sometimes, so we should use www. before the URL if we are not using and IP]

	#High level
	if level == "3":
		os.system("/root/pentestTools/wpscan-v3/bin/wpscan --url "+ipDomain+" --enumerate u1-50,vp,tt,vt --format json --output " + pathAndFileName)
	#Medium level
	if level == "2":
		os.system("/root/pentestTools/wpscan-v3/bin/wpscan --url "+ipDomain+" --enumerate u1-30,vp,tt,vt --format json --output " + pathAndFileName)
	#Low level
	if level == "1":
		os.system("/root/pentestTools/wpscan-v3/bin/wpscan --url "+ipDomain+" --enumerate --format json --output " + pathAndFileName)
