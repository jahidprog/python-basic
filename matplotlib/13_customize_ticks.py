import matplotlib.pyplot as plt
years = [2010, 2013, 2016, 2019, 2022, 2026]
revenue = [320, 350, 460, 680, 710, 860]
plt.figure(figsize=(9, 5))
plt.plot(years, revenue, marker="o")
plt.xticks(years, [str(year) for year in years], rotation=30)
plt.yticks(range(0, 1001, 100))
plt.title("Custom Axis Ticks")
plt.xlabel("Year")
plt.ylabel("Revenue (millions USD)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
