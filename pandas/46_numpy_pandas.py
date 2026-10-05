import pandas as pd
import numpy as np

df = pd.DataFrame({
    "score": [70, 80, 90, 100]
})

array = df["score"].to_numpy()

print("NumPy array:", array)
print("Mean:", np.mean(array))
