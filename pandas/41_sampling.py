import pandas as pd

df = pd.DataFrame({
    "id": range(1, 11),
    "score": range(60, 70)
})

print("Random sample:")
print(df.sample(n=3, random_state=42))
