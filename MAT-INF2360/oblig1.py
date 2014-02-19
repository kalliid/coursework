from numpy import *
import timeit

def DFTImpl(x):
    '''
    Computes the DFT of a 2**n dimensional column vector x,
    uses multiplication with the Fourier matrix.
    '''
    # Find the dimension of the x-vector
    N = x.shape[0]

    # Assemple the N-point fourier-matrix
    n = arange(N)
    k = n.reshape((N,1))
    F_N = exp(-2j*pi*n*k/N)/sqrt(N)

    # Perform the matrix-multiplication, giving the DFT of x
    return dot(F_N, x)


def FFT_recursive(x):
    N = x.shape[0]

    if N <= 32:
        return DFTImpl(x)

    ye = FFT_recursive(x[::2])
    yo = FFT_recursive(x[1::2])
    D = exp(-2j*pi*arange(N/2)/N)

    return concatenate([ye + D*yo, ye - D*yo])/sqrt(2)

def FFT_vectorized(x):
    # Find total number of elements
    N = x.shape[0]

    if N < 32:
       return DFTImpl(x)

    # Reshape vector into lower-order subproblem and solve it
    y = DFTImpl(x.reshape(32,-1))

    # Assemble total DFT layer by layer
    while y.shape[0] < N:
        ye = y[:, :y.shape[1]/2]
        yo = y[:, y.shape[1]/2:]
        D = exp(-1j*pi*arange(y.shape[0])/y.shape[0])[:, None]
        y = vstack([ye + D*yo, ye - D*yo])/sqrt(2)

    return y.ravel()


setup = """
from __main__ import DFTImpl, FFT_recursive, FFT_vectorized, fft, x
"""

t1 = []
t2 = []
t3 = []

for n in range(15, 23):
    x = random.random(2**n)

    t1 = min(timeit.Timer("FFT_recursive(x)", setup=setup).repeat(2, 1))
    t2 = min(timeit.Timer("FFT_vectorized(x)", setup=setup).repeat(2, 1))
    t3 = min(timeit.Timer("fft.fft(x)", setup=setup).repeat(2, 1))

    ofile.write("%i %.2e %.2e %.2e" % (n, t1, t2, t3))

from pylab import *

plot(n,array(t1)*1000.,'-o')
plot(n,array(t2)*1000.,'-o')
plot(n,array(t3)*1000.,'-o')
xlabel(r'$n$', fontsize=16)
ylabel(r'$t$ [ms]', fontsize=16)
axis([15,20,0,1000])
legend(['FFT_recursive','FFT_vectorized','numpy.fft.fft'])
grid()
savefig('times_d.pdf')
show()

