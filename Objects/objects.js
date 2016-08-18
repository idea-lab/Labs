var Person= function(age, name){
	this.name=name;
	this.age=age;
};
Person.prototype.getName = function() {
	return this.name;
};
Person.prototype.getAge=function(){
	return this.age;
}




var p=new Person("Sub", 12);
console.log(p.getName());
console.log(p.getAge())