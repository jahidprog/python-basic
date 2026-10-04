import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "score": [85, 92, 78]
})

print(df.iloc[0])
print(df.iloc[0:2, 0:2])
