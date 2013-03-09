for (var i = 1; i <11; i++) {
	var riga = "";
	for (var j = 1; j < 10; j++) {
		//Colonne da 1 a 9
		if(i===j){
			  	riga = riga + "\t1,";
			}else{
				riga = riga + "\t0,";
			};
		};
		//Ultima colonna
		if(i===j){
			  	riga = riga + "\t1";
			}else{
				riga = riga + "\t0";
			};	
	console.log(riga + "\n");
 };
