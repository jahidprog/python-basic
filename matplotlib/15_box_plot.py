import matplotlib.pyplot as plt
oscar_revenue = [320, 280, 410, 350, 490, 530, 460, 610, 570, 680]
non_oscar_revenue = [650, 720, 810, 760, 920, 1050, 980, 1200, 1150, 1300]
plt.boxplot([oscar_revenue, non_oscar_revenue],
            labels=["Oscar movies", "Non-Oscar movies"])
plt.title("Fictional Revenue Distribution")
plt.ylabel("Revenue (millions USD)")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
