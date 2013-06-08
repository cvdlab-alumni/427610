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
DRAW(totale)

