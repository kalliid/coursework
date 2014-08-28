echo Unpacking file week2/hw2c.py
cat > week2/hw2c.py <<EOF
import sys
from math import log

print "Hello, World!"

for r in sys.argv[1:]:
	r = float(r)
	if r > 0:
		print "ln(%g)=%g" % (r, log(r))
	else:
		print "ln(%g) is illegal" % r

'''
user$ python hw2c.py 1.4 -0.1 4 99
Hello, World!
ln(1.4)=0.336472
ln(-0.1) is illegal
ln(4)=1.38629
ln(99)=4.59512
'''EOF
Unpacking file week2/averagerandom2.py
cat > week2/averagerandom2.py <<EOF
#!/usr/bin/env python
import sys, random
def compute(n):
    i = 0; s = 0
    while i < n:
        s += random.random()
        i += 1
    return s/n

n = int(sys.argv[1])
print 'the average of %d random numbers is %g' % (n, compute(n))

'''
user$ python averagerandom2.py 1000
the average of 1000 random numbers is 0.498158
'''EOF
Unpacking file week2/hw2b.py
cat > week2/hw2b.py <<EOF
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
'''EOF
Unpacking file week2/averagerandom.py
cat > week2/averagerandom.py <<EOF
import numpy.random as npr

n = 1000
r = sum(npr.random(n)*2-1)/n
print "Average of %.1e random numbers drawn from [-1,1]: %.4f" % (n, r)

'''
user$ python averagerandom.py
Average of 1.0e+03 random numbers drawn from [-1,1]: 0.0166
'''EOF
Unpacking file week2/printrandom.py
cat > week2/printrandom.py <<EOF
import random

r = random.random()*2 - 1
print "Random number drawn uniformly from [-1,1]: %.4f" % r

'''
user$ python printrandom.py
Random number drawn uniformly from [-1,1]: 0.1988
'''EOF
Unpacking file week2/hw2a.py
cat > week2/hw2a.py <<EOF
import sys
from math import sin

print "Hello, World!"

for r in sys.argv[1:]:
	print "sin(%g)=%g" % (float(r), sin(float(r)))

'''
user$ python hw2a.py 1.4 -0.1 4 99
Hello, World!
sin(1.4)=0.98545
sin(-0.1)=-0.0998334
sin(4)=-0.756802
sin(99)=-0.999207
'''EOF
  
EOF
echo Unpacking file week2/averagerandom2.py
cat > week2/averagerandom2.py <<EOF
#!/usr/bin/env python
import sys, random
def compute(n):
    i = 0; s = 0
    while i < n:
        s += random.random()
        i += 1
    return s/n

n = int(sys.argv[1])
print 'the average of %d random numbers is %g' % (n, compute(n))

'''
user$ python averagerandom2.py 1000
the average of 1000 random numbers is 0.498158
'''EOF
echo Unpacking file week2/hw2b.py
cat > week2/hw2b.py <<EOF
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
'''EOF
echo Unpacking file week2/averagerandom.py
cat > week2/averagerandom.py <<EOF
import numpy.random as npr

n = 1000
r = sum(npr.random(n)*2-1)/n
print "Average of %.1e random numbers drawn from [-1,1]: %.4f" % (n, r)

'''
user$ python averagerandom.py
Average of 1.0e+03 random numbers drawn from [-1,1]: 0.0166
'''EOF
echo Unpacking file week2/printrandom.py
cat > week2/printrandom.py <<EOF
import random

r = random.random()*2 - 1
print "Random number drawn uniformly from [-1,1]: %.4f" % r

'''
user$ python printrandom.py
Random number drawn uniformly from [-1,1]: 0.1988
'''EOF
echo Unpacking file week2/hw2a.py
cat > week2/hw2a.py <<EOF
import sys
from math import sin

print "Hello, World!"

for r in sys.argv[1:]:
	print "sin(%g)=%g" % (float(r), sin(float(r)))

'''
user$ python hw2a.py 1.4 -0.1 4 99
Hello, World!
sin(1.4)=0.98545
sin(-0.1)=-0.0998334
sin(4)=-0.756802
sin(99)=-0.999207
'''EOF
  
EOF
echo Unpacking file week2/hw2b.py
cat > week2/hw2b.py <<EOF
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
EOF
echo Unpacking file week2/averagerandom.py
cat > week2/averagerandom.py <<EOF
import numpy.random as npr

n = 1000
r = sum(npr.random(n)*2-1)/n
print "Average of %.1e random numbers drawn from [-1,1]: %.4f" % (n, r)

'''
user$ python averagerandom.py
Average of 1.0e+03 random numbers drawn from [-1,1]: 0.0166
'''  
EOF
echo Unpacking file week2/printrandom.py
cat > week2/printrandom.py <<EOF
import random

r = random.random()*2 - 1
print "Random number drawn uniformly from [-1,1]: %.4f" % r

'''
user$ python printrandom.py
Random number drawn uniformly from [-1,1]: 0.1988
'''  
EOF
echo Unpacking file week2/hw2a.py
cat > week2/hw2a.py <<EOF
import sys
from math import sin

print "Hello, World!"

for r in sys.argv[1:]:
	print "sin(%g)=%g" % (float(r), sin(float(r)))

'''
user$ python hw2a.py 1.4 -0.1 4 99
Hello, World!
sin(1.4)=0.98545
sin(-0.1)=-0.0998334
sin(4)=-0.756802
sin(99)=-0.999207
'''  
EOF
