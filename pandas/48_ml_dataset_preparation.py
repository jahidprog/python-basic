import pandas as pd

df = pd.DataFrame({
    "age": [20, 25, 30, 35],
    "hours_studied": [2, 4, 6, 8],
    "score": [55, 65, 78, 90]
})

# Features
X = df[["age", "hours_studied"]]

# Target
y = df["score"]

print("X:")
print(X)

print("\ny:")
print(y)
