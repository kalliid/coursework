# -*- coding: utf-8 -*-

from RTMA import *

lmbda = 632
n = 1
w0 = 1200
R0 = 1200

q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
solver = TMA(q0, lmbda, n)

x1 = linspace(0, 150, 10001)
x2 = linspace(150, 1000, 20001)

W1 = solver.beam_through_air(x1)
solver.beam_through_lens(100)
W2 = solver.beam_through_air(x2)

x = concatenate((x1, x2))
Wfit = concatenate((W1, W2))

plot(x, Wfit, linewidth=2)
axvline(x=150, ymin=0, ymax=1, linewidth=2, color='r', linestyle="--")
grid()
xlabel(r'Distance along optical axis, $l$ [mm]', fontsize=20)
ylabel(r'Spot size, $W$ [mm]', fontsize=20)
#legend(['Beam', 'Lens location'], 'lower right', fontsize=20)
#savefig("beam_expander_dataset_%d.pdf" % i)
show()

print "Min: x: %e \t W: %e" % (x[argmin(Wfit)], min(Wfit))
print "Max: x: %e \t W: %e" % (x[argmax(Wfit)], max(Wfit))

xmin = x[argmin(Wfit)]
waistmin = min(Wfit)
xmax = x[argmax(Wfit)]
waistmax = max(Wfit)

print waistmax-waistmin
print xmax-xmin

print arctan(waistmax/(xmax-xmin)/1000)*180/pi

print "Airy angle: %f" % (arcsin(1.22*lmbda/(2.*1000*waistmin))*180/pi)

