from vec3d import Vec3D

if __name__=="__main__":
    # Example run
    u = Vec3D(1, 0, 0)
    u = eval(repr(u))  # Should leave u unchanged
    v = Vec3D(0, 1, 0)
    v[2] = 2.5
    print "str(u)  ", str(u)
    print "u.len() ", u.len()
    print "u[1]    ", u[1]
    print "print v ", v
    print "u**v    ", u**v
    print "u+v     ", u+v
    print "u-v     ", u-v
    print "u*v     ", u*v


'''
user$ python vec3d.py
str(u)   (1, 0, 0)
u.len()  1.0
u[1]     0
print v  (0, 1, 2.5)
u**v     (0, -2.5, 1)
u+v      (1, 1, 2.5)
u-v      (1, -1, -2.5)
u*v      0.0
'''