from functools import wraps

# Iterators, Generators and Decorators
# Hoje vamos aprender três conceitos muito importantes do Python moderno.

# 1. Iterators
# O que são?
# Um iterador é um objeto capaz de retornar um elemento por vez.
# Na verdade, quando fazemos:

'''for item in list:
    print(item)'''

# O Python faz algo parecido com:

'''iterator = iter(list)

print(next(iterator))
print(next(iterator))
print(next(iterator))'''

# Cada chamada de next() retorna um elemento.
# Quando não há mais elementos: StopIteration

# Exemplo: 
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# 2. Generators
# O que são?
# São funções especiais que produzem valores sob demanda.
# Ao invés de: return
# usamos: yield
# A função "pausa" e continua de onde parou.

def count():
    yield 1
    yield 2
    yield 3

for number in count():
    print(number)

# Vantagem
# Imagine:

'''Lista:

numbers = [1,2,3,...1000000]'''

# Toda a memória é ocupada.
# Generator:

def generate():
    for i in range(1000000):
        yield i

# Só gera quando necessário.
# Muito utilizado em:

#APIs;
#leitura de arquivos grandes;
#processamento de dados;
#FastAPI;
#Data Science.

# 3. Decorators
# O que são?
# São funções que modificam o comportamento de outras funções.
# Exemplo simples:

def decorator(function):

    def wrapper():
        print("Before")
        function()
        print("After")
    return wrapper

# Uso:

@decorator
def hello():
    print("Hello")

# Exercise 19.1
# Crie uma função: def number_generator():
# Ela deve usar:
# yield
# Para produzir: 1, 2, 3, 4, 5
# Depois percorra usando:
# for number in number_generator():
# Mostrando todos os números.

def number_generator():
    for number in range(1, 6):
        yield number

for n in number_generator():
    print(f"{n}° número: {n}")

# Exercise 19.2
# Crie uma função: def word_generator():
# Usando: yield
# Para produzir: Python, Backend, Developer
# Percorra usando: for

def word_generator():
    words = ["Python", "Backend", "Developer"]
    for word in words:
        yield word 

for word in word_generator():
    print(word)

# Mini Challenge
# Crie uma classe:
# class BookCollection:
# Atributo: books
# Exemplo: Python, FastAPI, Django, Docker
# Implemente: __iter__()
# Para permitir:
# library = BookCollection()
# for book in library:
    # print(book)
# Resultado: Python, FastAPI, Django, Docker

class BookCollection:
    def __init__(self):
        self.books = ["Python", "FastAPI", "Django", "Docker"]

    def __iter__(self):
        return iter(self.books)
    
library = BookCollection()

for book in library:
    print(book)

# Extra Challenge ⭐⭐⭐
# Vamos evoluir novamente nosso sistema bancário.
# Crie: class BankAccount:
# Atributos: owner, balance, transactions
# Onde: transactions
# é uma lista.
# Exemplo: Deposit $100, Withdraw $50, Deposit $300, Withdraw $25
# Método: deposit()
# Adicionar operação.
# Método withdraw()
# Adicionar operação.
# Implemente __iter__()
# Para permitir:
#for transaction in account:
    #print(transaction)
# Resultado: Deposit $100, Withdraw $50, Deposit $300, Withdraw $25

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self.transactions = []

    def __iter__(self):
        return iter(self.transactions)

    def deposit(self):
        try:
            amount = float(input("Insert amount to deposit: \n"))
        except ValueError:
            print(f"Amount invalid!")
            return
        if amount <= 0:
            print(f"Amount invalid!")
            return
        
        self.transactions.append(f"Deposit ${amount}")
        self._balance += amount

    def withdraw(self):
        try:
            amount = float(input("Insert amount to withdraw: \n"))
        except ValueError:
            print(f"Invalid Operation")
            return
        if self._balance < amount:
            print(f"Invalid operation!")
            return
        
        self.transactions.append(f"Withdraw ${amount}")
        self._balance -= amount

    def show_balance(self):
        return print(f"{self.owner.capitalize()}, your balance is ${self._balance:.2f}")

account = BankAccount("Wellington", 1200)
account.deposit()
account.deposit()
account.withdraw()
account.withdraw()
for transaction in account:
    print(f"Transaction: {transaction}")
account.show_balance()

# Desafio Bônus ⭐⭐⭐⭐
# Vamos criar seu primeiro decorator.
# Crie: def logger(function):
# Sempre que uma função for chamada:
# Mostrar:
# Starting operation...
# ...
# Operation finished.
# Exemplo:
# @logger
# def calculate():
    # print("Calculating...")
#Resultado:
#Starting operation...
#Calculating...
#Operation finished.

def logger(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Starting operation...")
        result = function(*args, **kwargs)
        print(f"Operation finished.")
        return result
    return wrapper

@logger
def show_history():
    for transaction in account:
        print(f"Transaction: {transaction}")

show_history()