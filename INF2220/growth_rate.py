from pylab import *


N = linspace(1,100,100)

f = zeros(100) + 1

plot(N, N)
plot(N, 1./N)
plot(N, f)


#legend(['N log^2 N', 'N^1.5', 'N^2', 'N^2 log N'])
show()