"""
Topic: Binomial Distribution & PMF / CDF
Uses scipy.stats to calculate probability mass and cumulative density functions.
"""
from scipy.stats import binom

# Experiment: 20 coin flips with a fair coin (p = 0.5)
n = 20
p = 0.5

# 1. Exact Probability Mass Function (PMF): P(X = 12)
p_exact_12 = binom.pmf(k=12, n=n, p=p)

# 2. Cumulative Density Function (CDF): P(X <= 10)
p_at_most_10 = binom.cdf(k=10, n=n, p=p)

# 3. Survival Function (Complementary CDF): P(X >= 15)
p_at_least_15 = binom.sf(k=14, n=n, p=p) # k=14 means strictly > 14

print("--- Binomial Distribution Analysis (20 Flips) ---")
print(f"P(Exactly 12 Heads): {p_exact_12:.4f}")
print(f"P(At most 10 Heads): {p_at_most_10:.4f}")
print(f"P(At least 15 Heads): {p_at_least_15:.4f}")