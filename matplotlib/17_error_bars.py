import matplotlib.pyplot as plt
years = [2020, 2021, 2022, 2023, 2024]
average_revenue = [620, 750, 710, 820, 790]
uncertainty = [45, 60, 50, 70, 55]  # illustrative values
plt.errorbar(years, average_revenue, yerr=uncertainty, fmt="o-", capsize=5)
plt.title("Sample Revenue with Error Bars")
plt.xlabel("Year")
plt.ylabel("Revenue (millions USD)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
