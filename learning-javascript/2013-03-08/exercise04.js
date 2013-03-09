var data = [
  {id:'01', name:'duffy'},
  {id:'02', name:'michey'},
  {id:'03', name:'donald'},
  {id:'04', name:'goofy'},
  {id:'05', name:'minnie'},
  {id:'06', name:'scrooge'}
];
var key = 'name';
var values = ['goofy', 'scrooge'];

/*
* Con filter e some
*/

function select(data,key,values){
	var dataFiltered = data.filter(
		function(item){
			return values.some(
				function(valore){
					return item[key]===valore;
				}
			);
		}
	);
	return dataFiltered;
}

/*
* Senza filter
*/
function select(data,key,values){
	var result = [];
	for (var i = 0; i < data.length; i++) {
		var obj = data[i];
		var name = obj[key];
		for(var j=0; j<values.length; j++){
			if(name===values[j]){
				result.push(obj);
			}
		}
	};
	return result;
}

