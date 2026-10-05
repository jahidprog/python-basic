import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "score": [85, np.nan, 78]
})

print(df.isna())
print(df.isna().sum())
