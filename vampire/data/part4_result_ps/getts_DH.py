"""
generate thermal stability factor(T) with different sizes
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import time
import matplotlib as mpl
from matplotlib import cm
import matplotlib
"""
generate KuV/KBT   with D  mesh figure
"""

fontfile="/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman_Italic.ttf"
lfont = matplotlib.font_manager.FontProperties(fname=fontfile,size=20)



from calcratio import get_thermal_factor
#reuslt[0]: Dimension information
#result[1]: temperature list
#result[2]: thermal stablility factor  list

#we have 8 files to get thermal stabliity factor
#file name ="output."+[2,4,6,8,10,12,14,16]+"nm"


#number of atoms with different dimensions
atom_num_list=[8484,29484,69104,130900]


alldatacontainer=[]
for dimen in range(4,12,2):
	dimenname=str(dimen)+"nm"
	filename="output."+dimenname+"D."+str(2*dimen)+"nmH"
	dimenname=dimenname+"D."+str(2*dimen)+"nmH"
	result=get_thermal_factor(filename,[2,9],atom_num_list[dimen/2-2],dimenname)
	alldatacontainer.append(result)



TEMP=alldatacontainer[0][1]

#filename=tt.Xnm
filenamebase="ttt."


for i in range(len(atom_num_list)):
	oneD=alldatacontainer[i][0]
	onesThermal=alldatacontainer[i][2]
	filename=filenamebase+oneD
	fd=open(filename,"w")

	fd.write("#"+oneD+"nm\n")
	for temp , thermal in zip(TEMP,onesThermal):
		line=str(temp)+"\t"+str(thermal)+"\n"
		fd.write(line)
	fd.close();






