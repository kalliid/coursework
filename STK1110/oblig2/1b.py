from scipy.stats import norm

n = 9
sample_percentiles = [100*(i-.375)/(n+.25) for i in range(1,n+1)]
z_percentiles = [norm.ppf(p/100.) for p in sample_percentiles]

m = [36.1, 36.3, 36.4, 36.6, 36.6, 36.6, 36.7, 37.0, 37.1]
k = [36.6, 36.7, 36.8, 36.8, 36.8, 37.0, 37.1, 37.3, 37.4]

import matplotlib.pyplot as plt
plt.subplot(2,1,1)
plt.axis([-2, 2, 36.0, 37.5])
plt.plot(z_percentiles, m, 'mo', ms=8)
plt.ylabel(r'Men', fontsize=14)
plt.grid()
plt.tick_params(\
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off
plt.subplot(2,1,2)
plt.plot(z_percentiles, k, 'ro', ms=8)
plt.axis([-2, 2, 36.5, 37.5])
plt.xlabel(r'z percentile', fontsize=14)
plt.ylabel(r'Women', fontsize=14)
plt.grid()
plt.savefig('probabilityplot.pdf')
plt.show()


