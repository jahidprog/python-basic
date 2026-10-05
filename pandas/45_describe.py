import pandas as pd

df = pd.DataFrame({
    "age": [20, 22, 25, 30, 28],
    "score": [70, 85, 90, 95, 88]
})

print(df.describe())
