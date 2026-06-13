# Agora vamos entrar em um assunto extremamente importante para qualquer desenvolvedor Python:
# Exception Handling (Tratamento de Exceções)
# O que é?
# Uma exceção é um erro que acontece durante a execução do programa.
# Exemplo:

number = int(input("Enter a number: "))

# Se o usuário digitar:
# abc
# O programa quebra:
# ValueError
# Mas podemos tratar isso:
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number.")
# Isso é fundamental em sistemas reais, APIs, bancos de dados e aplicações web.

# Exercise 16.1
# Crie uma classe em inglês.
# class Calculator:
# Método: divide()
# O método deve:
# receber dois números; tentar dividir; se o divisor for zero:
# Mostrar:
# Cannot divide by zero.
# Caso contrário:
# Result: ...
# Use:
# try
# except

class Calculator:
    def __init__(self):
        self.result = 0

    def divide(self, value1, value2):
        if value2 == 0:
            print(f"Cannot divide by zero")
        else:
            try:
                self.result = value1 / value2
                print(f"The divide is: {self.result}")
            except ValueError:
                print(f"You cant't show this division")
            

calculator1 = Calculator()
calculator1.divide(12, 3)
calculator1.divide(5, 0)

# Exercise 16.2
# Crie: class User:
# Método: set_age()
# O método deve: pedir uma idade; converter para inteiro;
# Se o usuário digitar texto:
# Invalid age.
# Caso contrário:
# Age registered successfully.
# Use:
# try
# except ValueError

