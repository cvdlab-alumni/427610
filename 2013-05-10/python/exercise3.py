from pyplasm import *
#Support function and inital data
dom1D = INTERVALS(1)(32)
dom2D = PROD([dom1D,dom1D])
DRAW = VIEW

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

def scambiaYZ(elemento):
	return [S1(elemento),S3(elemento),S2(elemento)]

def yZero(array):
	return AA(scambiaYZ)(array)


def scambiaXZ(elemento):
	return [S3(elemento),S2(elemento),S1(elemento)]

def xZero(array):
	return AA(scambiaXZ)(array)	

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

two = STRUCT([rim3Dvuoto,R([1,2])(-PI/8)(T([1,2])([-1.17,1.66])(rim3Dpieno))])
three = T([3])([0.1])(two)
three = T([1,2])([-5.4,-2.5])(three)
three = S([1,2])([0.65,0.65])(three)
wheel = T([1,2])([-0.15,-4.95])(wheel)

wheel = STRUCT([wheel,three])
wheel = S([1,2,3])([0.3,0.3,0.3])(wheel)


wheel1 = T([1,2,3])([-1.85,-0.5,2])(wheel)
wheel2 = T([1,2,3])([1.85,-0.5,2])(wheel)
wheel3 = T([1,2,3])([-1.85,-0.5,-1.8])(wheel)
wheel4 = T([1,2,3])([1.85,-0.5,-1.8])(wheel)

totale = STRUCT([totale,wheel1,wheel2,wheel3,wheel4])
DRAW(totale)

