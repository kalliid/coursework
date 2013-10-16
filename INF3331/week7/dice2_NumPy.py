import numpy as np
import random
import sys

def dice2(N):
    '''Non-vectorized, draw numbers in a loop and count successes'''
    s = 0
    for experiment in range(N):
        results = [random.randint(1,6) for i in range(2)]
        if 6 in results:
            s += 1
    return s/float(N)

def dice2_vec(N):
    '''Vecotrized, draw all numbers at once and extract successes'''
    # Draw random integers
    r = np.random.randint(1, 7, (N, 2))
    # Create a boolean array
    s = (r[:,0] == 6) | (r[:,1] == 6)
    # Sum all successes 
    c = np.sum(s)
    # Calculate and return probability
    return c/float(N)


if __name__ == '__main__':
    # Time the functions
    import timeit

    # The setup is used by timeit, but does not contribute to the final time
    setup = "from __main__ import N, dice2, dice2_vec"
    print "Run-time for functions\n%5s%10s%12s" % ('N', 'dice2', 'dice2_vec')
    for N in [10**3, 10**4, 10**5, 10**6, 10**7]:
        t1 = timeit.timeit('dice2(N)', setup=setup, number=1)
        t2 = timeit.timeit('dice2_vec(N)', setup=setup, number=1)
        print "%5.0e%10.2e%12.2e" % (N, t1, t2)

'''
user$ python dice2_NumPy.py
Run-time for functions
    N     dice2   dice2_vec
1e+03  2.98e-03    1.66e-04
1e+04  2.85e-02    5.75e-04
1e+05  2.84e-01    5.18e-03
1e+06  2.90e+00    6.17e-02
1e+07  2.89e+01    6.03e-01
'''
