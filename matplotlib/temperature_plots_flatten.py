import matplotlib.pyplot as plt

days = ["Mon", "Tues", "Wed", "Thu", "Fri"]
cities = ["New York", "London", "Dhaka", "Tokyo"]
temp = [
    [22, 23, 21, 24, 25],
    [18, 19, 17, 20, 21],
    [30, 32, 31, 33, 34],
    [25, 26, 24, 27, 28]
]

# Create a 2x2 subplot grid and flatten axes for easy iteration
fig, axes = plt.subplots(2, 2)
axes = axes.flatten()

# Loop through each city and its corresponding temperature data
for i, city in enumerate(cities):
    axes[i].plot(days, temp[i])
    axes[i].set_title(city)
    axes[i].set_ylabel("Temperature (°C)")
    axes[i].set_xlabel("Days")

plt.tight_layout()
plt.show()
