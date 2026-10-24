import matplotlib.pyplot as plt

days = list(range(1, 11))
bugs_fixed = [2, 4, 3, 7, 5, 8, 6, 9, 7, 10]
plt.stem(days, bugs_fixed)
plt.title("Bugs Fixed per Day")
plt.xlabel("Day")
plt.ylabel("Bugs Fixed")
plt.show()
