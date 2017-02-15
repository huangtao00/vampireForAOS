from calcratio import get_thermal_factor

"""
calc thermal stability from original file created by vampier
"""


"""
get_thermal_factor():
	opfile:data file name
	row_col: row and col list
	atom_num: the number of  total atom

	return value:
	#reuslt[0]: Dimension information
	#result[1]: temperature list
	#result[2]: thermal stablility factor 
"""



#start1:--------------------------------------------------------------------
if False:
	opfile="output.8nmD.16nmH"

	#effective cols [col start from  1]
	row_col=[2,9]
	#total atom numbers of the nanoparticles
	atom_num=69104

	result=get_thermal_factor(opfile,row_col,atom_num,"D=8nm,H=16nm")
	print result[0]
	print "temperature","thermal"
	for i in range(len(result[1])):
		print result[1][i],result[2][i]
#end1:--------------------------------------------------------------------

#start2:--------------------------------------------------------------------
if True:
	opfile="output.6nmD.12nmH"
	row_col=[2,9]
	atom_num=29484
	result=get_thermal_factor(opfile,row_col,atom_num,"D=6nm,H=12nm")
	print result[0]
	print "temperature","thermal"
	for i in range(len(result[1])):
		print result[1][i],result[2][i]
#end2:--------------------------------------------------------------------


# for d=10nm h=20nm
#atom_num=130900