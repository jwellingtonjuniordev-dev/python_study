'''Exercise 23.1

(Código em inglês, conforme combinamos.)

Crie:

class Calculator

Implemente:

@staticmethod

Métodos:

add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)

Teste:

print(Calculator.add(5, 3))
print(Calculator.divide(20, 4))'''

class Calculator: 

    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        return a / b
    
print(Calculator.add(5, 3))
print(Calculator.divide(20, 4))

'''
Exercise 23.2

Crie:

class User

Atributo:

name

Implemente:

@classmethod

Método:

guest()

Ele deve criar automaticamente:

Guest

Uso:

user = User.guest()

print(user.name)

Resultado:

Guest
'''

class User:
    def __init__(self, name):
        self.name = name

    @classmethod
    def guest(cls):
        return cls("Guest")
    
user = User.guest()
print(user.name)

user2 = User("Wellington")
print(user2.name)

'''
Mini Challenge

Crie:

class Temperature

Implemente dois métodos estáticos:

celsius_to_fahrenheit()

fahrenheit_to_celsius()

Exemplo:

25°C → 77°F

86°F → 30°C
'''

class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
print(Temperature.celsius_to_fahrenheit(25))
print(Temperature.fahrenheit_to_celsius(86))