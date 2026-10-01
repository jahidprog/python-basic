"""
NumPy - Array Slicing

Slicing allows us to extract parts of an array.
"""

import numpy as np


numbers = np.array([10, 20, 30, 40, 50, 60])


print("Array:")
print(numbers)

print("\nFirst three:")
print(numbers[:3])

print("\nFrom index 2:")
print(numbers[2:])

print("\nIndex 1 to 4:")
print(numbers[1:5])

print("\nEvery second element:")
print(numbers[::2])

print("\nReversed:")
print(numbers[::-1])