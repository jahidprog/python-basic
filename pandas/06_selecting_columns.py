import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [22, 25, 21],
    "score": [85, 92, 78]
})

print(df["name"])
print(df[["name", "score"]])
