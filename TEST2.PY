import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import cg
import matplotlib.pyplot as plt

# Parameters
n = 1000
T_left = 75
T_bottom = 0
T_right = 50
T_top = 100

# Create the sparse matrix A and the vector b
A = lil_matrix((n*n, n*n))
b = np.zeros(n*n)

# Fill the matrix A and vector b according to the boundary conditions
for i in range(1, n+1):
    for j in range(1, n+1):
        idx = (i-1) * n + (j-1)
        A[idx, idx] = -4
        if i > 1: 
            A[idx, idx-n] = 1
        else: 
            b[idx] -= T_bottom
        if i < n: 
            A[idx, idx+n] = 1
        else: 
            b[idx] -= T_top
        if j > 1: 
            A[idx, idx-1] = 1
        else: 
            b[idx] -= T_left
        if j < n: 
            A[idx, idx+1] = 1
        else: 
            b[idx] -= T_right

# Convert the matrix to CSR format
A_csr = A.tocsr()

# Solve the sparse linear system using Conjugate Gradient method
T_grid, info = cg(A_csr, b)

# Check for convergence
if info != 0:
    print("Warning: Conjugate Gradient did not converge")

# Reshape the solution to a 2D grid and flip it appropriately
T2_grid = np.flip(T_grid.reshape(n, n), axis=0)

# Plot the temperature distribution heatmap
plt.imshow(T2_grid, cmap='hot', interpolation='nearest')
plt.colorbar(label='Temperature')
plt.title('Temperature Distribution Heatmap')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xticks(np.linspace(0, n-1, 10), np.linspace(1, n, 10).astype(int))
plt.yticks(np.linspace(0, n-1, 10), np.flip(np.linspace(1, n, 10).astype(int)))
plt.show()
