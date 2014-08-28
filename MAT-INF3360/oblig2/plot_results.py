from pylab import *
from time import sleep

n = 11;
m = 250;


u1 = np.fromfile('CN1.bin', np.float64)
u1 = u1.reshape(n+2, m+2)

x = linspace(0,1,n+2)



ion()
figure()
line, = plot(x, u1[:,0])
xlim([0, 1]) 
draw()

for i in range(m):
    line.set_ydata(u1[:,i])
    draw()
    sleep(0.1)

ioff()
show()
