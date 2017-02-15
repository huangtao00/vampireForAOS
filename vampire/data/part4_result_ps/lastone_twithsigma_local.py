#!/usr/bin/env python
#!coding:utf-8
"""
a tool to generate beautiful figure for magnetic physic science
by huagntao 2015 11 27
"""
import numpy as np 
import matplotlib.pyplot as plt
import math
import matplotlib
from math import pow

#set font size and style belonging to  legned , check out line 84
fontfile="/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman_Italic.ttf"
zfont = matplotlib.font_manager.FontProperties(fname=fontfile,size=20)

#font for label
lfont = matplotlib.font_manager.FontProperties(fname=fontfile,size=30)

def get_volumn(N):
	unit_cell_length=2.866*10**-10
	volumn=float(N)*pow(unit_cell_length,3)/2
	return volumn

def get_KuVoverKBT(N,ku,T):
	volumn=get_volumn(N)
	Energy=float(ku)*volumn/10
	kB=1.380648813e-23 #Boltzman constant
	result=Energy/(kB*T)
	return result
def get_KuVoverKBTalpha(Energy,T):
	kB=1.380648813e-23 #Boltzman constant
	T=350
	result=Energy/(kB*T)
	return result

def fit_curieT(x):
	"""
	fit the M(t) figure
	M(t)=(1-t/Tc)^gamma
	Tc=curie temperate of this material
	gamma = we should adjust this parameter
	"""
	Tc=705.0   #705
	gamma=0.38 #0.409
	t=x
	if t<Tc:
		yy=(1-t/Tc)**gamma
	else:
		yy=0
	return yy




class gpt():
	def __init__(self):
			pass
	def fitting_f(sefl,x,func,ax):
		"""
			x:x range list 
			func:the function using to calculate y
			ax:the handler of the plot
		"""
		y=[func(a) for a in x]
		Curie=1043
		b=[a*10 for a in x if a!=1040]
		b.append(Curie)
		#ax.set_xticks(b)
		ax.plot(x,y,linestyle='-',color='blue',linewidth=4,label="$M(T)=(1-T/710)^{0.39}$") #add some style to this figure

	def add_all_curve(self,datas):
		"""
			add all curves to the figure
			onecurve["legend"]=legend
			onecurve["style"]=style
			onecurve["color"]=color
		"""
		fig, ax = plt.subplots()

		self.plt=plt
		#self.fitting_f([x for x in range(0,800,20)],fit_curieT,ax) #fitting_f(sefl,x,func,ax):
		xall=datas.alldatax
		yall=datas.alldatay
		xlabel=datas.xlabel
		ylabel=datas.ylabel
		allfile=datas.allfile
		curve_number=datas.curve_number
		for cid in range(0,curve_number):
			xarray=xall[cid]
			yarray=yall[cid]
			style=allfile[cid]["style"]
			color=allfile[cid]["color"]
			legend=allfile[cid]["legend"]
			marker=allfile[cid]["marker"]
			#print xarray,yarray
			ax.plot(xarray,yarray, linestyle=style,color=color,label=legend,marker=marker,linewidth=1,markersize=25)


		
		#add x,y label
		#plt.text(10, 70, 'Minimum Size')
		plt.xlabel(xlabel,fontproperties=lfont)
		plt.ylabel(ylabel,fontproperties=lfont)
		for xlabel_i in ax.get_xticklabels(): 
			xlabel_i.set_fontsize(35)
		for ylabel_i in ax.get_yticklabels(): 
			ylabel_i.set_fontsize(35)
		#adjust the legedt together
		#>legend = plt.legend(loc='upper right', shadow=True, fontsize='xxx-large',prop=zfont)
		#>plt.legend(prop=zfont)
		# set ticks and tick labels
		#ax.set_xlim((0, 2*np.pi))
		#ax.set_xticks(range(0,1200,100))
		#ax.set_xticklabels(['0', '$\pi$','2$\pi$'])
		#ax.set_ylim((-1, 3.5))



		# Only draw spine between the y-ticks
		#ax.spines['left'].set_bounds(-1, 1)
		# Hide the right and top spines
		#ax.spines['right'].set_visible(False)
		#ax.spines['top'].set_visible(False)
		# Only show ticks on the left and bottom spines


		#self.fitting_f(x,fit_curieT,ax)
		#ax.yaxis.set_ticks_position('left')
		#ax.xaxis.set_ticks_position('bottom')
		ax.set_xlim(200,750)
		ax.set_xticks(range(200,800,50))
		ax.set_yticks(range(0,150,10))

	def add_doule_axis_curve(self,datas):
			"""
				add all curves to the figure
				onecurve["legend"]=legend
				onecurve["style"]=style
				onecurve["color"]=color
			"""
			fig, ax = plt.subplots()
			fig.subplots_adjust(right=0.75)  ##???
			par1 = ax.twinx()


			#self.fitting_f([x for x in range(0,800,20)],fit_curieT,ax) #fitting_f(sefl,x,func,ax):
			xall=datas.alldatax
			yall=datas.alldatay
			xlabel=datas.xlabel
			ylabel=datas.ylabel
			allfile=datas.allfile
			curve_number=datas.curve_number

			for cid in range(0,curve_number):
				xarray=xall[cid]
				yarray=yall[cid]
				style=allfile[cid]["style"]
				color=allfile[cid]["color"]
				legend=allfile[cid]["legend"]
				marker=allfile[cid]["marker"]
				#print yarray
				if cid==0:
					p1, = ax.plot(xarray,yarray, linestyle=style,color=color,label=legend,marker=marker,linewidth=1,markersize=20)
				else:
					p2, = par1.plot(xarray,yarray, linestyle=style,color=color,label=legend,marker=marker,linewidth=1,markersize=20)

			#add x,y label
			#plt.xlabel(xlabel,fontproperties=lfont)
			#plt.ylabel(ylabel,fontproperties=lfont)
			for xlabel_i in ax.get_xticklabels(): 
				xlabel_i.set_fontsize(20)
			for ylabel_i in ax.get_yticklabels(): 
				ylabel_i.set_fontsize(20)
			for ylabel_i in par1.get_yticklabels(): 
				ylabel_i.set_fontsize(20)
			#adjust the legedt together
			#legend=plt.legend(loc='lower right', shadow=True, fontsize='xxx-large',prop=zfont)
			#plt.legend(prop=zfont)

			ax.set_xlim(0, 18)
			ax.set_ylim(1, 70)
			par1.set_ylim(1, 70)
			ax.set_xlabel(xlabel,fontproperties=lfont)
			ax.set_ylabel(ylabel,fontproperties=lfont)
			par1.set_ylabel("do it by yourself",fontproperties=lfont)

			ax.yaxis.label.set_color(p1.get_color())
			par1.yaxis.label.set_color(p2.get_color())

			tkw = dict(size=4, width=1.5)
			ax.tick_params(axis='y', colors=p1.get_color(), **tkw)
			par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
			ax.tick_params(axis='x', **tkw)
			lines = [p1, p2]
			ax.legend(lines, [l.get_label() for l in lines],(0.9,0))		
			#ax.set_xticks(range(0,18,2))
			self.plt=plt
	def show(self):
		self.plt.show()

