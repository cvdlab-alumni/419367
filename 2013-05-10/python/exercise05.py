
#Cofano
domain = GRID([10,10])

cu0 = BEZIER(S1)([[0.66,2.43, 4.05], [0.93,2.43, 4.14], [1.75,2.43, 4.92], [3.22,2.43, 4.55]])
curve01 = MAP(cu0)(domain)

cu1 = BEZIER(S1)([[0.69,5.2, 4.05], [0.9,5.2, 4.14], [1.72,5.2, 4.92], [3.19,5.2, 4.55]])
curve02 = MAP(cu1)(domain)

c0v = BEZIER(S2)([[3.19, 5.2,4.55], [1.67, 4.91,4.55], [1.99, 2.49,4.55], [3.22, 2.43,4.55]])
curve03 = MAP(c0v)(domain)

c1v = BEZIER(S2)([[0.69, 5.2,4.05], [0.17, 3.92,4.05], [0.6, 2.71,4.05], [0.66, 2.43,4.05]])
curve04 = MAP(c1v)(domain)

#VIEW(STRUCT([curve01,curve02,curve03,curve04]))

#s= BEZIER(S2)([cu0,cu1,c0v,c1v])
surface = COONSPATCH([cu1,cu0,c1v,c0v])
surf = MAP(surface)(domain)
cofano = S([1,2,3])([0.33,0.33,0.33])(T([1,2,3])([-13,-11.5,-9.5])(COLOR(RED)(surf)))


#2.5 MODEL
model = STRUCT([T_xy_profile,S_T_xz_profile,S_T_yz_section,cofano])
VIEW(model)