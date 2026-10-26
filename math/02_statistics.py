import numpy as np

scores = np.array([55, 60, 62, 70, 73, 80, 100], dtype=float)

mean = np.mean(scores)
median = np.median(scores)
variance = np.var(scores)  # Population variance
std_dev = np.std(scores)

print("Scores:", scores)
print(f"Mean: {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Standard deviation: {std_dev:.2f}")

# Z-score standardization
z_scores = (scores - mean) / std_dev
print("Z-scores:", np.round(z_scores, 2))
print("Z-score mean (about 0):", round(float(np.mean(z_scores)), 6))
print("Z-score standard deviation (about 1):", round(float(np.std(z_scores)), 6))
print("Sample variance (ddof=1):", round(float(np.var(scores, ddof=1)), 2))
