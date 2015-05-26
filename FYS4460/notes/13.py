from pylab import *

p = linspace(1e-4, 1-1e-4, 10001)
s = logspace(-3, 3, 100)
r = linspace(0,2,1001)

subplot(3,1,1)
plot(p, -1/log(p), linewidth=2.0)
xlabel(r'$p$', fontsize=22)
ylabel(r'$\xi(p)$', fontsize=22)
axis([0,1,0,50])

subplot(3,1,2)
plot(r, exp(-r), linewidth=2.0)
xlabel(r'$r/\xi$', fontsize=22)
ylabel(r'$g(r/\xi)$', fontsize=22)

subplot(3,1,3)
plot(log10(s), log10(exp(-s)), linewidth=2.0)
axis([-3, 3, -250, 30])
xlabel(r'$\log_{10}(r/\xi)$', fontsize=22)
ylabel(r'$\log_{10}g(r/\xi)$', fontsize=22)

tight_layout(pad=1.0, h_pad=-0.1)

savefig("13.pdf")
show()



# subplot(2,1,1)
# for p in 0.9, 0.99, 0.999:
# 	plot(log10(s), log10(p**s), linewidth=2.0)

# xlabel(r'$\log_{10} (s)$', fontsize=20)
# ylabel(r'$\log_{10} \ G(s)$', fontsize=20)
# grid()
# savefig("12.pdf")
# show()
