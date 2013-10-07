# Read in data from file
infile = open('efficiency.test', 'r')
lines = infile.readlines()
infile.close()

# Sort out lines with CPU-time data (and remove '\n')
cpulines = [l[:-1] for l in lines if l[:8]=="CPU-time"]

# Sort with respect to time
cpulines.sort(key=lambda line: float(line.split()[1]))

# Print out resulting order
print '\n'.join([line for line in cpulines])

'''
user$ python ranking.py
CPU-time:   5.41   g77 -O3 -ffast-math -funroll-loops original (optimal?) code
CPU-time:   5.55   g77 -O3 original (optimal?) code
CPU-time:   5.62   g77 -O2 original (optimal?) code
...
CPU-time: 255.97   f95 -O0 formatted I/O
CPU-time: 272.90   g77 -O0 formatted I/O
'''
