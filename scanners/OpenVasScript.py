#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import subprocess
from time import sleep

def startOpenVAS(ipDomain,level):
	pathAndFileName = "/temp/openvas_" + level + "_" + ipDomain + ".csv"

	#Delete file if exists
	if os.path.isfile(pathAndFileName):
		os.remove(pathAndFileName)

	#Choosing which kind of scan we want to run depending of the level and we save it in idTypeScan:
	cmdIdTypeScan = ""

	#High level
	if level == "3":
		cmdIdTypeScan = "omp -u admin -w admin -g | grep -e 'Full and very deep ultimate' | grep -oE '[0-9a-z]{8}-([0-9a-z]{4}-){3}[0-9a-z]{12}'"
	#Medium level
	if level == "2":
		cmdIdTypeScan = "omp -u admin -w admin -g | grep -e 'Full and very deep' | grep -oE '[0-9a-z]{8}-([0-9a-z]{4}-){3}[0-9a-z]{12}'"
	#Low level
	if level == "1":
		cmdIdTypeScan = "omp -u admin -w admin -g | grep -e 'Full and fast ultimate' | grep -oE '[0-9a-z]{8}-([0-9a-z]{4}-){3}[0-9a-z]{12}'"

	ps = subprocess.Popen(cmdIdTypeScan,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	result = ps.communicate()[0].split()
	idTypeScan = str(result[0])
	#Deleting b''
	idTypeScan = idTypeScan[2:-1]

	#Creating the target and saving the ID in idTarget:
	cmdIdTarget = "omp -u admin -w admin --xml='<create_target><name>Target_" + ipDomain + "</name><hosts>" + ipDomain + "</hosts></create_target>'"
	ps = subprocess.Popen(cmdIdTarget,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	result = ps.communicate()[0].split()
	resultFinal = result[1]
	idTarget = str(resultFinal[4:-1])
	#Eliminamos b''
	idTarget = idTarget[2:-1]

	#Creating the task with the specific type of scan and target selected and save the ID in idTask (to see the tasks omp -u admin -w admin --get-tasks):
	cmdIdTask = "omp -u admin -w admin -C -c " + idTypeScan + " --target=" + idTarget
	ps = subprocess.Popen(cmdIdTask,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	result = ps.communicate()[0].split()
	idTask = str(result[0])
	#Deleting b''
	idTask = idTask[2:-1]

	#Running the scan
	cmdStartTask = "omp -u admin -w admin --start-task " + idTask
	ps = subprocess.Popen(cmdStartTask,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

	#Wait until the progress is DONE
	notEnd = True
	while notEnd:
		cmdScan = "omp -u admin -w admin -G"
		ps = subprocess.Popen(cmdScan,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
		result = ps.communicate()[0]
		sys.stdout.flush()
		print ('\rProgress OpenVAS: %s' % result[38:-15], end="\r")
		sleep(1)
		if b'Done' in result:
			notEnd = False
			

	#Here we get the format ID and saving in the var idFormat:
		#omp -u admin -w admin -F
	#Original commnad -> omp -u admin -w admin -F | grep -e 'CSV Results' | grep -oE '[0-9a-z]{8}-([0-9a-z]{4}-){3}[0-9a-z]{12}'

	cmdIdFormat = "omp -u admin -w admin -F | grep -e 'CSV Results' | grep -oE '[0-9a-z]{8}-([0-9a-z]{4}-){3}[0-9a-z]{12}'"
	ps = subprocess.Popen(cmdIdFormat,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	result = ps.communicate()[0].split()
	idFormat = str(result[0])
	#Deleting b''
	idFormat = idFormat[2:-1]

	#Here we get the report ID and saving in the var idReport:
		#omp -u admin -w admin -iX '<get_tasks task_id="idTask" details="1"/>'
	#Original command -> omp -u admin -w admin -iX '<get_tasks task_id="3bbb54f6-499d-401e-b0a5-e6c2c52fd413" details="1"/>' | grep -e 'report id="' | grep -oE '[0-9a-z]{8}-([0-9a-z]{4}-){3}[0-9a-z]{12}' | tail -1

	cmdIdReport = "omp -u admin -w admin -iX '<get_tasks task_id=\"" + idTask + "\" details=\"1\"/>' | grep -e 'report id=\"' | grep -oE '[0-9a-z]{8}-([0-9a-z]{4}-){3}[0-9a-z]{12}' | tail -1"
	ps = subprocess.Popen(cmdIdReport,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
	result = ps.communicate()[0].split()
	idReport = str(result[0])
	#Deleting b''
	idReport = idReport[2:-1]

	#Generating the report with idReport and idFormat:
	#Original command -> omp -u admin -w admin -R " + idReport + " -f " + idFormat + " > /temp/openvas_"+level+"_"+ipDomain+".csv
	sleep(3)

	cmdReport = "omp -u admin -w admin -R " + idReport + " -f " + idFormat + " > /temp/openvas_"+level+"_"+ipDomain+".csv"
	ps = subprocess.Popen(cmdReport,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

	#Waiting for the report
	sleep(20)

	#Deleting the task created
	cmdDelTask = "omp -u admin -w admin -D " + idTask
	ps = subprocess.Popen(cmdDelTask,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

	#Waiting until the task is delete
	sleep(1)

	#Deleting the target
	cmdDelTarget = "omp -u admin -w admin --xml='<delete_target target_id=\"" + idTarget + "\"/>'"
	ps = subprocess.Popen(cmdDelTarget,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
