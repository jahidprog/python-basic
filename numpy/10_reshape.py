"""
NumPy - Reshape

reshape() changes the structure/shape of an array
without changing the number of elements.
"""

import numpy as np


numbers = np.arange(1, 7)

print("Original:")
print(numbers)

print("\nOriginal shape:")
print(numbers.shape)


matrix = numbers.reshape(2, 3)

print("\nReshaped:")
print(matrix)

print("\nNew shape:")
print(matrix.shape)


# Another example

array = np.arange(12)

print("\n12 elements:")
print(array)

print("\n3 x 4:")
print(array.reshape(3, 4))

print("\n4 x 3:")
print(array.reshape(4, 3))