"""A small introduction to Python generators."""


def count_up_to(limit):
    """Yield the numbers from 1 through limit, one at a time."""
    number = 1
    while number <= limit:
        yield number
        number += 1


def squares(numbers):
    """Yield the square of each value in an iterable."""
    for number in numbers:
        yield number**2


if __name__ == "__main__":
    # A generator produces values as they are requested.
    numbers = count_up_to(5)
    print(next(numbers))
    print(list(numbers))

    # Generators can be chained to process values lazily.
    print(list(squares(count_up_to(4))))
