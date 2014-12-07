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


# Diagram 3
# s = 0 
# for a in above_fermi:
# 	for b in above_fermi:
# 		for c in above_fermi:
# 			for i in below_fermi:
# 				for j in below_fermi:
# 					for k in below_fermi:
# 						s += assym(i,j,a,b)*assym(a,c,j,k)*assym(b,k,c,i)/eps((i,j),(a,b))/eps((k,j),(a,c))
# print s


# ga = linspace(-1,1,101)
# corr2 = []
# corr3 = []
# corrx = []


# Diagram 1
s1 = 0
for a in above_fermi:
	for b in above_fermi:
		for i in below_fermi:
			for j in below_fermi:
				s1 += 0.25*assym(a,b,i,j)*assym(i,j,a,b)/eps((i,j),(a,b))

# Diagram 4
s4 = 0
for a in above_fermi:
	for b in above_fermi:
		for c in above_fermi:
			for d in above_fermi:
				for i in below_fermi:
					for j in below_fermi:
						s4 += 0.125*assym(i,j,a,b)*assym(a,b,c,d)*assym(c,d,i,j)/eps((i,j),(a,b))/eps((i,j),(c,d))

# Diagram 5
s5 = 0
for a in above_fermi:
	for b in above_fermi:
		for i in below_fermi:
			for j in below_fermi:
				for k in below_fermi:
					for l in below_fermi:
						s5 += 0.125*assym(i,j,a,b)*assym(k,l,i,j)*assym(a,b,k,l)/eps((i,j),(a,b))/eps((k,l),(a,b))

# Diagram 8 (simplified)
s8 = 0 
for a in above_fermi:
	for b in above_fermi:
		for i in below_fermi:
			for j in below_fermi:
				for k in below_fermi:
					s8 -= 0.5*assym(i,j,a,b)*assym(a,b,i,k)*f(k,j)/eps((i,j),(a,b))/eps((i,k),(a,b))

# Diagram 9 (simplified)
s9 = 0 
for a in above_fermi:
	for b in above_fermi:
		for c in above_fermi:
			for i in below_fermi:
				for j in below_fermi:
					s9 += 0.5*assym(i,j,a,b)*assym(a,c,i,j)*f(b,c)/eps((i,j),(a,b))/eps((i,j),(a,c))


print s1
print s4
print s5
print s8
print s9

s_5 =  -0.0291521990740741*g**4
s14 =  -0.0308883101851853*g**4
s34 =  0.0163049768518519*g**4
s36 =  -0.0145760995370371*g**4
s38 =  -0.0201099537037037*g**4
s39 =  0.0176938657407407*g**4

ga = linspace(-1,1,10001)
e1 = []
corr2 = []
corr3 = []
corr4 = []
for g_val in ga:
	H1 = matrix([[2-g_val , -g_val/2.,  -g_val/2., -g_val/2., -g_val/2.,     0], 
		        [-g_val/2.,   4-g_val,  -g_val/2., -g_val/2.,    0., -g_val/2.],
		        [-g_val/2., -g_val/2.,    6-g_val,     0, -g_val/2., -g_val/2.],
				[-g_val/2., -g_val/2.,      0,   6-g_val, -g_val/2., -g_val/2.],
				[-g_val/2.,     0,  -g_val/2., -g_val/2.,   8-g_val, -g_val/2.],
				[0    , -g_val/2.,  -g_val/2., -g_val/2., -g_val/2.,  10-g_val]]) 

	u1, v1 = linalg.eig(H1)
	e1.append(min(u1))

	corr2.append((s1).subs(g,g_val))
	corr3.append((s1+s4+s5).subs(g,g_val))
	corr4.append((s1+s4+s5+2*s_5+2*s14+2*s34+2*s36+s38+2*s39).subs(g,g_val))

exact = e1 - (2-ga)

plot(ga, exact, linewidth=2.0)
plot(ga, corr2, linewidth=2.0)
plot(ga, corr3, linewidth=2.0)
plot(ga, corr4, linewidth=2.0)
xlabel(r'Interaction strength, $g$', fontsize=16)
ylabel(r'Correlation energy', fontsize=16)
axis([-1,1,-0.5,0.05])
grid()
legend(["Exact", "2. order MPBT", "3. order MPBT", "4. order MPBT"], 'lower left')
savefig("pert_2.pdf")
show()


error1 = zeros(len(exact))
error2 = zeros(len(exact))
error3 = zeros(len(exact))

for i in range(len(exact)):
	error1[i] = abs(float(exact[i]-corr2[i]))
	error2[i] = abs(float(exact[i]-corr3[i]))
	error3[i] = abs(float(exact[i]-corr4[i]))

error1 = array(error1)
error2 = array(error2)
error3 = array(error3)
print type(error1)

plot(ga, log10(error1))
plot(ga, log10(error2))
plot(ga, log10(error3))
xlabel(r"Strength of interaction, $g$", fontsize=16)
ylabel(r"Error, $\log_{\rm 10}({\rm abs}({\rm error})$", fontsize=16)
legend(["2. order MPBT", "3. order MPBT", "4. order MPBT"], 'lower left')
grid()
savefig("logerror.pdf")
show()