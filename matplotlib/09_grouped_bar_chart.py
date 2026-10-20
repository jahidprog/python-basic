import numpy as np
import matplotlib.pyplot as plt
years = [2020, 2021, 2022, 2023, 2024]
oscar_revenue = [620, 750, 710, 820, 790]
non_oscar_revenue = [1100, 1450, 1380, 1600, 1520]
x = np.arange(len(years))
width = 0.38
plt.figure(figsize=(9, 5))
plt.bar(x - width / 2, oscar_revenue, width, label="Oscar movies")
plt.bar(x + width / 2, non_oscar_revenue, width, label="Non-Oscar movies")
plt.xticks(x, years)
plt.title("Fictional Revenue Comparison")
plt.xlabel("Year")
plt.ylabel("Revenue (millions USD)")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
