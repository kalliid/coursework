from spanning_cluster_density import *

def experiment(p, L):
	r = rand(L, L)
	z = r < p
	return  spanning_cluster_density(z)


pc = 0.59275
L = 512
N = 500
PN = 51

prange = linspace(0.594,1,PN)
P = zeros(PN)

for i in range(PN):
	print i 
	s = 0
	for _ in range(N):
		s += experiment(prange[i], L)
	P[i] = s/N

a, b = polyfit(log(prange-pc), log(P), 1)
print a, b
plot(log(prange-pc), log(P), linewidth=2.0)
plot(log(prange-pc), log(prange-pc)*a + b)
# axis([0.5,1,0,1])
grid()
ylabel('log(P(p,L))')
xlabel('log(p)')
legend(['Numerical Data', 'Best linear fit'], 'upper left')
show()