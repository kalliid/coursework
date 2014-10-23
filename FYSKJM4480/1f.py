"""
Program for solving Hartree Fock iteratively.
1. Import radial integral results
2. Set up HF matrix using C = I as initial guess
3. Solve eigevalue problem using numpy.linalg
4. Use resulting eigenvectors to assemble new HF matrix
5. Repeat steps 3 and 4 until convergence is met.
6. Calculate ground state energy from resulting C.
"""

from __future__ import division
from sympy import *
from numpy import *
import pickle, sys

Z = Symbol("Z")

# Read in the radial_integrals from pickled object
with open("radial_integrals.p", "rb") as infile:
    radial_integrals = pickle.load(infile)

class HF:
    """
    Class for solving the Hartree Fock equations iteratively.
    """

    def __init__(self, N, basis, Z_value, first_C='identity'):
        """
        N is the number of particles in the system and basis
        is the single-particle basis for the system.
        """
        # Read in the radial_integrals from pickled object
        with open("radial_integrals.p", "rb") as infile:
            self.radial_integrals = pickle.load(infile)
        
        self.N = N # number of particles in the system
        self.basis = basis # single-particle basis for the system
        self.Z_value = Z_value # atomic number of the atom
        self.n = len(basis) # number of single-particle basis states
        self.ek = array((0,0,0,0,0,0)) # new single-particle energies
        self.E = 0 # energy
        # Set up the first coefficient matrix to be used
        if first_C == 'identity':
            self.C = identity(self.n)
        elif first_C == 'zero':
            self.C = zeros((self.n, self.n))
        elif first_C == 'rand':
            self.C = random.rand(self.n, self.n)
        else:
            print "first_C argument not understood"
            print "Legal values are: 'identity', 'zero', 'rand'"
            sys.exit(1)

        self.h_HF = zeros((self.n, self.n))
        self.assemble_HF_matrix() # set up HF matrix for C = I

    def h_0(self, p, q):
        """
        Takes the integer values of states and returns the 
        asymmetrized twobody matrix element <pq||rs>.
        """
        n1, s1 = self.basis[p]
        n2, s2 = self.basis[q]

        if n1 != n2 or s1 != s2:
            return 0
        else:
            return -Z**2/(2*n1**2)

    def rad(self, n1, n2, n3, n4):
        """
        Returns the radial integral <n1, n2|v|n3, n4>.
        """
        return self.radial_integrals[n1-1, n2-1, n3-1, n4-1]

    def h_1(self, p, q, r, s):
        """
        Takes the integer values of four basis-states and returns
        the asymmetrized twobody matrix element <pq||rs>.
        """
        n1, s1 = self.basis[p]
        n2, s2 = self.basis[q]
        n3, s3 = self.basis[r]
        n4, s4 = self.basis[s]

        if s1 == s2 == s3 == s4:
            return self.rad(n1, n2, n3, n4) - self.rad(n1, n2, n4, n3)
        if s1 == s3 and s2 == s4:
            return self.rad(n1, n2, n3, n4)
        if s1 == s4 and s2 == s3:
            return -self.rad(n1, n2, n4, n3)
        else:
            return 0

    def assemble_HF_matrix(self):
        """
        Assemble the HF matric from the coefficient matrix.
        """
        n, N = self.n, self.N
        C = self.C

        for a in range(n):
            for g in range(n):
                s = self.h_0(a,g)
                for p in range(N):
                    for b in range(n):
                        for d in range(n):
                            s += C[p,b]*C[p,d]*self.h_1(a,b,g,d)

                self.h_HF[a,g] = s.subs(Z, self.Z_value)

    def reorder_coefficients(self):
        ek, C = self.ek, self.C

        # Sort eigenvalues and coefficient matrix using numpy.argsort
        indices = argsort(ek)        
        ek = ek[indices]
        C = C[:, indices]

        self.ek, self.C = ek, C.T

    def calc_energy(self):
        """
        Calculates the ground state energy from the 
        current coefficient matric.
        """
        n, N = self.n, self.N
        C = self.C

        e = 0
        for p in range(N):
         for a in range(n):
           for b in range(n):
             e += C[p,a]*C[p,b]*self.h_0(a,b)
             for q in range(N):
              for c in range(n):
               for d in range(n):
                e += 0.5*C[p,a]*C[q,b]*C[p,c]*C[q,d]*self.h_1(a,b,c,d)

        self.E = e.subs(Z, Z_value).evalf()
        return self.E

    def solve(self, tol=1e-6, max_iters=40):
        iterations = 0
        n, N = self.n, self.N
        Ep = 0

        while iterations < max_iters:
            iterations +=1

            # Find eigenvalues and eigenvector of HF matrix
            self.ek, self.C = linalg.eig(self.h_HF)
            
            # Reorder eigenvalues and eigenvector
            self.reorder_coefficients()

            # Assemble the new HF matrix
            self.assemble_HF_matrix()
            
            # Test tolerance of lowest eigenvalue
            print self.calc_energy()
            error = abs(self.E - Ep)
            if error < tol:
                print "Solver converged after %d iterations." % (iterations)
                return

            Ep = self.E

        print "Solver failed to converge in %d iterations." % (iterations)


N = 4
Z_value = 4
basis = [(1,1), (1,-1), (2,1), (2,-1), (3,1), (3,-1)]

print "Solving with initial guess C=I."
solver = HF(N, basis, Z_value, first_C='identity')
solver.solve(max_iters=100)

print "\n\n\n Solving with initial guess C=0."
solver = HF(N, basis, Z_value, first_C='zero')
solver.solve(max_iters=100)

print "\n\n\n Solving with random initial guess."
solver = HF(N, basis, Z_value, first_C='rand')
solver.solve(max_iters=100)
