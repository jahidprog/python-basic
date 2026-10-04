import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "score": [85, 92]
})

df.to_csv("output.csv", index=False)
print("CSV saved.")
