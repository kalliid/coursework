from pylab import *

filename = ["../data/diffusion_coeff_ber_Nc8_T800.dat", 
	 		"../data/diffusion_coeff_nsh_Nc8_T800.dat", 
	 		"../data/diffusion_coeff_non_Nc8_T800.dat",
	 		"../data/diffusion_coeff_and_Nc8_T800.dat"]

slopes = []
color = ['r', 'b', 'g', 'k']

for i in range(4):
	with open(filename[i], 'r') as infile:
		# int(infile.readline())
		# float(infile.readline())

		lines = infile.readlines()
		N = len(lines)
		t = zeros(N); r2 = zeros(N)

		for j in range(N):
			t[j], r2[j] = lines[j].split()

	x = t[:,np.newaxis]
	y = r2
	a, _, _, _ = np.linalg.lstsq(x, y)
	print "Sigma: ", a/6.
	slopes.append(a)
	
	plot(t, r2, color[i], linewidth=2.5)

# plot(t, slopes[0]*t, 'r--', linewidth=1.5)
# plot(t, slopes[1]*t, 'b--', linewidth=1.5)
# plot(t, slopes[2]*t, 'g--', linewidth=1.5)

xlabel('$t$ $[t_0]$', fontsize=26)
ylabel(r'$\langle r^2 \rangle (t)$  $[\sigma^2] $', fontsize=26)
legend(['Nose-Hoover $D = 0.19$ $[\sigma^2/t_0]$', 'Berendsen $D = 0.19$ $[\sigma^2/t_0]$', 'Micro-cannonical, $D = 0.19$ $[\sigma^2/t_0]$', 'Andersen, $D=0.11$ $[\sigma^2/t_0]$'], 'upper left', fontsize=22)
grid()

ax = gca()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(18) 
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(18) 

show()



# dt = 1e-3
# t = array([i*dt for i in range(N)])

# # a, b = polyfit(t, r2, 1)
# # print a
# # print b

# x = t[:,np.newaxis]
# y = r2
# a, _, _, _ = np.linalg.lstsq(x, y)
# print a

# plot(t, r2, linewidth=2.0)
# plot(t, a*t, '--', linewidth=2.0)
# xlabel(r'$t$ [$t_0$]', fontsize=22)
# ylabel(r'$\langle r^2\rangle(t)$ [$\sigma^2/t_0$]', fontsize=22)
# axis([0, dt*N, 0, max(r2)*1.1])
# grid()
# legend(['Measurements', 'Linear fit'], 'upper left', fontsize=14)
# show()

