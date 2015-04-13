'''
Exercise 1. 
We calculate <X^2> for p=0.01, p=0.10, p=0.5 for N=1000 steps
and 1e5 realizations in our ensamble.
'''

from pylab import *

N = 1000
ensambles = 1e6

def walk_hist(p):
	X = zeros(ensambles)
	xi = ones(ensambles)

	for i in range(N):
		xi *= 2*(rand(ensambles) > p) - 1
		X += xi

	return X

X = walk_hist(0.5)
n, bins, patches = plt.hist(X, 50, normed=1, facecolor='green', alpha=0.75)
axis([-150,150,0,0.014])
xlabel('$X$', fontsize=18)
ylabel('$P(X)$',fontsize=18)
savefig('simple_hist.pdf')
show()

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
