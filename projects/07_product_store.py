# Product Store: 
# - Design & create an online store for products (name, price)
# - Track total products being created
# - Create a static method to calculate discount on each product based on a % parameters


class Product:
    cnt = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.cnt += 1

    def get_info(self):
        print(f"Product is {self.name} & price is {self.price}")

    @classmethod
    def total_product(cls):
        print(f"Total product in store: {cls.cnt}")

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (price  * discount / 100)
        print(f"Discounted Price is {final_price}")

p1 = Product("laptop", 50_000)
p2 = Product("Phone", 20_000)
p3 = Product("A", 2_000)
p4 = Product("B", 200)
p5 = Product("C", 200000)
p1.get_info()
p2.get_info()
p1.calc_discount(p2.price, 20)

Product.total_product()