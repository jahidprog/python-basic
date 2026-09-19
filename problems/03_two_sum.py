# Problem: Two Sum

def two_sum(numbers, target):
    seen = {}

    for index, number in enumerate(numbers):
        complement = target - number

        if complement in seen:
            return [seen[complement], index]

        seen[number] = index

    return []


print(two_sum([2, 7, 11, 15], 9))
