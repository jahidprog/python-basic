import pandas as pd

df = pd.DataFrame({
    "date": ["2026-01-10", "2026-02-15", "2026-03-20"]
})

df["date"] = pd.to_datetime(df["date"])

print(df)
print(df["date"].dt.year)
print(df["date"].dt.month)
