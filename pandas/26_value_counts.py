import pandas as pd

df = pd.DataFrame({
    "department": ["CSE", "EEE", "CSE", "BBA", "CSE", "EEE"]
})

print(df["department"].value_counts())
