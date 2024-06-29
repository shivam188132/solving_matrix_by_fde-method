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
print(type(T_grid))
print(T_grid)

# Verification step
# Create a function to plug the solution back into the original equations
def verify_solution(T_grid, n):
    verified = True
    for i in range(1, n+1):
        for j in range(1, n+1):
            Tij = T_grid[i-1, j-1]
            Ti_plus_1_j = T_grid[i, j-1] if i < n else T_top
            Ti_minus_1_j = T_grid[i-2, j-1] if i > 1 else T_bottom
            Ti_j_plus_1 = T_grid[i-1, j] if j < n else T_right
            Ti_j_minus_1 = T_grid[i-1, j-2] if j > 1 else T_left

            equation = Ti_plus_1_j + Ti_minus_1_j + Ti_j_plus_1 + Ti_j_minus_1 - 4 * Tij
            if not np.isclose(equation, 0):
                print(f"Verification failed at (i, j) = ({i}, {j}): {equation}")
                verified = False
    return verified

if verify_solution(T_grid, n):
    print("All equations verified successfully.")
else:
    print("There was an error in the solution.")