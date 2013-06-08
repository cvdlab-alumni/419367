/****************ROADS************/
function road(l,s){ 
	var base = T([1,2])([-s/2+0.005,-0.2])(COLOR([0.2,0.2,0.2])(SIMPLEX_GRID([[l],[s],[0.2]])));
	var line = COLOR([1,1,1])(SIMPLEX_GRID([[l/9.,-l/9.,l/9.,-l/9.,l/9.,-l/9.,l/9.,-l/9.,l/9.],[0.02],[0.001]]));
	return STRUCT([base,line]);
}

/******ROADS FIRST SETTLEMENT*****/
l_1 = Math.random()+2.5;
s_1 = Math.random()*0.4;
var tx_1 = 9.5;
var ty_1 = 4.8;
var roads1 = [];
roads1[0] = T([0,1,2])([tx_1,ty_1,-0.49])(road(l_1,s_1));
DRAW(roads1[0]);

for(var i=1;i<3;i++){
	l_1 = Math.random()+2.5;
	s_1 = Math.random()*0.4;
	var tx_1 = 9.5+i;
	var ty_1 = 3.1;
	roads1[i] = T([0,1,2])([tx_1,ty_1,-0.49])(R([0,1])(PI/2)(road(l_1,s_1)));
	DRAW(roads1[i]);;
 }

/*****ROADS SECOND SETTLEMENT*****/
l_2 = Math.random()+2.5;
s_2 = Math.random()*0.4;
var tx_2 = 3.1;
var ty_2 = 11;
var roads2 = [];
roads2[0] = T([0,1,2])([tx_2,ty_2,-0.49])(road(l_2,s_2));
DRAW(roads2[0]);

for(var i=1;i<3;i++){
	l = Math.random()+2.5;
	s = Math.random()*0.4;
	var tx_2 = 3.1+i;
	var ty_2 = 9.3;
	roads2[i] = T([0,1,2])([tx_2,ty_2,-0.49])(R([0,1])(PI/2)(road(l_2,s_2)));
	DRAW(roads2[i]);;
 }
