eps, C = eig(h_HF)

# Sort eigenvalues and coefficient matrix using numpy.argsort
indices = argsort(ek)        
ek = ek[indices]
C = C[:, indices]
C = C.T