"""
NumPy - Array Indexing

Access individual elements using indexes.
"""

import numpy as np


# 1D array
numbers = np.array([10, 20, 30, 40, 50])

print("Array:")
print(numbers)

print("\nFirst element:")
print(numbers[0])

print("\nThird element:")
print(numbers[2])

print("\nLast element:")
print(numbers[-1])


# 2D array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("\nMatrix:")
print(matrix)

print("\nFirst row:")
print(matrix[0])

print("\nElement at row 2, column 3:")
print(matrix[1, 2]) 