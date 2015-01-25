from pylab import *

# Constants
g = 9.81 # gravitational acceleration, m/s^2
m = 0.145 # mass of ball, kg
A = pi*0.038**2 # cross-sectional area of ball, m^2
C_d = 0.3 # Drag coefficient of ball
rho = 1.2 # Density of air # kg/m^3

# Define force function
def F(x, v, t):
    Fg = (0, -m*g)
    Fd = -0.5*C_d*A*rho*abs(v)*v
    print Fg+F
    return Fg + Fd

# Simulation parameters
N = 1000 # Number of time steps
t_0 = 0 # Start time
t_end = 10 # End time, s
t = linspace(0, 10, N+1) # time-array
dt = t[1] - t[0] # size of time step

# Create empty 2D arrays
r = zeros((N+1, 2))
v = zeros((N+1, 2))
a = zeros((N+1, 2))

# Set initial conditions
v[0] = (40*cos(pi/6.), 40*sin(pi/6.)) # m/s
r[0] = (0, 1) # m

# Solving equations of motion iteratively
for i in range(N):
	a[i] = F(r[i], v[i], t[i])/m
	v[i+1] = v[i] + a[i]*dt
	r[i+1] = r[i] + v[i]*dt

# Extract x and y coordinates as arrays
x = r[:,0]
y = r[:,1]

# Plot results
plot(x, y)
axis([0, 110, 0, 20])
xlabel('Horizontal distance [m]')
ylabel('Vertical distance [m]')
grid()
title('Path of a batted baseball')
show()



