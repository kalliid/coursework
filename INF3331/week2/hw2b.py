import sys
from math import sin

print "Hello, World!"

while (len(sys.argv) > 1):
	r = float(sys.argv.pop(1))
	print "sin(%g)=%g" % (r, sin(r))

'''
user$ python hw2b.py 1.4 -0.1 4 99
Hello, World!
sin(1.4)=0.98545
sin(-0.1)=-0.0998334
sin(4)=-0.756802
sin(99)=-0.999207
'''  
