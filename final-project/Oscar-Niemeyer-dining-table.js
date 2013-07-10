NN = REPLICA

var dom1D = INTERVALS([1])([32])
var dom2D = DOMAIN([[0,1],[0,1]])([30,30])

function bezierS0(controlpoints){
	return BEZIER(S0)(controlpoints)
}

function bezierS1(f){
	return BEZIER(S1)(f)
}

function bezierMappata_1D(controlpoints){
	return MAP(bezierS0(controlpoints))(INTERVALS(1)(32))
}

function bezierMappata_2D(functions){
	var x = BEZIER(S1)(functions)
	return MAP(x)(dom2D) 
}

function addDepth(z){
	function atPoint(punto){
		return [punto[0],punto[1],z];
	}
	return atPoint;
}

function traslaY(y){
	function atPoint(punto){
		return [punto[0],punto[1]+y,punto[2]];
	}
	return atPoint;
}

function color(arrayColor){
	return [arrayColor[0]/255,arrayColor[1]/255,arrayColor[2]/255]
}
//----------------------------------  Niemeyer dining table 1985  -------------------------------------------
var x1_p = [[1.89, 1.22], [2.48, 1.36], [3.27, 1.51], [3.27, 2.6]].map(addDepth(0));
var x1_2d = bezierMappata_1D(x1_p);
var x1_s0 = bezierS0(x1_p);

var x2_p = [[1.89, 1.32], [2.56, 1.49], [3.11, 1.69], [3.19, 2.6]].map(addDepth(0));
var x2_2d = bezierMappata_1D(x2_p);
var x2_s0 = bezierS0(x2_p);

var x1_dietro_p = [[1.89, 1.22], [2.48, 1.36], [3.27, 1.51], [3.27, 2.6]].map(addDepth(-5));
var x1_dietro_2d = bezierMappata_1D(x1_dietro_p);
var x1_dietro_s0 = bezierS0(x1_dietro_p);

var x2_dietro_p = [[1.89, 1.32], [2.56, 1.49], [3.11, 1.69], [3.19, 2.6]].map(addDepth(-5));
var x2_dietro_2d = bezierMappata_1D(x2_dietro_p);
var x2_dietro_s0 = bezierS0(x2_dietro_p);

var xt1_p = [[1.89, 1.22,0],[1.89, 1.22,-5]]
var xt1_2d = bezierMappata_1D(xt1_p);
var xt1_s0 = bezierS0(xt1_p);
//DRAW(xt_2d)

var xt2_p = [[1.89, 1.32,0],[1.89, 1.32,-5]]
var xt2_2d = bezierMappata_1D(xt2_p);
var xt2_s0 = bezierS0(xt2_p);
//DRAW(xt2_2d)

var zampa_parte1 = bezierMappata_2D([x1_s0,x2_s0])
var zampa_parte2 = bezierMappata_2D([x1_dietro_s0,x2_dietro_s0])
var zampa_parte3 = bezierMappata_2D([x1_s0,x1_dietro_s0])
var zampa_parte4 = bezierMappata_2D([x2_s0,x2_dietro_s0])
var zampa_parte5 = bezierMappata_2D([xt1_s0,xt2_s0])

mezzo = STRUCT([zampa_parte1,zampa_parte2,zampa_parte3,zampa_parte4,zampa_parte5]);
mezzo = T([0,1,2])([-3.4,-2,2.5])(mezzo)
mezzoRuotato = R([0,2])([PI])(mezzo)
zampeTavolo = STRUCT([mezzoRuotato,mezzo])
zampeTavolo = COLOR([222/255,184/255,135/255])(zampeTavolo)
DRAW(zampeTavolo)

circle = DISK(3)([30,1])
circle = EXTRUDE([0.1])(circle)
circle = R([1,2])([PI/2])(circle)
circle = T([1])([0.7])(circle)
circle = COLOR([92/255,51/255,23/255])(circle)
DRAW(circle)

tavolo = STRUCT([circle,zampeTavolo])
DRAW(tavolo)
