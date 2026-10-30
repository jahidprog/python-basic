"""
Topic: Combinatorics (Permutations & Combinations)
Solves arrangement and selection problems.
"""
import math

def permutations(n, r):
    # nP_r = n! / (n - r)!
    return math.perm(n, r)

def combinations(n, r):
    # nC_r = n! / (r! * (n - r)!)
    return math.comb(n, r)

# Example 1: Selecting a 3-person committee from 10 people (Order doesn't matter)
committee_ways = combinations(10, 3)

# Example 2: Assigning President, VP, and Secretary from 10 people (Order matters)
roles_ways = permutations(10, 3)

# Example 3: Probability of drawing 3 Hearts from a 52-card deck
total_hand_ways = combinations(52, 3)
heart_hand_ways = combinations(13, 3)
p_3_hearts = heart_hand_ways / total_hand_ways

print("--- Combinatorics Examples ---")
print(f"Ways to pick 3 committee members from 10: {committee_ways}")
print(f"Ways to assign 3 distinct roles from 10: {roles_ways}")
print(f"P(Drawing 3 Hearts out of 3 cards):      {p_3_hearts:.6f}")