'''
Exercise 2. 
We calculate var(X^2) as a function of the step i and plot it in a log-log plot.
'''

from pylab import *

N = 10**3
ensambles = 1e5

def plotvar(p):
	X = zeros(ensambles)
	xi = ones(ensambles)


	varX = zeros(N)

	for i in range(N):
		print i
		xi *= 2*(rand(ensambles) > p) - 1
		X += xi

		varX[i] = var(X)

	loglog(range(1, N+1), varX)

for p in 0.1, 0.01:
	plotvar(p)

xlabel(r"Number of steps taken, $t$", fontsize=18)
ylabel(r"Variance, $\langle \Delta X^2 \rangle$", fontsize=18)
legend(['p=0.1', 'p=0.01'], 'upper left')
grid()
savefig("loglog.pdf")
show()

