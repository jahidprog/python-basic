import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Alice", "Charlie"],
    "score": [85, 92, 85, 78]
})

print("Duplicate rows:")
print(df[df.duplicated()])

df = df.drop_duplicates()

print(df)
