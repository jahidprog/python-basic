import pandas as pd

df = pd.DataFrame({
    "hours_studied": [1, 2, 3, 4, 5],
    "score": [50, 60, 70, 80, 90]
})

print(df.corr())
print("Correlation:", df["hours_studied"].corr(df["score"]))
