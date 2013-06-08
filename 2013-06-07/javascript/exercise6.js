//Presi da https://github.com/cvdlab-cg/lessons/blob/master/lessons/2013-06-04/examples.py
FV = [[5,6,7,8],
[0,5,8],
[0,4,5],
[1,2,4,5],
[2,3,5,6],
[0,8,7], [3,6,7], [1,2,3], [0,1,4]
]

V = [[0,6],
[0,0],
[3,0],
[6,0],
[0,3],
[3,3],
[6,3],
[6,6],
[3,6]]

larModel = [V,FV]

var lar_to_obj = function(larModel){
	var V = larModel[0];
	var FV = larModel[1];
	var result = "";
	for (var i = 0; i < V.length; i++){
		result+= "v ";
		(V[i][2] !== undefined) ? 
			result+= V[i][0]+" "+V[i][1]+" "+V[i][2] : result+= V[i][0]+" "+V[i][1]+" 0"
		result+="\n";
	}
	result = result.concat("\n");
	for (var i = 0; i < FV.length; i++){
		result+="f ";
		for (var j = 0; j < FV[i].length; j++) {
			result+=FV[i][j] + " ";
		};
		result+="\n";
	}
	return result;
}

x = lar_to_obj(larModel);

