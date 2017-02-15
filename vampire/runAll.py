#!/usr/bin/python



import os
# print os.getcwd()

subdir="/LargeStepLongLoop"

desdir=os.getcwd()+subdir
#print desdir

allToRunDir=[]
for  one in os.listdir(desdir):
	one=desdir+"/"+one
	if os.path.isdir(one):
		# print one
		allToRunDir.append(one)
sortflag=["2","4","6","8","10","16"]

sortAllToRunDir=[]
for flag in sortflag:
	for onerun in allToRunDir:
		if flag in onerun:
			sortAllToRunDir.append(onerun)
			break

print sortAllToRunDir

for  one in sortAllToRunDir:
	if "16" in one:
		cmd="./vampire -f "+one+"/input.FePtL10 >/dev/zero"
		print "[+1:]Running: ["+cmd+"]"
		os.system(cmd)
		cmd="mv output "+one
		print "[+2:]Running: ["+cmd+"]"	
		os.system(cmd)
		print "[+++]next ..."






