function identity(n){
	var riga = "";
	for (var i = 0; i < n; i++) {
		for (var j = 0; j < n; j++) {
			if(i===j){
				riga += "1\t";
			}else{
				riga += "0\t";
			}
		};
		riga = riga + "\n";
	};
	return riga;
}

console.log(identity(10));