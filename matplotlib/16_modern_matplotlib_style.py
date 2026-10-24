import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-whitegrid")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
actual = [12, 15, 14, 19, 23, 27]
target = [10, 13, 16, 18, 22, 25]

fig, ax = plt.subplots(figsize=(10, 5), layout="constrained")
ax.plot(months, actual, marker="o", linewidth=2.5, label="Actual")
ax.plot(months, target, marker="s", linewidth=2, linestyle="--", label="Target")
ax.fill_between(months, actual, target, alpha=0.15)
ax.set_title("Monthly Progress", loc="left", fontsize=16, fontweight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Hours")
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False)
ax.grid(axis="y", alpha=0.3)
plt.show()
