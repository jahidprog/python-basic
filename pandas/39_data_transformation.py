import pandas as pd
import numpy as np

df = pd.DataFrame({
    "price": [100, 200, 300],
    "quantity": [2, 3, 1]
})

df["total"] = df["price"] * df["quantity"]
df["log_price"] = np.log(df["price"])

print(df)
