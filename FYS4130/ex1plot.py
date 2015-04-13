'''
Exercise 1. 
We calculate <X^2> for p=0.01, p=0.10, p=0.5 for N=1000 steps
and 1e5 realizations in our ensamble.
'''

from pylab import *

N = 10000
ensambles = 1e5
p = 0.5

X = zeros(ensambles)
xi = ones(ensambles)

for i in range(N):
	xi *= 2*(rand(ensambles) > p) - 1
	X += xi


n, bins, patches = hist(X, 50, normed=1.0, facecolor='green', alpha=0.75)

x = linspace(-300,300,1001)
plot(x, normpdf(x, 0, sqrt(N)), 'r--', linewidth=2)

axis([-300,300,0,0.0045])
xlabel(r'$\langle X \rangle$')
ylabel('Probability')
legend([r"Normal(0,$\sqrt{N}$)", "Numerical results"])
grid()
show()

# # title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
# # axis([40, 160, 0, 0.03])
# grid()
# show()

