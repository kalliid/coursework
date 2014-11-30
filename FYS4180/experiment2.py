# -*- coding: utf-8 -*-

from RTMA import *

lmbda = 632 # wavelength [nm]
n = 1.0 	# refraction index of air

l = array([0, 150, 242, 252, 262, 272, 282, 292, 302, 312, 322, 332, 342, 352, 362, 382, 402, 422, 462, 502])
W_hor = array([804, 813, 455, 393, 301, 239, 163, 113, 79, 96, 171, 258, 329, 417, 483, 660, 792, 951, 1260, 1544]) # [mikro m]
W_vert = array([808, 815, 454, 394, 301, 236, 163, 112, 79, 94, 174, 260, 338, 421, 492, 657, 786, 957, 1260, 1566]) # [mikro m]

# Dataset 1
l1 = array([0, 150, 242, 252, 262, 272, 282, 292, 302, 312, 322, 332, 342, 352, 362, 382, 402, 422, 462, 502, 547, 567, 587, 672, 772, 887, 1019])
Wh1 = array([804, 813, 455, 393, 301, 239, 163, 113, 79, 96, 171, 258, 329, 417, 483, 660, 792, 951, 1260, 1544, 1545, 1545, 1552, 1571, 1593, 1606, 1620])/2. # [mikro m]
Wv1 = array([808, 815, 454, 394, 301, 236, 163, 112, 79, 94, 174, 260, 338, 421, 492, 657, 786, 957, 1260, 1566, 1561, 1542, 1562, 1572, 1561, 1600, 1628])/2. # [mikro m]

# Dataset 2
l2 = array([0, 150, 242, 252, 262, 272, 282, 292, 302, 312, 322, 332, 342, 352, 362, 382, 402, 422, 462, 502, 548, 557, 657, 757, 857, 1084, 1209, 1509, 2059, 2559])
Wh2 = array([804, 813, 455, 393, 301, 239, 163, 113, 79, 96, 171, 258, 329, 417, 483, 660, 792, 951, 1260, 1544, 1560, 1561, 1557, 1579, 1590, 1595, 1594, 1613, 1651, 1745])/2.
Wv2 = array([808, 815, 454, 394, 301, 236, 163, 112, 79, 94, 174, 260, 338, 421, 492, 657, 786, 957, 1260, 1566, 1597, 1600, 1580, 1586, 1580, 1605, 1626, 1650, 1700, 1836])/2.

# Dataset 3
l3 =  array([0, 150, 242, 252, 262, 272, 282, 292, 302, 312, 322, 332, 342, 352, 362, 382, 402, 422, 462, 502, 552, 622, 722, 822, 1084, 1184, 1284, 1509, 1859, 2159, 2609])
Wh3 = array([804, 813, 455, 393, 301, 239, 163, 113, 79, 96, 171, 258, 329, 417, 483, 660, 792, 951, 1260, 1544, 1580, 1576, 1574, 1565, 1522, 1511, 1501, 1500, 1474, 1459, 1464])/2.
Wv3 = array([808, 815, 454, 394, 301, 236, 163, 112, 79, 94, 174, 260, 338, 421, 492, 657, 786, 957, 1260, 1566, 1592, 1580, 1570, 1571, 1551, 1564, 1561, 1559, 1551, 1558, 1591])/2.

