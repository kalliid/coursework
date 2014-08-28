from pylab import *

class v:
    def __init__(self, n):
        h = 1/(n+1.)
        self.mu1 = 4/h/h*(sin(pi*h/2.)**2)
        self.mu4 = 4/h/h*(sin(4*pi*h/2.)**2)

    def __call__(self, x, t):
        mu1, mu4 = self.mu1, self.mu4
        return 3*exp(-mu1*t)*sin(pi*x) + 5*exp(-mu4*t)*sin(4*pi*x)

def u(x,t):
    return 3*exp(-pi*pi*t)*sin(pi*x) + 5*exp(-16*pi*pi*t)*sin(4*pi*x)


v2 = v(2)
v4 = v(4)
v6 = v(6)
v8 = v(8)

x = linspace(0,1,10001)
t = 0

ion()
figure()
line1, = plot(x,  u(x,t))
line2, = plot(x, v2(x,t))
line3, = plot(x, v4(x,t))
line4, = plot(x, v6(x,t))
grid()
xlabel(r"$x$",fontsize=20)
ylabel(r"$u(x,t)$",fontsize=20)
draw()


while t < 1:
    line1.set_ydata( u(x,t))
    line2.set_ydata(v2(x,t))
    line3.set_ydata(v4(x,t))
    line4.set_ydata(v6(x,t))
    title("t=%.4f" % t)
    draw()


    t += 0.0001

ioff()
show()

# plot(x,u(x,0.01))
# plot(x,v2(x,0.01))
# plot(x,v4(x,0.01))
# plot(x,v6(x,0.01))
# legend([r"Analytic", r"n=2", r"n=4", r"n=6"])
# grid()
# xlabel(r"$x$",fontsize=20)
# ylabel(r"$u(x,0.01)$",fontsize=20)
# savefig("plot_h.pdf")
# show()