import matplotlib.pyplot as plt
movies = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"]
revenue = [420, 610, 350, 780, 540]
bars = plt.bar(movies, revenue)
plt.title("Sample Movie Revenue")
plt.xlabel("Movie")
plt.ylabel("Revenue (millions USD)")
plt.bar_label(bars, padding=3)
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
