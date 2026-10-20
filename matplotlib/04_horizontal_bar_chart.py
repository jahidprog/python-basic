import matplotlib.pyplot as plt
categories = ["Action", "Comedy", "Drama", "Animation", "Sci-Fi"]
revenue = [950, 620, 430, 870, 790]
plt.barh(categories, revenue)
plt.title("Fictional Revenue by Genre")
plt.xlabel("Revenue (millions USD)")
plt.ylabel("Genre")
plt.grid(axis="x", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
