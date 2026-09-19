# Scope & Lambda

message = "global"


def show_scope():
    message = "local"
    print("Inside:", message)


show_scope()
print("Outside:", message)

square = lambda x: x * x
print(square(5))
