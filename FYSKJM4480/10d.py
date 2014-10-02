from sympy import *
import numpy as np

# J_z = 0

# a = Rational(1,2)*sqrt(6-J_z*(J_z-1))*sqrt(6-(J_z-1)*(J_z-2))
# b = Rational(1,2)*sqrt(6-J_z*(J_z+1))*sqrt(6-(J_z+2)*(J_z+1))

# print a
# print b

# eps = 2
# V = -Rational(4,3)
# W = -1

# A = Matrix([
# 	[-2*eps, 0, sqrt(6)*V, 0, 0],
# 	[0, 3*W-eps, 0, 3*V, 0],
# 	[sqrt(6)*V, 0, 4*W, 0, sqrt(6)*V],
# 	[0, 3*V, 0, 3*W+eps, 0],
# 	[0, 0, sqrt(6)*V, 0, 2*eps]])

# for v in A.eigenvects():
# 	if re(v[0].evalf()) < -7.75:
# 		print "yes"
#  		ground_state = np.array(v[2][0].evalf())

# print ground_state

# ground_state = np.array([38.5804402374521, 0, 10.0586786143627, 0, 1.00000000000000])
ground_state = np.array([3.13263749357984, 0, 3.59806269536288, 0, 1.00000000000000])

ground_state /= sqrt(sum(ground_state**2))

print ground_state
print sum(ground_state**2)