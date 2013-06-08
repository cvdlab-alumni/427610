var dominio = DOMAIN([[-30, 30], [-30, 30]])([30,30]);
//ES 1 e 2
//Mappa per salvare la z di ogni punto
var mappaZ = {};

var montagneF = function(punto){
	var x = punto[0];
	var y = punto[1];
	var z =  Math.random()*3 * SIN(x) * COS(y);
	var random = Math.random()/5;
	z = random + z;
	mappaZ[punto[0]+","+punto[1]] = z;
	return [x, y, z];
}

var lagoF = function (max) {
	function l (punto) {
		var x = punto[0];
		var y = punto[1];
		var z = max;
		//console.log("["+ x + " , " + y + ", " +z + "]")
		return [x, y, z];
	}
	return l;	
}

var minimo = function(){
	var m = 100;
	for (var i = 0; i <= 5; i++) {
		for (var j = 0; j <= 5; j++) {
			if(mappaZ[i+","+j]<m) m=mappaZ[i+","+j];	
		};
	};
	return m;
}

var massimo = function(){
	var m = -100;
	for (var i = 0; i <= 5; i++) {
		for (var j = 0; j <= 5; j++) {
			if(mappaZ[[i+","+j]]>m){ 
				m=mappaZ[[i+","+j]]; 
				//console.log(m);	
			}
		};
	};
	return m;
}

//Ex1
var territorio = MAP(montagneF)(dominio);
DRAW(territorio);

//Ex 2
var min = minimo(mappaZ);
var max = massimo(mappaZ);
var dominioLago = DOMAIN([[0, 5], [0, 5]])([1,1]);
var medio = (max-min)/2 -0.4;
lagoF = lagoF(medio);
var lago = MAP(lagoF)(dominioLago);
DRAW(COLOR([0,1,0])(lago))
//--------------------------------------------- ES3 ----------------------------------------
var domain2D = DOMAIN([[0,1],[0,1]])([30,30]);

function bezierS0(controlpoints){
  return BEZIER(S0)(controlpoints)
}

function bezierMappata_2D(functions){
  var x = BEZIER(S1)(functions)
  return MAP(x)(domain2D) 
}

function cerc(r,z){
  var points = [[1,0,0],[1,1,0],[0,1.7,0],[-1.7,1,0],[-1.7,0,0],[-1,-1.4,0],[0,-1.6,0],[1,-0.9,0],[1,0,0]];
  var c = points.map(function(point){return [point[0]*r,point[1]*r,point[2]+z]})
  var cerchio = bezierS0(c);
  return cerchio;
}

var treeModel = function(raggio,z,altezzaTronco){
	var baseAlbero = cerc(raggio,z);
	var fin = cerc(raggio,altezzaTronco);
	var tronco = bezierMappata_2D([fin,baseAlbero]);
	var baseCono = cerc(raggio+0.5,altezzaTronco);
	var first = [0,0,altezzaTronco+1];
	var second =[0,0,altezzaTronco]
	var foglie = MAP(CONICAL_SURFACE(first)(baseCono))(domain2D);
	var baseFoglie = MAP(CONICAL_SURFACE(second)(baseCono))(domain2D);
	return STRUCT([COLOR([150/255, 75/255, 0])(tronco),COLOR([0,1,0])(foglie),COLOR([0,1,0])(baseFoglie)])
}

a = treeModel(0.1,0,2);

for (var i = 23; i <30; i++) {
	for (var j = 23; j < 30; j++) {
		z = mappaZ[i+","+j];
		//z
		DRAW(T([0,1,2])([i,j,z])(a))
	};
};
//---------------------------------------------------------------- ES4
NN = REPLICA

function house(width,height){
	var points = [[0,0],[width,0],[0,height],[width,height],[width/2,height+height*0.5]];
	var cells = [[0,1,2],[1,3,2],[2,3,4]];
	var single_house = SIMPLICIAL_COMPLEX(points)(cells);
	single_house = EXTRUDE([1])(single_house);
	return single_house;
}

function settlement(offset_x,offset_y,offset_house_x,offset_house_y, many_x,many_y) {
		horizontal = STRUCT(
				NN(many_x)
				(
					[ 
					house(1,1.5), T([0])([offset_house_x]), house(0.5,1), T([0])([offset_house_x])
					]
				)
				)
		horizontal  = R([1,2])([PI/2])(horizontal)
		var matrix = []
		for (var i = 0;i < many_y; i++) {
			matrix.push(horizontal);
			matrix.push(T([1])([offset_house_y]))
		};
		matrix = STRUCT(matrix);
		
		matrix = T([0,1])([offset_x,offset_y])(matrix);
		return matrix
}

firstSettlement = settlement(30,15,5,5,5,5)
secondSettlement = settlement(-48,7,3,6,3,4)
DRAW(firstSettlement)
DRAW(secondSettlement)
//--------------------------------- ES5
NN = REPLICA
function road(width,height){
	return CUBOID([width,height,0.1])
}

function roadsHorizontal(offset_x,offset_y,width_road,height_road,offset_house_x, offset_house_y, many_x,many_y) {
	horizontal = STRUCT(
				NN(many_x)
				(
					[ 
					road(width_road,height_road), T([1])([offset_house_y])
					]
				)
				)

	horizontal = T([0,1])([offset_x,offset_y])(horizontal)
	return horizontal;
}

function roadsVertical(offset_x,offset_y,width_road,height_road,offset_house_x, offset_house_y, many_x,many_y) {
	vertical = STRUCT(
				NN(many_y)
				(
					[ 
					road(width_road,height_road), T([0])([offset_house_x])
					]
				)
				)
	vertical = T([0,1])([offset_x,offset_y])(vertical)
	return vertical;
}

//Strade per il primo villaggio
stradeHor = roadsHorizontal(30,15,46,3.6,0,5,4,0)
stradeVer = roadsVertical(31,15,3,15,5,0.1,0,9)
DRAW(stradeHor)
DRAW(stradeVer)

//Strade per il secondo villaggio
stradeHor = roadsHorizontal(-49,7,18,3.8,0,6.3,3,0)
stradeVer = roadsVertical(-50,5,2,19,3,0.4,0,7)
DRAW(stradeHor)
DRAW(stradeVer)