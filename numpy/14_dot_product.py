"""
NumPy - Dot Product

The dot product is an important mathematical operation
used in Machine Learning.
"""

import numpy as np


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])


print("a:")
print(a)

print("\nb:")
print(b)


result = np.dot(a, b)

print("\nDot product:")
print(result)


"""
Calculation:

(1 * 4) + (2 * 5) + (3 * 6)

= 4 + 10 + 18

= 32
"""