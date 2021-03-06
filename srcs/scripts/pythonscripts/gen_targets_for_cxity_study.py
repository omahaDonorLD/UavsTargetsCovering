import random
from random import randint
import math

# automatize the generation of tests input data

delta=510
crop=50
withinpointsdeviation=150
maxtours=30
allcentroids=[]
centroidseed=[[235.699, 303.518], [257.699, 703.518], [735.699, 353.518], [705.699, 703.518]]
x0,xinf=0.,10000.
y0,yinf=0.,10000.


def euclidiandistance(p1, p2):
	return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def satisfyConstraint(aPoint):
	# within map
	if(aPoint[0]<crop or aPoint[0]>xinf-crop or aPoint[1]<crop or aPoint[1]>yinf-crop):
		return False
	for centroid in allcentroids:
		if euclidiandistance(aPoint, centroid) < withinpointsdeviation:
			return False
	return True

for l in range(20) :
	for i in range(10) :
		for j in range(10) :
			if random.randint(0,1) > 0.2:
				continue
			for k in range(len(centroidseed)):
				tours = 0
				while True and tours < maxtours:
					tours = tours + 1
					#print(round(random.uniform(-xinf,xinf),3))
					aPoint=[0., 0.]
					aPoint[0]=round(i*(xinf/10.)+centroidseed[k][0]+random.uniform(-xinf,xinf),3)
					aPoint[1]=round(j*(yinf/10.)+centroidseed[k][0]+random.uniform(-yinf,yinf),3)
					if satisfyConstraint(aPoint):
						allcentroids.append(aPoint)# round to 2nd member decimal
						break

f=open("./outs/input_"+str(len(allcentroids))+"_centroids_"+str(int(xinf))+"_"+str(int(yinf))+"_map.csv","w")

for point in allcentroids :
	f.write(str(point[0])+","+str(point[1])+"\n")

f.close()
