for (var i = 1; i <11; i++) {
	var riga = "";
	for (var j = 1; j < 11; j++) {
		if(j===10){
			riga = riga + i*j;
		}else{
			riga = riga + i*j + ",\t";
		}
	};
	console.log(riga + "\n");
 };