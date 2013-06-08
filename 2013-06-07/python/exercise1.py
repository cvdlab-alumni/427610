from pyplasm import *
import random

dom1D = INTERVALS(60)(16)
dominio = PROD([dom1D,dom1D])
DRAW = VIEW

def montagne(punto):
	x = punto[0];
	y = punto[1];
	z =  (random.random()*3 * SIN(x) * COS(y))**2;
	ran = random.random()/5;
	return [x, y, ran+z];

territorio = MAP(montagne)(dominio);
territorio = T([1,2])([-30,-30])(territorio)
DRAW(territorio);