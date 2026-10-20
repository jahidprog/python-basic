import matplotlib.pyplot as plt
marketing_spend = [20, 35, 25, 50, 45, 60, 30, 70, 55, 40]
revenue = [180, 290, 220, 410, 360, 490, 260, 560, 430, 330]
plt.scatter(marketing_spend, revenue, s=80, alpha=0.8)
plt.title("Marketing Spend vs Revenue (Fictional Data)")
plt.xlabel("Marketing spend (millions USD)")
plt.ylabel("Revenue (millions USD)")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
