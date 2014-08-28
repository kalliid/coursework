from pylab import *

def crank_nicolson(u, r, n, m):
    b = zeros(n+1)
    v = zeros(n+1)
    c = 2-2*r
    
    for j in range(m):
        # Initialize tridiagonal matrices
        b[:] = (2+2*r)
        v[1:] = r*u[2:, j] + c*u[1:-1,j] + r*u[:-2,j]
        
        # Decomposition of A
        for i in range(1,n):
            p = -r/b[i]
            b[i+1] += p*r
            v[i+1] -= p*v[i]

        # Forward substitution
        u[n,j+1] = v[n]/b[n]
        for i in range(n-1, 0, -1):
            u[i,j+1] = (v[i] + r*u[i+1,j+1])/b[i]

n = 501
m = 250

L = 1
T = 0.5
dx = L/(n+1.)
dt = T/(m+1.)
r = dt/dx/dx

x = linspace(0,L,n+2)
t = linspace(0,T,m+2)

u = zeros((n+2,m+2))

# Initial condition
u[:,0] = 2*x*(x<0.5) + 2*(1-x)*(x>=0.5)
    
crank_nicolson(u, r, n, m);
plot(x, u[:,200])
xlabel(r"$x$",fontsize=20)
ylabel(r"$v(x,t=0.4)$",fontsize=20)
title(r"$r=500$", fontsize=20)
show()

# ion()
# figure()
# line, = plot(x, u[:,0])
# xlim([0, 1]) 
# draw()



# for i in range(m):
#     line.set_ydata(u[:,i])
#     draw()

# ioff()
# show()
