from products import Product
from cart import ShoppingCart


def main():
    cart = ShoppingCart()

    laptop = Product("Laptop", 1200)
    mouse = Product("Mouse", 30)
    keyboard = Product("Keyboard", 80)

    cart.add_product(laptop)
    cart.add_product(mouse)
    cart.add_product(keyboard)

    cart.show_cart()
    cart.calculate_total()

if __name__ == "__main__":
    main()