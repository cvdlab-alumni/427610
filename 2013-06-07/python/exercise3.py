from pyplasm import *
import random

dom1D = INTERVALS(60)(16)
dominio = PROD([dom1D,dom1D])
DRAW = VIEW
mappaZ = {};

def montagne(punto):
	x = punto[0];
	y = punto[1];
	z =  (random.random()*3 * SIN(x) * COS(y))**2;
	ran = random.random()/5;
	return [x, y, ran+z];


def lagoF(max) :
	def l (punto):
		x = punto[0];
		y = punto[1];
		z = max;
		return [x, y, z];
	return l;	


dominioLago = INTERVALS(5)(10);
dominioLago = PROD([dominioLago,dominioLago]);
medio = 0.52;
lagoF = lagoF(medio);
lago = MAP(lagoF)(dominioLago);
lago = T([0,1])([-10,-10])(COLOR(BLUE)(lago))

territorio = MAP(montagne)(dominio);
territorio = T([1,2])([-30,-30])(territorio)

totale = STRUCT([lago,territorio])
#-  EX 3----------------------------------------------------------------------------------------------------
def bezierS1(controlpoints):
	return BEZIER(S1)(controlpoints)

def bezierS2(f):
	return BEZIER(S2)(f)

def mappedBezier_1D(controlpoints):
	x = bezierS1(controlpoints)
	return MAP(x)(INTERVALS(1)(32))

def mappedBezier_2D(functions):
	x = BEZIER(S2)(functions)
	return MAP(x)(dominio) 

def scalaRaggio(radius):
	def prova(punto):
		y = 5;
		return [punto[0]*radius,punto[1]*radius+y,punto[2]]
	return prova

def bezier_circumference(radius,z):
	controlpoints = [[1,0,z],[1,1,z],[0,1.62,z],[-1.22,1.22,z],[-2,0,z],[-1.22,-1.22,z],[0,-1.63,z],[1,-1,z],[1,0,z]]
	controlpoints = AA(scalaRaggio(radius))(controlpoints)
	return bezierS1(controlpoints)

def treeModel(raggio,z,altezzaTronco):
	circle = CIRCLE(raggio)([30,1])
	tronco = EXTRUDE([1,circle,altezzaTronco])
	baseCono = bezier_circumference(raggio+0.5,altezzaTronco);
	first = [0,0,altezzaTronco+1];
	second =[0,0,altezzaTronco]
	foglie = MAP(CONICALSURFACE([first,baseCono]))(dominio)
	baseFoglie = MAP(CONICALSURFACE([second,baseCono]))(dominio);
	return STRUCT([tronco,foglie,baseFoglie])

a = treeModel(1,0,20);
DRAW(a)
#a = bezier_circumference(10,0);
#DRAW(a)