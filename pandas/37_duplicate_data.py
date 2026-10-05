import pandas as pd

df = pd.DataFrame({
    "email": ["a@example.com", "b@example.com", "a@example.com"],
    "score": [80, 90, 80]
})

print("Duplicate emails:")
print(df[df.duplicated("email", keep=False)])

df = df.drop_duplicates("email")

print(df)
