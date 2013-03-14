//Esercizio2a
function randomN(n) {
	var vettore = [];
	for(i=1;i<=n;i++){
	    vettore.push(Math.floor(Math.random()*101));
	}
return vettore;	
}

//Esercizio2b
var vettore = randomN(10);

var filterResult = vettore.filter(function(item,index,array){
	return (item % 2===0);
});

filterResult;

//Esercizio2c
var compare = function(value1,value2){
	return value1 - value2;
};

vettore.sort(compare);
vettore;
