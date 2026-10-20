import matplotlib.pyplot as plt
genres = ["Action", "Comedy", "Drama", "Animation", "Sci-Fi"]
revenue_share = [30, 15, 12, 23, 20]
plt.figure(figsize=(7, 7))
plt.pie(revenue_share, labels=genres, autopct="%1.1f%%", startangle=90)
plt.title("Fictional Revenue Share by Genre")
plt.axis("equal")
plt.show()
