
with open('times2.dat', 'r') as infile:
    data = infile.readlines()

from pylab import *

N = len(data)
n = zeros(N)
t1 = zeros(N)
t2 = zeros(N)
t3 = zeros(N)

for i in range(N):
    n[i], t1[i], t2[i], t3[i] = data[i].split()

# plot(n,t1*1000.,'-o')
# plot(n,t2*1000.,'-o')
# plot(n,t3*1000.,'-o')
# plot(n,t4*1000.,'-o')
# xlabel(r'$n$', fontsize=16)
# ylabel(r'$t$ [ms]', fontsize=16)
# axis([4,14,0,1])
# legend(['DFTImpl', 'FFT_recursive','FFT_vectorized','numpy.fft.fft'])
# grid()
# savefig('times_a.pdf')
# show()

# plot(n,t1*1000.,'-o')
# plot(n,t2*1000.,'-o')
# plot(n,t3*1000.,'-o')
# plot(n,t4*1000.,'-o')
# xlabel(r'$n$', fontsize=16)
# ylabel(r'$t$ [ms]', fontsize=16)
# axis([4,14,0,10])
# legend(['DFTImpl', 'FFT_recursive','FFT_vectorized','numpy.fft.fft'], loc=2)
# grid()
# savefig('times_b.pdf')
# show()

# plot(n,t1*1000.,'-o')
# plot(n,t2*1000.,'-o')
# plot(n,t3*1000.,'-o')
# plot(n,t4*1000.,'-o')
# xlabel(r'$n$', fontsize=16)
# ylabel(r'$t$ [ms]', fontsize=16)
# axis([4,14,0,100])
# legend(['DFTImpl', 'FFT_recursive','FFT_vectorized','numpy.fft.fft'], loc=2)
# grid()
# savefig('times_c.pdf')
# show()

# from pylab import *

plot(n,array(t1)*1000.,'-o')
plot(n,array(t2)*1000.,'-o')
plot(n,array(t3)*1000.,'-o')
xlabel(r'$n$', fontsize=16)
ylabel(r'$t$ [ms]', fontsize=16)
axis([15,22,0,1500])
legend(['FFT_recursive','FFT_vectorized','numpy.fft.fft'])
grid()
savefig('times_d.pdf')
show()
