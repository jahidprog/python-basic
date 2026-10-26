# Probability examples using a simple email dataset

total_emails = 100
spam = 30
emails_with_link = 40
spam_and_link = 18

p_spam = spam / total_emails
p_link = emails_with_link / total_emails
p_not_spam = 1 - p_spam
p_spam_and_link = spam_and_link / total_emails

# Conditional probability: P(Spam | Link)
p_spam_given_link = p_spam_and_link / p_link

# Union rule: P(Spam OR Link)
p_spam_or_link = p_spam + p_link - p_spam_and_link

print(f"P(Spam): {p_spam:.2f}")
print(f"P(Not Spam): {p_not_spam:.2f}")
print(f"P(Link): {p_link:.2f}")
print(f"P(Spam AND Link): {p_spam_and_link:.2f}")
print(f"P(Spam OR Link): {p_spam_or_link:.2f}")
print(f"P(Spam | Link): {p_spam_given_link:.2f}")

# Independence: P(A and B) must equal P(A) * P(B)
print("P(Spam) * P(Link):", round(p_spam * p_link, 2))
print("Independent?", abs(p_spam_and_link - p_spam * p_link) < 1e-9)