for i in range(3):
	l = [l1, l2, l3][i]
	Wh = [Wh1, Wh2, Wh3][i]
	Wv = [Wh1, Wh2, Wh3][i]
	xmax = [1100, 2600, 2650][i]
	W = (Wh + Wv)/2.

	w0 = W[0]

	def calculate_beam(R0, eps):
		q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
		solver = TMA(q0, lmbda, n)

		x1 = linspace(0,200,201)
		x2 = linspace(200,500+eps,301+eps)
		x3 = linspace(500+eps, xmax, xmax+1-500-eps)

		W1 = solver.beam_through_air(x1)
		solver.beam_through_lens(100)
		W2 = solver.beam_through_air(x2)
		solver.beam_through_lens(200)
		W3 = solver.beam_through_air(x3)

		x = concatenate((x1, x2, x3))
		Wfit = concatenate((W1, W2, W3))
		return x, Wfit

	def error(y):
		R0, eps = y
		x, Wfit = calculate_beam(R0, eps)
		residuals = zeros(len(l))
		for i in range(len(l)):
			residuals[i] = Wfit[l[i]] - W[i] 

		return residuals

	R0fit, eps = leastsq(error, (-10**4, 0))[0]
	print "Least squares estimations of Dataset 1:"
	print "R0: %.2e" % R0fit
	print "w0: %.2e" % w0
	print "eps: %.2e" % eps

	x, Wfit = calculate_beam(R0fit, eps)

	plot(l, W, 'o')
	plot(x, Wfit, linewidth=2.0)
	axvline(x=200, ymin=0, ymax=1, linewidth=2, color='r', linestyle="--")
	axvline(x=500+eps, ymin=0, ymax=1, linewidth=2, color='r', linestyle="--")
	grid()
	xlabel(r'Distance along optical axis, $l$ [mm]', fontsize=20)
	ylabel(r'Spot size, $w$ [$\mu$m]', fontsize=20)
	legend(['Measurements', 'Best TMA Fit', 'Lenses'], 'lower right', fontsize=20)
	title("Dataset %d" % i, fontsize=20)
	axis([-1, 1200, -1, 850])
	savefig("beam_expander_dataset_%d.pdf" % i)
	show()


# l_speil1 = 987 # Distance to mirror 1 [mm]
# l_speil2 = 650 # Distance between two mirror [mm]

# #########
# # Data set 1
# # Best distance between lenses from ABCD-fit 297 +- 2 mm
# # With R0 = -10^4, w0 = 393 microns.
# d0 = 22
# l1 = array([525,545,565,650,750,865,10+l_speil1])+d0 # [mm]
# UD1 = array([10,10,10,10,10,10,10]) # [mikro m]
# ###########################

# print l1

# # ###########################
# # Måleserie nr. 2
# # Beste avstand mellom linsene ved ABCD-tilpasning: 301 +- 2 mm
# # Med R0 = -10^4, w0 = 393 mikro m.
# l2 = array([526,535,635,735,835,75+l_speil1,200+l_speil1,500+l_speil1,400+l_speil1+l_speil2,900+l_speil1+l_speil2])+d0 # [mm]
# D_H2 = array([1560,1561,1557,1579,1590,1595,1594,1613,1651,1745]) # [mikro m]
# D_V2 = array([1597,1600,1580,1586,1580,1605,1626,1650,1700,1836]) # [mikro m]
# UD2 = array([10,10,10,10,10,10,10,10,20,20])  # [mikro m]
# ###########################

# ###########################
# # Måleserie nr. 3
# # Beste avstand mellom linsene ved ABCD-tilpasning: 305 +- 2 mm
# # Med R0 = -10^4, w0 = 393 mikro m.
# l3 = array([530,600,700,800,75+l_speil1,175+l_speil1,275+l_speil1,500+l_speil1,200+l_speil1+l_speil2,500+l_speil1+l_speil2,950+l_speil1+l_speil2])+d0 # [mm]
# D_H3 = array([1580,1576,1574,1565,1522,1511,1501,1500,1474,1459,1464]) # [mikro m]
# D_V3 = array([1592,1580,1570,1571,1551,1564,1561,1559,1551,1558,1591]) # [mikro m]
# UD3 = array([10,10,10,10,10,10,10,10,20,20,20])  # [mikro m]
# ###########################

# print "Measurements of beam through lens"
# # Beam now passes through a biconvex lens with focal length 100 mm
	# UD2 = [2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 10, 10, 10]) # [mikro m]



# #beam_through_air(q0, x, None)
# #beam_through_lens(q0, f, M)
# #beam_through_air(q0, x, M)


# 	# # ### Experiment 1

# 	# lmbda = 632 # wavelength [nm]
# 	# n = 1.0 # Refraction index of air

