import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7]
commits = [1, 2, 2, 4, 3, 6, 8]
fig, ax = plt.subplots(figsize=(9, 5), layout="constrained")
ax.plot(days, commits, marker="o", linewidth=2)
ax.annotate("Best day", xy=(7, 8), xytext=(5, 6.5), arrowprops={"arrowstyle": "->"})
ax.set_title("GitHub Commits This Week")
ax.set_xlabel("Day")
ax.set_ylabel("Commits")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(alpha=0.25)
plt.show()
