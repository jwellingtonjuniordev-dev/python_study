"""
Extra Challenge ⭐⭐⭐⭐

Vamos evoluir novamente seu sistema bancário.

Crie:

class BankAccount

Atributos:

owner
balance

Implemente:

Método de instância
deposit()
withdraw()
show_balance()
Static Method
validate_amount(amount)

Regras:

retorna True se o valor for maior que zero.
retorna False caso contrário.

Todos os depósitos e saques devem usar essa validação.

Class Method
create_default_account()

Ela deve retornar automaticamente:

Owner:
Anonymous

Balance:
0

Exemplo:

account = BankAccount.create_default_account()

account.show_balance()

Resultado:

Owner: Anonymous
Balance: $0.00
"""

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if self.validate_amount(amount):
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if self.validate_amount(amount) and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def show_balance(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: ${self.balance:.2f}")

    @staticmethod
    def validate_amount(amount):
        return amount > 0

    @classmethod
    def create_default_account(cls):
        return cls("Anonymous", 0.0)
    
account = BankAccount.create_default_account()
account.show_balance()

my_account = BankAccount("John Doe", 100.0)
my_account.deposit(50)
my_account.withdraw(30)
my_account.show_balance()

other_account = BankAccount("Jane Smith", 200.0)
other_account.withdraw(30)
other_account.show_balance()