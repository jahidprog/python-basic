try:
    x = int(input("Enters x = "))
    ans = 10/x
except ZeroDivisionError:
    print("Divide by Zero is not allowed!!")
except ValueError:
    print("Invalid input")
else:
    print(ans)