'''
Exercise 2. 
We calculate var(X^2) as a function of the step i and plot it in a log-log plot.
'''

from pylab import *

N = 300
ensambles = 1e7
p = 0.01

for p in 0.01, 0.1, 0.25, 0.5:
	xi = ones(ensambles)	
	d = zeros(300)

	for i in range(N):
		print i
		xi *= 2*(rand(ensambles) > p) - 1
		d[i] = (sum(xi == 1)/ensambles)

	plot(d, linewidth=2.0)

legend(["p=0.01", "p=0.1", "p=0.25", "p=0.5"])
grid()
xlabel('Number of steps, $t$', fontsize=18)
ylabel('$P(R)$', fontsize=20)
savefig("system_memory.pdf")
show()