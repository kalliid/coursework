from numpy import *
import timeit

def IDFTImpl(y):
    '''
    Computes the IDFT of vector y through matrix-multiplication
    '''
    # Find the dimension of the y-vector
    N = y.shape[0]

    # Assemple the N-point inverse fourier-matrix
    n = arange(N)
    k = n.reshape((N,1))
    F_N = exp(2j*pi*n*k/N)/sqrt(N)

    # Perform the matrix-multiplication, giving the IDFT of y
    return dot(F_N, y)


def IFFT_vectorized(y):
    '''
    Vectorized impl. of the IFFT
    '''
    # Find total number of elements
    N = y.shape[0]

    if N < 32:
       return IDFTImpl(y)

    # Reshape vector into lower-order subproblem and solve it
    x = IDFTImpl(y.reshape(32,-1))

    # Assemble total IDFT layer by layer
    while x.shape[0] < N:
        xe = x[:, :x.shape[1]/2]
        xo = x[:, x.shape[1]/2:]
        D = exp(1j*pi*arange(x.shape[0])/x.shape[0])[:, None]
        x = vstack([xe + D*xo, xe - D*xo])/sqrt(2)

    return x.ravel()

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

from scitools.sound import read, write, play

# Extract the first 2**17 samples from the first channel
x = read('castanets.wav')
x = x[::2]
x = x[:2**17]

write(x, 'original.wav')

# Calculate the DFT coefficients
y = FFT_vectorized(x)

N = len(y)-1
fs = 44100.
min_freq = 4000

min_index = ceil(min_freq*N/fs)
max_index = N-min_index

y[:min_index] = 0
y[max_index:] = 0

x = IFFT_vectorized(y)
x = real(x)
write(x, 'min_f=4000.wav')
play('original.wav')
#play('max_f=5000.wav')

