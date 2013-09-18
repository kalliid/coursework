#!/usr/bin/env python
import numpy as np
import sys

usage = 'Usage: %s outfile dt **infiles' % sys.argv[0]

# Try reading cmd-line arguments
try:
	outfile = sys.argv[1]
	dt = sys.argv[2]
	infiles = sys.argv[3:]
except:
	print usage; sys.exit(1)

# Open outfile for writing
outfile = open(outfile+'.dat', 'w') 
outfile.write('Outfile for inverseconvert.py\n%s\n' % dt)

# Read in data from infiles
data = []
for i in range(len(infiles)):
	outfile.write("  " + infiles[i][:-4])
	data.append(np.loadtxt(infiles[i])[:,1])

# Write data to new outfile
outfile.write("\n")
for i in range(len(data)):
	for j in range(len(data[0])):
		length = (len(infiles[j])-6)/2
		outfile.write(' '*length + str(data[j][i]) + ' '*(length+2))
	outfile.write('\n')

'''
user$ python inverseconvert.py outfile 1.5 \ 
tmp-measurements.dat  tmp-model1.dat  tmp-model2.dat

user$ more outfile.dat
Outfile for inverseconvert.py
1.5
  tmp-measurements  tmp-model1  tmp-model2
       0.0             0.1          1.0      
       0.1             0.1          0.188      
       0.2             0.2          0.25  
'''