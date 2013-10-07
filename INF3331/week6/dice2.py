import random, sys

# Read number of experiments from cmd-line
try:
    N = eval(sys.argv[1])
except IndexError:
    errormsg = 'IndexError: Number of experiments must be specified.'; 
    print errormsg; sys.exit(1)
except ValueError:
    errormsg = 'ValueError: Input must be an integer.'
    print errormsg; sys.exit(1)
    
# Perform experiments
counter = 0
for experiment in range(N):
    results = [random.randint(1,6) for i in range(2)]
    if 6 in results:
        counter += 1

# Calculate probability
p = counter/float(N)
p_exact = 11./36
error = abs(p - p_exact)

# Print results
print """
Number of experiments: %d
Exact probability:     %.4g
Estimated probability: %.4g
Error:                 %.2e
""" % (N, p_exact, p, error)


"""
user$ python dice2.py 1000

Number of experiments: 1000
Exact probability:     0.3056
Estimated probability: 0.304
Error:                 1.56e-03

user$ python dice2.py 100000

Number of experiments: 100000
Exact probability:     0.3056
Estimated probability: 0.3054
Error:                 1.66e-04

user$ python dice2.py 10000000

Number of experiments: 10000000
Exact probability:     0.3056
Estimated probability: 0.3055
Error:                 5.69e-05
"""
