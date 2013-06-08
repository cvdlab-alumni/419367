/************ SETTLEMENTS ************/
function z(u,v) {
	return SIN(u)+SIN(v);
}

var plain1 = T([0,1,2])([9.1,2.6,-1.2])(COLOR([0.545,0.27,0.0745])(CUBOID([4.1,4.1,0.7])));
var plain2 = T([0,1,2])([2.6,9.1,-1.2])(COLOR([0.545,0.27,0.0745])(CUBOID([4.1,4.1,0.7])));
DRAW(STRUCT([plain1,plain2]));

function building(a,b,h,l){
	var points = [[0,0],[a,0],[0,b],[a,b],[a/2,b+h]];
	var cells = [[0,1,2],[1,3,2],[2,3,4]];
	var house = R([1,2])(PI/2)(EXTRUDE([l])(SIMPLICIAL_COMPLEX(points)(cells)));
	return house;
}

var settlement1_0 = [];
for(var i=0;i<=2;i++){
	var tx = 9.7+i;
	var ty = 6;
	var a = Math.random()*0.5+0.1;
	var b = Math.random()*0.5+0.1;
	var h = Math.random()*0.5+0.1;
	var l = Math.random()*0.5+0.5;
	settlement1_0[i] = COLOR([0.803,0,0])(T([0,1,2])([tx,ty,-0.5])(building(a,b,h,l)));
	DRAW(settlement1_0[i]);
}

var settlement1_1 = [];
for(var i=0;i<=2;i++){
	var tx = 9.7+i;
	var ty = 4.5;
	var a = Math.random()*0.5+0.1;
	var b = Math.random()*0.5+0.1;
	var h = Math.random()*0.5+0.1;
	var l = Math.random()*0.5+0.5;
	settlement1_1[i] = COLOR([0.803,0,0])(T([0,1,2])([tx,ty,-0.5])(building(a,b,h,l)));
	DRAW(settlement1_1[i]);
}

var settlement2_0 = [];
for(var i=0;i<=2;i++){
	var tx = 3.3+i;
	var ty = 10.8;
	var a = Math.random()*0.5+0.1;
	var b = Math.random()*0.5+0.1;
	var h = Math.random()*0.5+0.1;
	var l = Math.random()*0.5+0.5;
	settlement2_0[i] = COLOR([0.803,0,0])(T([0,1,2])([tx,ty,-0.5])(building(a,b,h,l)));
	DRAW(settlement2_0[i]);
}

var settlement2_1 = [];
for(var i=0;i<=2;i++){
	var tx = 3.3+i;
	var ty = 12.0;
	var a = Math.random()*0.5+0.1;
	var b = Math.random()*0.5+0.1;
	var h = Math.random()*0.5+0.1;
	var l = Math.random()*0.5+0.5;
	settlement2_1[i] = COLOR([0.803,0,0])(T([0,1,2])([tx,ty,-0.5])(building(a,b,h,l)));
	DRAW(settlement2_1[i]);
}
