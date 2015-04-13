'''
Exercise 1. 
We calculate <X^2> for p=0.01, p=0.10, p=0.5 for N=1000 steps
and 1e5 realizations in our ensamble.
'''

from pylab import *

N = 1000
ensambles = 1e7

def walk_hist(p):
	X = zeros(ensambles)
	xi = ones(ensambles)

	for i in range(N):
		print i
		xi *= 2*(rand(ensambles) > p) - 1
		X += xi

	return X

X = walk_hist(0.9)
mu = mean(X)
sigma = std(X)

n, bins, patches = plt.hist(X, 50, normed=1, facecolor='green', alpha=0.75)

plot(bins, normpdf(bins, mu, sigma), 'r--', linewidth=2.0)

axis([-50,50,0,0.044])
xlabel('$X_{1000}$', fontsize=24)
ylabel('$P(X_{1000})$',fontsize=24)
title('$\mu = ' + '%.1f'%(mu) + "$, $\sigma = " + '%.2f$'%(sigma), fontsize=24)
legend(['Numerical results', 'Gaussian fit'])
savefig('simple_hist4.pdf')
show()

