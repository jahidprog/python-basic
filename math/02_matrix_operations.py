"""
Topic: Matrix Operations (Multiplication, Transpose, Determinant, Inverse, Trace)
"""
import numpy as np

A = np.array([[1, 2], 
              [3, 4]])

B = np.array([[5, 6], 
              [7, 8]])

# 1. Matrix Multiplication (Dot product using @ or np.dot)
# Note: * performs element-wise multiplication, @ performs true matrix multiplication
matrix_mult = A @ B

# 2. Transpose
transpose_A = A.T

# 3. Determinant (must be square matrix)
det_A = np.linalg.det(A)

# 4. Inverse Matrix (A^-1 such that A @ A^-1 = Identity Matrix)
inv_A = np.linalg.inv(A)

# 5. Trace (Sum of diagonal elements)
trace_A = np.trace(A)

print("--- Matrix Operations ---")
print("Matrix A:\n", A)
print("Matrix Multiplication (A @ B):\n", matrix_mult)
print("Transpose of A:\n", transpose_A)
print(f"Determinant of A: {det_A:.2f}")
print("Inverse of A:\n", inv_A)
print(f"Trace of A: {trace_A}")