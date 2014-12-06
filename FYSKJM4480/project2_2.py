from numpy import *
from sympy import *
from matplotlib.pyplot import *


g_array = linspace(-1, 1, 1001)
e1_array = []
e2_array = []

for g in g_array:
	H1 = matrix([[2-g , -g/2.,  -g/2., -g/2., -g/2.,     0], 
		        [-g/2.,   4-g,  -g/2., -g/2.,    0., -g/2.],
		        [-g/2., -g/2.,    6-g,     0, -g/2., -g/2.],
				[-g/2., -g/2.,      0,   6-g, -g/2., -g/2.],
				[-g/2.,     0,  -g/2., -g/2.,   8-g, -g/2.],
				[0    , -g/2.,  -g/2., -g/2., -g/2.,  10-g]]) 

	H2 = matrix([[2-g , -g/2.,  -g/2., -g/2., -g/2.], 
		        [-g/2.,   4-g,  -g/2., -g/2.,    0.],
		        [-g/2., -g/2.,    6-g,     0, -g/2.],
				[-g/2., -g/2.,      0,   6-g, -g/2.],
				[-g/2.,     0,  -g/2., -g/2.,   8-g]]) 

	

	u1, v1 = linalg.eig(H1)
	u2, v2 = linalg.eig(H2)

	e1_array.append(min(u1))
	e2_array.append(min(u2))


# plot(g_array, e1_array, linewidth=2.0)
# plot(g_array, e2_array, linewidth=2.0)
plot(g_array, e1_array-(2-g_array), linewidth=2.0)
grid()
xlabel(r'$g$', fontsize=20)
ylabel(r'$E_{gs}$', fontsize=20)
axis([-1,1,-0.4,0.05])
savefig("proj2_correlation.pdf")
#legend(['Exact', '2p2h CI approximation', 'Reference energy'])
show()
	
