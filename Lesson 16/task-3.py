class Product:
    pass


class ProductStore:
    pass


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
