import numpy as np

# Constants and parameters
l = 4  # Number of segments (excluding boundaries)
T_left = 100.0  # Left boundary condition
T_right = 50.0  # Right boundary condition
initial_bc = np.zeros(l)
Time_steps = 10  # Initial temperatures for T1^0 to T4^0

# Parameters for the explicit finite difference method
α= 1.0  # Diffusion coefficient
Δt = 0.1  # Time step
Δx = 1.0  # Spatial step
#λ = α* Δt / (Δx ** 2)  # Stability parameter
λ = 0.021

# Function to solve for temperatures at each time step
def solve_temperature(T_prev):
    T_next = np.zeros_like(T_prev)
    T_next[0] = λ * T_prev[1] + (1 - 2 * λ) * T_prev[0] + λ * T_left
    for i in range(1, l-1):
        T_next[i] = λ * (T_prev[i+1] + T_prev[i-1]) + (1 - 2 * λ) * T_prev[i]
    T_next[l-1] = λ * T_prev[l-2] + (1 - 2 * λ) * T_prev[l-1] + λ * T_right
    return T_next

# Initialize the temperature array
T = initial_bc

# Time steps
  # Number of time steps to compute
print(f"Initial temperatures: {T}")

# Compute temperatures for each time step
for step in range(Time_steps):
    T = np.round(solve_temperature(T), 3)
    print(f"Time interval {step+1}: {T}")
