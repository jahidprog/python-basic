import matplotlib.pyplot as plt
years = list(range(2010, 2027))
revenue = [320, 280, 410, 350, 490, 530, 460, 610, 570, 680, 620, 750, 710, 820, 790, 900, 860]
i = revenue.index(max(revenue))
plt.figure(figsize=(10, 5))
plt.plot(years, revenue, marker="o")
plt.annotate(f"Highest: {revenue[i]}", xy=(years[i], revenue[i]),
             xytext=(years[i] - 4, revenue[i] + 100),
             arrowprops={"arrowstyle": "->"})
plt.title("Annotating a Data Point")
plt.xlabel("Year")
plt.ylabel("Revenue (millions USD)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
