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

