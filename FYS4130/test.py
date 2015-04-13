from pylab import * 

x = linspace(0,2*pi,1001)

subplot(2,2,1)
plot(x, sin(x))
subplot(2,2,2)
plot(x, cos(x))
subplot(2,2,4)
plot(x, x**2)
show()


def normalized_cross_corr(a, v):
	a = (a - mean(a)) / std(a) 
	v = (v - mean(v)) / std(v)

	return np.correlate(a, v)