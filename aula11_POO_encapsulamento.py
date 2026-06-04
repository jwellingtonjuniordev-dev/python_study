# Conceito novo: Encapsulamento 
# Agora vamos para o próximo pilar da POO.
# O que é Encapsulamento? É proteger os dados do objeto contra alterações indevidas.
# Imagine uma conta bancária.
# Isso seria perigoso: conta.saldo = 1000000
# Qualquer pessoa poderia alterar.

# Exercício 11.1
# Crie uma classe: class Funcionario:
# Atributos privados: __nome, __salario
# Métodos: get_nome(), get_salario()

class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def get_nome(self):
        return self.__nome
    
    def get_salario(self):
        return self.__salario

funcionario1 = Funcionario("wellington", 1380.95)
print(f"Olá {funcionario1.get_nome().capitalize()}")
print(f"{funcionario1.get_nome().capitalize()}, seu salário é ${funcionario1.get_salario():.2f}")

# Exercício 11.2
# Crie uma classe: class Produto:
# Atributos privados: __nome, __preco
# Métodos: get_nome(), get_preco(), set_preco()
# O preço não pode ser negativo.

class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    def set_preco(self, value):
        if value > 0:
            self.__preco = value
            return self.__preco
        
produto1 = Produto("Maçã", 2.99)
print(f"Produto: {produto1.get_nome()}")
print(f"Preço $ {produto1.get_preco():.2f}")
produto1.set_preco(3.99)
print(f"Preço $ {produto1.get_preco():.2f}")

# Mini desafio 11
# Crie uma classe: class ContaBancaria:
# com: __titular, __saldo
# Métodos: depositar(), sacar(), get_saldo()

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return self.__saldo
        
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return self.__saldo
        
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
conta1 = ContaBancaria("Wellington", 100)
print(f"Olá {conta1.get_titular()}, seu saldo é ${conta1.get_saldo():.2f}")
conta1.depositar(500)
print(f"Olá {conta1.get_titular()}, seu saldo é ${conta1.get_saldo():.2f}")
conta1.sacar(200)
print(f"Olá {conta1.get_titular()}, seu saldo é ${conta1.get_saldo():.2f}")

# Desafio extra
# Transforme seu sistema bancário atual usando encapsulamento.
# Regras: saldo privado; titular privado; nenhuma alteração direta; todas as operações passando pelos métodos.

class NovaContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            print(f"Você precisa inserir um valor válido!")
        else:
            self.__saldo += valor
            print(f"Você fez um depósito de ${valor:.2f}")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Você não tem saldo suficiente para essa operaçãoS!")
        else:
            self.__saldo -= valor
            print(f"Você fez um saque de ${valor:.2f}")

    def mostrar_saldo(self):
        if self.__saldo <= 0:
            print(f"Não há saldo na sua conta")
        else:
            print(f"Senhor(a) {self.__titular}, seu saldo atual é de ${self.__saldo:.2f}")

conta2 = NovaContaBancaria("Wellington Júnior", 100)
conta2.depositar(750.75)
conta2.sacar(200)
conta2.mostrar_saldo()