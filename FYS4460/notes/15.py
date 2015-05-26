from pylab import *

p = linspace(0,1,1001)
q = 1-p
pc = 0.59275

subplot(2,1,1)
plot([0, 1, 1], [0, 0, 1], linewidth=2.0)
plot(p, p, '--', linewidth=2.0)
axis([-0.05,1.05,-0.05,1.05])
ylabel('$\Pi(p,\infty)$', fontsize=22)
legend([r'$L=\infty$', r'$L=1$'], 'upper left')
grid()

subplot(2,1,2)
plot([0, pc, pc, 1], [0, 0, 1, 1], linewidth=2.0)
plot(p, p, '--', linewidth=2.0)
axis([-0.03,1.03,-0.03,1.03])
ylabel('$\Pi(p,\infty)$', fontsize=22)
xlabel('$p$', fontsize=22)
grid()
savefig("15.pdf")
show()


subplot(2,1,1)
for L in 1, 2, 4, 8, 16:
	plot(p, p**L, linewidth=2.0)

ylabel('$\Pi(p,\infty)$', fontsize=22)
grid()

subplot(2,1,2)
plot([0, pc, pc, 1], [0, 0, 1, 1], linewidth=2.0)
plot(p, p, '--', linewidth=2.0)
plot(p, 4*p*p*q*q + 4*p*p*p*q + p*p*p*p, linewidth=2.0)
ylabel('$\Pi(p,\infty)$', fontsize=22)
xlabel('$p$', fontsize=22)
axis([0,1,0,1.03])
savefig("15b.pdf")
show()