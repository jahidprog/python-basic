from pathlib import Path
import matplotlib.pyplot as plt
years = [2020, 2021, 2022, 2023, 2024]
revenue = [620, 750, 710, 820, 790]
plt.figure(figsize=(9, 5))
plt.plot(years, revenue, marker="o")
plt.title("Sample Revenue")
plt.xlabel("Year")
plt.ylabel("Revenue (millions USD)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
output = Path("sample_revenue.png")
plt.savefig(output, dpi=300, bbox_inches="tight")
print(f"Chart saved to: {output.resolve()}")
plt.show()
