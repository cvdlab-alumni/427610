var dominio = DOMAIN([[-30, 30], [-30, 30]])([30,30]);

var montagneF = function(punto){
	var x = punto[0];
	var y = punto[1];
	//var z =  Math.random()*3 * SIN(x) * COS(y);
	var z =  Math.pow(Math.random()*3 * SIN(x) * COS(y),1.3);
	var random = Math.random()/5;
	z = random + z;
	return [x, y, z];
}
var territorio = MAP(montagneF)(dominio);

DRAW(COLOR([160/255, 82/255, 45/255])(territorio));