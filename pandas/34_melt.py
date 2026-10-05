import pandas as pd

df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "math": [80, 90],
    "science": [85, 88]
})

long_df = df.melt(
    id_vars="name",
    var_name="subject",
    value_name="score"
)

print(long_df)
