import numpy as np
import random
import sys

def dice4(n):
    '''Non-vectorized, draw numbers in a loop and count successes'''
    money = 0
    for _ in range(n):
        money -= 1
        die = [random.randint(1,6) for _ in range(4)]
        if sum(die) < 9:
            money += 10
    return money/float(n)

def dice4_vec(n):
    '''Vecotrized, draw all numbers at once and extract successes'''
    # Draw random integers and reshape
    r = np.random.randint(1,7, 4*n).reshape((n,4))
    # Could also have simply done 
    #r = np.random.randint(1,7,(n,4))
    
    # Sum the 4 integers for every game
    s = np.sum(r, axis=0)
    # Find the winning results
    wins = s[s<9]
    # Calculate total winnings
    money = 10*len(wins) - n
    return money/float(n)

if __name__ == '__main__':
    # Time the functions
    import timeit

    # The setup is used by timeit, but does not contribute to the final time
    setup = "from __main__ import n, dice4, dice4_vec"
    print "Run-time for functions\n%5s%10s%12s" % ('n', 'dice4', 'dice4_vec')
    for n in [10**3, 10**4, 10**5, 10**6, 10**7]:
        t1 = timeit.timeit('dice4(n)', setup=setup, number=1)
        t2 = timeit.timeit('dice4_vec(n)', setup=setup, number=1)
        print "%5.0e%10.2e%12.2e" % (n, t1, t2)

'''
user$ python dice4_NumPy.py
Run-time for functions
    n     dice4   dice4_vec
1e+03  5.70e-03    1.83e-04
1e+04  5.73e-02    9.87e-04
1e+05  5.73e-01    9.64e-03
1e+06  5.76e+00    1.29e-01
1e+07  5.78e+01    1.29e+00
'''
