import numpy as np

infilename = "hmt.out"

with open(infilename, 'r') as f:
    f.readline();
    dt = float(f.readline())
    data = np.genfromtxt(f, names=True, delimiter=" ", dtype=None)

y = {name : data[name] for name in data.dtype.names}

#print 'y dictionary:\n', y

# write out 2-column files with t and y[name] for each name:
for name in y.keys():
    ofile = open(name+'.dat', 'w')
    for k in range(y[name].size):
        ofile.write('%12g %12.5e\n' % (k*dt, y[name][k]))
