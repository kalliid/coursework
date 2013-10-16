'''
Program for testing the SparseVec class
'''

from SparseVec import SparseVec

a = SparseVec(4)
a[2] = 9.2
a[0] = -1
print "a:\n\t", a
print "a.nonszeros():\n\t", a.nonzeros()

b = SparseVec(5)
b[1] = 1
print "b:\n\t", b
print "b:\n\t", b.nonzeros()

c = a + b
print "c:\n\t", c
print "c.nonzeros():\n\t", c.nonzeros()

print "Testing iterator"
for ai, i in a:  # SparseVec iterator
    print 'a[%d]=%g ' % (i, ai),


'''
user$ python SparseVec_example.py 
a:
    [0]=-1 [1]=0 [2]=9.2 [3]=0
a.nonszeros():
    {0: -1, 2: 9.2}
b:
    [0]=0 [1]=1 [2]=0 [3]=0 [4]=0
b:
    {1: 1}
c:
    [0]=-1 [1]=1 [2]=9.2 [3]=0 [4]=0
c.nonzeros():
    {0: -1, 1: 1, 2: 9.2}
'''