# Entender imputs e conversão de dados
# Tudo que vem pelos inputs é recebido como string, é importante converter algum valor numerico caso queira.

# Exercício 1
# Criar programa que peça: nome, idade e cidade depois exibir

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
cidade = input("Qual a sua cidade: ")

print(f"""
    Olá {nome}
    Você tem {idade} anos
    E mora em {cidade}.
""")

# Exercício 2
# Crie um programa que: peça dois números; some os números; mostre o resultado.

primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))
resultado = primeiro + segundo

print(f"Resultado: {resultado}")

# Desafio
# Crie uma calculadora de desconto dinâmica: O programa deve pedir: preço do produto; porcentagem de desconto.
# Depois calcular: valor do desconto; valor final.

preco = float(input("Digite o preço do produto: "))
desconto = int(input('Digite o percentual de desconto: '))

# calculos
valor_desconto = (desconto / 100) * preco
valor_final = preco - valor_desconto

print(f'''
    Preço: {preco:.2f}$
    Desconto: {desconto}%
      
    Você economizou: {valor_desconto:.2f}$
    Valor final: {valor_final:.2f}$
''')