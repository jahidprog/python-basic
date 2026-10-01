"""
NumPy - Transpose

Transpose changes rows into columns
and columns into rows.
"""

import numpy as np


matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])


print("Original:")
print(matrix)

print("\nOriginal shape:")
print(matrix.shape)


transposed = matrix.T

print("\nTransposed:")
print(transposed)

print("\nTransposed shape:")
print(transposed.shape)