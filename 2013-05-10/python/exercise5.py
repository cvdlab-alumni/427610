from pyplasm import *
#Support function and inital data
dom1D = INTERVALS(1)(32)
dom2D = PROD([dom1D,dom1D])
DRAW = VIEW


def scambiaYZ(elemento):
	return [S1(elemento),S3(elemento),S2(elemento)]

def yZero(array):
	return AA(scambiaYZ)(array)


def scambiaXZ(elemento):
	return 2[S3(elemento),S2(elemento),S1(elemento)]

def xZero(array):
	return AA(scambiaXZ)(array)	

def bezierS1(controlpoints):
	return BEZIER(S1)(controlpoints)

def bezierS2(f):
	return BEZIER(S2)(f)

def mappedBezier_1D(controlpoints):
	x = bezierS1(controlpoints)
	return MAP(x)(INTERVALS(1)(32))

def mappedBezier_2D(functions):
	x = BEZIER(S2)(functions)
	return MAP(x)(dom2D) 

def scalaRaggio(radius):
	def prova(punto):
		y = 5;
		return [punto[0]*radius,punto[1]*radius+y,punto[2]]
	return prova

def bezier_circumference(radius,z):
	controlpoints = [[1,0,z],[1,1,z],[0,1.62,z],[-1.22,1.22,z],[-2,0,z],[-1.22,-1.22,z],[0,-1.63,z],[1,-1,z],[1,0,z]]
	controlpoints = AA(scalaRaggio(radius))(controlpoints)
	return bezierS1(controlpoints)
#-----------------------------------------------------------------------------------------------------
#Ex.2
#-----------------------------------------------------
#XY Plans
x1_p = [[2.63, 2.55,0],[3.04, 2.48,0], [3.18, 2.53,0],[3.62, 2.53,0]]
x1_2d = mappedBezier_1D(x1_p);

x2_p = [[3.62, 2.53,0], [3.2, 2.74,0], [3.24, 3.6,0], [3.87, 3.68,0]]
x2_2d = mappedBezier_1D(x2_p);

x3_p = [[3.87, 3.68,0], [4.59, 3.79,0], [4.84, 2.92,0], [4.65, 2.53,0]]
x3_2d = mappedBezier_1D(x3_p);

x4_p = [[4.65, 2.53,0], [5.52, 2.57,0],[6.89, 2.54,0], [8.09, 2.53,0] ]
x4_2d = mappedBezier_1D(x4_p);

x5_p = [[8.09, 2.53,0],  [7.84, 2.74,0], [7.79, 3.6,0], [8.49, 3.68,0] ]
x5_2d = mappedBezier_1D(x5_p);

x6_p = [ [8.49, 3.68,0],[9.2, 3.79,0],[9.3, 2.92,0],[9.0, 2.53,0] ]
x6_2d = mappedBezier_1D(x6_p);

x7_p = [[9.0, 2.53,0],[9.46, 2.53,0], [9.73, 2.53,0], [10.11, 2.53,0] ]
x7_2d = mappedBezier_1D(x7_p);

x8_p = [[10.11, 2.53,0],[10.38, 2.84,0],[10.11, 3.93,0],[7.63, 3.87,0] ]
x8_2d = mappedBezier_1D(x8_p);

x9_p = [[7.63, 3.87,0], [7.17, 4.15,0], [6.44, 4.5,0], [5.96, 4.54,0] ]
x9_2d = mappedBezier_1D(x9_p);

x10_p =[[3.44, 3.93,0], [4.41, 4.27,0], [5.27, 4.53,0], [5.96, 4.54,0]]
x10_2d = mappedBezier_1D(x10_p);

x11_p = [[2.66, 3.47,0], [2.76, 3.75,0], [3.21, 3.78,0], [3.44, 3.93,0]]
x11_2d = mappedBezier_1D(x11_p);

x12_p =[[2.66, 3.47,0], [2.65, 3.25,0], [2.56, 2.84,0],[2.63, 2.55,0]]
x12_2d = mappedBezier_1D(x12_p);

