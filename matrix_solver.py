import numpy as np
from scipy.linalg import solve

# Define the grid size (3x3 internal points)
n = 3

# Initialize the matrix A and vector b
A = np.zeros((n*n, n*n))
b = np.zeros(n*n)

# Define the boundary values
T_left = 75
T_bottom = 0
T_right = 50
T_top = 100

# Function to convert (i, j) to index in the linear system
def index(i, j, n):
    return (i - 1) * n + (j - 1)

# Fill the matrix A and vector b
for i in range(1, n+1):
    for j in range(1, n+1):
        idx = index(i, j, n)
        
        A[idx, idx] = -4
        
        if i > 1:  # T_(i-1,j)
            A[idx, index(i-1, j, n)] = 1
        else:  # Bottom boundary
            b[idx] -= T_bottom

        if i < n:  # T_(i+1,j)
            A[idx, index(i+1, j, n)] = 1
        else:  # Top boundary
            b[idx] -= T_top

        if j > 1:  # T_(i,j-1)
            A[idx, index(i, j-1, n)] = 1
        else:  # Left boundary
            b[idx] -= T_left

        if j < n:  # T_(i,j+1)
            A[idx, index(i, j+1, n)] = 1
        else:  # Right boundary
            b[idx] -= T_right

# Solve the linear system
T = solve(A, b)

# Reshape the solution to a 2D array
T_grid = T.reshape((n, n))

print("Temperature distribution:")
print(T_grid)
