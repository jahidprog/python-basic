import pandas as pd

df = pd.DataFrame({
    "score": [80, 90, 75, 95, 88]
})

print("Mean:", df["score"].mean())
print("Median:", df["score"].median())
print("Min:", df["score"].min())
print("Max:", df["score"].max())
print("Standard deviation:", df["score"].std())
