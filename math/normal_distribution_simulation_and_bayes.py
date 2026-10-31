import numpy as np

rng = np.random.default_rng(42)

# Simulate 1,000 exam scores from a normal distribution
scores = rng.normal(loc=70, scale=10, size=1000)
print("Simulated mean:", round(float(np.mean(scores)), 2))
print("Simulated standard deviation:", round(float(np.std(scores)), 2))
print("Estimated P(score >= 80):", round(float(np.mean(scores >= 80)), 3))

# Bayes' theorem: simplified spam detector
p_spam = 0.30
p_not_spam = 1 - p_spam
p_word_given_spam = 0.80
p_word_given_not_spam = 0.10

p_word = p_word_given_spam * p_spam + p_word_given_not_spam * p_not_spam
p_spam_given_word = p_word_given_spam * p_spam / p_word

print("\nP(Word appears):", round(p_word, 3))
print("P(Spam | Word appears):", round(p_spam_given_word, 3))
