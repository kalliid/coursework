from matplotlib.pylab import *

t = linspace(0,360,101)

x = 2*cos(t)
y = 2*sin(t)

plot(x,y)
axis([-3,3,-3,3])
show()
