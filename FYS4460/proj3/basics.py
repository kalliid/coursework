from pylab import *
from scipy.ndimage import measurements
# from walk import walk



# Generate perc matrix
L = 100
r = rand(L, L)
p = 0.6
z = r < p

imshow(z, origin='lower', cmap='Greys', interpolation='nearest')
show()

lw, num = measurements.label(z)
# b = arange(lw.max() + 1)
# shuffle(b)
# shuffledLw = b[lw]
# imshow(shuffledLw, origin='lower', interpolation='nearest')
# colorbar()
# show()

area = measurements.sum(z, lw, index=arange(lw.max() + 1))
areaImg = area[lw]
im3 = imshow(areaImg, origin='lower', interpolation='nearest')
colorbar()
title("Clusters by area")


sliced = measurements.find_objects(areaImg == areaImg.max())
if(len(sliced) > 0):
    sliceX = sliced[0][1]
    sliceY = sliced[0][0]

    plotxlim=im3.axes.get_xlim()
    plotylim=im3.axes.get_ylim()
    plot([sliceX.start, sliceX.start, sliceX.stop, sliceX.stop, sliceX.start], \
                      [sliceY.start, sliceY.stop, sliceY.stop, sliceY.start, sliceY.start], \
                      color="red")
    xlim(plotxlim)
    ylim(plotylim)

show()