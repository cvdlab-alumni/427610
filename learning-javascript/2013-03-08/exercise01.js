function exercise01(n){
	var array = [];
	var filterResult;
	var doubleResult;
	var divisibleByFour;
	var sum;

	for(var i=1;i<=n;i++){
		array.push(i);
	}
	filterResult = array.filter(odd_numbers);
	console.log("Filtrati" + filterResult);
	doubleResult = filterResult.map(multply);
	console.log("Raddoppiare" + doubleResult);
	divisibleByFour = doubleResult.filter(isDivisibleByFour);
	console.log("divisibili" + divisibleByFour);
	sum = divisibleByFour.reduce(sumAll);
	return sum;
}

function odd_numbers(item){
	return (item%2)===1;
}

function multply(item){
	return item * 4;
}

function isDivisibleByFour(item){
	return (item%4)===0;
}

function sumAll(prev, cur){
 return prev + cur;
}