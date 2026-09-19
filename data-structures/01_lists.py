# Lists

numbers = [10, 20, 30, 40]

numbers.append(50)
numbers.insert(0, 5)
numbers.remove(20)

print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])

for number in numbers:
    print(number)

squares = [number ** 2 for number in numbers]
print(squares)
