#!/usr/bin/python

"""
display the specific column of a line
"""
import os
import commands
def get_itme(filename,row,column):

	cmd="cat %s |sed '%d!d'" %(filename,row)
	ret = commands.getoutput(cmd)
	retlist=ret.split()
	if len(retlist)==10:
		return  ret.split()[column-1]
	else:
		return  "None"


if __name__=="__main__":
	filename="output."  #2 4 6 8 10 12 14 16
	row=80			#730k  80   750k 82    
	column=9
	for i in range (2,18,2):
		#print i
		filename="output."+str(i)+"nm"
		print i,get_itme(filename,row,column)