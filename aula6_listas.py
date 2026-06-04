# Listas uma variavel que entre colchetes recebe diversos valores e tipos diferentes dentro dela
# EX: list = ['Jose', 'Banana', 1, 8.9, True] tipo string, tipo int, tipo float, tipo boolean
# para acessar a posição em uma lista eu utilizo o nome da variavel e entre colchetes a posição do item que eu quero
# print(list[0]) ---> 'Jose'
# a lista no python é ordenada com o primeiro item do indice começando em 0 até o enésimo ítem

# adiciona valores na lista = list.append('João')
# remove = list.remove('Banana')
# tamanho da lista = len(list)
# percorrendo lista = for i in list: print(i)

# Exercício 6.1

# Crie uma lista com: 5 linguagens de programação.
# Depois:
# mostre a lista inteira;
# mostre apenas a primeira;
# mostre apenas a última.
# Dica: lista[-1]

'''linguagens = ['Python', 'C++', 'Java', 'Cobol', 'JavaScript']

for i in linguagens:
    print(i)

print(linguagens[0])
print(linguagens[-1])

# Exercício 6.2
# Crie uma lista vazia.
# O programa deve:
# pedir 3 nomes;
# adicionar na lista usando .append().
# Depois mostrar todos os nomes.

nomes = []

while len(nomes) < 3:
    nome = input('Digite o nome que deseja adicionar a lista: ')
    nomes.append(nome)
    
for nome in nomes:
    print(f'O nome adicionado a lista foi {nome}')

# Mini desafio 6
# Crie um sistema de compras:
# O usuário poderá:
# adicionar produtos;
# listar produtos;
# sair.
# Use:
# while;
# lista;
# menu.

produtos = []
menu = 0
menu_produto = 0

print('Bem vindo a loja de produtos, sinta-se a vontade!')

while menu != 3:
    menu = int(input('Selecione uma opção: \n1- Adicionar produtos \n2- Listar produtos \n3- Sair \n'))
    if menu == 1:
        menu_produto = input('Digite o produto que deseja adicionar: \n')
        produtos.append(menu_produto)
        print(f'\nVocê adicionou {menu_produto} a lista de produtos.\n')
    elif menu == 2:
        if len(produtos) == 0:
            print('\nAinda não há produtos adicionados, por favor adicione um produto!\n')
        else:
            for produto in produtos:
                print(f'\nVocê tem ({produto}) disponível\n')
    elif menu == 3:
        print(f'\nObrigado pela visita\n')
    else:
        print(f'\nOpção {menu} inválida, tente novamente...\n') 

# Desafio Extra 6.
# Crie um carrinho de compras com:
# lista de produtos;
# soma total;
# quantidade de itens.

# vou fazer um menu que 
# 1 - lista os produtos e os preços de cada produto.
# 2 - adiciona ao carrinho o produto e o preço
#   Selecionar em outro menu o produto que deseja adicionar 1 - 7
# 3 - finaliza a compra'''

lista_produtos = ['Feijão', 'Arroz', 'Macarrão', 'Carne', 'Frango', 'Suco', 'Alface', 'Tomate']
lista_preco_produto = [3.75, 1.67, 0.99, 14.90, 6.98, 1.30, 1, 1.22]
menu_principal = 0
menu_adicionar_carrinho = 0
count = 0
carrinho = 0
lista_pedidos = []
indice = 0

print(f'Bem vindo ao mercado welldev, Fique a vontade.')
while menu_principal != 4:
    menu_principal = int(input('Selecione a opção desejada: \n1- Listar produtos \n2- Adicionar produto ao carrinho \n3- Listar produtos adicionados \n4- Finalizar compra \n'))
    if menu_principal == 1:
        for produto in lista_produtos:
            print(f'{count}. {produto} = {lista_preco_produto[count]:.2f}R$')
            count += 1
    if menu_principal == 2:
        indice = int(input('Qual produto você deseja da lista acima: \n'))
        lista_pedidos.append(lista_produtos[indice])
        carrinho += lista_preco_produto[indice]
        print(f'Você tem o produto {lista_produtos[menu_adicionar_carrinho]} adicionado ao carrinho, o valor total atual é de {carrinho:.2f}R$')
        if indice < 0 or indice >= len(lista_produtos):
            print(f'O item que você digitou não está disponível, por favor tente novamente.')
    elif menu_principal == 3:
        print(f'Os protos no seu carrinho são: \n{lista_pedidos} e o total atual é de {carrinho:.2f}R$')
    elif menu_principal == 4:
        print(f'Você comprou {lista_pedidos} \nO total pago foi de: {carrinho:.2f}R$ \nObrigado pelas compras!!!')
    count = 0