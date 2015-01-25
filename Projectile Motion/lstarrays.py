# Import various functions meant for numerical science
from pylab import *

t_0 = 0 # Start time, s
t_end = 10 # End time, s
N = 1000 # Number of time steps

# Create a uniformly spaced time-array
t = linspace(t_0, t_end, N+1)

# Calculate the size of a time step
dt = t[1] - t[0]

# Create empty acceleration, velocity and position arrays
a = zeros((2, N+1))
v = zeros((2, N+1))
r = zeros((2, N+1))

# Set initial conditions
v[0] = (10,0) # inital velocity, m/s
r[0] = (0,1)  # initial position, m
