'''
Exercise 1. 
We calculate <X^2> for p=0.01, p=0.10, p=0.5 for N=1000 steps
and 1e5 realizations in our ensamble.
'''

from pylab import *

N = 1000
ensambles = 1e5

def walk(p):
	X = zeros(ensambles)
	xi = ones(ensambles)

	y = zeros(N)

	for i in range(N):
		xi *= 2*(rand(ensambles) > p) - 1
		X += xi
		y[i] = sum(X**2)/ensambles

	plot(y)

walk(0.5)
walk(0.1)
walk(0.01)
show()

