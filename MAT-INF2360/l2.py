from pylab import *
import numpy.random as random

def newtonbacktrack(x0, x):
    def f(a):
        return -sum(log((1+a*x)/2.))

    def df(a):
        return -sum(x/(1+a*x))

    def d2f(a):
        return sum(x**2/((1+a*x)**2))

    beta, s, sigma = 0.2, 0.5, 10**(-3)
    epsilon = 10**(-3)
    xopt = x0
    maxit = 100
    for numit in range(1,maxit+1):
        d = -df(xopt)/d2f(xopt)
        eta = -df(xopt)*d
        if eta/2.0<epsilon:
           break
        m=0
        while (f(xopt)-f(xopt+beta**m*s*d) < -sigma *beta**m*s *df(xopt)*d):
            m=m+1
        xopt = xopt + beta**m*s*d
        if xopt > 1: xopt = 1
        elif xopt < -1: xopt = -1
    return xopt, numit

def randmuon(alpha,m,n):
    return (-1+sqrt(1-alpha*(2-alpha-4*random.rand(m,n))))/alpha


results1 = []
results2 = []
results3 = []
for i in range(10):
    x1 = randmuon(0.5,1,10)
    x2 = randmuon(0.5,1,1000)
    x3 = randmuon(0.5,1,100000)
    xopt1, numit = newtonbacktrack(0,x1)
    xopt2, numit = newtonbacktrack(0,x2)
    xopt3, numit = newtonbacktrack(0,x3)
    results1.append(xopt1)
    results2.append(xopt2)
    results3.append(xopt3)

fig, ax = plt.subplots()
fig.set_size_inches(8,4)
ax.boxplot(results1)
ax.set_xticks([])
title(r'$n=10$',fontsize=18)
ylabel(r'Estimated $\alpha$', fontsize=18)
savefig("boxes1.pdf")
show()

fig, ax = plt.subplots()
ax.boxplot(results2)
fig.set_size_inches(8,4)
ax.set_xticks([])
title(r'$n=1000$',fontsize=18)
ylabel(r'Estimated $\alpha$', fontsize=18)
savefig("boxes2.pdf")
show()

fig, ax = plt.subplots()
ax.boxplot(results3)
fig.set_size_inches(8,4)
ax.set_xticks([])
title(r'$n=100000$',fontsize=18)
ylabel(r'Estimated $\alpha$', fontsize=18)
savefig("boxes3.pdf")
show()

