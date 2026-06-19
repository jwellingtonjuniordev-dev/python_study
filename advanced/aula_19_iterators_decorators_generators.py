# Iterators, Generators and Decorators
# Hoje vamos aprender três conceitos muito importantes do Python moderno.

# 1. Iterators
# O que são?
# Um iterador é um objeto capaz de retornar um elemento por vez.
# Na verdade, quando fazemos:

'''for item in list:
    print(item)'''

# O Python faz algo parecido com:

'''iterator = iter(list)

print(next(iterator))
print(next(iterator))
print(next(iterator))'''

# Cada chamada de next() retorna um elemento.
# Quando não há mais elementos: StopIteration

# Exemplo: 
numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# 2. Generators
# O que são?
# São funções especiais que produzem valores sob demanda.
# Ao invés de: return
# usamos: yield
# A função "pausa" e continua de onde parou.

def count():
    yield 1
    yield 2
    yield 3

for number in count():
    print(number)

# Vantagem
# Imagine:

'''Lista:

numbers = [1,2,3,...1000000]'''

# Toda a memória é ocupada.
# Generator:

def generate():
    for i in range(1000000):
        yield i

# Só gera quando necessário.
# Muito utilizado em:

#APIs;
#leitura de arquivos grandes;
#processamento de dados;
#FastAPI;
#Data Science.

# 3. Decorators
# O que são?
# São funções que modificam o comportamento de outras funções.
# Exemplo simples:

def decorator(function):

    def wrapper():
        print("Before")
        function()
        print("After")
    return wrapper

# Uso:

@decorator
def hello():
    print("Hello")
