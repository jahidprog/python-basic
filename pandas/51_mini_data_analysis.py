import pandas as pd

df = pd.DataFrame({
    "department": ["CSE", "CSE", "EEE", "EEE", "CSE"],
    "hours_studied": [3, 5, 2, 4, 6],
    "score": [65, 80, 55, 72, 90]
})

print("=== Dataset ===")
print(df)

print("\n=== Basic Information ===")
print("Shape:", df.shape)
print("Columns:", list(df.columns))

print("\n=== Statistics ===")
print(df.describe())

print("\n=== Average Score by Department ===")
print(df.groupby("department")["score"].mean())

print("\n=== Top Students ===")
print(df.sort_values("score", ascending=False).head(3))
