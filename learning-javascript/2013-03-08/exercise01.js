//Esercizio01a
function pushN(n){
	var vettore = [];
	for(i=1;i<=n;i++){
	  vettore.push(i);		
	}
return vettore;
}

//Esercizio01b
var numbers = pushN(10);

var filterResult = numbers.filter(function(item){
 return (item % 2===0);
});

filterResult;

//Esercizio01c
var mapResult = filterResult.map(function(item, index, array){   
 return item * 2;
});

mapResult;

//Esercizio01d
var filterResult = mapResult.filter(function(item){
 return (item % 4===0);
});

filterResult;

//Esercizio01e
var sum = mapResult.reduce(function(prev, cur, index, array){
 return prev + cur;
});

sum;

//Esercizio02a
function randomN(n){
	var rand = [];
	for(i=1;i<=n;i++){
	  rand.push(i);		
	}
return vettore;
}

