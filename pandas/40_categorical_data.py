import pandas as pd

df = pd.DataFrame({
    "department": ["CSE", "EEE", "CSE", "BBA"]
})

df["department"] = df["department"].astype("category")

print(df.dtypes)
print(df["department"].cat.categories)
