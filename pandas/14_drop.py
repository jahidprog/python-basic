import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [22, 25, 21],
    "score": [85, 92, 78]
})

df = df.drop(columns=["age"])
df = df.drop(index=[1])

print(df)
