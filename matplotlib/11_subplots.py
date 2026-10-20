import matplotlib.pyplot as plt
years = [2020, 2021, 2022, 2023, 2024]
oscar_revenue = [620, 750, 710, 820, 790]
non_oscar_revenue = [1100, 1450, 1380, 1600, 1520]
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].plot(years, oscar_revenue, marker="o")
axes[0].set_title("Oscar Movies")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Revenue (millions USD)")
axes[0].grid(True, alpha=0.3)
axes[1].bar(years, non_oscar_revenue)
axes[1].set_title("Non-Oscar Movies")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Revenue (millions USD)")
axes[1].grid(axis="y", alpha=0.3)
fig.suptitle("Fictional Movie Revenue")
fig.tight_layout()
plt.show()
