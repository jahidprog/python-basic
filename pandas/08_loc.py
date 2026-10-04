import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "score": [85, 92, 78]
}, index=["a", "b", "c"])

print(df.loc["b"])
print(df.loc["a":"b", ["name", "score"]])
