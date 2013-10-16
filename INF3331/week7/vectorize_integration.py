import numpy as np

def trapez(f, a, b, n):
    '''Integrate f(x) on x in [a,b] using trapezoidal rule
    with a mesh of n cells.'''

    h = (b-a)/float(n)
    s =  h/2.*(f(a) + f(b))
    for i in range(1, n):
        s += h * f(a+i*h)

    return s

def trapez_vectorized(f, a, b, n):
    '''A vectorized version of the trapezoidal function.'''

    x = np.linspace(a, b, n+1)
    h = x[1]-x[0]
    y = h*f(x)
    y[0] /= 2.
    y[-1] /= 2.

    return np.sum(y)

if __name__ == '__main__':
    # Test the difference in run-times between the functions
    import numpy as np
    import timeit

    # Integrands to be tested
    f_1 = lambda x: 1+x
    f_2 = lambda x: np.exp(-x*x)*np.log(x + x*np.sin(x))

    # The setup is used by timeit, but does not contribute to the final time
    setup = "from __main__ import f_1, f_2, trapez, trapez_vectorized"
    
    def time_function(integrator, f, a, b, n):
        # Define the command to be timed
        command = "%s(%s, %g, %g, %d)" % (integrator, f, a, b, n)
        # Run and time the command
        t = timeit.timeit(command, setup=setup, number = 1)
        return t

    for f in ['f_1', 'f_2']:
        print "\nTimes for %s\n  n  %8s%14s" % (f, 'loop', 'vectorized')
        for n in [1e3, 1e4, 1e5, 1e6, 1e7]:
            t1 = time_function('trapez', f, 1, 5, n)
            t2 = time_function('trapez_vectorized', f, 1, 5, n)
            print "%5.0e%10.2e%11.2e"  % (n, t1, t2)

'''
user$ python vectorized_integration.py

Times for f_1
  n      loop    vectorized
1e+03  4.66e-04   1.15e-04
1e+04  3.41e-03   3.02e-04
1e+05  3.69e-02   2.71e-03
1e+06  3.64e-01   4.24e-02
1e+07  3.67e+00   4.32e-01

Times for f_2
  n      loop    vectorized
1e+03  9.99e-03   2.18e-04
1e+04  9.81e-02   1.39e-03
1e+05  9.86e-01   1.27e-02
1e+06  9.99e+00   1.69e-01
1e+07  1.00e+02   2.02e+00
'''