import pandas as pd

df = pd.DataFrame({
    "status": ["yes", "no", "yes", "no"]
})

mapping = {"yes": 1, "no": 0}
df["status_encoded"] = df["status"].map(mapping)

print(df)
