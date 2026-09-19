# Abstraction

from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        return f"Paid ${amount} using credit card."


payment = CreditCardPayment()
print(payment.pay(100))
