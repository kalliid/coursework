# -*- coding: utf-8 -*-

from RTMA import *

# # ### Experiment 1

lmbda = 532 # wavelength [nm]
n = 1.0 # Refraction index of air

# mirror1 = 987  # position of mirror 1
# mirror2 = 1637 # position of mirror 2

# l = array([159, 359, 759, 1159, 1876, 2516])
# Wh = array([1177,1192,1172,1195,1183,1236])/2.
# Wv = array([1025,1030,1149,1201,1250,1360])/2.

# x1 = linspace(159, 2517, 2518-159)

# def calculate_beam(R0):
# 	q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
# 	solver = TMA(q0, lmbda, n)
 	
#  	W1 = solver.beam_through_air(x1)
# 	#solver.beam_through_lens(100)
# 	#W2 = solver.beam_through_air(x2)

# 	#x = concatenate((x1))
# 	#Wfit = concatenate((W1))
# 	return x1, W1

# def error(y):
# 	R0 = y
# 	x, Wfit = calculate_beam(R0)
# 	residuals = zeros(len(l))
# 	for i in range(len(l)):
# 		residuals[i] = Wfit[l[i]-159] - W[i] 

# 	return residuals


# W = (Wv+Wh)/2.
# w0 = W[0]

# R0fit = leastsq(error, (10**4))[0]
# print R0fit

# x, Wfit = calculate_beam(R0fit)

# plot(l, W, 'o-', linewidth=2.0)
# plot(x, Wfit, linewidth=2.0)
# legend(['Observations', 'TMA Fit'], 'upper left',  fontsize=16)
# axis([0, 2600, 0, 1200])
# grid()
# xlabel(r'Distance along optical axis, $l$ [mm]', fontsize=20)
# ylabel(r'Spot size, $w$ [$\mu$m]', fontsize=20)
# savefig('laserpenn_vh.pdf')
# show()

def calculate_beam(eps):
	q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
	solver = TMA(q0, lmbda, n)

	x1 = linspace(0, eps, 101)
	x2 = linspace(eps, 800*1000, 1001)

	solver.beam_through_lens(14)
	W1 = solver.beam_through_air(x1)
	solver.beam_through_lens(810)
	W2 = solver.beam_through_air(x2)

	x = concatenate((x1, x2))
	Wfit = concatenate((W1, W2))
	return x, Wfit

def error(eps):
	x, Wfit = calculate_beam(810+14+eps)
	return Wfit[-1]


R0 = 2.7434e+11
w0 = 1101

#print leastsq(error, 0.5)[0]
 	
for eps in 0, 0.5, 0.92616377, 1.25:
	x, Wfit = calculate_beam(810+14+eps)
	plot(x/1000., Wfit/1000, linewidth=2.0)

xlabel('Distance from source, $l$ [m]', fontsize=20)
ylabel('Beam spot size, $w$ [mm]', fontsize=20)
grid()
axvline(x=710, ymin=0, ymax=1, linewidth=2, color='r', linestyle="--")
legend([r"$\epsilon=0$", r"$\epsilon=0.5$", r"$\epsilon=0.926$", r"$\epsilon=1.25$"], 'lower left', fontsize=20)
savefig("e3p3.pdf")
show()