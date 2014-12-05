# -*- coding: utf-8 -*-

from RTMA import *

# # ### Experiment 1

lmbda = 532 # wavelength [nm]
n = 1.0 # Refraction index of air
w0 = 1.0*10**6
d = 384400*10**6

def calculate_beam(R0):
	x = linspace(0, d, 10001)
	q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
	solver = TMA(q0, lmbda, n)
	W = solver.beam_through_air(x)
	return x, W

def error(R0):
	x, Wfit = calculate_beam(R0)
	return Wfit[-1]

R0fit = leastsq(error, 10e12)[0]

R0 = R0fit
x = linspace(0, d, 10001)
q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
solver = TMA(q0, lmbda, n)
W1 = solver.beam_through_air(x)

W2 = W1[::-1]

plot(x/(10**6), W1/(10**6), linewidth=2.0)
plot(x/(10**6), W2/(10**6), linewidth=2.0)
xlabel(r"Distance from source, $l$ [km]", fontsize=20)
ylabel(r"Beam spot size, $w$ [m]", fontsize=20)
axvline(x=384400, ymin=0, ymax=1, linewidth=2, color='r', linestyle="--")
axis([0,max(x/(10**6))*1.05,0,85])
grid()
legend(["Transmitted beam", "Reflected beam"], 'upper center', fontsize=20)
savefig('moon_beams.pdf')
show()