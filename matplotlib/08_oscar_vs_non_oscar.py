import matplotlib.pyplot as plt
# Synthetic sample values; each value represents category revenue per year.
years = list(range(2010, 2027))
oscar_revenue = [320, 280, 410, 350, 490, 530, 460, 610, 570, 680, 620, 750, 710, 820, 790, 900, 860]
non_oscar_revenue = [650, 720, 810, 760, 920, 1050, 980, 1200, 1150, 1300, 1100, 1450, 1380, 1600, 1520, 1750, 1900]
plt.figure(figsize=(12, 6))
plt.plot(years, oscar_revenue, marker="o", label="Oscar movies")
plt.plot(years, non_oscar_revenue, marker="s", label="Non-Oscar movies")
plt.title("Fictional Movie Revenue: Oscar vs Non-Oscar (2010–2026)")
plt.xlabel("Year")
plt.ylabel("Revenue (millions USD)")
plt.xticks(years, rotation=45)
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()
plt.show()
