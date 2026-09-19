# Problem: Find the number that appears once.
# Every other number appears exactly twice.

def single_number(numbers):
    result = 0

    for number in numbers:
        result ^= number

    return result


print(single_number([4, 1, 2, 1, 2]))
