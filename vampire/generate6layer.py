
fileheader="""
#======================================================
# Vampire material file for a FePt Ferrimagnet
#======================================================
#
#  Huangtao 26/10/15
#
#---------------------------------------------------
# Number of Materials
#---------------------------------------------------
material:num-materials=6
#---------------------------------------------------
# Material 1 Pt first layer (bottom layer)
#--------------------------------------------------

"""

filename="CoPtpy.mat"

fd=open(filename,"w")

minimum_height=[-1,0,   0.21,0.34,0.54,0.67, 0.88]
maximum_height=[-1,0.21,0.34,0.54,0.67,0.88, 1]
fd.write(fileheader)

for i in range(1,7):
	fixContent="""
#####layer
material[%d]:material-name=TM
material[%d]:damping-constant=1
material[%d]:atomic-spin-moment=1.66 !muB
material[%d]:uniaxial-anisotropy-constant=7.3219471534e-24
material[%d]:uniaxial-anisotropy-direction=0,0,1
material[%d]:material-element=Pt
	""" %(i,i,i,i,i,i)
	exchangeContent=""
	for a in range(1,7):
		one="""
material[%d]:exchange-matrix[%d]=3.5e-21""" %(i,a)
		exchangeContent+=one
	heightContent="""
material[%d]:minimum-height = %f
material[%d]:maximum-height = %f
	""" %(i,minimum_height[i],i,maximum_height[i])
	fd.write(fixContent)
	fd.write(exchangeContent)
	fd.write(heightContent)


fd.close()
print "done"



