from pylab import *


below_fermi = (0,1,2,3)
above_fermi = (4,5,6,7)

states = [(1,1),(1,-1),(2,1),(2,-1),(3,1),(3,-1),(4,1),(4,-1)]
N = 8
g = 1

def h0(p,q):
	if p == q:
		p1, s1 = states[p]
		return (p1 - 1)	
	else:
		return 0

def assym(p,q,r,s):
	p1, s1 = states[p]
	p2, s2 = states[q]
	p3, s3 = states[r]
	p4, s4 = states[s]

	if p1 != p2 or p3 != p4 or s1 == s2 or s3 == s4:
		return 0
	else:
		return -g/2.


s = 0 
for a in above_fermi:
	for b in above_fermi:
		for c in above_fermi:
			for i in below_fermi:
				for j in below_fermi:
					for k in below_fermi:
						s += assym(i,j,a,b)*assym(a,c,j,k)*assym(b,k,c,i)

print s