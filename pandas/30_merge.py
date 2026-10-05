import pandas as pd

students = pd.DataFrame({
    "student_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"]
})

scores = pd.DataFrame({
    "student_id": [1, 2, 3],
    "score": [85, 92, 78]
})

result = pd.merge(students, scores, on="student_id")

print(result)
