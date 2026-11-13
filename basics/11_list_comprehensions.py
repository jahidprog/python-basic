# List Comprehensions
# Build a new list from an iterable in a compact, readable way.

numbers = [1, 2, 3, 4, 5, 6]

# Transform every item: keep the squares of the numbers.
squares = [number**2 for number in numbers]
print("Squares:", squares)

# Filter items with a condition.
even_numbers = [number for number in numbers if number % 2 == 0]
print("Even numbers:", even_numbers)

# Combine filtering and transforming.
even_squares = [number**2 for number in numbers if number % 2 == 0]
print("Squares of even numbers:", even_squares)

# The equivalent loop can be easier to read for more complex logic.
loop_squares = []
for number in numbers:
    loop_squares.append(number**2)

print("Same result with a loop:", loop_squares)
