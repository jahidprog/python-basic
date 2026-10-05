import pandas as pd

df = pd.DataFrame({
    "department": ["CSE", "CSE", "EEE", "EEE"],
    "semester": [1, 2, 1, 2],
    "score": [80, 90, 75, 85]
})

result = df.groupby(["department", "semester"])["score"].mean()

print(result)
