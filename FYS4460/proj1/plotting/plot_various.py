from pylab import *
import re


pattern = re.compile(r'T:(.+) E:(.+) P:(.+) r2:(.+)')

with open("../data/bigrun.dat", 'r') as infile:
	lines = infile.readlines()

	N = len(lines)
	T = zeros(N)
	E = zeros(N)
	P = zeros(N)
	r2 = zeros(N)
	
	for i in range(N):
		m = pattern.search(lines[i])

		T[i] = m.group(1)
		E[i] = m.group(2)
		P[i] = m.group(3)
		r2[i] = m.group(4)
		

dt = 1e-3
t = array([i*dt for i in range(N)])

# a, b = polyfit(t, r2, 1)
# print a
# print b

x = t[:,np.newaxis]
y = r2
a, _, _, _ = np.linalg.lstsq(x, y)
print a

plot(t, r2, linewidth=2.0)
plot(t, a*t, '--', linewidth=2.0)
xlabel(r'$t$ [$t_0$]', fontsize=22)
ylabel(r'$\langle r^2\rangle(t)$ [$\sigma^2/t_0$]', fontsize=22)
axis([0, dt*N, 0, max(r2)*1.1])
grid()
legend(['Measurements', 'Linear fit'], 'upper left', fontsize=14)
show()
