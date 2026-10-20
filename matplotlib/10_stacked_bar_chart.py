import matplotlib.pyplot as plt
years = [2020, 2021, 2022, 2023, 2024]
oscar_revenue = [620, 750, 710, 820, 790]
non_oscar_revenue = [1100, 1450, 1380, 1600, 1520]
plt.bar(years, oscar_revenue, label="Oscar movies")
plt.bar(years, non_oscar_revenue, bottom=oscar_revenue, label="Non-Oscar movies")
plt.title("Fictional Combined Revenue by Year")
plt.xlabel("Year")
plt.ylabel("Revenue (millions USD)")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
