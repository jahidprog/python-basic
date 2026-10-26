import numpy as np

# Vectors: a data point and its model weights
x = np.array([22, 5, 80])       # e.g. age, study hours, score
w = np.array([0.2, 1.5, 0.05])

print("Vector x:", x)
print("Vector w:", w)
print("Dot product (weighted sum):", np.dot(x, w))

# Matrix: rows are data points, columns are features
X = np.array([[22, 5, 80], [25, 2, 65], [20, 8, 90]])
print("\nFeature matrix:\n", X)
print("Shape (rows, columns):", X.shape)
print("Matrix-vector multiplication:", X @ w)
print("Transpose:\n", X.T)
