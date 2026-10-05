import pandas as pd

df = pd.DataFrame({
    "department": ["CSE", "CSE", "EEE", "EEE"],
    "score": [80, 90, 75, 85]
})

result = df.groupby("department")["score"].agg(["mean", "min", "max", "count"])

print(result)
