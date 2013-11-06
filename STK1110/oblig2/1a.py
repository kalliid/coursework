m = [36.1, 36.3, 36.4, 36.6, 36.6, 36.6, 36.7, 37.0, 37.1]
k = [36.6, 36.7, 36.8, 36.8, 36.8, 37.0, 37.1, 37.3, 37.4]

import matplotlib.pyplot as plt
from scipy.stats import norm, normaltest, skewtest


ax = plt.axes()
ax.boxplot([m, k], 0)
ax.set_xticklabels(['Men', 'Women'], fontsize=16)
plt.ylabel(r'Measured temperature ($^\circ C$)', fontsize=16)
plt.grid()
#plt.savefig('boxplot.pdf')
#plt.show()

print normaltest(m)