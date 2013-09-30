import sys
from numpy import *

usage = 'Usage: %s start:stop,step func' % sys.argv[0]
if len(sys.argv) != 3:
    print usage;sys.exit(1)

start, tmp = sys.argv[1].split(':')
stop, step = tmp.split(',')

x = arange(float(start), float(stop)+float(step), float(step))
y = eval(sys.argv[2])
for i in range(len(x)):
    print "%12g%12g" % (x[i], y[i])

'''
user$ python xygenerator.py '0:500,0.5' 'x*sin(x)' > outfile.dat
user$ more outfile.dat 
           0           0
         0.5    0.239713
           1    0.841471
         ...    ...
         499     245.007
       499.5     6.60915
         500    -233.886
'''