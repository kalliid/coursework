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
	y1 = []
	y2 = []
	y3 = []

	for i in range(N):
		xi *= 2*(rand(ensambles) > p) - 1
		X += xi
		y1.append(X[0])
		y2.append(X[1])
		y3.append(X[2])

	plot(y1, linewidth=1.0)
	plot(y2, linewidth=1.0)
	plot(y3, linewidth=1.0)

subplot(3,1,1)
walk(0.5)
title(r"$p=0.5$", fontsize=18)
gca().get_xaxis().set_ticklabels([])

subplot(3,1,2)
walk(0.1)
title(r"$p=0.1$", fontsize=18)
ylabel("Displacement, $X_t$", fontsize=14)
gca().get_xaxis().set_ticklabels([])

subplot(3,1,3)
title(r"$p=0.01$", fontsize=18)
walk(0.01)
xlabel("Time, $t$", fontsize=14)

savefig("small_stock.png")
savefig("small_stock.svg")
savefig("small_stock.pdf")

show()
