from pylab import *

with open("../data/test_thermostat.dat", 'r') as infile:
	T = np.array([float(T) for T in infile.readlines()])

# E /= max(E)

T0 = 119.735
T *= T0

# print T[0]

dt = 1e-2
t = linspace(0, len(T)*dt, len(T))

# meanT = sum(T[500:])/len(T[500:])
# print "Average temp: ", meanT
# print "Max temperature oscillation: ", (max(T[500:])-meanT)/meanT

plot(t, T)
xlabel(r'$\bar{t}$', fontsize=22)
ylabel(r'$\bar{T}$', fontsize=22)
grid()
# axis([0,100,0,1])
show()
