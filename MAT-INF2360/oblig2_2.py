from pylab import *

t = linspace(-1,1,1001)


phi1 = ((1+t)*(t<=0) + (1-t)*(t>0))*(t>-1)*(t<1)
phi2 = convolve(phi1,phi1)

plot(phi2)
show()

#phi1 = (1+t)*(t[-1<=t<0])


# def phi1(t):
#     if -1<=t<0:
#         return 1+t
#     elif 0<=t<1:
#         return 1-t
#     else:
#         return 0

# phi=[]
# t_values = linspace(-1,1,1001)
# for t in t_values:
#     phi.append(phi1(t))

# plot(phi)
# show()

# t = linspace(-2,2,2001)
# phi2 = convolve(phi, phi)
# plot(t, phi2)
# show()

# def phi1(t):
#     if -1<=t<0:
#         return 1+t
#     elif 0<=t<1:
#         return 1-t
#     else:
#         return 0



# x_values = linspace(-1,1,1001)
# t_values = linspace(-2,2,1001)
# dx = x_values[1]-x_values[0]

# phi = []

# for t in t_values:
#     s = 0
#     for x in x_values:
#         s += phi1(x)*phi1(t-x)
#     phi.append(s*dx)


# plot(t_values, phi)
# xlabel(r'$t$', fontsize=22)
# ylabel(r'$\phi(t)$', fontsize=22)
# grid()
# savefig("phi.pdf")
# show()