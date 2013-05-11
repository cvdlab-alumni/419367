
# XZ PROFILE

domain= GRID([20,40])

c01=BEZIER(S1)([[3.34,0, 3.52], [3.32,0, 3.46], [3.39,0, 3.45], [3.44,0, 3.45]])
curve01 = MAP(c01)(domain)

c02=BEZIER(S1)([[3.34,0, 3.52], [3.62,0, 4.9], [1.7,0, 4.94], [1.98,0, 3.49]])
curve02 = MAP(c02)(domain)

c03=BEZIER(S1)([[1.89,0, 3.42], [1.94,0, 3.42], [1.99,0, 3.43], [1.98,0, 3.49]])
curve03 = MAP(c03)(domain)

c04=BEZIER(S1)([[0.6,0, 3.43], [0.78,0, 3.38], [1.28,0, 3.42], [1.89,0, 3.42]])
curve04 = MAP(c04)(domain)

c05=BEZIER(S1)([[0.6,0, 3.43], [0.63,0, 3.63], [0.52,0, 3.55], [0.58,0, 3.66]])
curve05 = MAP(c05)(domain)

c06=BEZIER(S1)([[0.66,0, 3.89], [0.76,0, 3.87], [0.71,0, 3.71], [0.58,0, 3.66]])
curve06 = MAP(c06)(domain)

c07=BEZIER(S1)([[0.66,0, 3.89], [0.61,0, 3.98], [0.84,0, 4.11], [1.03,0, 4.25]])
curve07 = MAP(c07)(domain)

c08=BEZIER(S1)([[2.76,0, 4.72], [2.33,0, 4.75], [1.26,0, 4.39], [1.03,0, 4.25]])
curve08 = MAP(c08)(domain)

c09=BEZIER(S1)([[2.76,0, 4.72], [2.93,0, 4.8], [2.93,0, 4.8], [2.97,0, 4.78]])
curve09 = MAP(c09)(domain)

c10=BEZIER(S1)([[5.96,0, 5.4], [4.06,0, 5.56], [4.36,0, 5.3], [2.97,0, 4.78]])
curve10 = MAP(c10)(domain)

c11=BEZIER(S1)([[5.96,0, 5.4], [5.96,0, 5.3], [6.33,0, 5.21], [7.74,0, 5.04]])
curve11 = MAP(c11)(domain)

c12=BEZIER(S1)([[8.69,0, 5.41], [8.56,0, 5.39], [8.45,0, 5.24], [7.74,0, 5.04]])
curve12 = MAP(c12)(domain)

c13=BEZIER(S1)([[8.69,0, 5.41], [8.81,0, 5.46], [9.07,0, 5.33], [9.34,0, 5.46]])
curve13 = MAP(c13)(domain)

c14=BEZIER(S1)([[9.09,0, 4.86], [9.14,0, 4.96], [9.09,0, 5.25], [9.34,0, 5.46]])
curve14 = MAP(c14)(domain)

c15=BEZIER(S1)([[9.09,0, 4.86], [9.37,0, 5.01], [9.13,0, 4.53], [9.4,0, 4.33]])
curve15 = MAP(c15)(domain)

c16=BEZIER(S1)([[9.26,0, 3.7], [9.29,0, 3.78], [9.39,0, 4.11], [9.4,0, 4.33]])
curve16 = MAP(c16)(domain)

c17=BEZIER(S1)([[9.26,0, 3.7], [9.21,0, 3.69], [8.98,0, 3.62], [8.61,0, 3.63]])
curve17 = MAP(c17)(domain)

c18=BEZIER(S1)([[8.55,0, 3.7], [8.54,0, 3.65], [8.6,0, 3.64], [8.61,0, 3.63]])
curve18 = MAP(c18)(domain)

c19=BEZIER(S1)([[8.55,0, 3.7], [8.59,0, 4.98], [6.74,0, 4.95], [7.03,0, 3.57]])
curve19 = MAP(c19)(domain)

c20=BEZIER(S1)([[6.97,0, 3.5], [6.99,0, 3.5], [7.02,0, 3.57], [7.02,0, 3.57]])
curve20 = MAP(c20)(domain)

c21=BEZIER(S1)([[3.44,0, 3.45], [4.43,0, 3.45], [7.03,0, 3.49], [6.97,0, 3.5]])
curve21 = MAP(c21)(domain)

xz_profile = STRUCT([curve01,curve02,curve03,curve04,curve05,curve06,curve07,curve08,curve09,curve10,
			curve11,curve12,curve13,curve14,curve15,curve16,curve17,curve18,curve19,curve20,curve21])

S_T_xz_profile = S(1)(0.94)(T([1,3])([-5,-3.45])(xz_profile))

#XY PROFILE

c_xy_01=BEZIER(S1)([[7.97, 5.56,0], [8.35, 5.56,0], [8.42, 2.23,0], [7.98, 2.14,0]])
curve_xy_01 = MAP(c_xy_01)(domain)

