# Agora vamos entrar em um assunto extremamente importante para qualquer desenvolvedor Python:
# Exception Handling (Tratamento de Exceções)
# O que é?
# Uma exceção é um erro que acontece durante a execução do programa.
# Exemplo:

number = int(input("Enter a number: "))

# Se o usuário digitar:
# abc
# O programa quebra:
# ValueError
# Mas podemos tratar isso:
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number.")
# Isso é fundamental em sistemas reais, APIs, bancos de dados e aplicações web.

# Exercise 16.1
# Crie uma classe em inglês.
# class Calculator:
# Método: divide()
# O método deve:
# receber dois números; tentar dividir; se o divisor for zero:
# Mostrar:
# Cannot divide by zero.
# Caso contrário:
# Result: ...
# Use:
# try
# except

class Calculator:
    def __init__(self):
        self.result = 0

    def divide(self, value1, value2):
        if value2 == 0:
            print(f"Cannot divide by zero")
        else:
            try:
                self.result = value1 / value2
                print(f"The divide is: {self.result}")
            except ValueError:
                print(f"You cant't show this division")
            

calculator1 = Calculator()
calculator1.divide(12, 3)
calculator1.divide(5, 0)

# Exercise 16.2
# Crie: class User:
# Método: set_age()
# O método deve: pedir uma idade; converter para inteiro;
# Se o usuário digitar texto:
# Invalid age.
# Caso contrário:
# Age registered successfully.
# Use:
# try
# except ValueError

class User:
    def __init__(self):
        self.age = 0

    def set_age(self):
        entry = input(f"Insert your age ")
        try:
            self.age = int(entry)
            print(f"Age registered successfully")
        except ValueError:
            print(f"Invalid age")

user1 = User()
user1.set_age()

# Mini Challenge
# Crie: class ShoppingCart:
# Atributos: products, prices
# Método: add_product()
# Deve pedir: Product name:, Product price:
# Se o preço não for numérico: Invalid price.
# Caso contrário, adicionar o produto.
# Crie também:
# show_products()
# Mostrando: Laptop - $1200, Mouse - $20, Keyboard - $80

class ShoppingCart:
    def __init__(self):
        self.list_products = []
        self.produtct_name = ''
        self.product_price = 0
        self.products = {}

    def add_product(self):
        prod_name = input(f"Insert the product name:\n")
        prod_price = input(f"Insert the price:\n")

        if prod_name.isdigit():
            print(f"The product's name cannot have numbers, please insert correct name")
        else:
            self.product_name = prod_name.capitalize()

        try:
            self.product_price = float(prod_price)
            self.products = {"name": self.product_name, "price":self.product_price}
            self.list_products.append(self.products.copy())
            print(f"Product added")
        except ValueError:
            print(f"Invalid price")

    def show_products(self):

        for product in self.list_products:
            print(
                f"Product: {product["name"]} | "
                f"Price ${product["price"]:.2f}"
            )

shopping_cart = ShoppingCart()
shopping_cart.add_product()
shopping_cart.add_product()
shopping_cart.add_product()
shopping_cart.show_products()

