import sympy as sp

# Define symbolic variables
x = sp.Symbol('x')

# Define a loss function: L(x) = x^2 - 4x + 4
loss_func = x**2 - 4*x + 4

# Compute the derivative (slope)
derivative = sp.diff(loss_func, x)
print("Derivative:", derivative)  # Output: 2*x - 4

# Evaluate slope at x = 3
slope_at_3 = derivative.subs(x, 3)
print("Slope at x=3:", slope_at_3)  # Output: 2