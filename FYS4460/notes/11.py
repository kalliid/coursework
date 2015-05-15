from pylab import *

p = linspace(0,1,1001)
q = 1-p

perc_prob = 4*p*p*q*q + 4*p*p*p*q + p*p*p*p
P = (2*4*p*p*q*q + 3*4*p*p*p*q + 4*p*p*p*p)/4

subplot(2,1,1)
plot(p, perc_prob, linewidth=2.0)
plot(p, p, '--')
grid()
ylabel(r'$\Pi(p, 2)$', fontsize=20)
subplot(2,1,2)
grid()
plot(p, P, linewidth=2.0)
plot(p, p, '--')
ylabel(r'$P(p, 2)$', fontsize=20)
xlabel(r'$p$', fontsize=20)
savefig("11.pdf")
show()