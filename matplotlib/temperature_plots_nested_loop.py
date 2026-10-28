import matplotlib.pyplot as plt

days = ["Mon", "Tues", "Wed", "Thu", "Fri"]
cities = ["New York", "London", "Dhaka", "Tokyo"]
temp = [
    [22, 23, 21, 24, 25],
    [18, 19, 17, 20, 21],
    [30, 32, 31, 33, 34],
    [25, 26, 24, 27, 28]
]

fig, ax = plt.subplots(2, 2)
city_no = 0
for i in range(2):
    for j in range(2):
        ax[i][j].plot(days, temp[city_no], marker="o")
        ax[i][j].set_title(cities[city_no])

        city_no += 1

fig.suptitle("Tempearture in Cities over the weeks")
fig.supxlabel("Days")
fig.supylabel("Temperature (°C)")

plt.tight_layout()
plt.show()