# 	# # print "Measurements of beam through air, no lenses"
# 	# # l_mirror1 = 987 # distance to mirror 1 [mm]
# 	# # l_mirror2 = 650 # distance between mirror 1 and 2 [mm]
# 	# # l1 = array([0, 150, 300, 450, 600, 750, 75+l_mirror1, 475+l_mirror1, 300+l_mirror1+l_mirror2, 900+l_mirror1+l_mirror2]) # [mm]

# 	# # D_H1 = array([804, 813, 825, 831, 900, 982, 1190, 1480, 1883, 2409])/2.
# 	# # D_V1 = array([808, 815, 827, 837, 903, 989, 1201, 1495, 1901, 2401])/2.

# 	# # h = least_squares_analysis(l1, D_H1)
# 	# # v = least_squares_analysis(l1, D_V1)
# 	# # am = least_squares_analysis(l1, (D_V1+D_H1)/2.)

# 	# # R0_h = leastsq(h.error, -2000)[0]
# 	# # R0_v = leastsq(v.error, -2000)[0]
# 	# # R0_am = leastsq(am.error, -2000)[0]

# 	# # print "Error in horizontal  : %.1f" % h.error(R0_h)
# 	# # print "Error in vertical      : %.1f" % v.error(R0_v)
# 	# # print "Error in arithmetic mean: %.1f" % am.error(R0_am)

# 	# # R0 = R0_v
# 	# # W = D_V1
# 	# # w0 = W[0]
# 	# # q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
# 	# # M = matrix([[1,0],[0,1]])
# 	# # W1, M = beam_through_air(q0, l1, M)

# 	# # plot(l1, D_V1, 'o', linewidth=2.0)
# 	# # plot_beam([l1], [W1])
# 	# # legend(['Observations', 'TMA Fit'], 'upper left',  fontsize=16)
# 	# # axis([min(l1)-100,max(l1)+100, min(W1)-25, max(W1)+25])
# 	# # savefig('fig1.pdf')
# 	# # show()

# 	# print "\n\n ---------------------------------------- \n"
# 	# print "Measurements of beam through lens"
# 	# # Beam now passes through a biconvex lens with focal length 100 mm
# 	# d0 = 20 # Avstand fra fot til bildebrikke [mm]
# 	# l2 = array([20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 160, 180, 200, 240, 280, 320, 400, 480, 640]) + d0 # [mm]
# 	# D_H2 = array([455, 393, 301, 239, 163, 113, 79, 96, 171, 258, 329, 417, 483, 660, 792, 951, 1260, 1544, 1835, 2490, 3080, 4392]) # [mikro m]
# 	# D_V2 = array([454, 394, 301, 236, 163, 112, 79, 94, 174, 260, 338, 421, 492, 657, 786, 957, 1260, 1566, 1859, 2514, 3130, 4467]) # [mikro m]
# 	# UD2 = [2, 2, 3, 3, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 10, 10, 10]) # [mikro m]

# 	# h = least_squares_analysis(l2, D_H2)
# 	# v = least_squares_analysis(l2, D_V2)
# 	# am = least_squares_analysis(l2, (D_V2+D_H2)/2.)

# 	# R0_h = leastsq(h.error, -60)[0]
# 	# R0_v = leastsq(v.error, -60)[0]
# 	# R0_am = leastsq(am.error, -60)[0]

# 	# print "Error in horizontal     : %.1f" % h.error(R0_h)
# 	# print "Error in vertical       : %.1f" % v.error(R0_v)
# 	# print "Error in arithmetic mean: %.1f" % am.error(R0_am)
# 	# print R0_am
# 	# R0 = R0_am
# 	# W = (D_V2+D_H2)/2.
# 	# w0 = W[0]
# 	# q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
# 	# M = matrix([[1,0],[0,1]])
# 	# l = linspace(40,1000,1001)
# 	# Wfit, M = beam_through_air(q0, l, M)
# 	# plot_beam([l], [Wfit])
# 	# plot(l2, W, 'o', linewidth=2.0)
# 	# legend(['Observations', 'TMA Fit'], 'upper left',  fontsize=16)
# 	# axis([0, 700, 0, 4500])
# 	# savefig('fig2.pdf')
# 	# show()

