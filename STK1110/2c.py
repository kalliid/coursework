from numpy import random, sqrt, zeros

# Number of data set
N = 1000
# Number of samples per set
n = 14
# Number of experiments
m = 100
# Parameters
mu = 14.5
sigma = 1

# Conduct experiment
results = zeros(m)
for i in range(m):
    s = 0
    for j in xrange(N):
        # Draw n random numbers
        x = random.normal(mu, sigma, n)
        # Calculate interval
        x_avrg = sum(x)/n
        S = sqrt(sum((x-x_avrg)**2)/(n-1))
        lower = x_avrg - 1.96*S/sqrt(n)
        upper = x_avrg + 1.96*S/sqrt(n)
        # Check if interval contains mu
        if lower <= mu and upper >= mu:
            s += 1
    results[i] = s

# Plot results as a histogram
import matplotlib.pyplot as plt
plt.hist(results, histtype='stepfilled', color='b')
plt.axis([900,960,0,30])
plt.xlabel(r"Number of intervals containing $\mu$", fontsize=16)
plt.ylabel(r"Occurances", fontsize=16)
plt.grid()
plt.savefig('2c.pdf')
plt.show()
