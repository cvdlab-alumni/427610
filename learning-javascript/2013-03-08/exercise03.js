function capitalize(word){
	return word.toUpperCase();
}

function capitalizeEachWord(){
	var phrase = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
	var phraseCapitalized = "";
	var array = phrase.split(" ");
	for (var i = 0; i <  array.length; i++) {
		 array[i] = array[i].toUpperCase();
		 phraseCapitalized += array[i] + " ";
	};
	return phraseCapitalized;
}