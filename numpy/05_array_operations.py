"""
NumPy - Array Operations

NumPy allows mathematical operations directly on arrays.
"""

import numpy as np


a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])


print("a:", a)
print("b:", b)

print("\nAddition:")
print(a + b)

print("\nSubtraction:")
print(a - b)

print("\nMultiplication:")
print(a * b)

print("\nDivision:")
print(a / b)


# Scalar operations

print("\nAdd 10:")
print(a + 10)

print("\nMultiply by 2:")
print(a * 2)

print("\nSquare:")
print(a ** 2)