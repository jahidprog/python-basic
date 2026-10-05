import pandas as pd

df = pd.DataFrame({
    "department": ["CSE", "CSE", "EEE", "EEE"],
    "semester": [1, 2, 1, 2],
    "score": [80, 90, 75, 85]
})

pivot = pd.pivot_table(
    df,
    values="score",
    index="department",
    columns="semester",
    aggfunc="mean"
)

print(pivot)
