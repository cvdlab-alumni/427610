var dominio = DOMAIN([[-30, 30], [-30, 30]])([30,30]);

var montagne = function(punto){
	var x = punto[0];
	var y = punto[1];
	var z =  Math.pow(Math.random()*3 * SIN(x) * COS(y),2);
	var random = Math.random()/5;
	return [x, y, random+z];
}

var territorio = MAP(montagne)(dominio);

DRAW(territorio);