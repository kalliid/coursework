from pylab import *

rcut = 3
Ushift = 0.00547944

def U(r):
	return (4*(1/(r**12) - 1/(r**6)) + Ushift)*(r<rcut)


r = linspace(0.2,10, 1001)

plot(r, U(r))
axis([0,10,-1,5])
show()