x13_p =[[4.95, 4.23,0], [5.24, 3.4,0], [4.92, 3.19,0], [5.6, 2.67,0]]
x13_2d = mappedBezier_1D(x13_p);

x14_p =[[7.33, 2.71,0], [6.84, 2.66,0], [6.3, 2.72,0], [5.6, 2.67,0]]
x14_2d = mappedBezier_1D(x14_p);

x15_p =[[7.33, 2.71,0], [7.65, 3.7,0], [6.87, 4.1,0], [5.98, 4.39,0]]
x15_2d = mappedBezier_1D(x15_p);

x16_p = [[4.95, 4.23,0], [5.29, 4.3,0], [5.6, 4.4,0], [5.98, 4.39,0]]
x16_2d = mappedBezier_1D(x16_p);

x17_p =[[4.45, 4.01,0], [4.63, 4.05,0], [4.72, 4.22,0], [4.95, 4.23,0]]
x17_2d = mappedBezier_1D(x17_p);

x18_p = [[4.45, 4.01,0],[4.51, 3.87,0]]
x18_2d = mappedBezier_1D(x18_p);

x19_p = [[4.51,3.87,0], [7.05, 3.87,0]]
x19_2d = mappedBezier_1D(x19_p);

xy = STRUCT([x1_2d,x2_2d,x3_2d,x4_2d,x5_2d,x6_2d,x7_2d,x8_2d,x9_2d,x10_2d,x11_2d,x12_2d,x13_2d,x14_2d,x15_2d,x16_2d,x17_2d,x18_2d,x19_2d])
#DRAW(xy)
#------------------------------------------------------------------------------
#XZ Plans
x20_p = [[2.85,1.39,0], [2.75,1.51,0], [2.9,1.62,0], [2.59,1.74,0]]
x20_2d = mappedBezier_1D(yZero(x20_p));

x21_p = [[2.62, 4.48,0], [2.46, 3.68,0], [2.53,2.28,0], [2.59,1.74,0]]
x21_2d = mappedBezier_1D(yZero(x21_p));

x22_p = [[2.62, 4.48,0], [2.72, 4.54,0], [2.8, 4.69,0], [2.89, 4.83,0]]
x22_2d = mappedBezier_1D(yZero(x22_p));

x23_p = [[9.79, 4.85,0], [8.43, 4.85,0], [5.64, 4.81,0], [2.89, 4.83,0]]
x23_2d = mappedBezier_1D(yZero(x23_p));

x24_p = [[9.79, 1.39,0], [8.43,1.39,0], [5.64, 1.39,0], [2.89, 1.39,0]]
x24_2d = mappedBezier_1D(yZero(x24_p));

x25_p = [[9.79, 4.85,0], [10.99, 3.43,0], [10.32, 2.02,0], [9.79, 1.39,0]]
x25_2d = mappedBezier_1D(yZero(x25_p));

x26_p = [[7.35, 4.48,0], [7.79, 4.35,0], [8.27, 2.43,0], [7.4, 1.72,0]]
x26_2d = mappedBezier_1D(yZero(x26_p));

x27_p = [[6.51, 2.06,0], [6.84, 1.96,0], [7.15, 1.78,0], [7.4, 1.72,0]]
x27_2d = mappedBezier_1D(yZero(x27_p));

x28_p = [[6.54, 4.09,0], [6.82, 4.19,0], [7.04, 4.32,0], [7.35, 4.47,0]]
x28_2d = mappedBezier_1D(yZero(x28_p));

x29_p = [[6.54, 4.09,0], [6.73, 3.59,0], [6.61, 2.23,0], [6.51, 2.06,0]]
x29_2d = mappedBezier_1D(yZero(x29_p));

x30_p = [[5.1, 2.16,0], [5.84, 2.21,0], [6.26, 2.17,0], [6.51, 2.06,0]]
x30_2d = mappedBezier_1D(yZero(x30_p));

x31_p = [[5.08, 4.07,0], [5.61, 4,0], [5.98, 4.09,0],[6.54, 4.09,0]]
x31_2d = mappedBezier_1D(yZero(x31_p));