# 	# waist = min(Wfit)
# 	# l_waist = l[argmin(Wfit)]
# 	# print l[-1] - l_waist
# 	# print Wfit[-1]

# 	# print "Waist width: %.4f \t waist location: %.4f" % (waist, l_waist)
# 	# print "Rayleigh range: %.4f" % (sqrt(2)*waist)
# 	# plot_beam([l], [Wfit])
# 	# plot(l2, W, 'o', linewidth=2.0)
# 	# axis([0, 1000, 0, 7500])
# 	# axvline(x=l_waist-sqrt(2)*waist, ymin=0, ymax=1, linewidth=2, color='r', linestyle="--")
# 	# axvline(x=l_waist+sqrt(2)*waist, ymin=0, ymax=1, linewidth=2, color='r', linestyle="--")
# 	# legend(['Observations', 'TMA Fit', 'Rayleigh Range'], 'upper center',  fontsize=16)
# 	# savefig('fig3.pdf')
# 	# show()

# 	# print "\n\n ---------------------------------------- \n"
# 	# print "Measurements of beam through lens, focusing on Rayleigh range"


# 		# w0 = 402 # waist [microns]
# 		# R0 = -4000 # curvature [mm]

# 		# plot_beam([l1],  [W1])
# 		# hold('on')	

# 		# #D_H is the horisontal width
# 		# #D_V is the vertical width
# 		# #UD1 is the estimated abs. uncertainty of the measurements
# 		# #l1 is the distance of the accompying measurements



# 		# UD1 = [4,  4,  5, 4, 5, 4, 2, 3, 3, 3]

# 		# plot(l1, D_V1)
# 		# errorbar(l1, D_V1, UD1)
# 		# show()

# 	### EXPERIMENT TWO
# 	lmbda = 632 # wavelength [nm]
# 	n = 1.0 # Refraction index of air

# 	# Measurements made on friday 07.11.14
# 	# Two biconvex lenses with focal lengths f_1=100 mm, f_2=200 mm
# 	# Measurements are given in abs
# 	# Mirror 1 is placed at 200 mm
# 	# Mirror 2 is placed at 500 mm
# 	# The three datasets are made with ajustments of this placement

# 	l_speil1 = 987 # Distance to mirror 1 [mm]
# 	l_speil2 = 650 # Distance between two mirror [mm]
# 	d0 = 22 # Distance from foot to chip [mm]

# 	###########################
# 	# Data set 1
# 	# Best distance between lenses from ABCD-fit 297 +- 2 mm
# 	# With R0 = -10^4, w0 = 393 microns.
# 	l1 = array([525,545,565,650,750,865,10+l_speil1])+d0 # [mm]
# 	D_H1 = array([1545,1545,1552,1571,1593,1606,1620]) # [mikro m]
# 	D_V1 = array([1561,1542,1562,1572,1561,1600,1628]) # [mikro m]
# 	UD1 = array([10,10,10,10,10,10,10])  # [mikro m]
# 	###########################

# 	###########################
# 	# Måleserie nr. 2
# 	# Beste avstand mellom linsene ved ABCD-tilpasning: 301 +- 2 mm
# 	# Med R0 = -10^4, w0 = 393 mikro m.
# 	l2 = array([526,535,635,735,835,75+l_speil1,200+l_speil1,500+l_speil1,400+l_speil1+l_speil2,900+l_speil1+l_speil2])+d0 # [mm]
# 	D_H2 = array([1560,1561,1557,1579,1590,1595,1594,1613,1651,1745]) # [mikro m]
# 	D_V2 = array([1597,1600,1580,1586,1580,1605,1626,1650,1700,1836]) # [mikro m]
# 	UD2 = array([10,10,10,10,10,10,10,10,20,20])  # [mikro m]
# 	###########################

