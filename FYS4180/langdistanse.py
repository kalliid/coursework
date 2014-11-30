# -*- coding: utf-8 -*-

from RTMA import *

# ### Experiment 1

lmbda = 632 # wavelength [nm]
n = 1.0 # Refraction index of air
R0 = -710000
w0 = 1104.12528196

x1 = linspace(0, 710000, 1001)

def calculate_beam(R0):
	q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
	solver = TMA(q0, lmbda, n)
 	
 	W1 = solver.beam_through_air(x1)
	#solver.beam_through_lens(100)
	#W2 = solver.beam_through_air(x2)

	#x = concatenate((x1))
	#Wfit = concatenate((W1))
	return x1, W1

def error(R0):
	x, Wfit = calculate_beam(R0)
	return Wfit[-1] - 480

R0fit = leastsq(error, 25185.2072652)[0]

x, Wfit = calculate_beam(R0)
plot(x, Wfit/1000., linewidth=2.0)
grid()
show()

# R0fit, w0fit = leastsq(error, (10**4, w0))[0]
# print R0fit, w0fit

# x, Wfit = calculate_beam(R0fit, w0fit)

# plot(l, W, 'o-', linewidth=2.0)
# plot(x, Wfit, linewidth=2.0)
# legend(['Observations', 'TMA Fit'], 'upper left',  fontsize=16)
# axis([0, 2600, 1000, 1500])
# grid()
# xlabel(r'Distance along optical axis, $l$ [mm]', fontsize=20)
# ylabel(r'Spot size, $w$ [$\mu$m]', fontsize=20)
# savefig('laserpeng_vh.pdf')
# show()
