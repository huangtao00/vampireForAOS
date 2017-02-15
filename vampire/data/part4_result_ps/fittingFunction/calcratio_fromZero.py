from sizewithku import *

"""
from original file created by vampire ,using the function: get_KuVoverKBT ,we get thermal stability factor
"""

def get_thermal_factor(opfile,row_col,atom_num,D):
	"""
	opfile:data file name
	row_col: row and col list
	atom_num: the number of  total atom

	return value:
	#reuslt[0]: Dimension information
	#result[1]: temperature list
	#result[2]: thermal stablility factor 
	"""
	templist=[]
	thermal_factorlist=[]
	dset=Datas()
	curve={}
	filename="xxx"
	curve["filename"]=opfile
	curve["dataxy"]=row_col #[2,9]
	curve["legend"]="abc"
	curve["style"]=""
	curve["color"]="r"
	curve["marker"]=r'$\lambda$'
	dset.add_data_dict(curve)


	N=atom_num  # 65450
	temperature=dset.alldatax[0]
	ku=dset.alldatay[0]
	for i in range(len(ku)):
		aku=ku[i]
		t=temperature[i]
		#print ku[i]
		if aku<0:
			aku=abs(aku)
		aN=N
		t=int(t)
		#print aN,t,aku
		if t==0:
			continue
		# if t<200:
		# 	continue
		#print str(t)+"\t"+str(get_KuVoverKBT(aN,aku,t))
		thermal_fact=get_KuVoverKBT(aN,aku,t)
		templist.append(t)
		thermal_factorlist.append(thermal_fact)
	result=[D,templist,thermal_factorlist]
	return result



if __name__=="__main__":

	dset=Datas()
	curve={}
	filename="output"
	curve["filename"]="output.10nm"
	curve["dataxy"]=[2,9]
	curve["legend"]="abc"
	curve["style"]=""
	curve["color"]="r"
	curve["marker"]=r'$\lambda$'
	dset.add_data_dict(curve)


	N=65450
	temperature=dset.alldatax[0]
	ku=dset.alldatay[0]

	for i in range(len(ku)):
		aku=ku[i]
		t=temperature[i]
		#print ku[i]
		if aku<0:
			aku=abs(aku)
		aN=N
		t=int(t)
		#print aN,t,aku
		if t==0:
			continue
		print str(t)+"\t"+str(get_KuVoverKBT(aN,aku,t))

