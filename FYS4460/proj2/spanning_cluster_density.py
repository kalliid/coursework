from pylab import *
from scipy.ndimage import measurements


def spanning_cluster_density(perc_matrix):
	# Calculate and return the spanning cluster density
	total_area = 0
	Lx, Ly = perc_matrix.shape
	Lmin = min(Lx, Ly)


	lw, num = measurements.label(perc_matrix)
	labels = arange(lw.max()+1)

	area = measurements.sum(perc_matrix, lw, index=labels)
	
	for l in labels:
		if area[l] > Lmin:
		 	sliced = measurements.find_objects(lw == l)
		 	sliceX = sliced[0][1]
		 	sliceY = sliced[0][0]

		 	width = sliceX.stop - sliceX.start
		 	height = sliceY.stop - sliceY.start

		 	if width == Lx or height == Ly:
		 		total_area += area[l]

	return total_area/Lx/Ly

if __name__ == '__main__':
	# Generate perc matrix
	L = 100
	r = rand(L, L)
	p = 0.6
	z = r < p

	print spanning_cluster_density(z)

