from __future__ import division
from sympy import *
from numpy import *
import pickle 

Z = Symbol("Z")

# Read in the radial_integrals from pickled object
with open("radial_integrals.p", "rb") as infile:
    radial_integrals = pickle.load(infile)

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

def matrix_element(SD1, SD2):
    i, a = SD1
    j, b = SD2

    s = 0
    if a == -1 and b == -1:
        for k in range(N):
            s += h_0(k,k)
            for l in range(N):
                s += asym(k,l,k,l)/2
        return s

    elif b == -1:
        s += h_0(a,i)
        for k in range(N):
            s += asym(a,k,i,k)
        return s

    elif a == -1:
        s += h_0(b,j)
        for k in range(N):
            s += asym(b,k,j,k)
        return s

    s += asym(a,j,i,b)
    if a==b:
        s -= h_0(i,j)
        for k in range(N):
            s -= asym(i,k,j,k)
      

    if i==j:
        s += h_0(a,b)
        for k in range(N):
            s += asym(a,k,b,k)
    
    if a==b and i==j:
        for k in range(N):
            s += h_0(k,k)
            for l in range(N):
                s += asym(k,l,k,l)/2

            
    return s


N = 4
Z_value = 4

# Define the single-particle states used
states = [(1,1), (1,-1), (2,1), (2,-1), (3,1),(3,-1)]
# Define the SDs used
SDs = [(-1,-1),(0,4),(1,5),(2,4),(3,5)]

H = zeros((5,5))

for i in range(5):
    for j in range(5):
        H[i,j] = matrix_element(SDs[i], SDs[j]).subs(Z, Z_value).evalf()
        print "%.3f & " % H[i,j],
    print r"\\"
        
vals, vecs = linalg.eig(H)
print vals