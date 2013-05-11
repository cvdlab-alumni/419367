#Pneumatico
#Funzione che permette di traslare sulle x una sezione di copertone
#In modo da ottenere uno pneumatico di spessore variabile
def Pneumatico(v):
	x = v[0]
	def Pneumatico0(p0):
		point = []
		for t in p0:
			u = [0,0,0]
			u[0] = t[0]+x
			u[1] = t[1]+0
			u[2] = t[2]+0
			point.append(u)
		return point
	return Pneumatico0

dominio_2D =GRID([50,50])
c0 = [[0,0,0],[6,0,0],[0,0,4],[6,0,7],[0,0,7]]
p = Pneumatico([8])(c0)
curve0 = BEZIER(S1)(p)
pneumatico = COLOR(BLACK)(MAP(ROTATIONALSURFACE(curve0))(S(2)(2*PI)(dominio_2D)))

#Cerchione esterno

rim_inner = CIRCLE(7.1)([40,1]);
rim_outer = CIRCLE(8)([40,1]);

rim = PROD([STRUCT([DIFFERENCE([rim_outer,rim_inner])]),Q(7)])

#Hub
outer_hub = CIRCLE(4)([40,1])
inner_hub = CIRCLE(2)([40,1])
hub = PROD([DIFFERENCE([outer_hub,inner_hub]), Q(7)])

#Superfici cerchione interno
domain = GRID([20,20])
domain_3D = GRID([10,10,10])

c01=BEZIER(S1)([[2.85, 4.57,0], [3.1, 3.68,0], [3.26, 3.81,0], [2.42, 3.48,0]])
curve01 = MAP(c01)(domain)

c03=BEZIER(S1)([[3.04, 4.77,0], [3.77, 3.34,0], [3.79, 3.91,0], [2.48, 3.12,0]])
curve03 = MAP(c03)(domain)

s = BEZIER(S2)([c01,c03])
solid = THINSOLID(s)

s_1 = T([1,2])([15,-18.5])(S([1,2])([4,5.2])(R([1,2])((PI/2)+(PI*5/180))(MAP(solid)(domain_3D))))
s_2 = R([1,2])(PI*72/180)(s_1)
s_3 = R([1,2])(PI*72/180)(s_2)
s_4 = R([1,2])(PI*72/180)(s_3)
s_5 = R([1,2])(PI*72/180)(s_4)

#HUB
outer_hub = CIRCLE(3)([200,1])
inner_hub = CIRCLE(2)([200,1])
hub = T(3)(1)(PROD([DIFFERENCE([outer_hub,inner_hub]), Q(1.5)]))

#SPHERE
sphere = T(3)(1.7)(SPHERE(2)([40,40]))

#DISC BRAKE
brake_inner = CIRCLE(1.2)([40,1]);
brake_outer = CIRCLE(5)([40,1]);
brake = T(3)(3)(COLOR(RED)(PROD([DIFFERENCE([brake_outer,brake_inner]), Q(0.5)])))

wheel = S([1,2])([1/2,1/2])(COLOR(WHITE)(STRUCT([pneumatico,rim,hub,s_1,s_2,s_3,s_4,s_5,sphere,brake])))

#Ruote parte destra
wheel_01 = T([1,2,3])([-2.17,1.7,0.56])(R([2,3])(PI/2)(S([1,2,3])([0.05,0.05,0.05])(wheel)))
wheel_02 = T([1,2])([4.7,0.1])(wheel_01)

#Ruote parte sinistra
wheel_03 = T([1,2])([0.36,-0.1])(R([1,2])(PI)(wheel_01))
wheel_04 = T([1,2])([0.36,0.05])(R([1,2])(PI)(wheel_02))

#2.5D MODEL 
model = STRUCT([T_xy_profile,S_T_xz_profile,T_yz_section,wheel_01,wheel_02,wheel_03,wheel_04])
VIEW(model)


#Per motivi di tempo ho testato la posizione delle ruote evitando di mettere qualche oggetto come hub sphere
#e brake nella STRUCT del modello in modo che visualizzasse in poco tempo il risultato




