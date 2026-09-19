# Conditionals

age = 20

if age >= 18:
    print("Adult")
elif age > 0:
    print("Minor")
else:
    print("Invalid age")

# Ternary expression
status = "Adult" if age >= 18 else "Minor"
print(status)
