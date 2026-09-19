# Parameters & Arguments

def introduce(name, age=18, *, city="Unknown"):
    return f"{name} is {age} years old and lives in {city}."

print(introduce("Jahid", 25, city="Chittagong"))
print(introduce("Alex"))


def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))


def profile(**info):
    return info

print(profile(name="Jahid", role="Developer"))
