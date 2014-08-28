from pylab import *

x = array([10, 20, 68])

y1 = array([4.8664*10**4, 7.0455*10**4, 1.7484*10**5])
y2 = array([7.2422*10**4, 1.15653*10**5, 3.1225*10**5])

plot(x, y1)
# plot(x,ymax)
# show()


#x = [1,2,3,4]
#y = [3,5,7,10] # 10, not 9, so the fit isn't perfect

#fit = polyfit(x,y,1)
#fit_fn = poly1d(fit) # fit_fn is now a function which takes in x and returns an estimate for y

#plot(x,y, 'yo', x, fit_fn(x), '--k')
#xlim(0, 5)
#ylim(0, 12)