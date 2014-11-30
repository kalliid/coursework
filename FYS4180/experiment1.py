# -*- coding: utf-8 -*-

from RTMA import *

# ### Experiment 1

lmbda = 632 # wavelength [nm]
n = 1.0 # Refraction index of air

print "Measurements of beam through air, no lenses"
mirror1 = 987  # position of mirror 1
mirror2 = 1637 # position of mirror 2

l = array([0, 150, 300, 450, 600, 750, 1062, 1462, 1937, 2537])
Wh = array([804, 813, 825, 831, 900, 982, 1190, 1480, 1883, 2409])/2.
Wv = array([808, 815, 827, 837, 903, 989, 1201, 1495, 1901, 2401])/2.

W = (Wh + Wv)/2.
w0 = W[0]
x1 = linspace(0, 2600, 2601)

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
	residuals = zeros(len(l))
	for i in range(len(l)):
		residuals[i] = Wfit[l[i]] - W[i] 

	return residuals

for W in Wh, Wv, (Wh+Wv)/2.:
	R0fit = leastsq(error, -2000)[0]
	print R0fit, sum(error(R0fit)**2)

x, Wfit = calculate_beam(R0fit)

plot(l, W, 'o-', linewidth=2.0)
plot(x, Wfit, linewidth=2.0)
legend(['Observations', 'TMA Fit'], 'upper left',  fontsize=16)
axis([0, 2600, 0, 1500])
grid()
xlabel(r'Distance along optical axis, $l$ [mm]', fontsize=20)
ylabel(r'Spot size, $w$ [$\mu$m]', fontsize=20)
savefig('experiment_1.pdf')
show()



# print "Measurements of beam through 1 lens"

# # % 2) Stråle etter passering av (konveks) linse med f=100mm.
# # % Avstand fra første speil til linse: 200mm.
# # % Samme navnkonvensjon som på variable som i 1):
# # % Avstand fra kameraets fot til bildebrikken anslått til å være d0=20mm.
# # d0 = 20; % Avstand fra fot til bildebrikke [mm]


# l = array([40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 180, 200, 220, 260, 300, 340, 420, 500, 660])
# Wh = array([455, 393, 301, 239, 163, 113, 79, 96, 171, 258, 329, 417, 483, 660, 792, 951, 1260, 1544, 1835, 2490, 3080, 4392])/2.
# Wv = array([454, 394, 301, 236, 163, 112, 79, 94, 174, 260, 338, 421, 492, 657, 786, 957, 1260, 1566, 1859, 2514, 3130, 4467])/2.

# W = (Wh + Wv)/2.
# w0 = W[0]
# x1 = linspace(40, 1040, 1001)

# def calculate_beam(R0):
# 	q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
# 	solver = TMA(q0, lmbda, n)
	
#  	W1 = solver.beam_through_air(x1)
# 	#solver.beam_through_lens(100)
# 	#W2 = solver.beam_through_air(x2)

# 	#x = concatenate((x1))
# 	#Wfit = concatenate((W1))
# 	return x1, W1

# def error(R0):
# 	x, Wfit = calculate_beam(R0)
# 	residuals = zeros(len(l))
# 	for i in range(len(l)):
# 		residuals[i] = Wfit[l[i]-40] - W[i] 

# 	return residuals

# R0fit = leastsq(error, -50)[0]
# print R0fit, sum(error(R0fit)**2)

# x, Wfit = calculate_beam(R0fit)

# plot(l, W, 'o-', linewidth=2.0)
# plot(x, Wfit, linewidth=2.0)
# legend(['Observations', 'TMA Fit'], 'upper left',  fontsize=16)
# axis([0, 400, 0, 1000])
# grid()
# xlabel(r'Distance along optical axis, $l$ [mm]', fontsize=20)
# ylabel(r'Spot size, $w$ [$\mu$m]', fontsize=20)
# savefig('experiment_1_wlens.pdf')
# show()


# l = array([40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150]) #, 160, 180, 200, 220, 260, 300, 340, 420, 500, 660])
# Wh = array([455, 393, 301, 239, 163, 113, 79, 96, 171, 258, 329, 417])/2. #, 483, 660, 792, 951, 1260, 1544, 1835, 2490, 3080, 4392])/2.
# Wv = array([454, 394, 301, 236, 163, 112, 79, 94, 174, 260, 338, 421])/2. #, 492, 657, 786, 957, 1260, 1566, 1859, 2514, 3130, 4467])/2.

# W = (Wh + Wv)/2.
# w0 = W[0]
# x1 = linspace(40, 150, 111)

# def calculate_beam(R0, w0):
# 	q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
# 	solver = TMA(q0, lmbda, n)
	
#  	W1 = solver.beam_through_air(x1)
# 	#solver.beam_through_lens(100)
# 	#W2 = solver.beam_through_air(x2)

# 	#x = concatenate((x1))
# 	#Wfit = concatenate((W1))
# 	return x1, W1

# def error(y):
# 	R0, w0 = y
# 	x, Wfit = calculate_beam(R0, w0)
# 	residuals = zeros(len(l))
# 	for i in range(len(l)):
# 		residuals[i] = Wfit[l[i]-40] - W[i] 

# 	return residuals

# # R0fit, w0fit = leastsq(error, (-65, 225))[0]

# # x, Wfit = calculate_beam(R0fit, w0fit)

# # plot(l, W, 'o-', linewidth=2.0)
# # plot(x, Wfit, linewidth=2.0)
# # legend(['Observations', 'TMA Fit'], 'upper left',  fontsize=16)
# # axis([0, 160, 0, 300])
# # grid()
# # xlabel(r'Distance along optical axis, $l$ [mm]', fontsize=20)
# # ylabel(r'Spot size, $w$ [$\mu$m]', fontsize=20)
# # savefig('experiment_1_rayleigh.pdf')
# # show()
