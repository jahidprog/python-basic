"""
NumPy - Array Creation

NumPy's main data structure is the ndarray (N-dimensional array).

In this file:
- Creating arrays from Python lists
- zeros()
- ones()
- full()
- arange()
- linspace()
"""

import numpy as np


# Creating an array from a Python list
numbers = np.array([1, 2, 3, 4, 5])

print("Array:")
print(numbers)


# Array filled with zeros
zeros = np.zeros(5)

print("\nZeros:")
print(zeros)


# 2D array filled with zeros
zeros_2d = np.zeros((2, 3))

print("\n2D zeros:")
print(zeros_2d)


# Array filled with ones
ones = np.ones(5)

print("\nOnes:")
print(ones)


# Array filled with a specific value
full = np.full(5, 10)

print("\nFull:")
print(full)


# Numbers from 0 to 9
numbers = np.arange(10)

print("\nArange:")
print(numbers)


# Numbers from 1 to 10
numbers = np.arange(1, 11)

print("\nArange 1-10:")
print(numbers)


# Even numbers
even_numbers = np.arange(0, 11, 2)

print("\nEven numbers:")
print(even_numbers)


# Equally spaced numbers
numbers = np.linspace(0, 1, 5)

print("\nLinspace:")
print(numbers)