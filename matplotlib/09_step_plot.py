import matplotlib.pyplot as plt

epochs = [1, 2, 3, 4, 5, 6]
accuracy = [0.60, 0.68, 0.72, 0.79, 0.83, 0.87]
plt.step(epochs, accuracy, where="mid", marker="o")
plt.title("Model Accuracy by Epoch")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.ylim(0.5, 1.0)
plt.grid(alpha=0.3)
plt.show()
