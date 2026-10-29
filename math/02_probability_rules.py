"""
Topic: Basic Probability, Addition Rule, and Multiplication Rule
"""

# --- 1. Basic Probability ---
# Example: Rolling a fair 6-sided die
sample_space = {1, 2, 3, 4, 5, 6}
event_even = {2, 4, 6}

p_even = len(event_even) / len(sample_space)
print(f"P(Rolling an Even Number): {p_even:.4f}")

# --- 2. Addition Rule: P(A or B) = P(A) + P(B) - P(A and B) ---
# Example: Drawing a card from a standard 52-card deck
total_cards = 52
kings = 4
hearts = 13
king_of_hearts = 1

p_king = kings / total_cards
p_heart = hearts / total_cards
p_king_and_heart = king_of_hearts / total_cards

# Addition Rule formula
p_king_or_heart = p_king + p_heart - p_king_and_heart
print(f"P(King or Heart): {p_king_or_heart:.4f}")

# --- 3. Multiplication Rule: P(A and B) = P(A) * P(B|A) ---
# Example: Drawing 2 Aces in a row without replacement
aces = 4
p_first_ace = aces / total_cards
p_second_ace_given_first = (aces - 1) / (total_cards - 1)

p_two_aces = p_first_ace * p_second_ace_given_first
print(f"P(Two Aces in a row without replacement): {p_two_aces:.4f}")