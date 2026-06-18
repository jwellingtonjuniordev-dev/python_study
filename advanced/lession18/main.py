import calculator
import greetings as greet
import bank_utils as bank

print(calculator.add(3, 6))
print(calculator.subtract(12, 3))
print(calculator.multiply(3, 3))
print(calculator.divide(18, 2))

print(greet.say_hello("wellington"))

amount = 0
balance = 0
menu = 0

while menu != 4:
    menu = int(input(f"Wellington, Welcome to bank system!\nPlease, select a option\n1- Deposit\n2- Withdraw\n3- Show balance\n4- Exit\n"))
    if menu == 1:
        amount = float(input("Insert the amount $: "))
        balance = bank.deposit(balance, amount)
    elif menu == 2:
        amount = float(input("Insert the amount $: "))
        balance = bank.withdraw(balance, amount)
    elif menu == 3:
        print(bank.show_balance(balance))
    elif menu == 4:
        print(f"Exit...")
    else:
        print("Insert a correct option")
        continue

