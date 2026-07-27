# Create:
# class BankAccount
#
# Attributes:
#
# owner: str
# balance: float
# history: list[str]
#
# Methods:
#
# deposit(amount: float)
#
# withdraw(amount: float)
#
# show_history()
#
# Use Type Hints in EVERYTHING.
#
# Every attribute.
#
# Every parameter.
#
# Every return.

class BankAccount:
    def __init__(self):
        self.owner: str = "Guest"
        self._balance: float = 0.0
        self.history: list[str] = []

    def deposit(self, amount: float) -> None:

        if amount <= 0:
            print(f"Invalid operation")
        else:
            self._balance += amount
            self.history.append(f"Deposit ${amount:.2f}")

    def withdraw(self, amount: float) -> None:

        if amount > self._balance:
            print(f"Insuficient founds")
        else:
            self._balance -= amount
            self.history.append(f"Withdraw ${amount:.2f}")

    def show_history(self) -> None:
        for value in self.history:
            print(value)

account = BankAccount()

account.deposit(1000)
account.withdraw(200)
account.withdraw(150)
account.show_history()
