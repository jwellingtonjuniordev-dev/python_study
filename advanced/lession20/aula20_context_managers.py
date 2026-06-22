# Exercise 20.1
# Create:
# class FileManager
#
# Implement:
# __enter__()
# __exit__()
#
# When entering:
# Show:
# Opening file...
#
# When exiting:
# Show:
# Closing file...
#
# Example:
#
# with FileManager():
#     print("Reading file")

class FileManager:
    def __enter__(self):
        print("Opening file...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing file...")

with FileManager():
    print("Reading file...")

# Exercise 20.2
# Create:
# class DatabaseConnection
#
# __enter__()
# Connected.
#
# __exit__()
# Disconnected.
#
# Example:
#
# with DatabaseConnection():
#     print("Executing query...")

class DataBaseConnection:
    def __enter__(self):
        print("Connected.")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Disconnected.")

with DataBaseConnection():
    print("Executing query...")

# Mini Challenge
# Create:
# class ShoppingSession
#
# __enter__()
# Shopping session started.
#
# __exit__()
# Shopping session finished.
#
# Example:
#
# with ShoppingSession():
#     print("Adding products...")

class ShoppingSession:
    def __enter__(self):
        print(f"Shopping session started.")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Shopping session finished.")

with ShoppingSession():
    print(f"Adding products...")

# Extra Challenge ⭐⭐⭐
# Create:
# class TransactionSession
#
# __enter__()
# Start transaction.
#
# __exit__()
# End transaction.
#
# Use:
#
# with TransactionSession(account):
#
#     account.deposit(500)
#     account.withdraw(100)
#
# When leaving:
# Show account balance automatically.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self.history = []

    def deposit(self):
        amount = 0
        try:
            amount = float(input(f"Insert amount to deposit: \n"))
        except ValueError:
            print("Invalid Operation")
        if amount <= 0:
            print("Value is incorrect.")
            return

        self._balance += amount
        self.history.append(f"Deposit ${amount}")

    def withdraw(self):
        amount = 0
        try:
            amount = float(input(f"Insert amount to withdraw: \n"))
        except ValueError:
            print(f"Invalid Operation")
        if self._balance < amount:
            print(f"Insuficient fonds")
            return

        self._balance -= amount
        self.history.append(f"Withdraw ${amount}")

    def show_history(self):
        count = 1
        print(f"You went {len(self.history)} operations")
        for value in self.history:
            print(f"{count}° - {value}")
            count += 1

    def show_balance(self):
        print(f"{self.owner.capitalize()}, your balance is: ${self._balance:.2f}")

account = BankAccount("wellington", 0)

class TransactionSession:

    def __init__(self, account):
        self.account = account

    def __enter__(self):
        print("Start transaction.")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("End transaction.")
        self.account.show_balance()

def menu_account(account):
    menu = int(input(f"Insert your option:\n1- Deposit\n2- Withdraw\n3- Show operations history\n4- Exit\n"))
    while menu != 4:
        if menu == 1:
            account.deposit()
            menu = 0
        elif menu == 2:
            account.withdraw()
            menu = 0
        elif menu == 3:
            account.show_history()
            menu = 0
        elif menu == 4:
            print("End operations.")
            menu = 0
        elif menu == 0:
            menu = int(input(f"Insert your option:\n1- Deposit\n2- Withdraw\n3- Show operations history\n4- Exit\n"))
        else:
            print("Option incorrect!")


with TransactionSession(account):
    menu_account(account)