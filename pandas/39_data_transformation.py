import pandas as pd

df = pd.DataFrame({
    "price": [100, 200, 300],
    "quantity": [2, 3, 1]
})

df["total"] = df["price"] * df["quantity"]
df["log_price"] = df["price"].apply(lambda x: x ** 0.5)

print(df)
