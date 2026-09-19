# Attributes & Methods

class BankAccount:
    bank_name = "Python Bank"  # class attribute

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance.")


account = BankAccount("Jahid", 1000)
account.deposit(500)
account.withdraw(200)

print(account.owner)
print(account.balance)
print(account.bank_name)
