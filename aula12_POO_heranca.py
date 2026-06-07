'''Próxima etapa: Herança
O que é?
Herança permite que uma classe reaproveite características de outra.
Exemplo do mundo real:
Animal
├── Cachorro
├── Gato
└── Pássaro
Todos são animais.
Logo:
possuem nome;
possuem idade.
Mas cada um tem comportamentos próprios.
Exemplo simples
class Animal:
    def __init__(self, nome):
        self.nome = nome
Agora:
class Cachorro(Animal):
    pass
Cachorro herda tudo de Animal.
Utilização
dog = Cachorro("Rex")
print(dog.nome)
Resultado:
Rex
Mesmo sem criar um __init__ em Cachorro.
Adicionando comportamento próprio
class Cachorro(Animal):
    def latir(self):
        print("Au au")
Uso:
dog = Cachorro("Rex")
dog.latir()'''

# Exercício 12.1
# Crie uma classe: class Pessoa:
# com: nome, idade
# Depois crie: class Aluno(Pessoa):
# com: matrícula
# Método: apresentar() Mostrando: Olá, sou Wellington, tenho 33 anos e minha matrícula é 123.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def apresentar(self, matricula):
        print(f"Olá, sou {self.nome}, tenho {self.idade} anos e minha matrícula é {matricula}.")

aluno1 = Aluno("Wellington", 33)
aluno1.apresentar(123654)

# Exercício 12.2
# Crie uma classe: class Veiculo:
# com: marca
# Depois: class Carro(Veiculo):
# com: modelo
# Método: detalhes() Mostrando: Este é um carro da marca Toyota, modelo Corolla.

class Veiculo:
    def __init__(self, marca):
        self.marca = marca

class Carro(Veiculo):
    def detalhes(self, modelo):
        print(f"O carro é o {self.marca} {modelo}.")

carro1 = Carro("BMW")
carro1.detalhes("iX")

# Mini desafio 12
# crie: class Funcionario:
# com: nome, salário
# depois: class Gerente(Funcionario):
# com: bônus 
# Método: calcular_salario() retornando: salário + bônus.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
class Gerente(Funcionario):
    def calcular_salario(self, bonus):
        return self.salario + bonus
    
funcionario1 = Gerente("Wellington", 2500)
print(f"O salario atual do gerente, é de $ {funcionario1.calcular_salario(550)}")

# Desafio extra
# Crie um sistema bancário usando herança:
# Classe base: Conta
# Atributos: titular, saldo
# Métodos: depositar(), sacar()
# Classe filha: ContaPremium
# Novo atributo: limite_extra
# Regra: A conta premium pode sacar além do saldo usando o limite extra.

class Conta:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            print(f"Você precisa inserir um valor válido")
        else:
            self._saldo += valor
    
    def sacar(self, valor):
        if self._saldo < valor:
            print(f"Você não tem saldo suficiente para esta operação")
        else:
            self._saldo -= valor

    def get_saldo(self):
        return self._saldo
    
class ContaPremium(Conta):

    def __init__(self, titular, saldo, limite_extra):
        super().__init__(titular, saldo)
        self.limite_extra = limite_extra

    def sacar(self, valor):
        # Regra: pode sacar além do saldo usando o limite extra
        if valor > self._saldo + self.limite_extra:
            print(f"Você não tem saldo suficiente (incluindo limite extra) para esta operação")
        else:
            self._saldo -= valor


conta_premium = ContaPremium("Wellington", 2500, 1000)
conta_premium.depositar(3757.79)
print(f"Seu saldo atual é de $ {conta_premium.get_saldo()}")
conta_premium.sacar(2000)
print(f"Seu saldo atual é de $ {conta_premium.get_saldo()}")
conta_premium.sacar(4500)
print(f"Seu saldo atual é de $ {conta_premium.get_saldo():.2f}")
conta_premium.sacar(3000)