# 	###########################
# 	# Måleserie nr. 3
# 	# Beste avstand mellom linsene ved ABCD-tilpasning: 305 +- 2 mm
# 	# Med R0 = -10^4, w0 = 393 mikro m.
# 	l3 = array([530,600,700,800,75+l_speil1,175+l_speil1,275+l_speil1,500+l_speil1,200+l_speil1+l_speil2,500+l_speil1+l_speil2,950+l_speil1+l_speil2])+d0 # [mm]
# 	D_H3 = array([1580,1576,1574,1565,1522,1511,1501,1500,1474,1459,1464]) # [mikro m]
# 	D_V3 = array([1592,1580,1570,1571,1551,1564,1561,1559,1551,1558,1591]) # [mikro m]
# 	UD3 = array([10,10,10,10,10,10,10,10,20,20,20])  # [mikro m]
# 	###########################

# 	print "EXPERIMENT 2"
# 	print "------------------"
# 	print "DATASET 1"
# 	h = least_squares_analysis(l1, D_H1)
# 	v = least_squares_analysis(l1, D_V1)
# 	am = least_squares_analysis(l1, (D_V1+D_H1)/2.)

# 	R0_h = leastsq(h.error, -200)[0]
# 	R0_v = leastsq(v.error, -200)[0]
# 	R0_am = leastsq(am.error, -200)[0]
# 	R0_1 = R0_am

# 	print "Error in horizontal     : %.1f \t R_0: %.2e" % (h.error(R0_h),R0_h)
# 	print "Error in vertical       : %.1f \t R_0: %.2e" % (v.error(R0_v),R0_v)
# 	print "Error in arithmetic mean: %.1f \t R_0: %.2e" % (am.error(R0_am), R0_am)

# 	print "\nDATASET 2"
# 	h = least_squares_analysis(l2, D_H2)
# 	v = least_squares_analysis(l2, D_V2)
# 	am = least_squares_analysis(l2, (D_V2+D_H2)/2.)

# 	R0_h = leastsq(h.error, 1.4e04)[0]
# 	R0_v = leastsq(v.error, 1.4e04)[0]
# 	R0_am = leastsq(am.error, 1.4e04)[0]
# 	R0_2 = R0_am

# 	print "Error in horizontal     : %.1f \t R_0: %.2e" % (h.error(R0_h),R0_h)
# 	print "Error in vertical       : %.1f \t R_0: %.2e" % (v.error(R0_v),R0_v)
# 	print "Error in arithmetic mean: %.1f \t R_0: %.2e" % (am.error(R0_am), R0_am)

# 	print "\nDATASET 3"
# 	h = least_squares_analysis(l3, D_H3)
# 	v = least_squares_analysis(l3, D_V3)
# 	am = least_squares_analysis(l3, (D_V3+D_H3)/2.)

# 	R0_h = leastsq(h.error, -1000)[0]
# 	R0_v = leastsq(v.error, -1000)[0]
# 	R0_am = leastsq(am.error, -10)[0]
# 	R0_3 = R0_h

# 	print "Error in horizontal     : %.1f \t R_0: %.2e" % (h.error(R0_h),R0_h)
# 	print "Error in vertical       : %.1f \t R_0: %.2e" % (v.error(R0_v),R0_v)
# 	print "Error in arithmetic mean: %.1f \t R_0: %.2e" % (am.error(R0_am), R0_am)

# 	W1 = (D_V1+D_H1)/2.
# 	W2 = (D_V2+D_H2)/2.
# 	W3 = D_H3

# 	for i in range(3):
# 		l = [l1, l2, l3][i]
# 		W = [W1, W2, W3][i]
# 		R0 = [R0_1, R0_2, R0_3][i]
# 		loc = ['upper left', 'upper left', 'upper right'][i]

# 		w0 = W[0]
# 		q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))	
# 		M = matrix([[1,0],[0,1]])
# 		lfit = linspace(l[0], l[-1], 1001)
# 		Wfit, M = beam_through_air(q0, lfit, M)

# 		plot_beam([lfit], [Wfit])
# 		plot(l, W, 'o', linewidth=2.0)
# 		legend(['Observations', 'TMA Fit'], loc, fontsize=16)
# 		savefig('fig_exper2_after_lens%d.pdf' % i)
# 		show()
