# instance, class, and static methods

class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} Storage with {self.storage_type} type")

l1 = Laptop("16gb", "512gb")
l1.get_info()