x32_p = [[5.08, 4.07,0], [5.16, 3.39,0], [5.07, 2.53,0],[5.1, 2.16,0]]
x32_2d = mappedBezier_1D(yZero(x32_p));

x33_p = [[5.08, 4.07,0], [3.33, 4.2,0], [3.79, 3.45,0], [3.7, 2.96,0]]
x33_2d = mappedBezier_1D(yZero(x33_p));

x34_p = [[5.11, 2.16,0], [4.05, 2.27,0], [3.8, 1.87,0], [3.7, 2.96,0]]
x34_2d = mappedBezier_1D(yZero(x34_p));

x35_p = [[3.2, 4.85,0], [3.18, 3.63,0], [3.19, 1.42,0], [3.17, 1.39,0]]
x35_2d = mappedBezier_1D(yZero(x35_p));

xz = STRUCT([x20_2d,x21_2d,x22_2d,x23_2d,x24_2d,x25_2d,x26_2d,x27_2d,x28_2d,x29_2d,x30_2d,x31_2d,x32_2d,x33_2d,x34_2d,x35_2d])
#DRAW(xz)
#----------------------------------------------------------------------------
#yz
x36_p = [[1, 3,0], [3.11, 2.99,0], [3.52, 2.97,0], [4.42, 2.99,0]]
x36_2d = mappedBezier_1D(xZero(x36_p));

x37_p = [[1, 3,0], [1.03, 3.39,0], [1, 3.79,0], [0.99, 4.21,0]]
x37_2d = mappedBezier_1D(xZero(x37_p));

x38_p = [[1.37, 4.21,0], [1.28, 4.21,0], [1.16, 4.21,0], [0.99, 4.21,0]]
x38_2d = mappedBezier_1D(xZero(x38_p));

x39_p = [[1.37, 4.21,0], [1.43, 4.45,0], [1.54, 4.72,0], [1.67, 4.87,0]]
x39_2d = mappedBezier_1D(xZero(x39_p));

x40_p = [[3.74, 4.84,0], [3.19, 5.02,0], [2.14, 4.93,0], [1.67, 4.84,0]]
x40_2d = mappedBezier_1D(xZero(x40_p));

x41_p = [[3.74, 4.84,0], [3.88, 4.76,0], [4, 4.42,0], [4.08, 4.2,0]]
x41_2d = mappedBezier_1D(xZero(x41_p));

x42_p = [[4.4, 4.22,0], [4.29, 4.23,0], [4.18, 4.22,0], [4.08, 4.2,0]]
x42_2d = mappedBezier_1D(xZero(x42_p));

x43_p = [[4.4, 4.22,0], [4.38, 4.04,0], [4.49, 3.53,0], [4.45, 3.02,0]]
x43_2d = mappedBezier_1D(xZero(x43_p));

yz = STRUCT([x36_2d,x37_2d,x38_2d,x39_2d,x40_2d,x41_2d,x42_2d,x43_2d])
#DRAW(yz)
#------------------------------------------------------------------------------
# Adjustments xy,xz,yz
xy = T([1,2])([-6,-3.4])(xy)
xz = T([1])([-6])(xz)
xz = T([3])([-3])(xz)
yz = T([2,3])([-3.8,-2.75])(yz)
totale = STRUCT([xy,xz,yz])
#DRAW(totale)
#-------------------------------------------------------------------------------------------------------
#Exercise 3
#Black Wheel
r_1 = bezier_circumference(1,0.3)
r_2 = bezier_circumference(1.2,0.3)
r_3 = bezier_circumference(1.5,0.3)

r_1Specchio = bezier_circumference(1,-0.3)
r_2Specchio = bezier_circumference(1.2,-0.3)
r_3Specchio = bezier_circumference(1.5,-0.3)

#Mapping
primo_1 = mappedBezier_2D([r_1,r_1Specchio])
primo_2 = mappedBezier_2D([r_2,r_2Specchio])
primo_3 = mappedBezier_2D([r_3,r_3Specchio])

