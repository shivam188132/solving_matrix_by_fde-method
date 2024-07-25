import numpy as np

# Constants and parameters
l = 4  # Number of segments (excluding boundaries)
T_left = 100.0  # Left boundary condition
T_right = 50.0  # Right boundary condition
initial_T = np.zeros(l)  # Initial temperatures for T1^0 to T4^0

# Parameters for the explicit finite difference method
alpha = 1.0  # Diffusion coefficient
delta_t = 0.1  # Time step
delta_x = 1.0  # Spatial step
#lambda_ = alpha * delta_t / (delta_x ** 2)  # Stability parameter
lambda_ = 0.021

# Function to solve for temperatures at each time step
def solve_temperature(T_prev):
    T_next = np.zeros_like(T_prev)
    T_next[0] = lambda_ * T_prev[1] + (1 - 2 * lambda_) * T_prev[0] + lambda_ * T_left
    for i in range(1, l-1):
        T_next[i] = lambda_ * (T_prev[i+1] + T_prev[i-1]) + (1 - 2 * lambda_) * T_prev[i]
    T_next[l-1] = lambda_ * T_prev[l-2] + (1 - 2 * lambda_) * T_prev[l-1] + lambda_ * T_right
    return T_next

# Initialize the temperature array
T = initial_T

# Time steps
num_steps = 10  # Number of time steps to compute
print(f"Initial temperatures: {T}")

# Compute temperatures for each time step
for step in range(num_steps):
    T = np.round(solve_temperature(T), 3)
    print(f"Time step {step+1}: {T}")
