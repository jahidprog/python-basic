import numpy as np

# 1. Vectors and Dot Product (measures similarity/alignment)
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
dot_product = np.dot(v1, v2)
print("Dot Product:", dot_product)  # Output: 32

# 2. Matrix Multiplication (core of neural network layers: W * x + b)
matrix = np.array([[1, 2], [3, 4]])
vector = np.array([10, 20])

# Using np.dot or the '@' operator
output = matrix @ vector
print("Matrix-Vector Multiplication:", output)  # Output: [ 50 110]