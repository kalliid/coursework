from sympy import *
from sympy.physics.secondquant import *

p_1, p_2, p_3, p_4 = symbols('p_1 p_2 p_3 p_4', above_fermi=True)
m_1, m_2, m_3, m_4 = symbols('m_1 m_2 m_3 m_4', above_fermi=True)




Jp = Fd(p_1)*F(m_1) + Fd(p_2)*F(m_2) + Fd(p_3)*F(m_3) + Fd(p_4)*F(m_4)

print latex(simplify(Jp*Jp*Fd(m_1)*Fd(m_2)*Fd(m_3)*Fd(m_4)))