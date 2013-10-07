import numpy as np
import sys

# Read number of games from cmd-line
try:
    N = eval(sys.argv[1])
except IndexError:
    errormsg = 'IndexError: Number of games must be specified.'; 
    print errormsg; sys.exit(1)
except ValueError:
    errormsg = 'ValueError: Input must be an integer.'
    print errormsg; sys.exit(1)

# Draw 4 integers from [1,7), N times
results = np.random.randint(1,7,(4,N))
# Sum the 4 integers for every game
s = np.sum(results, axis=0)
# Separate winning and loosing results
wins = s[s<9]
loss = s[s>=9]
# Calculate losses and rewards
money = 9*len(wins) - len(loss)
average = money/float(N)
# Analyze results
r = 'No' if average < 0 else 'Yes'

# Print results
print """
Number of games:           %d
Total money won/lost:      %g
Estimated average winning: %.2g
Should you play?:          %s
""" % (N, money, average, r)


"""
user$ python dice4.py 1000

Number of games:           1000
Total money won/lost:      -480
Estimated average winning: -0.48
Should you play?:          No

user$ python dice4.py 1000000

Number of games:           1000000
Total money won/lost:      -463230
Estimated average winning: -0.46
Should you play?:          No
"""
