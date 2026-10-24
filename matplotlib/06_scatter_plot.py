import matplotlib.pyplot as plt
import numpy as np

np.random.seed(3)
study_hours = np.random.uniform(1, 10, 50)
scores = 45 + study_hours * 5 + np.random.normal(0, 8, 50)
plt.scatter(study_hours, scores, alpha=0.75, edgecolors="black")
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.grid(alpha=0.25)
plt.show()
