# Encapsulation

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, password):
        return self.__password == password


user = User("jahid", "secret123")

print(user.username)
print(user.check_password("secret123"))
print(user.check_password("wrong"))
