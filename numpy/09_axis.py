"""
NumPy - Axis

For a 2D array:

axis=0 -> operate down the rows / column-wise
axis=1 -> operate across the columns / row-wise
"""

import numpy as np


matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])


print("Matrix:")
print(matrix)


print("\nTotal:")
print(np.sum(matrix))


print("\nColumn-wise sum (axis=0):")
print(np.sum(matrix, axis=0))


print("\nRow-wise sum (axis=1):")
print(np.sum(matrix, axis=1))


print("\nColumn-wise mean:")
print(np.mean(matrix, axis=0))


print("\nRow-wise mean:")
print(np.mean(matrix, axis=1))