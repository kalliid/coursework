from pylab import *

x_0 = 0
x_1 = 2
u_0 = 4
N = 100001 # N should be big, so that dx becomes small

x = linspace(x_0, x_1, N) # H
u = zeros(N)

dx = x[1]-x[0]
u[0] = u_0

for i in range(N-1):
	u[i+1] = (1-dx)*u[i]

# Can now calculate the relative error!
u_e = 4*exp(-x)

plot(x, u)
plot(x, u_e)
grid()
xlabel('x')
ylabel('u(x)')
legend(['Numerical', 'Analytical'])
show()


abs_error = abs(u-u_e)
rel_error = abs_error/u_e

plot(x, rel_error)
show()