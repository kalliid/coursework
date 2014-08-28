from pylab import *

def P(x, A, B):
    if B*exp(-A) < x < B*exp(A):
        return 1./(2*A*x)
    else:
        return 0



A=6
B=100

y = []
x_values = linspace(0,1000,1001)
for x in x_values:
    y.append(P(x,A,B))

plot(x_values,y)
show()