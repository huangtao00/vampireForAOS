position=[(0,0),(1,0),(-1,0)]
newposition=[]
for i in [-1,1]:
	for  x,y in position:
		y=y+i
		newposition.append((x,y))

newposition.extend(position)
alla=[]
allb=[]

for z in [-1,0,1]:
	for x,y in newposition:
		alla.append((x,y,z))

allb_temp=[(0.5,0.5),(0.5,-0.5),(-0.5,0.5),(-0.5,-0.5)]

for z in [-1,0,1]:
	for  x,y in allb_temp:
		allb.append((x,y,z))



colorfora=(0.7,0.7,0.7)
colorforb=(1,0,1)

filename="ENp_py.inc"
fd=open(filename,"w")

length=2.887  #spacing between atom


#create a atoms 27
for x,y,z in alla:
	#spinm0(0,0,0,0,0,1,0.9,0,0)
	r,g,b=colorfora
	x=x*length
	y=y*length
	z=z*length
	line="spinm0(%f,%f,%f,0,0,1,%f,%f,%f)\n" %(x,y,z,r,g,b)
	#print line
	fd.write(line)

#create b atoms  12

for x,y,z in allb:
	#spinm0(0,0,0,0,0,1,0.9,0,0)
	r,g,b=colorfora
	x=x*length
	y=y*length
	z=z*length
	line="spinm0(%f,%f,%f,0,0,1,%f,%f,%f)\n" %(x,y,z,r,g,b)
	#print line
	fd.write(line)


#Bone(sx,sy,sz,endx,endy,endz,r,cr,cg,cb)
def isneighbour(start,end):
	sx,sy,sz=start
	ex,ey,ez=end
	if sx==ex:
		if sy==ey:
			if abs(abs(sz)-abs(ez))==1:
				return True
			else:
				return False
		elif(sz==ez):
			if abs(abs(sy)-abs(ey))==1:
				return True
			else:
				return False
	elif(abs(abs(sx)-abs(ex))==1):
		if sy==ey and sz==ez:
			return True
		else:
			return False
	else:
		return False


lena=len(alla)
for i in range(0,lena-1):
	start=alla[i]
	for  j in range(i+1,lena):
		end=alla[j]
		line1=""
		if isneighbour(start,end):
			#print start,"-",end
			sx,sy,sz=start
			ex,ey,ez=end
			sx=sx*length
			sy=sy*length
			sz=sz*length
			ex=ex*length
			ey=ey*length
			ez=ez*length
			if (sx==sy and sz==sy and sx==0) or (ex==ey and ey==ez and ez==0):
				#green color
				line="Bone(%f,%f,%f,%f,%f,%f,0.05,0,1,0)\n" %(sx,sy,sz,ex,ey,ez)
				if sx==sy and sz==sy and sx==0:
					line1="spinm0(%f,%f,%f,0,0,1,%f,%f,%f)\n" %(ex,ey,ez,1,0,0)
				else:
					line1="spinm0(%f,%f,%f,0,0,1,%f,%f,%f)\n" %(sx,sy,sz,1,0,0)
			else:
				#yellow
				pass
				line="Bone(%f,%f,%f,%f,%f,%f,0.05,1,1,0.4)\n" %(sx,sy,sz,ex,ey,ez)
				#line=""
			fd.write(line)
			if len(line1):
				fd.write(line1)

#Bone(sx,sy,sz,endx,endy,endz,r,cr,cg,cb)
print "done"
for  point in allb:
	ex,ey,ez=point
	if (ez==0):
		sx,sy,sz=(0,0,0)
		ex=ex*length
		ey=ey*length
		ez=ez*length
		line="Bone(%f,%f,%f,%f,%f,%f,0.05,0,0,1)\n" %(sx,sy,sz,ex,ey,ez)
		line1="spinm0(%f,%f,%f,0,0,1,%f,%f,%f)\n" %(ex,ey,ez,1,1,0)
		fd.write(line)
		fd.write(line1)

line1="spinm0(%f,%f,%f,0,0,1,%f,%f,%f)\n" %(0,0,0,1,1,0)
fd.write(line1)
fd.close()