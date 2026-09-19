# Mini Project: CLI Calculator

def calculator():
    print("🧮 CLI Calculator")

    a = float(input("First number: "))
    operator = input("Operator (+, -, *, /): ")
    b = float(input("Second number: "))

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b == 0:
            print("Cannot divide by zero.")
            return
        result = a / b
    else:
        print("Invalid operator.")
        return

    print("Result:", result)


if __name__ == "__main__":
    calculator()
