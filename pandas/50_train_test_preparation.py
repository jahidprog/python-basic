import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    "age": [20, 22, 25, 28, 30, 35, 40, 45],
    "hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "score": [50, 55, 62, 68, 75, 80, 88, 95]
})

X = df[["age", "hours"]]
y = df["score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

print("X_train:")
print(X_train)

print("\nX_test:")
print(X_test)

print("\ny_train:")
print(y_train)

print("\ny_test:")
print(y_test)
