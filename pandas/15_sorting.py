import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "score": [85, 92, 78]
})

print(df.sort_values("score"))
print(df.sort_values("score", ascending=False))
