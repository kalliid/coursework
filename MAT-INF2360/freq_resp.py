from pylab import *

def g0(w):
    return 1./16*(6+8*cos(w)+2*cos(2*w))

def g1(w):
    return 1./64*(5*cos(5*w)+20*cos(4*w)+cos(3*w)-96*cos(2*w)-70*cos(w)+140)

w = linspace(0,2*pi,1001)
plot(w, g0(w))
axis([0,2*pi,0,1])
grid()
xlabel(r"$\omega$",fontsize=22)
ylabel(r"$\lambda_{G_0}(\omega)$",fontsize=22)
savefig("g0.pdf")
show()

w = linspace(0,2*pi,1001)
plot(w, g1(w))
axis([0,2*pi,0,4.1])
grid()
xlabel(r"$\omega$",fontsize=22)
ylabel(r"$\lambda_{G_1}(\omega)$",fontsize=22)
savefig("g1.pdf")
show()

