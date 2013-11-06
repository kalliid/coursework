import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.array([23.1, 32.8, 31.8, 32.0, 30.4, 24.0, 39.5, 24.2, 52.5, 
37.9, 30.5, 25.1, 12.4, 35.1, 31.5, 21.1, 27.6, 27.6])

y = np.array([10.5, 16.7, 18.2, 17.0, 16.3, 10.5, 23.1, 12.4, 24.9,
22.8, 14.1, 12.9, 8.80, 17.4, 14.9, 10.5, 10.5, 16.1])

def f(x):
    return 0.28 + 0.5056*x

l = np.linspace(min(x), max(x),1001)
fitted = f(l)

def scatter():
    plt.plot(x,y,'o')
    plt.grid()
    plt.xlabel(r'Amount of snow, $x$', fontsize=16)
    plt.ylabel(r'Water-level, $y$', fontsize=16)

# Plot observations in scatterplot
scatter()
plt.savefig('scatter.pdf')
plt.show()

# Plot observations with fitted line
scatter()
plt.plot(l,f(l))
plt.savefig('fittedreg.pdf')
plt.show()

# Calculate and plot residuals vs predictor variable x
residuals = y-f(x)
plt.plot(x,residuals,'ro')
plt.grid()
plt.xlabel(r'$x$', fontsize=16)
plt.ylabel(r'residuals, $y_i-\hat{y}_i$', fontsize=16)
plt.savefig('residuals.pdf')
plt.show()

SSE = np.sum(residuals**2)
print SSE
print np.sum(y**2) - 0.28*np.sum(y) - 0.5056*sum(x*y)


# Calculate and plot probabiliy plot
n = len(x)
sample_percentiles = [100*(i-.375)/(n+.25) for i in range(1,n+1)]
z_percentiles = [norm.ppf(p/100.) for p in sample_percentiles]

#plt.axis([-2, 2, 0, 60])

plt.plot(z_percentiles, np.sort(residuals), 'mo')
plt.xlabel(r'z percentile', fontsize=16)
plt.ylabel(r'Residuals', fontsize=16)
plt.grid()
plt.savefig('probabilityplot2.pdf')
plt.show()