secondo_1 = COLOR(RED)(mappedBezier_2D([r_1,r_2]))
secondo_2 = COLOR(BLACK)(mappedBezier_2D([r_2,r_3]))
secondoSpecchio_1 = COLOR(RED)(mappedBezier_2D([r_1Specchio,r_2Specchio]))
secondoSpecchio_2 =  COLOR(BLACK)(mappedBezier_2D([r_2Specchio,r_3Specchio]))

wheel = STRUCT([primo_1,primo_2,primo_3,secondo_1,secondo_2,secondoSpecchio_1,secondoSpecchio_2])
#Rim
z = 0.1
zSpecchio = -0.1

x43_p = [[5.01, 2.76,z], [5.25, 2.68,z], [5.16, 2.68,z], [5.32, 2.55,z]]
x43_2d = mappedBezier_1D(x43_p);
x43_s0 = bezierS1(x43_p);

x44_p = [[6.36, 3.39,z], [5.32, 2.55,z]]
x44_2d = mappedBezier_1D(x44_p);
x44_s0 = bezierS1(x44_p);

x45_p = [[6.36, 3.39,z], [6.38, 3.65,z], [6.18, 3.87,z], [5.66, 4.03,z]]
x45_2d = mappedBezier_1D(x45_p);
x45_s0 = bezierS1(x45_p);

x46_p = [[5.01, 2.76,z], [5.66, 4.03,z]]
x46_2d = mappedBezier_1D(x46_p);
x46_s0 = bezierS1(x46_p);

x43Specchio_p = [[5.01, 2.76,zSpecchio], [5.25, 2.68,zSpecchio], [5.16, 2.68,zSpecchio], [5.32, 2.55,zSpecchio]]
x43Specchio_2d = mappedBezier_1D(x43Specchio_p);
x43Specchio_s0 = bezierS1(x43Specchio_p);

x44Specchio_p = [[6.36, 3.39,zSpecchio], [5.32, 2.55,zSpecchio]]
x44Specchio_2d = mappedBezier_1D(x44Specchio_p);
x44Specchio_s0 = bezierS1(x44Specchio_p);

x45Specchio_p = [[6.36, 3.39,zSpecchio], [6.38, 3.65,zSpecchio], [6.18, 3.87,zSpecchio], [5.66, 4.03,zSpecchio]]
x45Specchio_2d = mappedBezier_1D(x45Specchio_p);
x45Specchio_s0 = bezierS1(x45Specchio_p);

x46Specchio_p = [[5.01, 2.76,zSpecchio], [5.66, 4.03,zSpecchio]]
x46Specchio_2d = mappedBezier_1D(x46Specchio_p);
x46Specchio_s0 = bezierS1(x46Specchio_p);

#rim2D = STRUCT([x43_2d,x44_2d,x45_2d,x46_2d,x43Specchio_2d,x44Specchio_2d,x45Specchio_2d,x46Specchio_2d])
#Empty
m1 = mappedBezier_2D([x43_s0,x43Specchio_s0])
m2 = mappedBezier_2D([x44_s0,x44Specchio_s0])
m3 = mappedBezier_2D([x45_s0,x45Specchio_s0])
m4 = mappedBezier_2D([x46_s0,x46Specchio_s0])
#Full
m5 = mappedBezier_2D([x45_s0,x46_s0])
m6 = mappedBezier_2D([x43_s0,x44_s0])
#Single 
rim3Dvuoto = STRUCT([m1,m2,m3,m4])
rim3Dpieno = STRUCT([m1,m2,m3,m4,m5,m6])

#two = STRUCT([rim3Dvuoto,R([1,2])(-PI/8)(T([1,2])([-1.17,1.66])(rim3Dpieno))])
GRAY = Color4f([0.5, 0.5, 0.5, 1.0])
two = CUBOID([0.1,1.2,0.2])
two = STRUCT(NN(8)([two, ROTN([PI/4,[0,0,2]])]))


