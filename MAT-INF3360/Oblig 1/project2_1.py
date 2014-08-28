from numpy import *

def solver(f, n):
    x = linspace(0,1,n+2)
    h = x[1]-x[0]
    u = zeros(n+2)
    a = zeros(n+2)
    b = zeros(n+2)

    if callable(f):
        for i in range(n+1):
            a[i+1] = a[i] + h/4.*(f(x[i]) + 2*f(x[i]+h/2.) + f(x[i+1]))
            b[i+1] = b[i] + h/4.*(x[i]*f(x[i]) 
                + 2*(x[i]+h/2.)*f(x[i]+h/2.) + x[i+1]*f(x[i+1]))
    else:
        for i in range(n+1):
            a[i+1] = a[i] + h/2.*(f[i] + f[i+1])
            b[i+1] = b[i] + h/4.*((2*x[i]+h/2.)*f[i] + (2*x[i+1]-h/2.)*f[i+1])

    u[:-1] = x[:-1]*(a[-1] - b[-1]) + b[:-1] - x[:-1]*a[:-1] 

    return x, u


f1 = lambda x: 1 + (x-x)
f2 = lambda x: x
f3 = lambda x: x*x
f4 = lambda x: exp(x)
f5 = lambda x: cos(2*x)
e1 = lambda x: 0.5*x*(1-x)
e2 = lambda x: 1/6.*x*(1-x*x)
e3 = lambda x: 1/12.*x*(1-x**3)
e4 = lambda x: (exp(1)-1)*x-exp(x) + 1
e5 = lambda x: 1/4.*((1-cos(2))*x + cos(2*x) - 1)

source_terms = [f1, f2, f3, f4, f5]
exact_solutions = [e1, e2, e3, e4, e5]

ep = 100
hp = 100
for i in range(5):
    for n in 8, 16, 32, 64, 128, 256, 1024:
        x, u = solver(source_terms[i], n)
        u_e = exact_solutions[i](x)
        e = max(abs(u-u_e))

        h = x[1]-x[0]
        r = log(ep/e)/log(hp/h)

        ep = e
        hp = h

        print "%8i %8i %8.1e %8.3f" % (i, n, e, r)

