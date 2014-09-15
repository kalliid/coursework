from sympy import *
from sympy.physics.secondquant import *

a_1, a_2, a_3, b_1, b_2, b_3 = symbols('a_1 a_2 a_3 b_1 b_2 b_3', above_fermi=True)
i, j, k, l = symbols('i,j,k,l', above_fermi=True)

print latex(wicks(F(a_3)*F(a_2)*F(a_1)*Fd(i)*Fd(j)*F(l)*F(k)*Fd(b_1)*Fd(b_2)*Fd(b_3), keep_only_fully_contracted=True))


# a_1, a_2, a_3, b_1, b_2, b_3 = symbols('a_1, a_2, a_3, b_1, b_2, b_3')

# print latex(Fd(a_1)*F(a_2)*Fd(a_3))

# print latex(wicks(Fd(a_1)*F(a_2)*Fd(b_1)*F(b_2), keep_only_fully_contracted=True))
# '''

'''
a,c,e = symbols('a,c,e,', above_fermi=True)
b,d,f = symbols('b,d,f,', above_fermi=True)

res = wicks(F(a)*Fd(b)*F(c)*Fd(d)*F(e)*Fd(f), keep_only_fully_contracted=True)

print latex(res)
'''

# # # print latex(Fd(a)*F(b)*Fd(c)*F(d)*Fd(e)*F(f))
# # # print simplify((wicks(Fd(a)*F(b)*Fd(c)*F(d)*Fd(e)*F(f), keep_only_fully_contracted=True)))

# #i = symbols('i', below_fermi=True, cls=Dummy)
# #a = symbols('a', above_fermi=True, cls=Dummy)
# # t_ai = AntiSymmetricTensor('t', (a,), (i,))
# # ai = NO(Fd(a)*F(i))
# #i, j = symbols('i,j', below_fermi=True, cls=Dummy)
# #a, b = symbols('a,b', above_fermi=True, cls=Dummy)
# # t_abij = AntiSymmetricTensor('t', (a, b), (i, j))
# # abji = NO(Fd(a)*Fd(b)*F(j)*F(i))

# #print wicks(Fd(a)*Fd(b)*F(j)*F(i), keep_only_fully_contracted=True)

# above_fermi=True