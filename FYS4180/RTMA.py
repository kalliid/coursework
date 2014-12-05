# -*- coding: utf-8 -*-

'''
Ray Transfer Matrix Analaysis of laser beams
(aka ABCD Matrix Analysis)
Assumes gaussian beam profiles and narrow lenses.
'''

from numpy import *
from matplotlib.pyplot import *
from scipy.optimize import leastsq

class TMA:
	def __init__(self, q0, lmbda, n):
		self.q, self.lmbda, self.n = q0, lmbda, n
		self.M = matrix([[1,0],[0,1]])

	def beam_through_air(self, x):
		'''
		Calculate the change in q of a beam
		travelling through air.
		    x - array of spatial points
		'''
		dx = x - x[0]
		L = x[-1] - x[0]
		W = zeros(len(x))
		
		lmbda, n, q0 = self.lmbda, self.n, self.q

		for i in range(len(x)):
			q = q0 + dx[i]
			W[i] = sqrt(-lmbda/(pi*n*(1/q).imag))

		self.n = n
		self.M = matrix([[1, L], [0, 1]])
		self.last_q = q
		return W

	def beam_through_lens(self, f):
		'''
		Calculate the change in a beam that passes 
		through a narrow lens.
			q0 - The q-value before the lens
			L  - The position of the lens
			f  - The focal length of the lens.
		'''
		M_lens = matrix([[1, 0], [-1./f, 1]])
		M = M_lens*self.M
		q0 = self.q
		self.q = (q0*M[0,0] + M[0,1])/(q0*M[1,0] + M[1,1])
		self.M = M
			
	def plot_beam(self, x, W):
		N = len(x)
		for i in range(N):
			plot(x[i], W[i], 'b', linewidth=2)
			
			if i != N-1:
				axvline(x=x[i][-1], ymin=0, ymax=1, 
	            	    linewidth=2, color='r', linestyle="--")

		grid()
		xlabel(r'$x$', fontsize=22)
		ylabel(r'$W$', fontsize=22)

class least_squares_analysis:
	def __init__(self, x, W):
		self.x, self.W = x, W

	def error(self, R0):
		w0 = self.W[0]
		q0 = 1./(1./R0 - 1j*lmbda/(pi*n*w0*w0))
		M = matrix([[1,0],[0,1]])
		W, M = beam_through_air(q0, self.x, M)
		residuals = self.W - W
		return sqrt(sum(residuals**2))
