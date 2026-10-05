import pandas as pd

df = pd.DataFrame({
    "score": [45, 72, 88, 95]
})

def grade(score):
    if score >= 80:
        return "A"
    if score >= 60:
        return "B"
    return "C"

df["grade"] = df["score"].apply(grade)

print(df)
