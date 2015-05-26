from pylab import *

p = linspace(0,1,1001)
q = 1-p

def pq(n):
	return (p**n)*(q**(9-n))


Pi = 6*pq(3) + 6*6*pq(4) + 6*15*pq(5) + 6*10*pq(6) + 6*15*pq(7) + 6*15*pq(8) + pq(9) 

plot(p, Pi)
show()


