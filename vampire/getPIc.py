#!/usr/bin/python

"""
read pov file and change content:
1:background color
2:unset arrow
3:change color of atoms
4:rescale atom size
"""


isChangeBackColor=True
isShowArrow=False
atom1Color="rgb <1 0 .5>}finish"
atom2Color="rgb <0.76 0.76 0.76>}finish"
isChangeAtomSize=True
height=600
width=800
import fileinput
import sys

def replaceAll(file,searchExp,replaceExp,one=False):
	count=0
	for line in fileinput.input(file, inplace=1):
		if count==0:
			if searchExp in line:
				count+=1
				line = line.replace(searchExp,replaceExp)
		sys.stdout.write(line)


import sys,os
if __name__=="__main__":
	filename=sys.argv[1]
	if isChangeBackColor:
		replaceAll(filename,"color Gray30","color rgb<0.9 0.9 0.9>")
	if isShowArrow==False:
		replaceAll(filename,"arrows0=1","arrows0=0")
		replaceAll(filename,"arrows1=1","arrows1=0")

	replaceAll(filename,"rgb <cr cg cb>}finish",atom1Color,True)	
	replaceAll(filename,"rgb <cr cg cb>}finish",atom2Color,True)	
	if isChangeAtomSize==True:
		replaceAll(filename,"0.5*rscale0","rscale0")	
		replaceAll(filename,"0.5*rscale1","rscale1")			
	if len(sys.argv)==4:
		height=int(sys.argv[2])
		width=int(sys.argv[3])
	cmd="povray %s +H%d +W%d" %(filename,height,width)

	os.system(cmd)
