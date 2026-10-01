"""
NumPy - Array Properties

Important properties:
- ndim  -> number of dimensions
- shape -> size of each dimension
- size  -> total number of elements
- dtype -> data type of elements
"""

import numpy as np


array = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


print("Array:")
print(array)

print("\nNumber of dimensions:")
print(array.ndim)

print("\nShape:")
print(array.shape)

print("\nTotal elements:")
print(array.size)

print("\nData type:")
print(array.dtype)