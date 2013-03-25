Triangle.protoype.perimeter = function () {
	var perimetro = e1.length() + e2.length() + e3.length();
return perimetro;
}

Triangle.protoype.area = function () {
	var p = this.perimeter() / 2;
	var a = Math.sqrt(this.p * (p-this.e1.length()) * (p- this.e2.length()) * (p-this.e3.length()));
return a;
}