import matplotlib.pyplot as plt
revenues = [120, 180, 210, 230, 250, 280, 300, 320, 340, 360,
            390, 410, 430, 460, 480, 510, 550, 590, 620, 700,
            740, 810, 900, 1050, 1200]
plt.hist(revenues, bins=8, edgecolor="black")
plt.title("Distribution of Fictional Movie Revenues")
plt.xlabel("Revenue (millions USD)")
plt.ylabel("Number of movies")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
