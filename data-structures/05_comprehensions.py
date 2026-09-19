# Comprehensions

numbers = range(1, 11)

squares = [n ** 2 for n in numbers]
even_numbers = [n for n in numbers if n % 2 == 0]
square_map = {n: n ** 2 for n in numbers}

print(squares)
print(even_numbers)
print(square_map)
