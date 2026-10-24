import matplotlib.pyplot as plt

models = ["Model A", "Model B", "Model C"]
accuracy = [0.81, 0.86, 0.84]
error = [0.03, 0.02, 0.025]
plt.errorbar(models, accuracy, yerr=error, fmt="o", capsize=6)
plt.title("Model Accuracy with Error Bars")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.ylim(0.7, 0.95)
plt.grid(axis="y", alpha=0.3)
plt.show()
