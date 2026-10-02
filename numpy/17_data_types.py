"""
NumPy - Data Types

NumPy arrays have a specific data type (dtype).
"""

import numpy as np


# Integer array
integers = np.array([1, 2, 3, 4])

print("Integer array:")
print(integers)

print("dtype:", integers.dtype)


# Float array
floats = np.array([1.5, 2.5, 3.5])

print("\nFloat array:")
print(floats)

print("dtype:", floats.dtype)


# Explicit dtype
numbers = np.array([1, 2, 3, 4], dtype=np.float64)

print("\nConverted to float:")
print(numbers)

print("dtype:", numbers.dtype)


# Different integer sizes

small = np.array([1, 2, 3], dtype=np.int32)
large = np.array([1, 2, 3], dtype=np.int64)

print("\nint32:")
print(small.dtype)

print("int64:")
print(large.dtype)