#three = T([3])([0.1])(two)
#three = T([1,2])([-5.4,-2.5])(three)
#three = S([1,2])([0.65,0.65])(three)
three = COLOR(BLACK)(two)
wheel = T([1,2])([-0.15,-4.95])(wheel)

wheel = STRUCT([wheel,three])
wheel = S([1,2,3])([0.3,0.3,0.3])(wheel)


wheel1 = T([1,2,3])([-1.85,-0.5,2])(wheel)
wheel2 = T([1,2,3])([1.85,-0.5,2])(wheel)
wheel3 = T([1,2,3])([-1.85,-0.5,-1.8])(wheel)
wheel4 = T([1,2,3])([1.85,-0.5,-1.8])(wheel)

totale = STRUCT([totale,wheel1,wheel2,wheel3,wheel4])
#----------------------------------------------------------------------------
#Exercise 4
zDavanti = 0.1
z = 0
zDietro = -0.1

r1Davanti = bezier_circumference(1,zDavanti)
r1Dietro = bezier_circumference(1,zDietro)
r1Centro = bezier_circumference(0.6,z)

r2Davanti = bezier_circumference(1.1,zDavanti)
r2Dietro = bezier_circumference(1.1,zDietro)
r2Centro = bezier_circumference(0.1,z)

r3Davanti = bezier_circumference(0.9,zDavanti)
r3Dietro = bezier_circumference(0.9,zDietro)
r3Centro = bezier_circumference(0.1,z)

pMappata_p1 = mappedBezier_2D([r1Davanti,r1Centro,r1Dietro])
pMappata_p2 = mappedBezier_2D([r2Davanti,r2Dietro])
pMappata_p3 = mappedBezier_2D([r1Davanti,r2Davanti])
pMappata_p4 = mappedBezier_2D([r1Dietro,r2Dietro])
racingWheel = STRUCT([pMappata_p1,pMappata_p2,pMappata_p3,pMappata_p4])
racingWheel = T([2])([-5])(racingWheel)


x47_p = [[1.44, 3.13,zDavanti], [3.11, 3.82,zDavanti], [3.8, 3.3,zDavanti], [4.53, 3.21,zDavanti]]
x47_2d = mappedBezier_1D(x47_p);
x47_s0 = bezierS1(x47_p);

x47Specchio_p = [[1.44, 3.13,zDietro], [3.11, 3.82,zDietro], [3.8, 3.3,zDietro], [4.53, 3.21,zDietro]]
x47Specchio_2d = mappedBezier_1D(x47Specchio_p);
x47Specchio_s0 = bezierS1(x47Specchio_p);

x47_p = [[1.44, 3.13,zDavanti], [3.11, 3.82,zDavanti], [3.8, 3.3,zDavanti], [4.53, 3.21,zDavanti]]
x47_2d = mappedBezier_1D(x47_p);
x47_s0 = bezierS1(x47_p);

x48_p = [[1.4, 2.69,zDavanti], [2.36, 3,zDavanti], [3.11, 2,zDavanti], [2.72, 1.39,zDavanti]]
#x48_p = [[1.4, 2.69,zDavanti], [2.36, 3.5,zDavanti], [3.11, 2.13,zDavanti], [2.72, 1.39,zDavanti]]
x48_2d = mappedBezier_1D(x48_p);
x48_s0 = bezierS1(x48_p);

x48Specchio_p = [[1.4, 2.69,zDietro], [2.36, 3,zDietro], [3.11, 2,zDietro], [2.72, 1.39,zDietro]]
x48Specchio_2d = mappedBezier_1D(x48Specchio_p);
x48Specchio_s0 = bezierS1(x48Specchio_p);

x49_p =	[[4.54, 2.75,zDavanti], [3.21, 3,zDavanti], [3.03, 2,zDavanti], [3.37, 1.41,zDavanti]]
#x49_p =	[[4.54, 2.75,zDavanti], [3.21, 3.32,zDavanti], [3.03, 1.92,zDavanti], [3.37, 1.41,zDavanti]]
x49_2d = mappedBezier_1D(x49_p);
x49_s0 = bezierS1(x49_p);

