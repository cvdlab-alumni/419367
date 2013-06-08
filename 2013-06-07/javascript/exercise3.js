/*** TREE MODEL ***/
var domain_Tree = PROD1x1([INTERVALS(1)(20),INTERVALS(1)(6)]);
//Parametri base cono
var x = 0.16
var y = 0.1
//Funzione che genera un albero parametrico
function Tree(h_body,h_head,r_body,r_head){
	var body = EXTRUDE([h_body])(DISK(r_body)(10));
	var profile = BEZIER(S0)([[0,0,0],[0,y*r_head,0],[x*r_head,y*r_head,0],[x*r_head,0,0],[x*r_head,-y*r_head,0],[0,-y*r_head,0],[0,0,0]]);
	var apex = [x*r_head/2,0,h_head];
	var head = T([0,2])([-x*r_head/2+r_body/2,h_body])(MAP(CONICAL_SURFACE(apex)(profile))(domain_Tree));
	return STRUCT([COLOR([0.545,0.278,0.149])(body),COLOR([0.153,0.545,0.153])(head)]);
}
//Genera foresta
var forest = [];
for(var i=0;i<=300;i++){
	var t1 = Math.random()+Math.random()*13;
	var t2 = Math.random()+Math.random()*13;
	var h_body = Math.random()+0.1;
	var h_head = Math.random()+0.1;
	var r_body = Math.random()*0.1+0.01;
	var r_head = Math.random()*10+1;
	if(z(t1,t2)>=0.05){
	forest[i] = T([0,1,2])([t1,t2,z(t1,t2)-0.15])(Tree(h_body,h_head,r_body,r_head));
	DRAW(forest[i]);
	}
}