c_xy_02=BEZIER(S1)([[4.46, 2.1,0], [5.13, 2.13,0], [6.62, 1.87,0], [7.98, 2.14,0]])
curve_xy_02 = MAP(c_xy_02)(domain)

c_xy_03=BEZIER(S1)([[4.46, 2.1,0], [4.01, 2.13,0], [3.66, 2.13,0], [3.38, 2.13,0]])
curve_xy_03 = MAP(c_xy_03)(domain)

c_xy_04=BEZIER(S1)([[3.57, 1.78,0], [3.55, 1.79,0], [3.37, 2.11,0], [3.38, 2.13,0]])
curve_xy_04 = MAP(c_xy_04)(domain)

c_xy_05=BEZIER(S1)([[3.57, 1.78,0], [3.39, 1.66,0], [3.27, 1.99,0], [3.24, 2.11,0]])
curve_xy_05 = MAP(c_xy_05)(domain)

c_xy_06=BEZIER(S1)([[0.8, 2.34,0], [1.67, 1.97,0], [2.28, 2.15,0], [3.24, 2.11,0]])
curve_xy_06 = MAP(c_xy_06)(domain)

c_xy_07=BEZIER(S1)([[0.8, 2.34,0], [0.3, 2.46,0], [0.26, 2.62,0], [0.23, 3.05,0]])
curve_xy_07 = MAP(c_xy_07)(domain)

c_xy_08=BEZIER(S1)([[0.25, 4.48,0], [0.12, 3.66,0], [0.33, 3.32,0], [0.23, 3.05,0]])
curve_xy_08 = MAP(c_xy_08)(domain)

c_xy_09=BEZIER(S1)([[0.25, 4.48,0], [0.2, 4.58,0], [0.24, 5.16,0], [0.46, 5.19,0]])
curve_xy_09 = MAP(c_xy_09)(domain)

c_xy_10=BEZIER(S1)([[3.21, 5.56,0], [1.84, 5.56,0], [1.45, 5.65,0], [0.46, 5.19,0]])
curve_xy_10 = MAP(c_xy_10)(domain)

c_xy_11=BEZIER(S1)([[3.21, 5.56,0], [3.31, 5.64,0], [3.26, 5.88,0], [3.49, 5.92,0]])
curve_xy_11 = MAP(c_xy_11)(domain)

c_xy_12=BEZIER(S1)([[3.37, 5.56,0], [3.46, 5.77,0], [3.61, 5.89,0], [3.49, 5.92,0]])
curve_xy_12 = MAP(c_xy_12)(domain)

c_xy_13=BEZIER(S1)([[3.37, 5.56,0], [4.95, 5.53,0], [6.47, 5.83,0], [7.97, 5.56,0]])
curve_xy_13 = MAP(c_xy_13)(domain)

xy_profile = STRUCT([curve_xy_01,curve_xy_02,curve_xy_03,curve_xy_04,curve_xy_05,curve_xy_06,
			curve_xy_07,curve_xy_08,curve_xy_09,curve_xy_10,curve_xy_11,curve_xy_12,curve_xy_13])

T_xy_profile = T([1,2,3])([-4.2,-3.85,0.8])(xy_profile)


#YZ SECTION

c_yz_01=BEZIER(S1)([[0,0.38, 4.31], [0,0.97, 4.28], [0,2.75, 4.3], [0,3.2, 4.31]])
curve_yz_01 = MAP(c_yz_01)(domain)

c_yz_02=BEZIER(S1)([[0,0.38, 4.31], [0,0.36, 5.4], [0,0.26, 5.2], [0,0.74, 5.26]])
curve_yz_02 = MAP(c_yz_02)(domain)

c_yz_03=BEZIER(S1)([[0,1.37, 5.8], [0,0.92, 5.81], [0,0.9, 5.53], [0,0.74, 5.26]])
curve_yz_03 = MAP(c_yz_03)(domain)

c_yz_04=BEZIER(S1)([[0,1.37, 5.8], [0,2.67, 5.8], [0,2.44, 5.88], [0,2.84, 5.26]])
curve_yz_04 = MAP(c_yz_04)(domain)

c_yz_05=BEZIER(S1)([[0,3.18, 4.31], [0,3.17, 5.28], [0,3.44, 5.23], [0,2.84, 5.26]])
curve_yz_05 = MAP(c_yz_05)(domain)

yz_section = STRUCT([curve_yz_01,curve_yz_02,curve_yz_03,curve_yz_04,curve_yz_05])

S_T_yz_section = S([2,3])([1.2,1.33])(T([2,3])([-1.8,-4.3])(yz_section))

#2.5 MODEL
model = STRUCT([T_xy_profile,S_T_xz_profile,S_T_yz_section])
VIEW(model)