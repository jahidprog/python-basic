import pandas as pd

df = pd.DataFrame({
    "id": range(1, 11)
})

shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

print(shuffled)
