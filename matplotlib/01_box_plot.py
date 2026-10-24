import matplotlib.pyplot as plt
import numpy as np

# Compare the distribution of scores across three classes
np.random.seed(10)
class_a = np.random.normal(70, 8, 100)
class_b = np.random.normal(75, 10, 100)
class_c = np.random.normal(68, 5, 100)

plt.boxplot([class_a, class_b, class_c], tick_labels=["Class A", "Class B", "Class C"])
plt.title("Exam Score Distribution by Class")
plt.xlabel("Class")
plt.ylabel("Score")
plt.grid(axis="y", alpha=0.3)
plt.show()
