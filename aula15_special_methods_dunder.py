# Próxima etapa: Métodos Especiais (Magic Methods / Dunder Methods)
# O que são?
# São métodos especiais do Python que começam e terminam com dois underlines.
# Exemplo: 
'''__init__
__str__
__repr__
__len__
__add__'''

# Eles permitem que nossos objetos se comportem como tipos nativos do Python.
# Por exemplo: Quando fazemos:
# print("Python")
# Na verdade, o Python está usando métodos especiais internamente.

# O método __init__
# Você já conhece.
# Ele é chamado quando criamos um objeto.
'''
class Pessoa:

    def __init__(self, nome):
        self.nome = nome

p = Pessoa("Wellington")
'''
# O método __str__
# O que é?
# Define como o objeto será exibido para o usuário.
# Sem ele:
'''
class Produto:
    pass

produto = Produto()

print(produto)
'''
# Resultado: <__main__.Produto object at 0x00000123...>
# Pouco útil.

# Com __str__:
'''
class Produto:

    def __str__(self):
        return "Produto do sistema"

produto = Produto()

print(produto)
'''
# Resultado: Produto do sistema
# Muito melhor.

# Exercício 15.1
# Crie uma classe: class Pessoa
# Atributos: nome, idade
# Implemente: __str__()
# Ao imprimir o objeto deve aparecer: Wellington, 33 anos.

class Person:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} anos"

person = Person("Wellington", 33)
print(person)

# O método __len__
# O que faz?
# Permite usar: len(objeto)
# Exemplo:
'''
class Time:

    def __init__(self):
        self.jogadores = ["Ana","Carlos","Pedro"]

    def __len__(self):
        return len(self.jogadores)

time = Time()

print(len(time))
'''
# Resultado: 3

# Exercicio 15.2
# Crie: class Biblioteca
# Ela deve armazenar uma lista de livros.
# Implemente: __len__()
# Ao fazer: 
# biblioteca = Biblioteca() 
# print(len(biblioteca))
# Deve mostrar a quantidade de livros.

class Biblioteca:

    def __init__(self):
        self.books = ["O monge e o executivo", "O segredo da mente milionária", "Pai rico pai pobre"]

    def __len__(self):
        return len(self.books)
    
biblioteca = Biblioteca()
print(len(biblioteca))

# mini desafio
# Crie: class Carrinho
# Atributo: produtos
# Implemente: __len__()
# Para retornar a quantidade de produtos.
# Exemplo:
'''Feijão
Arroz
Macarrão'''
# Resultado: 3

class Carrinho:

    def __init__(self):
        self.produtos = ["Alface", "Tomate", "Azeitona", "Cebola"]

    def __len__(self):
        return len(self.produtos)
    
carrinho = Carrinho()
print(len(carrinho))

# Desafio Extra
# Vamos fazer algo muito próximo do mercado.
# Crie uma classe: class ContaBancaria
# Atributos: titular, saldo
# Implemente: __str__
# Quando fizer: print(conta)
# Mostrar: Conta de Wellington.
# Saldo: R$ 1500.00
# Implemente também: __len__
# A conta terá: historico_operacoes
# Sempre que houver: depósito / saque
# adicione uma descrição na lista.
# Exemplo:
'''Depósito de R$100
Saque de R$50
Depósito de R$300'''
# Então: len(conta)
# deve retornar: 3

class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self.depositos = []
        self.saques = []
        self.historico_operacoes = []

    def __str__(self):
        return f"Conta de {self._titular}, saldo atual de R${self._saldo}"
    
    def __len__(self):
        return len(self.historico_operacoes)

    def depositar(self, valor):
        if valor <= 0:
            print(f"Operação inválida")
        else:
            self._saldo += valor
            self.historico_operacoes.append(f"Depósito de R${valor:.2f}")
            self.depositos.append(valor)

    def sacar(self, valor):
        if valor > self._saldo:
            print(f"Você não tem saldo suficiente!")
        else:
            self._saldo -= valor
            self.historico_operacoes.append(f"Saque de R${valor}")
            self.saques.append(valor)

    def historico(self):
        print(f"Você fez um total de {len(self.historico_operacoes)} operações na sua conta esse mês!")
        print(f"Seu histórico é:")
        for valor in self.historico_operacoes:
            print(f"{valor}")
        print(f"Total depositado R${sum(self.depositos):.2f}\nTotal sacado R${sum(self.saques):.2f}")

conta1 = ContaBancaria("Wellington", 1500)
print(conta1)
conta1.depositar(1750.75)
conta1.depositar(300.42)
conta1.depositar(1787.34)
conta1.sacar(100)
conta1.sacar(350.50)
print(len(conta1))
conta1.historico()