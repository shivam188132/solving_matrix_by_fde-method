import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

n, T_left, T_bottom, T_right, T_top =1000, 75, 0, 50, 100
A = lil_matrix((n*n, n*n))
b = np.zeros(n*n)

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

T_grid = spsolve(A.tocsr(), b)
T2_grid = np.flip(T_grid.reshape(n, n), axis=0)
print(T2_grid)

#heatmap
plt.imshow(T2_grid, cmap='hot', interpolation='nearest')
plt.colorbar(label='Temperature')
plt.title(f'{T_top}°C')
plt.xlabel(f'{T_bottom}°C')
plt.ylabel(f'{T_left}°C')
plt.xticks(np.linspace(0, n-1, 10), np.linspace(1, n, 10).astype(int))
plt.yticks(np.linspace(0, n-1, 10), np.flip(np.linspace(1, n, 10).astype(int)))
plt.show()