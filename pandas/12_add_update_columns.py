import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "score": [85, 92, 78]
})

df["passed"] = df["score"] >= 80
df["score_plus_5"] = df["score"] + 5

print(df)
