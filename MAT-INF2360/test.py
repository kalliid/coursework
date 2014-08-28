from pylab import *

x = linspace(-1,1,1001)
y = x/(1.+x)

plot(x,y)
show()