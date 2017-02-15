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
#result[2]: thermal stablility factor 

#we have 8 files to get thermal stabliity factor
#file name ="output."+[2,4,6,8,10,12,14,16]+"nm"


#number of atoms with different dimensions
atom_num_list=[532,4242,14742,34552,65450,80220,93639,106792]


alldatacontainer=[]
for dimen in range(2,18,2):
	dimenname=str(dimen)+"nm"
	filename="output."+dimenname
	dimenname=dimenname[0:-2]

	result=get_thermal_factor(filename,[2,9],atom_num_list[dimen/2-1],dimenname)
	alldatacontainer.append(result)


D=[]
TEMP=alldatacontainer[0][1]
Thermal=[]
for i in range(len(atom_num_list)):
	Thermal.append(alldatacontainer[i][2])
	D.append(int(alldatacontainer[i][0]))







#plot mesh figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_ylabel("Temperature$(K)$",fontproperties=lfont)
ax.set_xlabel("Dimension$(nm)$",fontproperties=lfont)
ax.set_zlabel(r"$K_{u}V/K_{B}T$",fontproperties=lfont)


templist, dimlsit = np.meshgrid(TEMP,D)
#print templist

#swframe = None
#tstart = time.time()
#oldcol = wframe
ax.set_zticks(np.linspace(0,230,15))
ax.set_xticks(range(2,18,2))
ax.set_yticks(range(200,810,50))
#ax.text(10, 350, 50, "red", color='red')


norm = mpl.colors.Normalize(vmin=0, vmax=50)
wframe = ax.plot_surface( dimlsit, templist,Thermal,cmap="autumn_r",norm=norm ,pickradius=8, linestyles="-",lw=.2, rstride=1, cstride=1,alpha=0.6)
#ax.contour(dimlsit,templist, Thermal, zdir="z",lw=3, cmap="autumn_r" , linestyles="solid", offset=-1)
ax.contour(dimlsit,templist, Thermal, zdir="x",lw=10, cmap="autumn_r" , linestyles="solid", offset=-1,marker="c")
#ax.contour(dimlsit,templist, Thermal, zdir="y",lw=5, cmap="autumn_r" , linestyles="solid", offset=2)

 
#ax.plot_wireframe( dimlsit, templist,Thermal,cmap=cm,norm=norm ,pickradius=8, linestyles="-",colors="#ff5533",linewidth=2, rstride=1, cstride=1)

plt.show()


#plt.pause(.001)
#print('FPS: %f' % (100 / (time.time() - tstart)))
