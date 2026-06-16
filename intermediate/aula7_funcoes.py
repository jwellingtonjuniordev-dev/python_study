# Funções  - bloco reutilizavel de códigos
# Exercício 7.1
# Crie uma função chamada: mensagem
# Ela deve mostrar: Bem-vindo ao sistema

def mensagem():
    print('Bem-vindo ao sistema!')

mensagem()

# Exercício 7.2
# Crie uma função que:
# receba nome;
# mostre: Olá Wellington 

def apresentacao(nome):
    print(f'Olá {nome}')

apresentacao('Wellington')

# Exercício 7.3
# Crie uma função que:
# receba 2 números;
# retorne a soma.

def somar(a, b):
    return a + b

print(somar(5, 6))

# Mini desafio 7
# Crie funções separadas para:
# adicionar produto;
# listar produtos;
# calcular total.
# Use no sistema de mercado.

lista_produtos = ['Feijão', 'Arroz', 'Macarrão', 'Carne', 'Frango', 'Suco', 'Alface', 'Tomate']
lista_preco_produto = [3.75, 1.67, 0.99, 14.90, 6.98, 1.30, 1, 1.22]
menu_principal = 0
menu_adicionar_carrinho = 0
count = 0
carrinho = 0
lista_pedidos = []
indice = 0

def listar_produtos(lista_produtos, lista_preco_produto, contador):
    for produto in lista_produtos:
        print(f'{contador}. {produto} = {lista_preco_produto[contador]:.2f}R$')
        contador += 1

def calcular_total(carrinho, listar_preco, indice):
    carrinho += listar_preco[indice]
    return carrinho

def adicionar_produtos(indice, lista_pedidos, lista_produtos):
    indice = int(input('Qual produto você deseja da lista acima: \n'))
    lista_pedidos.append(lista_produtos[indice])
    calcular_total(carrinho, lista_preco_produto, indice, menu_adicionar_carrinho, lista_produtos)
    if indice <= 0 and indice >= len(lista_produtos):
        print(f'O item que você digitou não está disponível, por favor tente novamente.')

carrinho = calcular_total(carrinho, lista_preco_produto, indice)

print(f'Bem vindo ao mercado welldev, Fique a vontade.')
while menu_principal != 4:
    menu_principal = int(input('Selecione a opção desejada: \n1- Listar produtos \n2- Adicionar produto ao carrinho \n3- Listar produtos adicionados \n4- Finalizar compra \n'))
    if menu_principal == 1:
        listar_produtos(lista_produtos, lista_preco_produto, count)
    if menu_principal == 2:
        adicionar_produtos(indice, lista_pedidos, lista_produtos)
    elif menu_principal == 3:
        print(f'Os produtos no seu carrinho são: \n{lista_pedidos} e o total atual é de {carrinho:.2f}R$')
    elif menu_principal == 4:
        print(f'Você comprou {lista_pedidos} \nO total pago foi de: {carrinho:.2f}R$ \nObrigado pelas compras!!!')
    count = 0

# Desafio Extra
# Crie um mini sistema bancário usando funções:
# Funções:
# depositar();
# sacar();
# ver_saldo();

# Menu:
# 1 depósito;
# 2 saque;
# 3 saldo;
# 4 sair.

print(f'Novo sistema bancário Wellbank!')

menu_principal = 0
valor = 0
lista_valores_depositados = []
lista_valores_sacados = []
valor_depositado = 0
valor_sacado = 0

def depositar(valor, valor_depositado, lista_depositos): # Essa função recebe um valor e adiciona a lista e ao seu saldo

    valor = float(input(f'Digite o valor que deseja depositar: \n')) # pede valor a ser depositado
    valor_depositado += valor # valor digitado é somado
    lista_depositos.append(valor) # valor digitado é adicionado a lista para histórico
    print(f'O valor depositado foi de: R$ {valor:.2f}') # mostra valor depositado
        
def sacar(valor, valor_depositos, lista_saques, lista_depositos): # Essa função recebe um valor e retira do saldo e adiciona a lista de saques para histórico

    valor = float(input(f'Digite o valor que deseja sacar: \n')) # pede o valor a ser sacado
    for v in lista_depositos: # percorre a lista de valores depositados para depois retirar
        valor_depositos += v # soma a variavel valor depositado
    if valor > valor_depositos: # verifica se o valor informado é menor que 2 e se há saldo para o saque
        print(f'Você não tem saldo suficiente para realizar essa operação!') # mostra mensagem que não há valor disponivel
    else:
        valor_depositos -= valor # retira o valor da conta
        lista_saques.append(valor) # adiciona o valor digitado na lista de saque
        print(f'O valor sacado foi de: R$ {valor:.2f}') # mostra o valor sacado

def saldo(valor_deposito, depositados, sacados): # Recebe um valor e mostra

    if valor_deposito <= 0 and len(depositados) <= 0: # verifica se o valor é menor ou igual a 0
        print('Você não tem saldo suficiente')
    else:
        '''for v in depositados: # percorre os itens adicionados na lista e soma eles 
            valor_deposito += v # para cada valor percorrido na lista de depositados soma-se a variavel valor_deposito
        for v in sacados: # percorre os itens adicionados na lista e soma eles 
            valor_saque += v # para cada valor percorrido na lista de sacados soma-se a variavel valor_saque'''
        saldo = sum(depositados) - sum(sacados)
    print(f'O seu saldo é de: R$ {saldo:.2f} \n') # mostra o total depositado

def historico(lista_depositos, lista_saques): # recebe o historico de depositos e saques como parametro e retorna os valores.

    if len(lista_depositos) <= 0: # verifica se há algum item na lista de deposito
        print('Não foi depositado nenhum valor até agora.') # mostra a mensagem de nenhum valor depositado
    else:
        print(f'Historico de depósitos é: \n{lista_depositos}') # mostra a lista com os depositos feitos

    if len(lista_saques) <= 0: # verifica se há algum item na lista de saques
        print('Não foi sacado nenhum valor até agora.') # mostra a mensagem de nenhum valor sacado
    else:
        print(f'Historico de saques é: \n{lista_saques}') # mostra a lista com os saques feitos

while menu_principal < 5:

    menu_principal = int(input(f'Digite a operação que deseja realizar \n1 - Depositar \n2 - Sacar \n3 - Ver saldo \n4 - Histórico \n5 - Sair \n'))
    if menu_principal == 1:
        depositar(valor, valor_depositado, lista_valores_depositados)
    elif menu_principal == 2:
        sacar(valor, valor_depositado, lista_valores_sacados, lista_valores_depositados)
    elif menu_principal == 3:
        saldo(valor_depositado, lista_valores_depositados, lista_valores_sacados)
    elif menu_principal == 4:
        historico(lista_valores_depositados, lista_valores_sacados)
    elif menu_principal == 5:
        print('Saindo...')
    else:
        break