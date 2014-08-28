from pylab import *

a = 2

def f(x):
    return x*x - a

def df(x):
    return 2.*x

def new(x):
    return x - f(x)/df(x)

x0 = 1
x1 = new(x0)
x2 = new(x1)
x3 = new(x2)

print x1
print 3./2
print x2
print 17./12
print x3
print (17*17*12 - 6)/(144*17.)
print sqrt(2)
