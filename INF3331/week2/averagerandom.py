import numpy.random as npr

n = 1000
r = sum(npr.random(n)*2-1)/n
print "Average of %.1e random numbers drawn from [-1,1]: %.4f" % (n, r)

'''
user$ python averagerandom.py
Average of 1.0e+03 random numbers drawn from [-1,1]: 0.0166
'''  
