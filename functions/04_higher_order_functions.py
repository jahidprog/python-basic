# Higher-order Functions

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(doubled)
print(evens)


def apply_operation(value, operation):
    return operation(value)

print(apply_operation(5, lambda x: x ** 2))
