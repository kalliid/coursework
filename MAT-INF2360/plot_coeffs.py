from pylab import * 
import pickle

with open('coeffs.dat', 'r') as ifile:
    y = pickle.load(ifile)

N = len(y)-1
fs = 44100.
max_freq = 5000

min_index = ceil(max_freq*N/fs)
max_index = N-min_index

y[min_index:max_index] = 0  

f = arange(N/2)*fs/N

plot(f, abs(y)[:N/2]/(max(abs(y))))
axis([0,max(f),0, 1.1])
xlabel(r'Frequency, [Hz]', fontsize=16)
ylabel(r'Magnitude of DFT coefficients [scaled]', fontsize=16)
grid()
savefig('trunc.pdf')
show()
plot(abs(y)/(max(abs(y))))
axis([0, N, 0, 1.1])
xlabel(r'DFT index', fontsize=16)
ylabel(r'Magnitude of DFT coefficients [scaled]', fontsize=16)
grid()
savefig('trunc2.pdf')
show()
