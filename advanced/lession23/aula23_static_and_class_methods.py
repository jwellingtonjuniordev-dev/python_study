'''Aula 23 — Static Methods e Class Methods
O que vamos aprender

Hoje você vai aprender:

@staticmethod
@classmethod
cls
diferença entre self e cls
quando usar cada um

Esses conceitos aparecem constantemente em bibliotecas como:

Django
FastAPI
SQLAlchemy
Pydantic
Requests
1. Métodos de instância (o que você já conhece)

Até agora quase todos os seus métodos eram assim:

class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello {self.name}")

Uso:

person = Person("Wellington")
person.say_hello()

O parâmetro

self

representa o objeto atual.

Cada objeto possui seus próprios dados.

2. Static Method

Às vezes uma função pertence à classe...

...mas não precisa acessar nenhum atributo.

Exemplo:

Uma calculadora.

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

Observe:

Não existe:

self

Nem:

cls

Porque o método não depende do objeto.

Uso:

print(Calculator.add(10, 20))

Resultado

30

Você nem precisa criar um objeto.

Quando usar?

Sempre que o método:

não usa self
não usa cls
apenas executa alguma lógica

Exemplos:

calcular idade
converter temperatura
validar email
validar CPF
gerar hash
formatar texto
3. Class Method

Agora imagine uma fábrica de objetos.

class Person:

    def __init__(self, name):
        self.name = name

Normalmente fazemos:

person = Person("John")

Mas podemos criar outro jeito de construir objetos.

class Person:

    def __init__(self, name):
        self.name = name

    @classmethod
    def anonymous(cls):
        return cls("Anonymous")

Uso

person = Person.anonymous()

print(person.name)

Resultado

Anonymous

Observe:

Não usamos

self

Usamos

cls

Porque estamos criando uma nova instância da classe.

self x cls
self

Representa um objeto.

person = Person("John")

↓

self

↓

person
cls

Representa a própria classe.

Person

↓

cls

Visualmente:

Person
   │
   ├── cls
   │
   ├── Person("John")
   │          │
   │         self
   │
   └── Person("Mary")
              │
             self
Quando usar cada um?
Tipo	Usa self?	Usa cls?	Cria objeto?
Método comum	✅	❌	Não
Static Method	❌	❌	Não
Class Method	❌	✅	Sim
Onde isso aparece na prática?

Você já usou isso sem perceber.

Por exemplo:

datetime.now()

é um classmethod.

Outro exemplo:

Path.cwd()

Também.

Já funções utilitárias como:

math.sqrt()

funcionam como métodos estáticos.'''

