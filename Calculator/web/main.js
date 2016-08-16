function add(x, y){
	return x+y;
}
function sub(x, y){
	return x-y;
}
function mult(x, y){
	return x*y;
}
function div(x, y){
	return x/y;
}
var input="";

function update(x){
	if(!isNaN(x)){
		input+=x;
		console.log(input);
		document.getElementById("calcText").innerHTML=input;
	}
	else{

	}
}
