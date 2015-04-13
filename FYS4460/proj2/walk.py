from pylab import *
from scipy.ndimage import measurements
# from walk import walk



# Generate perc matrix
L = 100
r = rand(L, L)
p = 0.6
z = r < p

# imshow(z, origin='lower', cmap='Greys', interpolation='nearest')
# show()

lw, num = measurements.label(z)
imshow(lw, origin='lower', interpolation='nearest')
show()