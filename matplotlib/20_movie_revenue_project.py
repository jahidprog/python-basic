from pathlib import Path
import matplotlib.pyplot as plt
years = list(range(2010, 2027))
oscar_revenue = [320, 280, 410, 350, 490, 530, 460, 610, 570, 680, 620, 750, 710, 820, 790, 900, 860]
non_oscar_revenue = [650, 720, 810, 760, 920, 1050, 980, 1200, 1150, 1300, 1100, 1450, 1380, 1600, 1520, 1750, 1900]
fig, ax = plt.subplots(figsize=(13, 6))
ax.plot(years, oscar_revenue, marker="o", linewidth=2, label="Oscar movies")
ax.plot(years, non_oscar_revenue, marker="s", linewidth=2, label="Non-Oscar movies")
i = non_oscar_revenue.index(max(non_oscar_revenue))
ax.annotate(f"Highest sample value: {non_oscar_revenue[i]}",
            xy=(years[i], non_oscar_revenue[i]),
            xytext=(years[i] - 5, non_oscar_revenue[i] - 250),
            arrowprops={"arrowstyle": "->"})
ax.set_title("Movie Revenue Practice Project (Synthetic Data)")
ax.set_xlabel("Year")
ax.set_ylabel("Revenue (millions USD)")
ax.set_xticks(years)
ax.tick_params(axis="x", rotation=45)
ax.grid(True, linestyle="--", alpha=0.35)
ax.legend()
fig.tight_layout()
output = Path("movie_revenue_project.png")
fig.savefig(output, dpi=300, bbox_inches="tight")
print(f"Saved chart to: {output.resolve()}")
plt.show()
