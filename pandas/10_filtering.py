import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David"],
    "score": [85, 92, 78, 95]
})

high_scores = df[df["score"] >= 90]

print(high_scores)
