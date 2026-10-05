import pandas as pd

df = pd.DataFrame({
    "department": ["CSE", "CSE", "EEE", "EEE"],
    "score": [80, 90, 75, 85]
})

print(df.groupby("department")["score"].mean())
