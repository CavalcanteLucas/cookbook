# Performing Matrix and Linear Algebra Calculations

import numpy as np
m = np.matrix([[1,-2,3], [0,4,5], [7,8,-9]])
m

# Return transpose
m.T

# Return inverse
m.I

# Create a vector and multiply
v = np.matrix([[2], [3], [4]])
v
m*v


import numpy.linalg

# Determinant
numpy.linalg.det(m)

# Eigenvalues
numpy.linalg.eigvals(m)

# Solve for x in mx = v
x = numpy.linalg.solve(m, v)
x
m * x
v