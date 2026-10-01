"""
NumPy - Random Numbers

Random number generation is commonly used in
Machine Learning and Deep Learning.
"""

import numpy as np


# Random values between 0 and 1
random_numbers = np.random.rand(5)

print("Random numbers:")
print(random_numbers)


# Random 2D array
matrix = np.random.rand(2, 3)

print("\nRandom 2D array:")
print(matrix)


# Random integers

numbers = np.random.randint(1, 10, size=5)

print("\nRandom integers:")
print(numbers)