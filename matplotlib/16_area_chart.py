import matplotlib.pyplot as plt
years = [2020, 2021, 2022, 2023, 2024]
oscar_revenue = [620, 750, 710, 820, 790]
plt.fill_between(years, oscar_revenue, alpha=0.4, label="Oscar movies")
plt.plot(years, oscar_revenue, marker="o")
plt.title("Fictional Oscar-Movie Revenue")
plt.xlabel("Year")
plt.ylabel("Revenue (millions USD)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
