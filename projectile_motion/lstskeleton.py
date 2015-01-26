from pylab import *

# Define physical constants used in the problem
m = ...
g = ...

# Define the force function of the system
def F(x, v, t):
	return ...

t_0 = ... # Start time, s
t_end = ...  # End time, s
N = ... # Number of time steps

# Create a uniformly spaced time-array
t = linspace(t_0, t_end, N+1)

# Calculate the size of a time step
dt = t[1] - t[0]

# Create empty acceleration, velocity and position arrays
a = zeros((2,N+1))
v = zeros((2,N+1))
r = zeros((2,N+1))

# Set initial conditions
v[0] = ... # inital velocity, m/s
r[0] = ... # initial position, m

# Solve equations of motions iteratively
for i in range(N):
	a[i] = F(x[i], v[i], t[i])
	v[i+1] = v[i] + a[i]*dt
	x[i+1] = x[i] + v[i]*dt