#linestyles = ['_', '-', '--', ':']
#colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')
#plt.plot(t, s, linestyles[axisNum], color=color, markersize=10)
class Datas():
	def __init__(self,datadic=""):
		self.curve_number=0
		self.allfile=[]
		self.alldatax=[]
		self.alldatay=[]
		if datadic:
			self.add_data_dict(datadict)
	def add_label(self,lable):
		self.xlabel=lable[0]
		self.ylabel=lable[1]
	def add_data(self,filename,dataxy,legend,style,marker,color="g"): #string list string string
	#"""
	#add one curve to the figure
	#"""
		onecurve={}
		onecurve["filename"]=filename
		onecurve["dataxy"]=dataxy
		onecurve["legend"]=legend
		onecurve["style"]=style
		onecurve["color"]=color
		onecurve["marker"]=marker
		self.allfile.append(onecurve)
		fd=open(filename)
		xdata=[]
		ydata=[]
		for line in fd:
			if line.startswith("#"):
				continue
			line=line.split("\t")
			#print line
			xd=line[dataxy[0]-1]
			yd=line[dataxy[1]-1]
			xdata.append(xd)
			#print yd
			ydata.append(abs(float(yd)))#/10**6
		self.alldatax.append(xdata)
		self.alldatay.append(ydata)
		self.curve_number+=1
	def add_data_dict(self,datadict):
		filename=datadict["filename"]
		dataxy=datadict["dataxy"]
		legend=datadict["legend"]
		style=datadict["style"]
		color=datadict["color"]
		marker=datadict["marker"]
		self.add_data(filename,dataxy,legend,style,marker,color)
import sys
if __name__=="__main__":
	marker = [
		r'H',
		r'o',
		r'd',
		r'8',

		r'v',
		r'$\lambda$',
		r'$\bowtie$',
		r'$\circlearrowleft$',
		r'$\clubsuit$',
		r'$\checkmark$']
	color=["r",'g','b','y']


	curve={}
	filename="output"
	curve["filename"]=filename
	curve["dataxy"]=[1,2]
	curve["legend"]="abc"
	curve["style"]=""
	curve["color"]="r"
	curve["marker"]=r'$\lambda$'


	dset=Datas()
	#add x,y label for this figure
	#label=["Diameter$(nm)$",r"$K_{u}V/K_{B}T$"]
	#label=["Temperature$(K)$",r"$K_{u}(\times 10^5J)$"]
	label=["Temperature$(K)$",r"$K_{u}V/K_{B}T$"]
	dset.add_label(label)

	#add curve to the figure
	legend=["T=350","T=0K","14 nm","10nm","12nm","14nm"]
	color=["#ff0000",'#000000','#000000','#007777','black','cyan']
	#fnlist=["last_t_sigma.data"]
	fnlist=["last_t_sigma200_800.data"]
	style=["--","",'']
	dataxy=[[1,2]]# T with ku
	for i in range(0,len(fnlist)):
		#4 6 8 10
		#0 1 2 3
		curve["style"]=style[i]
		curve["filename"]=fnlist[i]
		curve["color"]=color[i]
		curve["legend"]=legend[i]
		curve["marker"]=marker[i]
		curve["dataxy"]=dataxy[i]
		dset.add_data_dict(curve)

	figure=gpt()
	figure.add_all_curve(dset)
	figure.show()



		
