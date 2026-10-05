import pandas as pd

df = pd.DataFrame({
    "status": ["yes", "no", "unknown", "yes"]
})

df["status"] = df["status"].replace({"yes": 1, "no": 0, "unknown": -1})

print(df)
