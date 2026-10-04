import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [22, 25, 21],
    "score": [85, 90, 78]
})

print("Shape:", df.shape)
print("Columns:", df.columns)
print("Index:", df.index)
print("Dtypes:")
print(df.dtypes)
print("Size:", df.size)
print("Number of dimensions:", df.ndim)
