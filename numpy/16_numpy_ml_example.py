"""
NumPy - Machine Learning Example

A Machine Learning dataset can often be represented
as a NumPy matrix.

Rows    -> samples
Columns -> features
"""

import numpy as np


# Example:
# feature 1 = hours studied
# feature 2 = hours slept

X = np.array([
    [2, 6],
    [4, 7],
    [6, 8],
    [8, 7]
])


print("Feature matrix X:")
print(X)


print("\nShape:")
print(X.shape)


print("\nNumber of samples:")
print(X.shape[0])


print("\nNumber of features:")
print(X.shape[1])


# Target values
y = np.array([
    50,
    65,
    75,
    90
])


print("\nTarget values:")
print(y)


"""
Machine Learning mental model:

X
↓
Input features

y
↓
Target / output

For this example:

X =
[
    [2, 6],
    [4, 7],
    [6, 8],
    [8, 7]
]

4 samples
2 features

y =
[50, 65, 75, 90]

Later, a Machine Learning algorithm will try to
learn the relationship between X and y.
"""