import numpy as np

from pylab import normpdf
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import matplotlib.animation as animation

with open("../data/centrallimit.xyz") as infile:
	# Read Header
	N = int(infile.readline())
	infile.readline()

	fig, ax = plt.subplots()

	# histogram our data with numpy
	data = np.zeros(N)
	for i in range(N):
		data[i] = float(infile.readline().split(" ")[-2])

	manbins = np.arange(np.floor(data.min()),np.ceil(data.max()))
	n, bins = np.histogram(data, bins=manbins, density=1)

	# get the corners of the rectangles for the histogram
	left = np.array(bins[:-1])
	right = np.array(bins[1:])
	bottom = np.zeros(len(left))
	top = bottom + n
	nrects = len(left)

	# here comes the tricky part -- we have to set up the vertex and path
	# codes arrays using moveto, lineto and closepoly

	# for each rect: 1 for the MOVETO, 3 for the LINETO, 1 for the
	# CLOSEPOLY; the vert for the closepoly is ignored but we still need
	# it to keep the codes aligned with the vertices
	nverts = nrects*(1+3+1)
	verts = np.zeros((nverts, 2))
	codes = np.ones(nverts, int) * path.Path.LINETO
	codes[0::5] = path.Path.MOVETO
	codes[4::5] = path.Path.CLOSEPOLY
	verts[0::5,0] = left
	verts[0::5,1] = bottom
	verts[1::5,0] = left
	verts[1::5,1] = top
	verts[2::5,0] = right
	verts[2::5,1] = top
	verts[3::5,0] = right
	verts[3::5,1] = bottom

	barpath = path.Path(verts, codes)
	patch = patches.PathPatch(barpath,facecolor='green', edgecolor='yellow', alpha=0.5)
	ax.add_patch(patch)

	ax.set_xlim(-10, 10)
	ax.set_ylim(0, 0.2)

	x = np.linspace(-1,1,1001)
	
	plt.plot(x, normpdf(x, 0, 0.2))

	def animate(i):
		for i in range(N):
			data[i] = float(infile.readline().split(" ")[-2])

		n, bins = np.histogram(data, bins=manbins, density=1)

		top = bottom + n
		verts[1::5,1] = top
		verts[2::5,1] = top
		
	ani = animation.FuncAnimation(fig, animate, 100, repeat=False)
	plt.show()

