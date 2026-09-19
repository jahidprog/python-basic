# Sets

numbers = {1, 2, 3, 3, 4, 4}

print(numbers)  # duplicates removed

numbers.add(5)
numbers.remove(1)

print(numbers)

a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
