'''
Exercise 1. 
We calculate <X^2> for p=0.01, p=0.10, p=0.5 for N=1000 steps
and 1e5 realizations in our ensamble.
'''

from pylab import *
from scipy.stats import norm

N = 1000
ensambles = 1e5

print r"\begin{tabular}{|c||c|c|c|c|c|}\hline"
print r"$p$ & $0.01$ & $0.10$ & $0.50$ & $0.9$ & $0.99$ \\ \hline \hline" 
# print r"$<X^2>$",


for N in 100, 1000, 10000:
	print r"$N=%d$" % N,	
	for p in 0.01, 0.1, 0.5, 0.9, 0.99:
		X = zeros(ensambles)
		xi = ones(ensambles)

		for i in range(N):
			xi *= 2*(rand(ensambles) > p) - 1
			X += xi

		print "& %.0f" % (sum(X)/ensambles),
	print "\\ \hline"

print r"\\ \hline"
print r"\end{align}"


# X = 0
# xp = 1

# for i in range(n):
# 	for i in range(N):
# 		if rand() < p:
# 			xp *= -1
# 			X += xp
# 		else:
# 			X += xp

# print X
# print X**2
