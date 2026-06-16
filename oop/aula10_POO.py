# Próxima etapa: Programação Orientada a Objetos (POO)
# Programação Orientada a Objetos é uma forma de organizar o código usando objetos que representam coisas do mundo real.
'''A partir daqui você vai aprender:

classes;
objetos;
atributos;
métodos;
encapsulamento.

Isso é importante porque frameworks como:

Django
FastAPI

utilizam orientação a objetos constantemente.'''

# Exercício 10.1
# Crie uma classe:
# class Pessoa:
# com: nome, idade
# E um método:
# apresentar()
# que mostre: Olá, meu nome é Wellington e tenho 33 anos.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos")

wellington = Pessoa("Wellington", 33)
wellington.apresentar()

# Exercício 10.2
# Crie a classe: class Produto:
# Atributos: nome, preco, estoque
# Método: mostrar_produto()

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def mostrar_produto(self):
        print(f"Produto: {self.nome} | R$ {self.preco:.2f} | Tem {self.estoque} em estoque!")

    def calcular_total(self):
        print(f"O valor do total em estoque do produto é de R${self.preco * self.estoque:.2f}")

wheyprotein = Produto("Whey Zumub", 27.90, 3)
wheyprotein.mostrar_produto()
wheyprotein.calcular_total()

# Exercício 10.3
# Crie a classe: class Carro:
# Atributos: marca, modelo, ano
# Método: detalhes()

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def detalhes(self):
        print(f"O carro da marca {self.marca}, modelo {self.modelo}, ano de fabricação {self.ano}")

bmw = Carro("BMW", "iX", 2023)
bmw.detalhes()

# Mini desafio
# Crie uma classe: class ContaBancaria:
# Com: titular, saldo
# Métodos: depositar(), sacar(), mostrar_saldo()

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            print(f"Você precisa inserir um valor válido!")
        else:
            self.saldo += valor
            print(f"Você fez um depósito de ${valor:.2f}")

    def sacar(self, valor):
        if valor > self.saldo:
            print("Você não tem saldo suficiente para essa operaçãoS!")
        else:
            self.saldo -= valor
            print(f"Você fez um saque de ${valor:.2f}")

    def mostrar_saldo(self):
        if self.saldo <= 0:
            print(f"Não há saldo na sua conta")
        else:
            print(f"Senhor(a) {self.titular}, seu saldo atual é de ${self.saldo:.2f}")

conta1 = ContaBancaria("Wellington Júnior", 100)
conta1.sacar(50)
conta1.sacar(25.37)
conta1.mostrar_saldo()
conta1.depositar(1288.89)
conta1.mostrar_saldo()