x49Specchio_p =	[[4.54, 2.75,zDietro], [3.21, 3,zDietro], [3.03, 2,zDietro], [3.37, 1.41,zDietro]]
x49Specchio_2d = mappedBezier_1D(x49Specchio_p);
x49Specchio_s0 = bezierS1(x49Specchio_p);

x50_p = [[1.44, 2.69,zDavanti], [3, 3.10,zDavanti], [3.95, 2.9,zDavanti], [4.53, 2.77,zDavanti]]
x50_2d = mappedBezier_1D(x50_p);
x50_s0 = bezierS1(x50_p);

x50Specchio_p = [[1.44, 2.69,zDietro], [3, 3.10,zDietro], [3.95, 2.9,zDietro], [4.53, 2.77,zDietro]]
x50Specchio_2d = mappedBezier_1D(x50_p);
x50Specchio_s0 = bezierS1(x50_p);

pp1 = mappedBezier_2D([x47_s0,x47Specchio_s0])
pp2 = mappedBezier_2D([x48_s0,x48Specchio_s0])
pp3 = mappedBezier_2D([x49_s0,x49Specchio_s0])
pp4 = mappedBezier_2D([x47_s0,x50_s0])
pp5 = mappedBezier_2D([x47Specchio_s0,x50Specchio_s0])

p_total = STRUCT([pp1,pp2,pp3,pp4,pp5])
p_total = T([1,2])([-3,-2.75])(p_total)
p_total = S([1,2])([0.6,0.65])(p_total)

racingWheel = STRUCT([racingWheel,p_total])
#DRAW(racingWheel)
#-------------------------------------------------------------------------
#Adjustments
racingWheel = S([1,2])([0.15,0.15])(racingWheel)
racingWheel = R([1,3])(PI/2)(racingWheel)
racingWheel = T([1,3])([0.45,-0.45])(racingWheel)

totale = STRUCT([racingWheel,totale])
#Exercise 5
#Front glass
zDavanti = 0.005
zDietro = -0.005
x51_p = [[4.63, 1.24,zDavanti], [5.86, 1.44,zDavanti], [6.49, 1.33,zDavanti], [7.5, 1.24,zDavanti]]
x51_2d = mappedBezier_1D(x51_p);
x51_s0 = bezierS1(x51_p);

x51Specchio_p = [[4.63, 1.24,zDietro], [5.86, 1.24,zDietro], [6.49, 1.24,zDietro], [7.5, 1.24,zDietro]]
x51Specchio_2d = mappedBezier_1D(x51Specchio_p);
x51Specchio_s0 = bezierS1(x51Specchio_p);

x52_p = [[4.63, 1.24,zDavanti], [4.7, 1.46,zDavanti], [4.77, 1.65,zDavanti], [4.96, 1.84,zDavanti]]
x52_2d = mappedBezier_1D(x52_p);
x52_s0 = bezierS1(x52_p);

x52Specchio_p = [[4.63, 1.24,zDietro], [4.7, 1.46,zDietro], [4.77, 1.65,zDietro], [4.96, 1.84,zDietro]]
x52Specchio_2d = mappedBezier_1D(x52Specchio_p);
x52Specchio_s0 = bezierS1(x52Specchio_p);

x53_p = [[7.08, 1.82,zDavanti], [6.68, 1.82,zDavanti], [5.5, 1.82,zDavanti], [4.96,1.82,zDavanti]]
x53_2d = mappedBezier_1D(x53_p);
x53_s0 = bezierS1(x53_p);

x53Specchio_p =[[7.08, 1.82,zDietro], [6.68, 1.82,zDietro], [5.5,1.82,zDietro], [4.96, 1.82,zDietro]]
x53Specchio_2d = mappedBezier_1D(x53Specchio_p);
x53Specchio_s0 = bezierS1(x53Specchio_p);

