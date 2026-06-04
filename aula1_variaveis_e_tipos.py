# Exercício 1
#Criar programa com algumas variaveis e exibir;

nome = 'Wellington'
idade = 33
cidade = 'Natal - RN'
profissao = 'Back-End developer'

#comando para exibir no console print()

print(f"Meu nome é {nome} \nTenho {idade} anos \nMoro em {cidade}\nQuero ser {profissao}")

# Exercício 2
# criar variáveis numéricas

salario = 2500
investimento = 500

print (f"Eu ganho {salario}$ \nQuero investir {investimento}$ por mês")

# Desafio
# Crie um programa que: guarde o preço de um produto; guarde um desconto; calcule o valor final.

produto = 37.15
desconto = 17
valor_final = produto - ((desconto / 100) * produto)

# para exibir 2 casas decimais apos a virgula pode-se usar esse metodo "{:.2f}" ou nova_variavel = round(variavel, 2)
print(f"O preço do produto é {produto}$ \nDesconto de {desconto}% \nValor final do produto é de {valor_final:.2f}$")