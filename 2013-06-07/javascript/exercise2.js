var dominio = DOMAIN([[-30, 30], [-30, 30]])([30,30]);

//Mappa per salvare la z di ogni punto
var mappaZ = {};

var montagneF = function(punto){
	var x = punto[0];
	var y = punto[1];
	var z =  Math.pow(Math.random()*3 * SIN(x) * COS(y),2);
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
