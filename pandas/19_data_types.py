import pandas as pd

df = pd.DataFrame({
    "age": [20, 25, 30],
    "score": [80.5, 91.2, 77.8],
    "name": ["A", "B", "C"]
})

print(df.dtypes)
print(df["age"].astype(float).dtypes)
