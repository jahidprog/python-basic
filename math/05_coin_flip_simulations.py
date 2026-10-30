"""
Topic: Coin Flip Probability & Bernoulli Trials
Calculates theoretical probabilities and runs Monte Carlo simulations.
"""
import random

# Theoretical Probability
def coin_flip_theoretical(n_flips, target_heads):
    """
    Calculates exact probability of getting k heads in n flips:
    P(X = k) = (n choose k) * (0.5)^n
    """
    from math import comb
    ways = comb(n_flips, target_heads)
    prob = ways * (0.5 ** n_flips)
    return prob

# Empirical / Monte Carlo Simulation
def simulate_coin_flips(n_flips, target_heads, trials=100_000):
    successes = 0
    for _ in range(trials):
        # Simulate n_flips where 1 = Heads, 0 = Tails
        flips = [random.choice([0, 1]) for _ in range(n_flips)]
        if sum(flips) == target_heads:
            successes += 1
    return successes / trials

n = 10
k = 6
theo_p = coin_flip_theoretical(n, k)
sim_p = simulate_coin_flips(n, k, trials=50_000)

print("--- Coin Flip Probability (Getting exactly 6 Heads in 10 Flips) ---")
print(f"Theoretical Probability: {theo_p:.4f} ({theo_p * 100:.2f}%)")
print(f"Simulated Probability:   {sim_p:.4f} ({sim_p * 100:.2f}%)")