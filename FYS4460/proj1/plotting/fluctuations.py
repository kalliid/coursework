from pylab import *

filename = "../data/fluctuation_3thermo_Nc8.dat"

with open(filename, 'r') as infile:
	infile.readline()
	Natoms = int(infile.readline())

	lines = infile.readlines()
	N = len(lines)
	
	t1 = zeros(N); t2 = zeros(N); t3 = zeros(N)

	for i in range(N):
		t1[i], t2[i], t3[i] = lines[i].split()

dt = 1e-2
t = array([i*dt for i in range(N)])

plot(t, t1, linewidth=2.0)
plot(t, t2, linewidth=2.0)
plot(t, t3, linewidth=2.0)
plot(t, array([800 for i in range(N)]), '--', linewidth=1.5)

print "Berendsen: ", var(t1)/average(t1)**2
print "Andersen: ", var(t2)/average(t2)**2
print "Nose-Hoover: ", var(t3)/average(t3)**2

print "Theoretical: ", 2/(3.*Natoms)
	
xlabel(r'$t$ $[t_0]$', fontsize=22)
ylabel(r'$T$ $[\epsilon/k_b]$', fontsize=22)
legend(['Berendsen Thermostat', 'Andersen Thermostat', 'Nose-Hoover', 'Heat Bath'], 'lower right', fontsize=22)
axis([0, 3, 400, 1000])
savefig("../thermostat_fluct.pdf")

show()
