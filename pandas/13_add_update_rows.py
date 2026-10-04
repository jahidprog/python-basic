import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "score": [85, 92]
})

df.loc[len(df)] = ["Charlie", 78]
df.loc[0, "score"] = 90

print(df)
