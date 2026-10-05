import pandas as pd

df = pd.DataFrame({
    "student_name": ["Alice", "Bob"],
    "student_score": [85, 92]
})

df = df.rename(columns={
    "student_name": "name",
    "student_score": "score"
})

print(df)
