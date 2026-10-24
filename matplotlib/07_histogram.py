import matplotlib.pyplot as plt
import numpy as np

np.random.seed(4)
response_times = np.random.normal(250, 45, 500)
plt.hist(response_times, bins=20, edgecolor="black")
plt.title("API Response-Time Distribution")
plt.xlabel("Response Time (ms)")
plt.ylabel("Frequency")
plt.show()
