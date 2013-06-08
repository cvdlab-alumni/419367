/********************TERRITORY****************/
function z(u,v) {
	return SIN(u)+SIN(v);
}

function plain(x, y) {
	var lines = [];
	for (var i=0; i<x; i++) {
		for (var j=0; j<y; j++) {
			lines.push([i,j,z(i,j)]);
		}
	}
	return lines;
}

function pol(points, x) {
	var polygons = [];
	for (var k=1; k<points-x; k++) {
		if ((k%x)!==0) {
			polygons.push([k-1,k,k+x-1]);
			polygons.push([k,k+x-1,k+x]);
		}
	}
	return polygons;
}

var territory = COLOR([0.545,0.27,0.0745])(SIMPLICIAL_COMPLEX(plain(15,15))(pol(225,15)));
DRAW(territory)