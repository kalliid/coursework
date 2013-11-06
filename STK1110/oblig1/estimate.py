from numpy.random import random
from numpy import zeros

# Number of samples per trial
n = 20
# Number of trials
N = 1000

results = zeros((N,2))
for i in range(N):
	# Draws n random numbers uniformly from [0,1)
	x = random(n)
	# Calculate estimators
	mom = 2*sum(x)/len(x)
	mod = (n+1)/n * max(x)
	# Store results
	results[i,0] = mom
	results[i,1] = mod

# Plot results as a histogram
import matplotlib.pyplot as plt
plt.hist(results[:,0], bins=30, histtype='stepfilled',
			   color='b', label=r'$\hat{\theta}_{\rm mom}$')
plt.hist(results[:,1], bins=30, histtype='stepfilled',
			   color='g', alpha=0.5, label=r'$\hat{\theta}_{\rm mod}$')
plt.xlabel(r"Estimated value of $\theta$", fontsize=16)
plt.ylabel(r"Occurances", fontsize=16)
plt.legend(prop={'size':18})
plt.grid()
#plt.savefig('estimators_hist_n%s.pdf' % str(n))
plt.show()

