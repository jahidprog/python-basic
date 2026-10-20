import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng(42)
years = np.arange(2010, 2027)
revenue = rng.integers(200, 1500, size=len(years))
plt.plot(years, revenue, marker="o")
plt.title("Randomly Generated Practice Revenue")
plt.xlabel("Year")
plt.ylabel("Revenue (millions USD)")
plt.xticks(years, rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
