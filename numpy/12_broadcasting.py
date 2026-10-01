"""
NumPy - Broadcasting

Broadcasting allows NumPy to perform operations
between arrays with compatible shapes.
"""

import numpy as np


matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

vector = np.array([10, 20, 30])


print("Matrix:")
print(matrix)

print("\nVector:")
print(vector)


result = matrix + vector

print("\nMatrix + Vector:")
print(result)


"""
Conceptually:

[1, 2, 3]     [10, 20, 30]
[4, 5, 6]  +  [10, 20, 30]

             ↓

[11, 22, 33]
[14, 25, 36]

NumPy automatically broadcasts the vector
across each row.
"""