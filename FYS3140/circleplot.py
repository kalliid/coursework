from matplotlib.pylab import *

def greet(name):
	print "Hello ", name


greet(name)

name = "test"

t = linspace(0,360,1001)

x = 2*cos(t)
y = 2*sin(t)

plot(x,y)
axis([-4,4,-4,4])
show()
