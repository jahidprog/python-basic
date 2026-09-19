# Problem: Frequency Count

text = "hello world"

frequency = {}

for char in text:
    if char != " ":
        frequency[char] = frequency.get(char, 0) + 1

print(frequency)
