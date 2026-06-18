from utils import format_price


class ShoppingCart:
    def __init__(self):
        self.cart = []  # Lista de Product

    def add_product(self, product):
        self.cart.append(product)

    def remove_product(self, product_name):
        product_name = product_name.lower().strip()
        for product in list(self.cart):
            if product.name.lower().strip() == product_name:
                self.cart.remove(product)
                return True
        return False

    def show_cart(self):
        print("Products:")
        for product in self.cart:
            print(f"{product.name} - {format_price(product.price)}")

    def calculate_total(self):
        total = sum(product.price for product in self.cart)
        print(f"Total: {format_price(total)}")
        return total

