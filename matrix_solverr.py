import numpy as np
from scipy.linalg import solve

n, T_left, T_bottom, T_right, T_top = 3, 75, 0, 50, 100
A, b = np.zeros((n*n, n*n)), np.zeros(n*n)

for i in range(1, n+1):
    for j in range(1, n+1):
        idx = (i-1) * n + (j-1)
        A[idx, idx] = -4
        if i > 1: A[idx, idx-n] = 1
        else: b[idx] -= T_bottom
        if i < n: A[idx, idx+n] = 1
        else: b[idx] -= T_top
        if j > 1: A[idx, idx-1] = 1
        else: b[idx] -= T_left
        if j < n: A[idx, idx+1] = 1
        else: b[idx] -= T_right

T_grid = solve(A, b).reshape((n, n))
print("Temperature distribution:\n", T_grid)