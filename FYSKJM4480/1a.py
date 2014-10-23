from __future__ import division
from sympy import *
from numpy import *
import pickle 

Z = Symbol("Z")

# Read in the radial_integrals from pickled object
with open("radial_integrals.p", "rb") as infile:
    radial_integrals = pickle.load(infile)

# Define the single-particle states used
states = [(1,1), (1,-1)]

# Define matrix elements
def h_0(p, q):
    """
    Takes integer values and uses to global states 
    list to find the corresponding quantum numbers.
    Calculates and returns matrix element <p|h_0|q>.
    """
    n1, s1 = states[p]
    n2, s2 = states[q]

    if n1 != n2 or s1 != s2:
        return 0
    else:
        return -Z**2/(2*n1**2)

def h_1(n1, n2, n3, n4):
    """
    Takes the quantum numbers n and returns the radial
    integral <pq|v|rs>, disregarding spin.
    """
    return radial_integrals[n1-1,n2-1,n3-1,n4-1]

def asym(p,q,r,s):
    """
    Takes integer values and uses gobal states list
    to find the corresponding quantum numbers.
    Calculates the asymmetrized matrix element <pq||rs>.
    """
    n1, s1 = states[p]
    n2, s2 = states[q]
    n3, s3 = states[r]
    n4, s4 = states[s]

    if s1 == s2 == s3 == s4:
        return h_1(n1,n2,n3,n4) - h_1(n1,n2,n4,n3)
    elif s1 == s3 and s2 == s4:
        return h_1(n1,n2,n3,n4)
    elif s1 == s4 and s2 == s3:
        return -h_1(n1,n2,n4,n3)
    else:
        return 0

e = 0
for i in range(2):
	e += h_0(i,i)
	for j in range(2):
		e += 0.5*asym(i,j,i,j)


print e.subs(Z,2)