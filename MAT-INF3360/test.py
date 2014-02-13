from pylab import * 

hc = 1240

def simpson(xmin, xmax, steps, function):
    x = xmin
    dx =(xmax-xmin)/( 1.0*steps)
    I = 0
    for i in range(0,steps):
        I += dx*function(x[i])
        x += dx
    return I


def M_x(x, T=0.5):
    return 2*pi/(hc**2)*x**3/(exp(x/T)-1)

def M(T):
    x = linspace(0,10,101)
    I = 0
    dx = x[1]-x[0]
    for i in range(101):
        I += dx*M_x(x[i], T=T)
    return I

T = linspace(0.01,2,1001)
Ml = zeros(1001)
for i in range(1001):
    Ml[i] = M(T[i])

plot(T, Ml)
xlabel(r'$k_bT$ [eV]')
ylabel(r'$M(k_bT)$  [eV/nm$^2$]')
show()