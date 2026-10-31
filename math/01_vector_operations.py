"""
Topic: Vector Operations (Dot Product, Norm, Cross Product, Angle)
"""
import numpy as np

v1 = np.array([3, 4, 0])
v2 = np.array([1, 2, 3])

# 1. Dot Product (Scalar product)
dot_product = np.dot(v1, v2)

# 2. Vector Magnitude / Norm (Length)
norm_v1 = np.linalg.norm(v1)
norm_v2 = np.linalg.norm(v2)

# 3. Angle between vectors (in radians and degrees)
cos_theta = dot_product / (norm_v1 * norm_v2)
angle_rad = np.arccos(np.clip(cos_theta, -1.0, 1.0))
angle_deg = np.degrees(angle_rad)

# 4. Cross Product (Vector product, yields a vector orthogonal to both)
cross_product = np.cross(v1, v2)

print("--- Vector Operations ---")
print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Dot Product: {dot_product}")
print(f"Norm of Vector 1: {norm_v1:.2f}")
print(f"Angle between vectors: {angle_deg:.2f} degrees")
print(f"Cross Product: {cross_product}")