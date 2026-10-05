import pandas as pd

df1 = pd.DataFrame({"name": ["Alice", "Bob"], "score": [85, 92]})
df2 = pd.DataFrame({"name": ["Charlie", "David"], "score": [78, 95]})

result = pd.concat([df1, df2], ignore_index=True)

print(result)
