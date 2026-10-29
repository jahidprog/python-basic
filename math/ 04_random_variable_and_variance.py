"""
Topic: Discrete Random Variable, Expected Value E[X], and Variance Var(X)
"""

# Discrete Random Variable X = outcome of a weighted coin flip payout
# X = payout in dollars, P(X) = probability of payout
x_values = [0, 10, 20]
probabilities = [0.5, 0.3, 0.2]

# 1. Expected Value (Mean of Random Variable): E[X] = sum(x * P(x))
expected_value = sum(x * p for x, p in zip(x_values, probabilities))

# 2. Variance of Random Variable: Var(X) = E[X^2] - (E[X])^2
# Alternatively: sum((x - E[X])^2 * P(x))
variance_rv = sum(((x - expected_value) ** 2) * p for x, p in zip(x_values, probabilities))
std_dev_rv = variance_rv ** 0.5

print("--- Discrete Random Variable Analysis ---")
print(f"Values (X): {x_values}")
print(f"Probabilities P(X): {probabilities}")
print(f"Expected Value E[X]: {expected_value:.2f}")
print(f"Variance Var(X): {variance_rv:.2f}")
print(f"Standard Deviation SD(X): {std_dev_rv:.2f}")