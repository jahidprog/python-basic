import pandas as pd

df = pd.DataFrame({
    "date": pd.to_datetime(["2026-01-10", "2026-02-15", "2026-03-20"])
})

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["weekday"] = df["date"].dt.day_name()

print(df)
