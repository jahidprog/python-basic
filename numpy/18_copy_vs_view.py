"""
NumPy - Copy vs View

A view shares the same underlying data.
A copy creates independent data.
"""

import numpy as np


original = np.array([10, 20, 30, 40])

print("Original:")
print(original)


# View
view = original.view()

view[0] = 999

print("\nAfter changing view:")
print("Original:", original)
print("View:", view)


# Copy
original = np.array([10, 20, 30, 40])

copy = original.copy()

copy[0] = 999

print("\nAfter changing copy:")
print("Original:", original)
print("Copy:", copy)