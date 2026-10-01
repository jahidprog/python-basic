"""
NumPy - Vectorization

Vectorization means performing operations on an entire
array without explicitly writing a Python loop.
"""

import numpy as np


numbers = np.array([1, 2, 3, 4, 5])


# Python-style thinking

result = []

for number in numbers:
    result.append(number * 2)

print("Using loop:")
print(result)


# NumPy vectorized operation

result = numbers * 2

print("\nUsing NumPy:")
print(result)


"""
Instead of:

for x in numbers:
    x * 2

We can simply write:

numbers * 2

This becomes extremely useful when working with
large numerical datasets in Machine Learning.
"""