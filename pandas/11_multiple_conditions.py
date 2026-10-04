import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [22, 25, 21, 24],
    "score": [85, 92, 78, 95]
})

result = df[(df["age"] >= 22) & (df["score"] >= 90)]

print(result)
