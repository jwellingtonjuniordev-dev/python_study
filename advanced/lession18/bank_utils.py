def deposit(balance, amount):

    if amount <= 0:
        print("Invalid operation")
        return balance

    balance += amount
    print("Deposit done!")

    return balance
    
def withdraw(balance, amount):

    if amount > balance:
        print(f"Don't have found")
        return
    else:
        print(f"Withdraw done!")
        balance -= amount

def show_balance(balance):

    return f"Your balace is ${balance:.2f}"