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

