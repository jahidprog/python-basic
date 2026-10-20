import matplotlib.pyplot as plt
# 02 — Markers, line styles, labels, and grid
years = [2010, 2011, 2012, 2013, 2014, 2015]
revenue = [320, 280, 410, 350, 490, 530]
plt.figure(figsize=(9, 5))
plt.plot(years, revenue, marker="o", linestyle="--", linewidth=2,
         markersize=7, label="Sample revenue")
plt.title("Sample Revenue by Year")
plt.xlabel("Year")
plt.ylabel("Revenue (millions USD)")
plt.xticks(years)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
