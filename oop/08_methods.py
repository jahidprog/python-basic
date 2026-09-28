# instance, class, and static methods

class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"storage type {cls.storage_type}")

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} Storage with {self.storage_type} type")

    def calc_discount(price, discount):
        final_price = price - (discount * price/100)
        print(f"Discounted Price is {final_price}")

l1 = Laptop("16gb", "512gb")
l1.get_info()

Laptop.get_storage_type()
Laptop.calc_discount(40_000, 10) # 40_000 == 40000 (underscore is show the separation in int)