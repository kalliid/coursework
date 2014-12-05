# -*- coding: utf-8 -*-

from RTMA import *

# # ### Experiment 1

lmbda = 532 # wavelength [nm]
n = 1.0 # Refraction index of air
w0 = 1.4*10**6
d = 100*10**6

def calculate_beam(R0):
	x = linspace(0, d, 1001)
	q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
	solver = TMA(q0, lmbda, n)
	W = solver.beam_through_air(x)
	return x, W

def error(R0):
	x, Wfit = calculate_beam(R0)
	return Wfit[-1]

R0fit = leastsq(error, 10e12)[0]

print R0fit
x, Wfit = calculate_beam(R0fit)
print Wfit[-1]/(10**6)

plot(x, Wfit)
show()
