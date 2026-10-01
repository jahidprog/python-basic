"""
NumPy - Matrix Operations

Matrix operations are fundamental in Machine Learning.
"""

import numpy as np


A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])


print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)


# Element-wise multiplication
print("\nElement-wise multiplication:")
print(A * B)


# Matrix multiplication
print("\nMatrix multiplication:")
print(A @ B)


# Transpose
print("\nTranspose of A:")
print(A.T)