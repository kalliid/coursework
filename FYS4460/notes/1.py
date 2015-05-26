from pylab import *

r = linspace(0.3, 2.5, 1001)

axes([0.1, 0.1, 0.8, 0.4])
plot(r, 4*(r**(-12) - r**(-6)), linewidth=2.0)
axis([0.5, 2.5, -2, 3])
xlabel(r'$r/\sigma$', fontsize=22)
ylabel(r'$U/\epsilon$', fontsize=22)
grid()
savefig("1.pdf", bbox_inches="tight", pad_inches=0)

show()
