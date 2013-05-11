#Volante

volante_esterno = COLOR(BLACK)(TORUS([9.4,11.4])([20,20]))


domain = GRID([40,40])
domain_3D = GRID([10,10,10])

c01=BEZIER(S1)([[1.5, 2.11,0], [1.58, 1.82,0], [1.88, 2.03,0], [2.16, 1.98,0],[2.16, 1.9,0], [2.32, 1.95,0], [2.36, 1.97,2],[4.29, 2.09,2], 
	[3.95, 2.32,2], [4.55, 2.39,2],[5.35, 2.19,2], [4.92, 2.11,2], [6.66, 1.98,0],[6.83, 1.92,0], [6.88, 2.07,0], [7.17, 2.05,0],[7.48, 1.97,0], [7.59, 2.05,0], [7.56, 2.19,0]])
curve01 = MAP(c01)(domain)

c02=BEZIER(S1)([[1.5, 0.91,0], [1.68, 1.01,0], [1.54, 1.04,0], [2.16, 0.98,0], [2.23, 1.08,0], [2.35, 1.02,0], [2.37, 1.01,0], [4.48, 0.79,2], [3.87, 0.62,2], 
	[4.56, 0.57,2],[4.53, 0.58,2], [5.12, 0.55,2], [4.62, 0.79,2], [6.68, 1.05,0], [6.71, 0.98,0], [6.79, 1.06,0], [6.87, 1.04,0],[7.18, 1.03,0], [7.44, 1.16,0], [7.58, 0.92,0]])
curve02 = MAP(c02)(domain)

v01= BEZIER(S2)([[1.48, 2.08,0], [1.35, 1.62,0], [1.3, 1.43,0], [1.49, 0.89,0]])
curve03 = MAP(v01)(domain)

v02= BEZIER(S2)([[7.55, 2.2,0], [7.87, 1.62,0], [7.71, 1.19,0], [7.58, 0.88,0]])
curve04 = MAP(v02)(domain)

surface = COONSPATCH([c01,c02,v01,v02])
solidMapping = THINSOLID(surface)

volante_interno = T([1,2,3])([13.55,5,0.3])(R([1,2])(PI)(MAP(solidMapping)(domain_3D)))

#Circle
outer_circle = CIRCLE(1.6)([40,1])
inner_circle = CIRCLE(1.2)([40,1])
circle = T([2,3])([0.4,0.7])(COLOR(BLACK)(PROD([DIFFERENCE([outer_circle,inner_circle]), Q(0.3)])))

S_volante = S([1,2,3])([0.02,0.02,0.02])(R([1,3])(PI/2)(STRUCT([volante_interno,volante_esterno,circle])))
T_volante = T([1,2,3])([-0.9,-0.9,1.1])(R([2,3])(PI/2)(S_volante))


#2.5D Model
model = STRUCT([T_xy_profile,S_T_xz_profile,T_yz_section,wheel_01,wheel_02,wheel_03,wheel_04,T_volante])
VIEW(model)