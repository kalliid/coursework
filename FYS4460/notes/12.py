from pylab import *

s = logspace(0, 6, 1001)

subplot(2,1,1)
for p in 0.9, 0.99, 0.999:
	plot(log10(s), log10(p**s), linewidth=2.0)

xlabel(r'$\log_{10} (s)$', fontsize=20)
ylabel(r'$\log_{10} \ G(s)$', fontsize=20)
grid()
savefig("12.pdf")
show()
