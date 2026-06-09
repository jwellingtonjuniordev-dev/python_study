'''Próxima etapa: Classes Abstratas (Abstração)
O que é?
Uma classe abstrata serve como um modelo.
Ela diz:
"Toda classe filha DEVE implementar determinados métodos."
Exemplo:
Forma
│
├── Quadrado
├── Círculo
└── Triângulo
Toda forma deve ter:
calcular_area()
Mas cada uma calcula de um jeito.
Exemplo
from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def falar(self):
        pass

Agora:
class Cachorro(Animal):

    def falar(self):
        print("Au au")

Mas isto:
animal = Animal()
gera erro.
Você é obrigado a criar uma classe concreta.'''

# Exercício 14.1
# Crie uma classe abstrata: class Funcionario
# Método abstrato: trabalhar()
# Depois crie: Programador, Designer
# Cada um implementando seu próprio trabalho.

from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self):
        pass
    
    @abstractmethod
    def trabalhar(self):
        pass

class Programador(Funcionario):

    def __init__(self):
        super().__init__()

    def trabalhar(self):
        print(f"Trabalha escrevendo código e corrigindo bugs.")

class Designer(Funcionario):

    def __init__(self):
        super().__init__()

    def trabalhar(self):
        print(f"Trabalha ilustrando / desenhando e projetando.")

programador = Programador()
designer = Designer()

programador.trabalhar()
designer.trabalhar()

# Exercício 14.2
# Crie uma classe abstrata: class Pagamento
# Método: pagar()
# Depois: Cartao, Pix, Dinheiro
# Cada um exibindo uma mensagem diferente.

class Pagamento(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def pagar(self):
        pass

class Cartao(Pagamento):

    def __init__(self):
        super().__init__()

    def pagar(self):
        print(f"O pagamento com cartão permite você pagar o total da compra dividindo o valor em até 12x que pode ser acrecido de juros.")

class Pix(Pagamento):

    def __init__(self):
        super().__init__()

    def pagar(self):
        print(f"O pagamento com PIX permite você pagar o total da compra instantâneamente usando uma chave pix criptografada.")

class Dinheiro(Pagamento):

    def __init__(self):
        super().__init__()

    def pagar(self):
        print(f"Com o pagamento em dinheiro, você paga o total da compra, esse é o método mais tradicional.")

cartao = Cartao()
cartao.pagar()
pix = Pix()
pix.pagar()
dinheiro = Dinheiro()
dinheiro.pagar()

# Mini desafio 14
# Crie: class Transporte
# Método abstrato: viajar()
# Depois: Carro, Avião, Navio
# Cada um implementando seu próprio meio de viagem.

class Transporte(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def viajar(self):
        pass

class Carro(Transporte):

    def __init__(self):
        super().__init__()

    def viajar(self, meio):

        if meio.lower() == "anda":
            print(f"O carro deve andar...")
        else:
            print(f"O transoporte está incorreto")
    
class Aviao(Transporte):

    def __init__(self):
        super().__init__()

    def viajar(self, meio):
        if meio.lower() == "voa":
            print(f"O avião deve voar...")
        else:
            print(f"O transoporte está incorreto")
    
class Navio(Transporte):

    def __init__(self):
        super().__init__()

    def viajar(self, meio):
        if meio.lower() == "navega":
            print(f"O navio deve navegar...")
        else:
            print(f"O transoporte está incorreto")

carro = Carro()
carro.viajar("anda")
aviao = Aviao()
aviao.viajar("voa")
navio = Navio()
navio.viajar("navega")

# Desafio Extra
# Faça um sistema bancário com abstração: Classe abstrata: Conta
# Métodos obrigatórios: depositar(), sacar()
# Depois crie: ContaCorrente, ContaPoupanca
# Cada uma implementando suas próprias regras.

class Conta(ABC):

    def __init__(self, titular, saldo):
        self._titular = titular.capitalize()
        self._saldo = saldo
        self._depositos = []
        self._saques = []

    @abstractmethod
    def depositar(self, valor):

        if valor <= 0:
            print(f"Operação inválida")
        else:
            self._saldo += valor
            self._depositos.append(valor)
            print(f"{self._titular}, você fez {len(self._depositos)} depositos esse mês, o total foi de R$ {sum(self._depositos):.2f} depositados")
    
    @abstractmethod
    def sacar(self, valor): # será implementada taxa para cada um tipo de conta, corrente e poupança

        if self._saldo <= 0:
            print(f"Operação inválida!")
        else:
            self._saldo -= valor
            self._saques.append(valor)
            print(f"{self._titular}, você fez {len(self._saques)} saques esse mês, o total foi de R$ {sum(self._saques):.2f} sacados")

    def ver_saldo(self):
        print(f"{self._titular}, seu saldo atual é de {self._saldo:.2f}")

class ContaCorrente(Conta): # taxa de 2.00 para cada saque

    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def depositar(self, valor):

        if valor <= 0:
            print(f"Operação inválida!")
        else:
            self._saldo += valor
            self._depositos.append(valor)
            print(f"{self._titular}, você fez {len(self._depositos)} depositos esse mês, o total foi de R$ {sum(self._depositos)} depositados")

    def sacar(self, valor):

        taxa = 2.00

        if valor + taxa > self._saldo:
            print(f"Operação inválida")
        else:
            self._saldo -= valor + taxa
            self._saques.append(valor)
            print(f"{self._titular}, no seu tipo de conta há um acréscimo de R$ {taxa} para cada saque.")
            print(f"{self._titular}, você fez {len(self._saques)} saques esse mês, o total foi de R$ {sum(self._saques):.2f} sacados")

class ContaPoupanca(Conta): # sem taxa de saque e com um bônus de 0.30 para cada deposito

    def __init__(self, titular, saldo):
        super().__init__(titular, saldo)

    def depositar(self, valor):

        acrescimo = 0.50

        if valor <= 0:
            print(f"Operação inválida")
        else:
            self._saldo += valor + acrescimo
            print(f"Para cada depósito que você faz, recebe um acrescimo de R$ {acrescimo}.")

    def sacar(self, valor): # será implementada taxa para cada um tipo de conta, corrente e poupança

        if self._saldo < valor:
            print(f"Operação inválida")
        else:
            self._saldo -= valor
            self._saques.append(valor)
            print(f"{self._titular}, você fez {len(self._saques)} saques esse mês, o total foi de R$ {sum(self._saques):.2f} sacados")


conta_corrente = ContaCorrente("Wellington", 0)
conta_poupanca = ContaPoupanca("Zildenir", 1000)
conta_corrente.ver_saldo()
conta_corrente.depositar(250)
conta_corrente.depositar(1200)
conta_corrente.ver_saldo()
conta_corrente.sacar(30)
conta_corrente.sacar(250)
conta_corrente.ver_saldo()
conta_poupanca.ver_saldo()
conta_poupanca.depositar(250)
conta_poupanca.depositar(1450)
conta_poupanca.ver_saldo()
conta_poupanca.sacar(300)
conta_poupanca.sacar(200)
conta_poupanca.ver_saldo()