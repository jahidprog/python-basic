"""
Topic: Solving Systems of Linear Equations (Ax = b)
Example system:
  2x + y = 8
  3x - 2y = 5
"""
import numpy as np

# Coefficient matrix A
A = np.array([[2, 1], 
              [3, -2]])

# Right-hand side vector b
b = np.array([8, 5])

# Solve for x (where x contains [x, y])
solution = np.linalg.solve(A, b)

# Verification: A @ solution should equal b
verification = np.allclose(A @ solution, b)

print("--- Solving Linear Equations (Ax = b) ---")
print(f"Solution vector [x, y]: {solution}")
print(f"Verification (A @ x == b): {verification}")
