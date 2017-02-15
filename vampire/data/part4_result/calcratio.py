from sizewithku import *


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

