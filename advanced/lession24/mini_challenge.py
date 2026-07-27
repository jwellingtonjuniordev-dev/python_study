# Create:
# class ShoppingCart
#
# Attribute:
# products -> list[str]
#
# Methods:
#
# add_product(product: str)
#
# show_products()

class ShoppingCart:
    def __init__(self):
        self.products:  list[str] = []

    def add_product(self, product: str) -> None:
        self.products.append(product)

    def show_products(self) -> None:
        for product in self.products:
            print(product)

shopping = ShoppingCart()
shopping.add_product("Laptop")
shopping.add_product("Mouse")
shopping.add_product("Keyboard")
shopping.show_products()