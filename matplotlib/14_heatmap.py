import matplotlib.pyplot as plt
import numpy as np

values = np.array([[3, 5, 7, 8], [4, 6, 8, 9], [2, 4, 6, 7], [5, 6, 7, 10]])
fig, ax = plt.subplots()
image = ax.imshow(values, aspect="auto")
ax.set_xticks(range(4), ["Mon", "Tue", "Wed", "Thu"])
ax.set_yticks(range(4), ["Python", "SQL", "ML", "GenAI"])
ax.set_title("Practice Hours Heatmap")
ax.set_xlabel("Day")
ax.set_ylabel("Topic")
fig.colorbar(image, ax=ax, label="Hours")
plt.show()
