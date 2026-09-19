# Problem: Find maximum without max()

numbers = [10, 4, 25, 7, 18]

largest = numbers[0]

for number in numbers[1:]:
    if number > largest:
        largest = number

print(largest)
