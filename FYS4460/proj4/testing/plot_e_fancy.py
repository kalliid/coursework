from pylab import *

with open("../data/energy2.dat", 'r') as infile:
	E = np.array([float(E) for E in infile.readlines()])

E /= max(E)

dt = 0.01

T = len(E)*dt
t = linspace(0,T,len(E))

mean = sum(E[5000:])/len(E[5000:])
print "Average energy: ", mean
print "Max energy oscillation: ", (max(E[5000:])-mean)/mean


plot(t, E)
xlabel(r'$\bar{t}$', fontsize=22)
ylabel(r'$\bar{U}$', fontsize=22)
grid()
# axis([0,100,0,1])
show()
