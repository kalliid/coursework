from pylab import *


def f(x):
    return x

def sine_fourier(f, N, a, b):
    x = linspace(a,b,1001)
    y = zeros(1001)

    f = f(x)
    for i in range(1,N+1):
        s = sin(i*pi*x)
        c = 2*trapz(f*s, x)
        y += c*s

    plot(x, y)

def cosine_fourier(f, N, a, b):
    x = linspace(a,b,1001)
    f = f(x)
    y = trapz(f, x)
    for i in range(1,N+1):
        s = cos(i*pi*x)
        c = 2*trapz(f*s, x)
        y += c*s

    plot(x, y)

sine_fourier(f,4,-3,3)
show()