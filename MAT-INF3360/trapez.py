def trapez(F,a,b,n):
    h = (b-a)/(n+1.)

    x = a
    s = F(a)/2. + F(b)/2.
    for i in range(n):
        x += h
        s += F(x)
    
    return s*h



from math import sqrt

F = lambda x: x**5
G = lambda x: sqrt(abs(x-0.5))

eF = 1./6
eG = sqrt(2)/3
print eG

a=0
b=1
fp=0.5*(F(1)-F(0))
gp=0.5*(F(1)-F(0))
np = 1

from numpy import log

#print r"n & Rel. error $I_1$ & Rel. error $I_2$ \\"
for n in 10, 20, 40, 80, 160, 320, 640, 1280:
    f = abs(trapez(F,a,b,n)-eF)
    g = abs(trapez(G,a,b,n)-eG)
    h = 1./(n+1)
    
    if n != 10:
        #print '%.4f' % (log(fp/f)/log(hp/h))
        print "%.4f" %  (log(gp/g)/log(hp/h))
    
    fp = f
    gp = g
    hp = h
    #print r"%i & %4.2e & %4.2e \\" % (n, f, g)

