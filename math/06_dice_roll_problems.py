"""
Topic: Dice Roll Probability & Joint Outcomes
Calculates sum probabilities, 'at least' events, and multi-dice outcomes.
"""
from itertools import product

# Build sample space for 2 six-sided dice
dice = range(1, 7)
sample_space = list(product(dice, repeat=2)) # 36 total outcomes

# Event A: Sum equal to 7
sum_7 = [outcome for outcome in sample_space if sum(outcome) == 7]
p_sum_7 = len(sum_7) / len(sample_space)

# Event B: Sum greater than or equal to 10
sum_gte_10 = [outcome for outcome in sample_space if sum(outcome) >= 10]
p_sum_gte_10 = len(sum_gte_10) / len(sample_space)

# Event C: At least one die shows 6
at_least_one_6 = [outcome for outcome in sample_space if 6 in outcome]
p_at_least_one_6 = len(at_least_one_6) / len(sample_space)

print("--- Two-Dice Roll Analysis (Total Outcomes: 36) ---")
print(f"P(Sum == 7):             {len(sum_7)}/36 = {p_sum_7:.4f}")
print(f"P(Sum >= 10):            {len(sum_gte_10)}/36 = {p_sum_gte_10:.4f}")
print(f"P(At least one 6):       {len(at_least_one_6)}/36 = {p_at_least_one_6:.4f}")