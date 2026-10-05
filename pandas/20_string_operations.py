import pandas as pd

df = pd.DataFrame({
    "name": ["alice", "BOB", " Charlie "]
})

df["clean_name"] = df["name"].str.strip().str.title()

print(df)
