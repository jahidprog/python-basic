# Functions


def greet(name):
    """Return a friendly greeting for a person."""
    return f"Hello, {name}!"


def add_numbers(first, second=0):
    """Add two numbers; the second number is optional."""
    return first + second


def describe_person(name, *, city):
    """Show how a keyword-only argument works."""
    return f"{name} lives in {city}."


print(greet("Sam"))
print("Sum:", add_numbers(4, 6))
print("With the default:", add_numbers(4))
print(describe_person("Sam", city="Dhaka"))
