# Tuples

coordinates = (10, 20)
person = ("Jahid", 25, "CSE")

print(coordinates)
print(coordinates[0])

name, age, department = person
print(name, age, department)

# Tuples are immutable:
# coordinates[0] = 100  # TypeError
