# Agora vamos entrar em um assunto extremamente importante para qualquer desenvolvedor Python:
# Exception Handling (Tratamento de Exceções)
# O que é?
# Uma exceção é um erro que acontece durante a execução do programa.
# Exemplo:

# number = int(input("Enter a number: "))

# Se o usuário digitar:
# abc
# O programa quebra:
# ValueError
# Mas podemos tratar isso:
'''try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number.")'''
# Isso é fundamental em sistemas reais, APIs, bancos de dados e aplicações web.

