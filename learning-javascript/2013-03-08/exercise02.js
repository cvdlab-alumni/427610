function insertRandomElements(n){
	var array = [];
	for(var i=0;i<n;i++){
		array[i] = Math.floor(Math.random()*11);
	}
	var oddOnes = array.filter(filterOdd);
	var sortedArray = oddOnes.sort(incremental)
	return sortedArray;
}

function filterOdd(item){
	return (item%2)===0;
}

function incremental(x,y){
	return x-y;
}