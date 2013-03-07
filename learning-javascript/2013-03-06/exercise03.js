var s = '\n';
var n = 10;
var m = 10;

for (var i = 1; i <= n; i++) {
  for (var j = 1; j <= m; j++) {
    if(i===j)
	s += 1;
    else 
	s += 0;
    if (j%10===0){
    	s += '\t';}
    else {
	s += ',';
	s += '\t';
	}
  }
  s += '\n';
}

console.log(s);
