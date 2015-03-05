"""
Check the properties of the initial velocities of the cubic lattice.
These properties should be true:
1. Velocities should be normally distributed with a mean of 0 and std of sqrt(kb*T/m)
"""

from pylab import *

with open("../data/argon_lattice.xyz", 'r') as infile:
	N = int(infile.readline())
	infile.readline()
	
	v = zeros((N,3))
	for i in range(N):
		v[i] = (infile.readline().split(" ")[4:7])

k_b = 8.31447e-7 # Boltzmann's constant in Da*A^2/fs^2/K
m = 39.948 # Mass of Argon atom in amu
T = 100 # Initial temperature of system in Kelvin

mean = 0
std = sqrt(k_b*T/m)

vlin = linspace(-3*std, 3*std, 1001)
boltzmann = normpdf(vlin, mean, std)
boltzmann /= max(boltzmann)

# Plot vx
n, bins, patches = hist(v[:,0], bins=50, normed=True, alpha=0.7)
bincenters = 0.5*(bins[1:]+bins[:-1])
y = normpdf( bincenters, 0, sqrt(k_b*T/m))

plot(linspace(-0.005, 0.005, 1001), normpdf(linspace(-0.005, 0.005, 1001), 0, sqrt(k_b*T/m)), linewidth=2.0)
xlabel('Velocity, [A/fs]')
ylabel('Number of atoms')
show()




