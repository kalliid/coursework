from sympy import *
from pylab import *

below_fermi = (0,1,2,3)
above_fermi = (4,5,6,7)

states = [(1,1),(1,-1),(2,1),(2,-1),(3,1),(3,-1),(4,1),(4,-1)]
N = 8
g = Symbol('g')


def h0(p,q):
	if p == q:
		p1, s1 = states[p]
		return (p1 - 1)	
	else:
		return 0

def f(p,q):
	if p == q:
		return 0

	s = h0(p,q)
	for i in below_fermi:
		s += assym(p,i,q,i)
	return s


def assym(p,q,r,s):
	p1, s1 = states[p]
	p2, s2 = states[q]
	p3, s3 = states[r]
	p4, s4 = states[s]

	if p1 != p2 or p3 != p4:
		return 0
	if s1 == s2 or s3 == s4:
		return 0
	if s1 == s3 and s2 == s4:
		return -g/2.
	if s1 == s4 and s2 == s3:
		return g/2.

def eps(holes, particles):
	E = 0
	for h in holes:
		p, s = states[h]
		E += (p-1)
	for p in particles:
		p, s = states[p]
		E -= (p-1)
	return E

s5 = s14 = s34 = s36 = s38 = s39 = 0

for a in above_fermi:
	for b in above_fermi:
		for c in above_fermi:
			for d in above_fermi:
				for i in below_fermi:
					for j in below_fermi:
						for k in below_fermi:
							for l in below_fermi:
								s5 += 1/16.*assym(i,j,a,b)*assym(a,b,c,d)*assym(k,l,i,j)*assym(c,d,k,l)/(eps((i,j),(a,b))*eps((i,j),(c,d))*eps((k,l),(c,d)))


for a in above_fermi:
	for b in above_fermi:
		for c in above_fermi:
			for d in above_fermi:
				for e in above_fermi:
					for f in above_fermi:
						for i in below_fermi:
							for j in below_fermi:
								s14 += 1/16.*assym(i,j,a,b)*assym(a,b,c,d)*assym(c,d,e,f)*assym(e,f,i,j)/(eps((i,j),(a,b))*eps((i,j),(c,d))*eps((i,j),(e,f)))

for a in above_fermi:
	for b in above_fermi:
		for c in above_fermi:
			for d in above_fermi:
				for i in below_fermi:
					for j in below_fermi:
						for k in below_fermi:
							for l in below_fermi:
								s34 -= 1/4.*assym(i,j,a,b)*assym(a,b,i,k)*assym(k,l,c,d)*assym(c,d,k,l)/(eps((i,j),(a,b))*eps((i,j,k,l),(a,b,c,d))*eps((j,l),(c,d)))

for a in above_fermi:
	for b in above_fermi:
		for c in above_fermi:
			for d in above_fermi:
				for i in below_fermi:
					for j in below_fermi:
						for k in below_fermi:
							for l in below_fermi:
								s36 += 1/16.*assym(i,j,a,b)*assym(k,l,c,d)*assym(a,b,k,l)*assym(c,d,i,j)/(eps((i,j),(a,b))*eps((i,j,k,l),(a,b,c,d))*eps((i,j),(c,d)))

for a in above_fermi:
	for b in above_fermi:
		for c in above_fermi:
			for d in above_fermi:
				for i in below_fermi:
					for j in below_fermi:
						for k in below_fermi:
							for l in below_fermi:
								s38 += assym(i,l,a,d)*assym(j,k,b,c)*assym(c,d,k,l)*assym(a,b,i,j)/(eps((i,l),(a,b))*eps((i,j,k,l),(a,b,c,d))*eps((i,j),(a,b)))

for a in above_fermi:
	for b in above_fermi:
		for c in above_fermi:
			for d in above_fermi:
				for i in below_fermi:
					for j in below_fermi:
						for k in below_fermi:
							for l in below_fermi:
								s39 += -0.25*assym(i,j,a,b)*assym(k,l,c,d)*assym(c,d,k,l)*assym(a,b,i,k)/(eps((i,j),(a,b))*eps((i,j,k,l),(a,b,c,d))*eps((i,k),(a,b)))


print "s5 = ", repr(s5)
print "s14 = ", repr(s14)
print "s34 = ", repr(s34)
print "s36 = ", repr(s36)
print "s38 = ", repr(s38)
print "s39 = ", repr(s39)
