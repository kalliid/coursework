from pylab import *
from numpy import random

def newtonbacktrack(f,df,d2f,x0):
    beta, s, sigma = 0.2, 0.5, 10**(-3)
    epsilon = 10**(-3)
    xopt = x0
    maxit = 100
    for numit in range(1,maxit+1):
        d = -df(xopt)/d2f(xopt
)        eta = -df(xopt)*d
        if eta/2.0<epsilon:
           break
        m=0
        while (f(xopt)-f(xopt+beta**m*s*d) < -sigma *beta**m*s *df(xopt)*d):
            m=m+1
        xopt = xopt + beta**m*s*d
        if xopt > 1:
            xopt = 1
        elif xopt < -1:
            xopt = -1
    return xopt, numit

x = array([[0.4992, -0.8661, 0.7916, 0.9107, 0.5357, 
            0.6574, 0.6353, 0.0342, 0.4988, -0.4607]])

def randmuon(alpha,m,n):
    return (-1+sqrt(1-alpha*(2-alpha-4*random.rand(m,n))))/alpha

x = randmuon(1,100000,1)

def f(a):
    return -sum(log((1+a*x)/2.))

def df(a):
    return -sum(x/(1+a*x))

def d2f(a):
    return sum(x**2/((1+a*x)**2))

xopt, numit = newtonbacktrack(f, df, d2f, 0)
print xopt, numit


a = linspace(-1,1,1000)
y1 = []
y2 = []
for v in a:
    y1.append(f(v))
    y2.append(df(v))

plot(a,y1)
plot(a,y2)
show()