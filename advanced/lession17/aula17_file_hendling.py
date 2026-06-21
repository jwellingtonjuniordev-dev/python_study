# Tópico 17 — File Handling (Manipulação de Arquivos)
# O que é?
# É a capacidade do programa de:

# criar arquivos;
# abrir arquivos;
# ler informações;
# adicionar novas informações;
# alterar informações.

# Exemplos reais:

# 🏦 Banco:

# Deposit: $500
# Withdraw: $200

# 🛒 Mercado:

# Rice
# Beans
# Pasta

# 👥 Cadastro:

# John
# Mary
# Peter

# open()
# É a função usada para abrir arquivos.
# Exemplo:
# file = open("test.txt")
# Mas hoje quase nunca fazemos assim.

# Usamos:
# with open(...) as ...
# with
# O que faz?
# Abre o arquivo.
# Quando termina, fecha automaticamente.

# Exemplo:
# with open("test.txt", "r") as file:
#    print(file.read())

# Não precisamos fazer:
# file.close()
# O Python faz isso.

# Modos de abertura
# Read
# "r"
# Lê um arquivo.

# Write
# "w"
# Escreve.
# Se o arquivo existir:
# ⚠️ Apaga tudo.
# Exemplo:
# with open("test.txt", "w") as file:
#     file.write("Hello")

# Append
# "a"
# Adiciona conteúdo.
# Não apaga o existente.
# Exemplo:

# Arquivo:

# Hello

# Depois:

# with open("test.txt", "a") as file:
#     file.write("\nWorld")

# Resultado:
# Hello
# World

# read()
# Lê todo o arquivo.
# Exemplo:
# Apple
# Orange
# Banana
# print(file.read())

# Resultado:

# Apple
# Orange
# Banana

# write()
# Escreve texto.
# file.write("Python")

# "\n"
# Significa:
# Nova linha.

# Exemplo:
# file.write("Apple\n")
# file.write("Orange\n")

# Resultado:
# Apple
# Orange

# Exercise 17.1
# Crie uma classe:
# class Notes:
# Atributo: filename
# Método: save_note()
# Deve pedir:
# Write your note:
# Salvar no arquivo: notes.txt
# Use:
# with
# "a"
# write()
# Mostrar: Note saved.

# Exercise 17.2
# Na mesma classe:
# Crie: show_notes()
# Deve abrir: notes.txt
# Mostrar todas as notas.
# Use: read()
# Se o arquivo estiver vazio:
# No notes found.

class Notes:
    def __init__(self, filename):
        self.filename = filename

    def save_note(self):

        try:
            note = input("Write your note: \n").capitalize()

            with open(self.filename, "w") as file:
                file.write("Hello ")

            with open(self.filename, "a") as file:
                file.write(note)

            print(f"Note saved.")

        except FileNotFoundError:
            print("Not saved or file does not exists!")
            return
        
        if not note.strip():
            print("No text found")
            return
        
    def show_notes(self):

        try:
            with open(self.filename, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print(f"No notes found.")
            return
        
        if not self.filename:
            print(f"No notes found")
            
note = Notes("notes.txt")
note.save_note()
note.show_notes()

# Mini Challenge
# Crie uma classe: class ProductManager:
# Atributo: filename
# Método: save_product()
# Pedir: Product: Price:
# Salvar:
# Laptop - $1200
# Mouse - $30
# Keyboard - $80
# Arquivo: products.txt
# Crie: show_products()
# Mostrar todo o conteúdo.

class ProductManager:
    def __init__(self, filename):
        self.filename = filename

    def save_product(self):

        try:
            product = input("Insert product name: \n")
            price = float(input("Insert price: $ \n"))
            
            if not self.filename:
                with open(self.filename, "w") as file:
                    file.write(f"{product.capitalize()} - ${str(price)}\n")
                return

            with open(self.filename, "a") as file:
                file.write(f"{product.capitalize()} - ${str(price)}\n")

        except FileNotFoundError:
            print(f"Product not added")
            return
            
        if not self.filename:
            print(f"Eny product added")
            return
        
    def show_products(self):

        try:
            with open(self.filename, "r") as file:
                print(file.read())

        except FileNotFoundError:
            print(f"No product found.")
            return
        
        if not self.filename.strip():
            print(f"No product found")

products = ProductManager("products.txt")
products.save_product()
products.save_product()
products.save_product()
products.show_products()

# Extra Challenge
# Vamos evoluir novamente nosso sistema bancário.
# Crie: class BankAccount:
# Atributos: owner, balance, history_file
# deposit()
# Adicionar no arquivo:
# Deposit: $500
# withdraw()
# Adicionar:
# Withdraw: $200
# show_history()
# Ler o arquivo.
# Mostrar todas as operações.
# show_balance()
# Mostrar:
# Owner: Wellington
# Balance: $1500.00

# Pequeno desafio de arquitetura
# Tente fazer o construtor receber o nome do arquivo:

'''account = BankAccount(
    "Wellington",
    1000,
    "history.txt"
)'''

# Assim você poderá criar várias contas:

'''account1 = BankAccount(
    "John",
    500,
    "john.txt"
)

account2 = BankAccount(
    "Mary",
    900,
    "mary.txt"
)'''
# Cada uma com seu próprio histórico.

class BankAccount:
    def __init__(self, owner, balance, history_file):
        self._owner = owner
        self._balance = float(balance)
        self.history_file = history_file + ".txt"

    def deposit(self, amount):

        try:
            amount = float(amount)
            
            with open(self.history_file, "a") as file:
                file.write(f"Deposit: {amount:.2f}\n")

            if not self.history_file:
                with open(self.history_file, "w") as file:
                    file.write(f"Deposit: {amount:.2f}\n")
                return

        except ValueError:
            print(f"Invalid amount")
            return

        if amount <= 0:
            print(f"Invalid amount")
            return
        
        self._balance += amount

    def withdraw(self, amount):
        
        try:
            amount = float(amount)
            
            with open(self.history_file, "a") as file:
                file.write(f"Withdraw: {amount:.2f}\n")

            if not self.history_file:
                with open(self.history_file, "w") as file:
                    file.write(f"Withdraw: {amount:.2f}\n")
                return
            
        except ValueError:
            print(f"Invalid amount")
            return

        if amount <= 0 or self._balance < amount:
                print(f"Insuficient funds")
                return
        
        self._balance -= amount
        
    def show_history(self):
        try:
            with open(self.history_file, "r") as file:
                print(file.read(), end="")
        except FileNotFoundError:
            print("File not found")
            return

    def show_balance(self):

        if self._balance <= 0:
            print("Insuficient found")
        else:
            print(
                f"Owner: {self._owner.capitalize()}\n"
                f"Balance: ${self._balance:.2f}\n"
                f"{self._owner}.txt"
            )

account = BankAccount("wellington", 1000, "wellington")
account.deposit(100)
account.withdraw(50)
account.show_history()
account.show_balance()