from numpy import *

# Measured values
x = array([13.0, 15.0, 14.7, 13.3, 16.3, 15.8, 13.2, 15.6, 13.9, 13.4, 14.1, 15.4, 14.7, 12.7])

# Calculate the average
n = len(x)
x_avrg = sum(x)/n

# Calculate the sample variance
S2 = sum((x-x_avrg)**2)/(n-1)

# Calculate the sample standard deviation
S = sqrt(S2)

print "average       =", x_avrg
print "variance      =", S2
print "stndr dev     =", S
print "1.96S/sqrt(n) =", 1.96*S/sqrt(n)
print "lower         =", x_avrg - 1.96*S/sqrt(n)
print "upper		 =", x_avrg + 1.96*S/sqrt(n)


mu = 14.5
sigma = 1
s = random.normal(mu, sigma, (1000, 14))

for i in range(1000):
	x = s[0]
	n = len(x)
	x_avrg = sum(x)/n
	S = sqrt(sum((x-x_avrg)**2)/(n-1))

	lower = x_avrg - 1.96*S/sqrt(n)
	upper = x_avrg + 1.96*S/sqrt(n)
