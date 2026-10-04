import pandas as pd

# A Series is a one-dimensional labeled data structure.
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])

print(s)
print(s["b"])
print(s.values)
print(s.index)
