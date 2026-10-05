import pandas as pd

df = pd.DataFrame({
    "hours_studied": [2, 4, 6, 8],
    "practice_tests": [1, 2, 4, 5]
})

df["study_intensity"] = (
    df["hours_studied"] * df["practice_tests"]
)

print(df)
