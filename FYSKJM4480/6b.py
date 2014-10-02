from sympy import *
from sympy.physics.secondquant import *

x = symbols("x")


print latex(expand(sqrt(6 - x*(x+1))*sqrt(6 - (x+1)*(x+2))))