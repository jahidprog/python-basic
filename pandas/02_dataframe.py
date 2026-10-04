import pandas as pd

# DataFrame = table with rows and columns.
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [22, 25, 21],
    "score": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)
