import numpy as np

# Generate random data representing model errors or features
data = np.random.randn(1000)  # Standard normal distribution

mean = np.mean(data)
variance = np.var(data)
std_dev = np.std(data)

print(f"Mean: {mean:.2f}, Variance: {variance:.2f}, Std Dev: {std_dev:.2f}")