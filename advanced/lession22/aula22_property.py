# Agora vamos entrar em um recurso muito importante para encapsulamento elegante em Python.

# Até agora você fez coisas assim:

'''class Product:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value > 0:
            self.__price = value'''

# Isso funciona.
# Mas em Python existe uma forma melhor:

'''class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value'''

# Uso:

'''product = Product(100)
print(product.price)
product.price = 250'''

#Perceba a diferença:

#parece acesso normal a atributo;
#por trás, há validação;
#fica mais elegante e mais “Pythonic”.

# Exercise 22.1
# Create:
# class Product
#
# Private attribute:
# _price
#
# Create a @property:
# price
#
# Create a setter:
# price.setter
#
# Rule:
# price cannot be less than or equal to 0
#
# Test:
# product = Product(100)
# print(product.price)
# product.price = 250
# print(product.price)

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.price
    
    @price.setter
    def price(self, value):
        if value > 0:
            self.price = value
# Test:
product = Product(100)
print(product.price)
product.price = 250
print(product.price)

# Exercise 22.2
# Create:
# class Employee
#
# Private attribute:
# _salary
#
# Create:
# @property salary
# @salary.setter
#
# Rule:
# salary must be greater than 0
#
# Show the salary before and after updating it.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value > 0:
            self._salary = value

# Test:
employee = Employee("John", 5000)
print(f"Salary before update: {employee.salary}")
employee.salary = 6000
print(f"Salary after update: {employee.salary}")

# Mini Challenge
# Create:
# class BankAccount
#
# Private attribute:
# _balance
#
# Create:
# @property balance
#
# Do NOT create a setter for balance.
#
# Create methods:
# deposit(amount)
# withdraw(amount)
#
# Rule:
# balance can only change through deposit/withdraw
#
# Show:
# account.balance

class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    @property
    def balance(self):
        return self._balance    
    
# Test:
account = BankAccount(1000) 
print(f"Initial balance: {account.balance}")
account.deposit(500)
print(f"Balance after deposit: {account.balance}")
account.withdraw(300)
print(f"Balance after withdrawal: {account.balance}")

# Extra Challenge ⭐⭐⭐
# Create:
# class Student
#
# Attributes:
# name
# _grade
#
# Create:
# @property grade
# @grade.setter
#
# Rules:
# grade must be between 0 and 10
#
# Create:
# show_status()
#
# Rules:
# if grade >= 7:
#     "Approved"
# else:
#     "Failed"

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @property
    def grade(self):
        return self.grade
    
    @grade.setter
    def grade(self, value):
        if 0 <= value <= 10:
            self.grade = value

    def show_status(self):
        if self.grade >= 7:
            return "Approved"
        else:
            return "Failed"
        
# Test:
student = Student("Alice", 8)   
print(f"Student: {student.name}, Grade: {student.grade}, Status: {student.show_status()}")
student.grade = 6
print(f"Student: {student.name}, Grade: {student.grade}, Status: {student.show_status()}")
