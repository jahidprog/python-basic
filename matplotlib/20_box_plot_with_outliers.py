import matplotlib.pyplot as plt

response_times = [
    [120, 125, 128, 130, 132, 135, 140, 145, 150, 310],
    [100, 105, 110, 115, 118, 120, 122, 125, 130, 220],
    [90, 95, 98, 100, 102, 105, 108, 110, 115, 180]
]
plt.boxplot(response_times, tick_labels=["API A", "API B", "API C"], showmeans=True)
plt.title("API Response Times and Outliers")
plt.xlabel("API")
plt.ylabel("Response Time (ms)")
plt.grid(axis="y", alpha=0.25)
plt.show()
