# Problem: Reverse a string

text = "python"

# Approach 1
print(text[::-1])

# Approach 2
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

print(reversed_text)
