'''Próxima etapa: Polimorfismo
O que é?
Significa:
Um mesmo método pode ter comportamentos diferentes dependendo da classe.
Exemplo:
Animal
│
├── Cachorro → emitir_som() → Au au
├── Gato → emitir_som() → Miau
└── Vaca → emitir_som() → Muuu
Todos possuem:
emitir_som()
Mas cada classe implementa sua própria versão.
Exemplo
class Animal:
    def emitir_som(self):
        print("Som genérico")
class Cachorro(Animal):
    def emitir_som(self):
        print("Au au")
class Gato(Animal):
    def emitir_som(self):
        print("Miau")
Uso:
animais = [Cachorro(), Gato()]
for animal in animais:
    animal.emitir_som()
Saída:
Au au
Miau
O mesmo método teve comportamentos diferentes.
Isso é polimorfismo.'''

# Exercício 13.1
# Crie: class Animal
# Método: falar()
# Mostrando: O animal faz um som.
# Depois crie: class Cachorro(Animal)
# Sobrescreva: falar()
# Mostrando: Au au!

class Animal:
    def falar(self):
        print("Sons aleatorios")

class Cachorro(Animal):
    def falar(self):
        print(f"Au au!")

class Gato(Animal):
    def falar(self):
        print(f"Miaaaau!")

animais = [Cachorro(), Gato()]

for animal in animais:
    animal.falar()

# Exercício 13.2
# Crie: class Funcionario
# Método: trabalhar()
# Depois: class Programador(Funcionario) e class Designer(Funcionario)
# Cada um deve implementar trabalhar() de forma diferente.

class Funcionario():
    def __init__(self, nome):
        self.nome = nome
    
    def trabalhar(self):
        print("Trabalho genérico!")

class Programador(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)
    
    def trabalhar(self):
        print(f"Oi {self.nome} seu trabalho é: Escrever códigos, testar!")

class Designer(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)

    def trabalhar(self):
        print(f"Oi {self.nome} seu trabalho é: Projetar/desenhar!")

funcionarios = [Programador("Wellington"), Designer("Ana")]
for funcionario in funcionarios:
    funcionario.trabalhar()

# Mini desafio
# Crie: class Veiculo
# Método: mover()
# Depois: Carro → "O carro está andando.", Avião → "O avião está voando.", Barco → "O barco está navegando."

class Veiculo:
    def mover(self):
        print(f"Movimento do veículo")

class Carro(Veiculo):
    def mover(self):
        print("O carro está andando")

class Aviao(Veiculo):
    def mover(self):
        print(f"O avião está voando")

class Barco(Veiculo):
    def mover(self):
        print(f"O barco está navegando")

veiculos = [Carro(), Aviao(), Barco()]
for veiculo in veiculos:
    veiculo.mover()

# Desafio extra
# Pegue seu sistema bancário e crie: Conta, e duas classes filhas: ContaCorrente, ContaPoupanca
# As duas terão: sacar()
# Mas com regras diferentes: ContaCorrente cobra taxa de R$5,00 por saque, ContaPoupança não cobra taxa.

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            print(f"O valor que você tentou depositar é {valor}, por favor, tente novamente!")
        else:
            self._saldo += valor

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"{self.titular}, você sacou um total de $ {valor}")
        else:
            print(f"Você não tem saldo suficiente.")

    def ver_saldo(self):
        print(f"{self.titular}, o seu saldo atual é de $ {self._saldo:.2f}")

class ContaCorrente(Conta):

    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def sacar(self, valor):

        taxa = 5

        if valor + taxa <= self._saldo:
            print(f"{self.titular}, sua conta é Conta Corrente, há uma taxa de $ 5.00 por saque.")
            self._saldo -= valor + taxa
            print(f"{self.titular}, você sacou um total de $ {valor}")
        else:
            print(f"Você não tem saldo suficiente.")

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

conta1 = ContaCorrente("Wellington", 500)
conta2 = ContaPoupanca("Zildenir", 3700)

conta1.ver_saldo()
conta2.ver_saldo()
conta1.depositar(1500)
conta2.depositar(800)
conta1.ver_saldo()
conta2.ver_saldo()
conta1.sacar(5)
conta2.sacar(10)
conta1.ver_saldo()
conta2.ver_saldo()