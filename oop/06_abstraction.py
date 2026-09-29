# Abstraction

from abc import ABC, abstractmethod


# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass


# class CreditCardPayment(Payment):
#     def pay(self, amount):
#         return f"Paid ${amount} using credit card."


# payment = CreditCardPayment()
# print(payment.pay(100))

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar !!")

class Cat(Animal):
    def make_sound(self):
        print("Meow !!")

lion = Lion()
lion.make_sound()

cat = Cat()
cat.make_sound()
