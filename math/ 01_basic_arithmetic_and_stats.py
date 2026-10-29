"""
Topic: Basic Descriptive Statistics (Mean, Median, Mode, Variance, Standard Deviation)
"""
import numpy as np
from scipy import stats

data = [12, 15, 12, 18, 20, 22, 15, 12, 25, 30]

# Mean (Average)
mean_val = np.mean(data)

# Median (Middle value)
median_val = np.median(data)

# Mode (Most frequent value)
mode_res = stats.mode(data, keepdims=True)
mode_val = mode_res.mode[0]

# Sample Variance and Standard Deviation
variance_val = np.var(data, ddof=1)
std_dev_val = np.std(data, ddof=1)

print("--- Basic Statistics ---")
print(f"Data: {data}")
print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Mode: {mode_val}")
print(f"Variance: {variance_val:.2f}")
print(f"Standard Deviation: {std_dev_val:.2f}")