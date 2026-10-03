import numpy as np

arr = np.array([[1, 2], [3, 4]])

mean = np.mean(arr)
std_dev = np.std(arr)

normalized_arr = (arr - mean) / std_dev
print(normalized_arr)