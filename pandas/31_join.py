import pandas as pd

left = pd.DataFrame({"score": [85, 92]}, index=["Alice", "Bob"])
right = pd.DataFrame({"age": [22, 25]}, index=["Alice", "Bob"])

result = left.join(right)

print(result)
