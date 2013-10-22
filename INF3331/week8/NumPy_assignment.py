from scitools.numpytools import *
x = sequence(0, 1, 0.5)
# y = 2*x + 1:
y = x;  y*=2;  y += 1
# z = 4*x - 4:
z = x;  z*=4;  z -= 4
print x, y, z

from scitools.numpytools import *
x = sequence(0, 1, 0.5)
y = 2*x + 1
z = 4*x - 4
print x, y, z


from scitools.numpytools import *
x = sequence(0, 1, 0.5)
y = x.copy(); y *=2; y += 1
z = x.copy(); z *= 4; z -= 4
print x, y, z
