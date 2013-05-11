from pyplasm import *
#Support function and inital data
dom1D = INTERVALS(1)(32)
dom2D = PROD([dom1D,dom1D])
DRAW = VIEW

def bezierS1(controlpoints):
	return BEZIER(S1)(controlpoints)

def bezierS2(f):
	return BEZIER(S2)(f)

def bezierMappata_1D(controlpoints):
	return MAP(bezierS1(controlpoints))(INTERVALS(1)(32))

def bezierMappata_2D(functions):
	x = BEZIER(S2)(functions)
	return MAP(x)(dom2D) 

def scalaRaggio(radius):
	def prova(punto):
		y = 5;
		return [punto[0]*radius,punto[1]*radius+y,punto[2]]
	return prova

def bez_circumference(radius,z):
	controlpoints = [[1,0,z],[1,1,z],[0,1.62,z],[-1.22,1.22,z],[-2,0,z],[-1.22,-1.22,z],[0,-1.63,z],[1,-1,z],[1,0,z]]
	controlpoints = AA(scalaRaggio(radius))(controlpoints)
	return bezierS1(controlpoints)

#Black Wheel
r1_1 = bez_circumference(1,0.3)
r1 = bez_circumference(1.3,0)
r1Specchio_1 = bez_circumference(1,-0.3)

wheel1 = bezierMappata_2D([r1_1,r1])
wheel2 = bezierMappata_2D([r1Specchio_1,r1])

wheel = STRUCT([wheel1,wheel2])
#Rim
r_1 = bez_circumference(1,0.3)
r_2 = bez_circumference(1.2,0.3)
r_3 = bez_circumference(1.5,0.3)

r_1Specchio = bez_circumference(1,-0.3)
r_2Specchio = bez_circumference(1.2,-0.3)
r_3Specchio = bez_circumference(1.5,-0.3)

#Mapping
primo_1 = bezierMappata_2D([r_1,r_1Specchio])
primo_2 = bezierMappata_2D([r_2,r_2Specchio])
primo_3 = bezierMappata_2D([r_3,r_3Specchio])

secondo_1 = COLOR(RED)(bezierMappata_2D([r_1,r_2]))
secondo_2 = COLOR(BLACK)(bezierMappata_2D([r_2,r_3]))
secondoSpecchio_1 = COLOR(RED)(bezierMappata_2D([r_1Specchio,r_2Specchio]))
secondoSpecchio_2 =  COLOR(BLACK)(bezierMappata_2D([r_2Specchio,r_3Specchio]))

#Rim
circle = CIRCLE(2)([30,1])
x43_p = [[1.7, 4.55,0], [1.15, 5.04,0], [2.31, 4.94,0], [1.88, 4.59,0]]
x43_2d = bezierMappata_1D(x43_p);
x43_s0 = bezierS1(x43_p);

x44_p = [[1.7, 4.55,0], [1.73, 4.37,0], [2.01, 4.30,0], [1.88, 4.59,0]]
x44_2d = bezierMappata_1D(x44_p);
x44_s0 = bezierS1(x44_p);

x45_p =[[1.77, 4.51,0], [1.74, 4.66,0.2], [1.79, 4.88,0.2], [1.77, 4.74,0]]
x45_2d = bezierMappata_1D(x45_p);
x45_s0 = bezierS1(x45_p);

#DRAW(STRUCT([x43_2d,x44_2d,x45_2d]))
prova = bezierMappata_2D([x43_s0,x45_s0,x44_s0])
prova = T([1,2])([0,-5])(prova)
x = DIFFERENCE([circle,prova])
DRAW(x)


#DRAW(STRUCT([primo_1,primo_2,primo_3,secondo_1,secondo_2,secondoSpecchio_1,secondoSpecchio_2,circle]))