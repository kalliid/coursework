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
convert2_wNumPy.py  hmt.out
user$ python convert2_wNumPy hmt.out
user$ ls
c0.dat   CaJSR.dat  cCa3.dat            j.dat        pc2.dat  xto1.dat
c1.dat   CaNSR.dat  cCa4.dat            Ki.dat       po1.dat  yL.dat
c2.dat   Cass.dat   convert2_wNumPy.py  LTRPNCa.dat  po2.dat  yto1.dat
c3.dat   cCa0.dat   h.dat               m.dat        V.dat    z_b.dat
c4.dat   cCa1.dat   hmt.out             open.dat     xKr.dat
Cai.dat  cCa2.dat   HTRPNCa.dat         pc1.dat      xKs.dat
user$ less m.dat
           0  9.97681e-01
         0.5  9.97285e-01
           1  9.96574e-01
         1.5  9.95633e-01
           2  9.94415e-01
         2.5  9.92980e-01
           3  9.91259e-01
         3.5  9.89217e-01
           4  9.86821e-01
        ...
'''