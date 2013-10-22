import numpy as np
import sys

usage = 'Usage: %s infile' % sys.argv[0]
try:
    infilename = sys.argv[1]
except:
    print usage; sys.exit(1)

with open(infilename, 'r') as f:
    f.readline(); dt = float(f.readline()) # Read header and dt
    # Read in data from file, using first line as names
    data = np.genfromtxt(f, names=True, delimiter=" ", dtype=None)

# Write out 2-column files with t and data[name] for each name
for name in data.dtype.names:
    with open(name+'.dat', 'w') as ofile:
        for k in range(data[name].size):
            ofile.write('%12g %12.5e\n' % (k*dt, data[name][k]))


'''
user$ ls
'''