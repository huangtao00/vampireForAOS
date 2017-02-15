totalsize=3.3


step=[0.7,0.4]
"""
0.7 / 3.3 = 0.212121212121
1.1 / 3.3 = 0.333333333333
1.8 / 3.3 = 0.545454545455
2.2 / 3.3 = 0.666666666667
2.9 / 3.3 = 0.878787878788
3.3 / 3.3 = 1.0

"""

part=0
for i in range(0,3):
	for a in step:
		part+=a
		print part,"/",totalsize,"=",part/totalsize

