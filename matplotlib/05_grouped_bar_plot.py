import matplotlib.pyplot as plt
import numpy as np

categories = ["Python", "SQL", "ML", "GenAI"]
beginner = [60, 55, 30, 20]
advanced = [40, 45, 70, 80]
x = np.arange(len(categories))
width = 0.35

plt.bar(x - width / 2, beginner, width, label="Beginner")
plt.bar(x + width / 2, advanced, width, label="Advanced")
plt.xticks(x, categories)
plt.title("Skills by Experience Level")
plt.xlabel("Skill")
plt.ylabel("Learners")
plt.legend()
plt.show()
