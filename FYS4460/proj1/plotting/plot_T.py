from pylab import *

filename = ["../data/Tfluct_ber_Nc8_T800.dat",
            "../data/Tfluct_and_Nc8_T800.dat",
            "../data/Tfluct_coeff_nsh_Nc8_T800.dat",
            "../data/Tfluct_coeff_non_Nc8_T800.dat"]

slopes = []
color = ['r--', 'b', 'g']

for i in range(3):
	with open(filename[i], 'r') as infile:
		# T = float(infile.readline())

		lines = infile.readlines()
		N = len(lines)
		t = zeros(N); T = zeros(N)

		for j in range(N):
			t[j], T[j] = lines[j].split()

	t = linspace(0,2,2000)
	plot(t, T[1000:3000], color[i], linewidth=2.0)

	print "%e" % sqrt(var(T[1000:3000])/(average(T[1000:3000])**2))

print "%e" % sqrt(2/(3.*2048))

# plot(t, slopes[0]*t, 'r--', linewidth=1.5)
# plot(t, slopes[1]*t, 'b--', linewidth=1.5)
# plot(t, slopes[2]*t, 'k--', linewidth=1.5)

# xlabel('$t$ $[t_0]$', fontsize=22)
# ylabel(r'$\langle r^2 \rangle (t)$  $[\sigma^2/t_0] $', fontsize=22)
# legend(['Nose-Hoover Thermostat $\sigma = 1.23$', 'Berendsen Thermostat $\sigma = 1.20$', 'Andersen Thermostat, $\sigma=0.22$'], 'upper left')
# grid()
plot([-1,-1], [-1, -1], 'k--')
xlabel(r'$t$ $[t_0]$', fontsize=26)
ylabel(r'$T$ $[\epsilon/k_b]$', fontsize=26)
legend(['Berendsen Thermostat, rel. fluct = 9.37e-3', 'Andersen Thermostat, rel. fluct = 1.85e-2', 'Nose-Hoover, rel. fluct = 1.73e-2', 'Theoretical rel. fluct = 1.80e-2'], 'lower right', fontsize=22)
axis([0, 2, 650, 900])
# savefig("../thermostat_diffs.pdf")

ax = gca()
for tick in ax.xaxis.get_major_ticks():
	tick.label.set_fontsize(18) 
for tick in ax.yaxis.get_major_ticks():
	tick.label.set_fontsize(18) 


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

