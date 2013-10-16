from vec3d_ext import Vec3D

u = Vec3D(1, 0, 0)
v = Vec3D(0, -0.5, 2)

a = 1.5
b = 1
c = 2.5

print "Test vectors:"
print "u: ", u
print "v: ", v

print "\nTesting addition:"
print "u+v: ", u+v # Normal vector addition 
print "a+v: ", a+v # Reverse scalar addition
print "v+a: ", v+a # Forward scalar addition
print "b+u: ", b+u # Test for integer (instead of float)

print "\nTesting subtraction:"
print "u-v: ", u-v # Normal vector subtraction 
print "v-a: ", v-a # Forward scalar subtraction
print "a-v: ", a-v # Reverse scalar subtraction

print "\nTesting multiplication"
print "u*v: ", u*v # Normal dot product
print "c*u: ", c*u # Reverse multiplication by scalar
print "u*c: ", u*c # Forward multiplication by scalar

print "\nTesting division by scalar, and error-handling"
print "u/c: ", u/c # Forward division by scalar

print "\nTesting scalar divided by vector"
try:
    print c/u
except TypeError as error:
    print "c/u: TypeError:", error

print "\nTesting vector divided by vector"
try: 
    print u/v
except TypeError as error:
    print "u/v: TypeError:", error

'''
user$ python vec3d_ext_example.py
Test vectors:
u:  (1, 0, 0)
v:  (0, -0.5, 2)

Testing addition:
u+v:  (1, -0.5, 2)
a+v:  (1.5, 1, 3.5)
v+a:  (1.5, 1, 3.5)
b+u:  (2, 1, 1)

Testing subtraction:
u-v:  (1, 0.5, -2)
v-a:  (-1.5, -2, 0.5)
a-v:  (1.5, 2.0, -0.5)

Testing multiplication
u*v:  0.0
c*u:  (2.5, 0, 0)
u*c:  (2.5, 0, 0)

Testing division by scalar, and error-handling
u/c:  (0.4, 0, 0)

Testing scalar divided by vector
c/u: TypeError: Scalar divided by vector is not defined

Testing vector divided by vector
u/v: TypeError: Vector divided by vector is not defined
'''