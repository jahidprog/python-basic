import matplotlib.pyplot as plt
import numpy as np

np.random.seed(12)
groups = [np.random.normal(m, s, 80) for m, s in [(50, 7), (58, 9), (54, 5)]]
plt.boxplot(groups, vert=False, tick_labels=["Group 1", "Group 2", "Group 3"])
plt.title("Horizontal Box Plot")
plt.xlabel("Value")
plt.grid(axis="x", alpha=0.3)
plt.show()
