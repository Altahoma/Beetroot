class Product:
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.income = 0
        self.warehouse = {}

    def add(self, product, amount):
        product.price += product.price / 100 * 30
        self.warehouse[product] = self.warehouse.get(product, 0) + amount

    def sell_product(self, product_name, amount):
        for product, product_amount in self.warehouse.items():
            if product.name == product_name and product_amount >= amount:
                self.warehouse[product] = product_amount - amount
                self.income += product.price * amount
                return
        raise ValueError

    def set_discount(self, identifier, percent, identifier_type='name'):
        in_stock = False
        for product in self.warehouse.keys():
            if getattr(product, identifier_type) == identifier:
                in_stock = True
                product.price -= product.price / 100 * percent
        if not in_stock:
            raise ValueError

    def get_income(self):
        return self.income

    def get_all_products(self):
        result = [(product.name, amount, product.price) for product, amount in self.warehouse.items()]
        return result

    def get_product_info(self, product_name):
        for product, amount in self.warehouse.items():
            if product.name == product_name:
                return product.name, amount
        raise ValueError


product_1 = Product('Sport', 'Football T-Shirt', 100)
product_2 = Product('Food', 'Ramen', 1.5)

store = ProductStore()
store.add(product_1, 10)
store.add(product_2, 300)
store.sell_product('Ramen', 10)
store.set_discount('Sport', 50, 'type')

assert store.get_income() == 19.5
assert store.get_product_info('Ramen') == ('Ramen', 290)
assert store.get_all_products() == [('Football T-Shirt', 10, 65.0), ('Ramen', 290, 1.95)]
