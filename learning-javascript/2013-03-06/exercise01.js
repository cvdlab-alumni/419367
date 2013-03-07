var s = '\n';
var n = 10;
var m = 10;

for (var i = 1; i <= n; i++) {
  for (var j = 1; j <= m; j++) {
    s += j*i;
    s += '\t';
  }
  s += '\n';
}

console.log(s);
