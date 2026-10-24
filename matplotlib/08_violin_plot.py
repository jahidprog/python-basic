import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5)
models = [np.random.normal(m, s, 120) for m, s in [(0.78, 0.06), (0.84, 0.04), (0.81, 0.08)]]
plt.violinplot(models, showmedians=True)
plt.xticks([1, 2, 3], ["Model A", "Model B", "Model C"])
plt.title("Model Accuracy Distribution")
plt.ylabel("Accuracy")
plt.grid(axis="y", alpha=0.25)
plt.show()
