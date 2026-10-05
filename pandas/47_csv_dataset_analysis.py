import pandas as pd

# Replace this with a real dataset path when practicing.
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [22, 25, 21, 24],
    "score": [85, 92, 78, 95]
})

print(df.head())
print("\nShape:", df.shape)
print("\nStatistics:")
print(df.describe())
print("\nHighest scores:")
print(df.sort_values("score", ascending=False))
