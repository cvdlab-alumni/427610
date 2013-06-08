var dominio = DOMAIN([[-30, 30], [-30, 30]])([30,30]);

//Mappa per salvare la z di ogni punto
var mappaZ = {};

var montagneF = function(punto){
	var x = punto[0];
	var y = punto[1];
	var z =  Math.pow(Math.random()*3 * SIN(x) * COS(y),1.3);
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
		console.log("["+ x + " , " + y + ", " +z + "]")
		return [x, y, z];
	}
	return l;	
}

var minimo = function(){
	var m = 100;
	for (var i = 24; i <= 28; i++) {
		for (var j = -5; j <= 5; j++) {
			if(mappaZ[i+","+j]<m) m=mappaZ[i+","+j];	
		};
	};
	return m;
}

var massimo = function(){
	var m = -100;
	for (var i = 24; i <= 28; i++) {
		for (var j = -5; j <= 5; j++) {
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
DRAW(COLOR([160/255, 82/255, 45/255])(territorio));

//Ex 2
var min = minimo(mappaZ);
var max = massimo(mappaZ);
var dominioLago = DOMAIN([[0, 5], [-5, 5]])([1,1]);
var medio = 0.15;
lagoF = lagoF(medio);
var lago = MAP(lagoF)(dominioLago);
DRAW(COLOR([70/255,130/255,180/255])(lago))
