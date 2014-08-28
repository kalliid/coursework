from pylab import *

ta = linspace(-1,1,1000)

phi1 = []
for t in ta:
	phi1.append((1+t)*(-1<=t<0) + (1-t)*(0<=t<1))

phi2 = convolve(phi1,phi1)

phi2 /= max(phi2)

print size(phi2)

a = zeros(4000)
b = zeros(4000)
c = zeros(4000)
d = zeros(4000)
e = zeros(4000)

a[0:1999] = phi2[:]
b[500:2499] = phi2[:]
c[1000:2999] = phi2[:]
d[1500:3499] = phi2[:]
e[2000:3999] = phi2[:]

x = linspace(-2,2,4000)

plot(x, 1./8*a)
plot(x, 1./2*b)
plot(x, 3./4*c)
plot(x, 1./2*d)
plot(x, 1./8*e)
plot(x, 1./8*a + 1./2*b + 3./4*c + 1./2*d + 1./8*e)
xlabel(r"$t$")
axis([-2,2,0,1.1])
grid()
legend([r"$(1/8)\phi_{1,-2}$",r"$(1/2)\phi_{1,-1}$",r"$(3/4)\phi_{1,0}$",r"$(1/2)\phi_{1,1}$",r"$(1/8)\phi_{1,2}$",r"$\phi_{0,0}$"])
savefig("scaling_functions.pdf")
show()

