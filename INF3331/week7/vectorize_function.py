import numpy as np

def initial_condition(x):
    y = np.empty(np.shape(x))
    y.fill(3.0)
    return y

if __name__ == '__main__':
    shape = (5, 3)
    x = np.random.random(shape)
    y = initial_condition(x)
    print y.shape
    print y
    print initial_condition(7)

'''
user$ vectorize_function.py
(5, 3)
[[ 3.  3.  3.]
 [ 3.  3.  3.]
 [ 3.  3.  3.]
 [ 3.  3.  3.]
 [ 3.  3.  3.]]
3.0
'''