import matplotlib.pyplot as plt

model_sizes = [1, 3, 10, 30, 100, 300, 1000]
latency_ms = [2, 4, 8, 18, 45, 110, 350]
fig, ax = plt.subplots()
ax.plot(model_sizes, latency_ms, marker="o")
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_title("Model Size vs Latency (Log Scale)")
ax.set_xlabel("Model Size (log scale)")
ax.set_ylabel("Latency (ms, log scale)")
ax.grid(True, which="both", alpha=0.25)
plt.show()
