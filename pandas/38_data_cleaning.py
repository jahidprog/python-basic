import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": [" Alice ", "Bob", "Alice"],
    "age": [22, np.nan, 22],
    "score": [85, 92, 85]
})

df["name"] = df["name"].str.strip()
df["age"] = df["age"].fillna(df["age"].median())
df = df.drop_duplicates()

print(df)
