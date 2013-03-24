//Esercizio 1
function Point2D(x,y){
	this.x = x;
	this.y = y;
}

//Esercizio 2
function Edge(p1,p2){
	this.p1 = p1;
	this.p2 = p2;
}

var punto1 = new Point2D(0,0);
var punto2 = new Point2D(5,0);
var punto3 = new Point2D(2.5,2.5);
var lato1 = new Edge(punto1,punto2);
var lato2 = new Edge(punto1,punto3);
var lato3 = new Edge(punto2,punto3);

//Esercizio 3
Edge.prototype.length = function(){
	var x1 = this.p1.x;
	var x2 = this.p2.x;
	var y1 = this.p1.y;
	var y2 = this.p2.y;
	return Math.sqrt((Math.pow(x2-x1, 2))+(Math.pow(y2-y1, 2)));
}

//Esercizio 4
function Triangle(e1,e2,e3){
	this.e1 = e1;
	this.e2 = e2;
	this.e3 = e3;
}

var triangolo = new Triangle(lato1,lato2,lato3)

//Esercizio 5
Triangle.prototype.perimeter = function(){
	return this.e1.length() + this.e2.length() + this.e3.length();
}

//Esercizio 6
Triangle.prototype.area = function(){
	var semi = this.perimeter()/2;
	var a = this.e1.length();
	var b = this.e2.length();
	var c = this.e3.length();
	return Math.sqrt(semi*(semi-a)*(semi-b)*(semi-c));
}