#x54_p = [[7.08, 1.82,zDavanti], [7.19, 1.75,zDavanti], [7.32, 1.5,zDavanti],[7.5, 1.24,zDavanti]]
x54_p = [[7.5, 1.24,zDavanti], [7.32, 1.5,zDavanti], [7.32, 1.5,zDavanti],[7.08, 1.82,zDavanti]]
x54_2d = mappedBezier_1D(x54_p);
x54_s0 = bezierS1(x54_p);

#x54Specchio_p =  [[7.08, 1.82,zDietro], [7.19, 1.75,zDietro], [7.32, 1.5,zDietro],[7.5, 1.24,zDietro]]
x54Specchio_p =  [[7.5, 1.24,zDietro],[7.32, 1.5,zDietro],[7.19, 1.75,zDietro],[7.08, 1.82,zDietro]]
x54Specchio_2d = mappedBezier_1D(x54Specchio_p);
x54Specchio_s0 = bezierS1(x54Specchio_p);

x55_p = [[6.11, 1.29,zDavanti], [6.11, 1.56,zDavanti-0.5], [6.11, 1.68,zDavanti-0.5], [6.11, 1.8,zDavanti]]
x55_2d = mappedBezier_1D(x55_p);
x55_s0 = bezierS1(x55_p);

x55Specchio_p = [[6.11, 1.29,zDietro], [6.11, 1.56,zDietro-0.3], [6.11, 1.68,zDietro-0.3], [6.11, 1.8,zDietro]]
x55Specchio_2d = mappedBezier_1D(x55Specchio_p);
x55Specchio_s0 = bezierS1(x55Specchio_p);

fm1 = mappedBezier_2D([x51_s0,x51Specchio_s0])
fm2 = mappedBezier_2D([x52_s0,x52Specchio_s0])
fm3 = mappedBezier_2D([x53_s0,x53Specchio_s0])
fm4 = mappedBezier_2D([x54_s0,x54Specchio_s0])
fm5 = mappedBezier_2D([x52_s0,x55_s0,x54_s0])
fm6 = mappedBezier_2D([x52Specchio_s0,x55Specchio_s0,x54Specchio_s0])

frontGlass = STRUCT([fm1,fm2,fm3,fm4,fm5,fm6])
frontGlass = R([1,3])(PI/2)(frontGlass)
frontGlass = T([1,2,3])([0.9,-1,-6])(frontGlass)
#DRAW(frontGlass)
totale = STRUCT([totale,frontGlass])
#DRAW(totale)
#Second surface
zSopra = 0.1
zSotto = -0.1

x56_p = [[3.99, 2.23,zSopra], [3.6, 2.27,zSopra-0.1], [3.54, 3.77,zSopra-0.1], [3.99, 4.02,zSopra]]
x56_2d = mappedBezier_1D(x56_p);
x56_s0 = bezierS1(x56_p);

x56Specchio_p = [[3.99, 2.23,zSotto], [3.6, 2.27,zSotto], [3.54, 3.77,zSotto], [4.01, 4.02,zSotto]]
x56Specchio_2d = mappedBezier_1D(x56Specchio_p)
x56Specchio_s0 = bezierS1(x56Specchio_p)

x65_p = [[3.99, 2.23,zSopra], [4.01, 4.02,zSopra]]
x65_2d = mappedBezier_1D(x65_p)
x65_s0 = bezierS1(x65_p)

x65Specchio_p = [[3.99, 2.23,zSotto], [4.01, 4.02,zSotto]]
x65Specchio_2d = mappedBezier_1D(x65Specchio_p)
x65Specchio_s0 = bezierS1(x65Specchio_p)

x57_p = [[5.11, 4.04,zSopra+0.1], [4.63, 4.09,zSopra], [4.14, 4.03,zSopra], [3.99, 4.02,zSopra]]
x57_2d = mappedBezier_1D(x57_p)
x57_s0 = bezierS1(x57_p)

x57Specchio_p = [[5.11, 4.04,zSotto+0.1], [4.63, 4.09,zSotto], [4.14, 4.03,zSotto], [3.99, 4.02,zSotto]]
x57Specchio_2d = mappedBezier_1D(x57Specchio_p)
x57Specchio_s0 = bezierS1(x57Specchio_p)

