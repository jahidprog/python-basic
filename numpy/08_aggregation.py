"""
NumPy - Aggregation

Aggregation reduces multiple values into a single value.

Common functions:
- sum
- mean
- median
- min
- max
- std
- var
"""

import numpy as np


numbers = np.array([10, 20, 30, 40, 50])


print("Numbers:")
print(numbers)

print("\nSum:")
print(np.sum(numbers))

print("\nMean:")
print(np.mean(numbers))

print("\nMedian:")
print(np.median(numbers))

print("\nMinimum:")
print(np.min(numbers))

print("\nMaximum:")
print(np.max(numbers))

print("\nStandard deviation:")
print(np.std(numbers))

print("\nVariance:")
print(np.var(numbers))