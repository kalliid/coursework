from pylab import *

filename = ["../data/Tfluct_ber_Nc8_T800.dat",
		    "../data/Tfluct_and_Nc8_T800.dat",
		    "../data/Tfluct_nsh_Nc8_T800.dat"]

slopes = []
color = ['r', 'b', 'k']

for i in range(3):
	with open(filename[i], 'r') as infile:
		T = float(infile.readline())

		lines = infile.readlines()
		N = len(lines)
		T = zeros(N)

		for j in range(N):
			T[j] = lines[j]

	dt = 1e-3
	t = array([k*dt for k in range(N)])
	plot(t, T, color[i], linewidth=2.0)

	print var(T)/(average(T)**2)

print 2/(3.*2048)
# plot(t, slopes[0]*t, 'r--', linewidth=1.5)
# plot(t, slopes[1]*t, 'b--', linewidth=1.5)
# plot(t, slopes[2]*t, 'k--', linewidth=1.5)

# xlabel('$t$ $[t_0]$', fontsize=22)
# ylabel(r'$\langle r^2 \rangle (t)$  $[\sigma^2/t_0] $', fontsize=22)
# legend(['Nose-Hoover Thermostat $\sigma = 1.23$', 'Berendsen Thermostat $\sigma = 1.20$', 'Andersen Thermostat, $\sigma=0.22$'], 'upper left')
# grid()
xlabel(r'$t$ $[t_0]$', fontsize=22)
ylabel(r'$T$ $[\epsilon/k_b]$', fontsize=22)
legend(['Berendsen Thermostat', 'Andersen Thermostat', 'Nose-Hoover', 'Heat Bath'], 'lower right', fontsize=22)
axis([0, max(t)	, 650, 900])
# savefig("../thermostat_diffs.pdf")

grid()
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