x58_p = [[5.11, 2.19,zSopra+0.1], [4.8, 2.18,zSopra], [4.45, 2.21,zSopra], [3.99, 2.23,zSopra]]
x58_2d = mappedBezier_1D(x58_p)
x58_s0 = bezierS1(x58_p)

x58Specchio_p = [[5.11, 2.19,zSotto+0.1], [4.8, 2.18,zSotto], [4.45, 2.21,zSotto], [3.99, 2.23,zSotto]]
x58Specchio_2d = mappedBezier_1D(x58Specchio_p)
x58Specchio_s0 = bezierS1(x58Specchio_p)

zSopra = zSopra+0.1
zSotto = zSotto+0.1

x59_p = [[5.11, 2.19,zSopra], [5.05, 2.51,zSopra], [5.08, 3.34,zSopra], [5.11, 4.03,zSopra]]
x59_2d = mappedBezier_1D(x59_p)
x59_s0 = bezierS1(x59_p)

x59Specchio_p = [[5.11, 2.19,zSotto], [5.05, 2.51,zSotto], [5.08, 3.34,zSotto], [5.11, 4.03,zSotto]]
x59Specchio_2d = mappedBezier_1D(x59Specchio_p)
x59Specchio_s0 = bezierS1(x59Specchio_p)

x60_p = [[6.56, 4.14,zSopra-0.1], [6.01, 4.06,zSopra], [5.48, 4.09,zSopra], [5.11, 4.03,zSopra]]
x60_2d = mappedBezier_1D(x60_p)
x60_s0 = bezierS1(x60_p)

x60Specchio_p = [[6.56, 4.14,zSotto-0.1], [6.01, 4.06,zSotto], [5.48, 4.09,zSotto], [5.11, 4.03,zSotto]]
x60Specchio_2d = mappedBezier_1D(x60Specchio_p)
x60Specchio_s0 = bezierS1(x60Specchio_p)

x61_p = [[6.49, 2.05,zSopra-0.1], [6.15, 2.15,zSopra], [5.51, 2.17,zSopra], [5.11, 2.19,zSopra]]
x61_2d = mappedBezier_1D(x61_p)
x61_s0 = bezierS1(x61_p)

x61Specchio_p = [[6.49, 2.05,zSotto-0.1], [6.15, 2.15,zSotto], [5.51, 2.17,zSotto], [5.11, 2.19,zSotto]]
x61Specchio_2d = mappedBezier_1D(x61Specchio_p)
x61Specchio_s0 = bezierS1(x61Specchio_p)

p1 = mappedBezier_2D([x56_s0,x65_s0])
p1Specchio = mappedBezier_2D([x56Specchio_s0,x65Specchio_s0])
p2 = mappedBezier_2D([x56_s0,x56Specchio_s0])
p3 = mappedBezier_2D([x57_s0,x58_s0])
p3Specchio = mappedBezier_2D([x57Specchio_s0,x58Specchio_s0])
p4 = mappedBezier_2D([x58_s0,x58Specchio_s0])
p5 = mappedBezier_2D([x57_s0,x57Specchio_s0])
p6 = mappedBezier_2D([x59_s0,x59Specchio_s0])
p7 = mappedBezier_2D([x60_s0,x60Specchio_s0])
p8 = mappedBezier_2D([x61_s0,x61Specchio_s0])
p9 = mappedBezier_2D([x60_s0,x61_s0])
p10 = mappedBezier_2D([x60Specchio_s0,x61Specchio_s0])


roof = STRUCT([p1,p1Specchio,p2,p3,p3Specchio,p4,p5,p6,p7,p8,p9,p10])
roof = R([2,3])(-PI/2)(roof)
roof = T([1,2,3])([-5.65,1.98,3.2])(roof)
roof = S([2,3])([0.4,1.02])(roof)
roof = COLOR(BLACK)(roof)

totale = STRUCT([totale,roof])
DRAW(totale)
