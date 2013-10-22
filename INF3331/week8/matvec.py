import numpy as np

A = np.array([[1, 2, 3], [4, 5, 7], [6, 8, 10]], float)
b = np.array([-3, -2, -1], float)

print "A*b gives wrong result: \n", A*b
print "np.dot(A,b) gives right result: \n", np.dot(A,b)
print "A.dot(b) gives right result: \n", A.dot(b)

'''
user$ python matvec.py
A*b gives wrong result: 
[[ -3.  -4.  -3.]
 [-12. -10.  -7.]
 [-18. -16. -10.]]
np.dot(A,b) gives right result: 
[-10. -29. -44.]
A.dot(b) gives right result: 
[-10. -29. -44.]
'''