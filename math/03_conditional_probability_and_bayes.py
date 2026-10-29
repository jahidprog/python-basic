"""
Topic: Conditional Probability & Bayes' Theorem
"""

def conditional_probability(p_intersection, p_given_event):
    """
    Calculates P(A|B) = P(A ∩ B) / P(B)
    """
    return p_intersection / p_given_event

def bayes_theorem(p_b_given_a, p_a, p_b):
    """
    Calculates P(A|B) = (P(B|A) * P(A)) / P(B)
    """
    return (p_b_given_a * p_a) / p_b


# --- Conditional Probability Example ---
# P(Math and Science pass) = 0.40, P(Math pass) = 0.70
# What is P(Science pass | Math pass)?
p_math_and_sci = 0.40
p_math = 0.70
p_sci_given_math = conditional_probability(p_math_and_sci, p_math)

print("--- Conditional Probability ---")
print(f"P(Science | Math) = {p_sci_given_math:.4f}")

# --- Bayes' Theorem Example (Medical Test) ---
# P(Disease) = 0.01 (Prior)
# P(Test Positive | Disease) = 0.95 (Sensitivity)
# P(Test Positive | No Disease) = 0.05 (False Positive Rate)
p_disease = 0.01
p_no_disease = 0.99
p_pos_given_disease = 0.95
p_pos_given_no_disease = 0.05

# Total probability of testing positive: P(Pos) = P(Pos|Disease)*P(Disease) + P(Pos|No Disease)*P(No Disease)
p_positive = (p_pos_given_disease * p_disease) + (p_pos_given_no_disease * p_no_disease)

# Bayes' Theorem: P(Disease | Test Positive)
p_disease_given_pos = bayes_theorem(p_pos_given_disease, p_disease, p_positive)

print("--- Bayes' Theorem ---")
print(f"P(Disease | Positive Test) = {p_disease_given_pos:.4f}")