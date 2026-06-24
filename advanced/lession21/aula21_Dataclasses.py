# Próxima etapa (Aula 21)
# Agora entramos em algo que você verá muito em:
# Problema atual:

'''class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price'''

# Imagine uma classe com 15 atributos.
# Você escreve muito código repetitivo.
# Com Dataclass:

'''from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float'''

# Pronto.
# Python cria automaticamente:
# __init__
# __repr__
# __eq__
# para você.

# Exercise 21.1
# Create:
# @dataclass
# class Person
#
# Attributes:
# name
# age
#
# Create an object and print it.

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

person1 = Person("Wellington", 33)
print(f"Hello {person1.name.capitalize()}, you're {person1.age} years old.")

# Exercise 21.2
# Create:
# @dataclass
# class Product
#
# Attributes:
# name
# price
# stock
#
# Create 3 products and print them.

@dataclass
class Product:
    name: str
    price: float
    stock: int

product1 = Product("Laptop", 1200, 4)
product2 = Product("Mouse", 35, 7)
product3 = Product("Keyboard", 70, 5)

products = []
products.append(product1)
products.append(product2)
products.append(product3)

for product in products:
    print(f"Name: {product.name} | Price: ${product.price}")

# Mini Challenge
# Create:
# @dataclass
# class Book
#
# Attributes:
# title
# author
# pages
#
# Store 3 books in a list.
#
# Show all books.

@dataclass
class Book:
    title: str
    author: str
    pages: int

books = []

book1 = Book("Pai Rico, Pai Pobre", "Robert T. Kiyosaki", 336)
book2 = Book("O Segredo da Mente Milionária", "T. Harv Eker", 176)
book3 = Book("O Monge e o Executivo", "James C. Hunter", 144)

books.append(book1)
books.append(book2)
books.append(book3)

for book in books:
    print(f"Title: {book.title} |---| Author: {book.author} |---| Pages: {book.pages}")

# Extra Challenge ⭐⭐⭐
# Create:
# @dataclass
# class BankTransaction
#
# Attributes:
# operation
# amount
#
# Example:
#
# BankTransaction(
#     "Deposit",
#     500
# )
#
# Store transactions inside BankAccount.
#
# Show:
#
# Deposit - $500
# Withdraw - $200
# Deposit - $1000

@dataclass
class BankTransaction:
    operation: str
    amount: float

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner.capitalize()
        self._balance = balance
        self.history = []

    def add_transactions(self, transaction: BankTransaction):
    
        operation = transaction.operation.capitalize()
        amount = float(transaction.amount)

        if amount <= 0:
            print(f"Invalid Operation")
            return
        
        if operation == "Deposit":
            self._balance += amount
            self.history.append(transaction)
            
        elif operation == "Withdraw":
            if amount > self._balance:
                print("Insuficient founds.")
                return
            
            self._balance -= amount
            self.history.append(transaction)

        else:
            print("Invalid Operation.")

    def show_history(self):
        if not self.history:
            print("No transactions found.")
            return
            
        for transaction in self.history:
            print(f"{transaction.operation.capitalize()} - ${transaction.amount:.2f}")

    def show_balance(self):
        return print(f"{self.owner}, your balance is ${self._balance:.2f}")
    
class TransactionSessions:
    def __init__(self, account):
        self.account = account

    def __enter__(self):
        print("Start transaction.")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("End transaction.")
        self.account.show_balance()
    
account = BankAccount("wellington", 0)

with TransactionSessions(account):
    transaction1 = BankTransaction("deposit", 500)
    transaction2 = BankTransaction("withdraw", 200)
    transaction3 = BankTransaction("deposit", 1000)
    account.add_transactions(transaction1)
    account.add_transactions(transaction2)
    account.add_transactions(transaction3)
    account.show_history()