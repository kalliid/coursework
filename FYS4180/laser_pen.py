# -*- coding: utf-8 -*-

from RTMA import *

# ### Experiment 1

lmbda = 632 # wavelength [nm]
n = 1.0 # Refraction index of air

mirror1 = 987  # position of mirror 1
mirror2 = 1637 # position of mirror 2

l = array([159, 359, 759, 1159, 1876, 2516])
Wh = array([1177,1192,1172,1195,1183,1236])
Wv = array([1025,1030,1149,1201,1250,1360]) 

x1 = linspace(0, 2600, 2601)

def calculate_beam(R0, w0):
	q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
	solver = TMA(q0, lmbda, n)
 	
 	W1 = solver.beam_through_air(x1)
	#solver.beam_through_lens(100)
	#W2 = solver.beam_through_air(x2)

	#x = concatenate((x1))
	#Wfit = concatenate((W1))
	return x1, W1

def error(y):
	R0, w0 = y
	x, Wfit = calculate_beam(R0, w0)
	residuals = zeros(len(l))
	for i in range(len(l)):
		residuals[i] = Wfit[l[i]] - W[i] 

	return residuals


W = (Wh + Wv)/2.
w0 = W[0]

R0fit, w0fit = leastsq(error, (10**4, w0))[0]
print R0fit, w0fit

x, Wfit = calculate_beam(R0fit, w0fit)

plot(l, W/2, 'o-', linewidth=2.0)
plot(x, Wfit/2, linewidth=2.0)
legend(['Observations', 'TMA Fit'], 'upper left',  fontsize=16)
axis([0, 2600, 500, 750])
grid()
xlabel(r'Distance along optical axis, $l$ [mm]', fontsize=20)
ylabel(r'Spot size, $w$ [$\mu$m]', fontsize=20)
savefig('laserpenn_vh.pdf')
show()
