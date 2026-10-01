"""
NumPy - Boolean Indexing

Boolean indexing allows us to filter arrays
using conditions.
"""

import numpy as np


scores = np.array([45, 78, 92, 56, 88, 32])

print("Scores:")
print(scores)


# Create a Boolean condition
condition = scores >= 60

print("\nCondition:")
print(condition)


# Filter values
passed = scores[condition]

print("\nPassed scores:")
print(passed)


# Directly filter

print("\nScores greater than 80:")
print(scores[scores > 80])


print("\nScores between 50 and 90:")
print(scores[(scores >= 50) & (scores <= 90)])