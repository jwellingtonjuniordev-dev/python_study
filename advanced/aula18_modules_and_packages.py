# FASE 18 — Modules and Packages
# O que são Modules?
# Um módulo é simplesmente um arquivo Python.
# Exemplo:
# math_utils.py
# Dentro dele:
#def add(a, b):
#    return a + b

# Em outro arquivo:
#from math_utils import add

#print(add(5, 3))

# Resultado:
# 8

# O que são Packages?
# São pastas contendo vários módulos.
# Exemplo:
# project/
# main.py
#utils/
#    __init__.py
#    math.py
#    text.py

# Você pode fazer:

#from utils.math import add
# Importações comuns
#import math

#print(math.sqrt(25))
#5
# Ou:
#from math import sqrt
#print(sqrt(25))
#Ou:
#import math as m
#print(m.pi)

# --------------------------------------------------------------------------------
# Exercise 18.1
# Crie um arquivo chamado:
# calculator.py
# Dentro dele:
#def add(a, b):
#def subtract(a, b):
#def multiply(a, b):
#def divide(a, b):
# Depois, em outro arquivo:
# main.py
# Importe as funções e teste todas.

#--------------------------------------------------------------------------------
# Exercise 18.2
# Crie um módulo:
# greetings.py
# Função:
# say_hello(name)
# Deve mostrar:
# Hello, Wellington!
# No arquivo principal:
# main.py
# Importe e utilize a função.

#--------------------------------------------------------------------------------
# Mini Challenge
# Crie um módulo:
# bank_utils.py
# Funções:
# deposit(balance, amount)
# withdraw(balance, amount)
# show_balance(balance)
# Depois crie:
# main.py
# Com um pequeno menu utilizando essas funções.

#--------------------------------------------------------------------------------
# Extra Challenge ⭐⭐⭐
# Vamos criar algo parecido com um projeto real.
# Estrutura:
# store/
# main.py
# products.py
# cart.py
# utils.py

# products.py
# Classe:
# class Product
# Atributos: name, price

# cart.py
# Classe:
# class ShoppingCart
# Métodos:
# add_product()
# remove_product()
# show_cart()
# calculate_total()

# utils.py
# Função:
# format_price(value)
# Exemplo: $1500.00

# main.py
# Criar produtos.
# Adicionar ao carrinho.
# Mostrar:
# Products:
# Laptop - $1200.00
# Mouse - $30.00
# Keyboard - $80.00
# Total: $1310.00