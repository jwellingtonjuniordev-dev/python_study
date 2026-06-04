# Tuplas e JSON

# Tuplas são iguais a listas exceto por serem imutaveis
# JSON é igual a um DICT mas é tudo texto

# Exercício 9.1
# Crie uma tupla com:
# Python
# JavaScript
# Java
# C#
# Mostre:
# primeiro item;
# último item.

languages = ("Python", "JavaScript", "Java", "C#")
print(languages[0], languages[-1])

# Exercício 9.2
# Crie um dicionário:
cliente = {
    "nome": "Maria",
    "idade": 28,
    "cidade": "Natal"
}
# Percorra e mostre todas as chaves e valores.

cliente = {
    "nome": "Maria",
    "idade": 28,
    "cidade": "Natal"
}

for key in cliente:
    print(f"Chave: {key} | Valor {cliente[key]}")

# Mini desafio 9
# Crie uma lista contendo 3 dicionários de produtos:

products = [{"nome":"Tablet", "preco":350.00},{"nome":"Laptop", "preco":1230.35},{"nome":"SmartPhone", "preco":730}]

print("Os produtos que temos são: \n")
for product in products:
    for key, value in product.items():
        print(f"{key}: {value}")
    print("---- \n")
'''
# Desafio extra 9

# Crie um sistema de estoque: 
# Cada produto deve ter:

'''
{
    "nome": "...",
    "preco": ...,
    "quantidade": ...
}

# Menu:
# Adicionar produto
# Listar produtos
# Atualizar estoque
# Sair

MENU = 0
products = []
key_to_update = ''
result = 0

def add_product():
    product_name = input("Digite o nome do produto que deseja: \n").capitalize()
    product_price = float(input("Digite o valor do produto: \n"))
    product_quantity = int(input("Digite a quantidade para adicionar no stock: \n"))
    if len(product_name) <= 2 or product_price <= 0 or product_quantity <= 0:
        print(f"Você deve inserir o produto corretamente, o valor e a quantidade em estoque")
    else:
        prod = {"nome": product_name, "preco": product_price,"quantidade": product_quantity}
        products.append(prod.copy())

def show_products(list_products):
    for product in list_products:
        print(f'produto: {product["nome"]} \npreço unitário: R$ {product["preco"]} \nquantidade em stock: {product["quantidade"]} \n')

def update_products(list):
    update_menu = input("Deseja alterar informação de algum produto 's' - sim, 'n' - não: \n").lower()
    
    if update_menu == "s":
        key_to_update = input("Digite o nome do produto que deseja alterar o preço ou quantidade: \n").capitalize()
        for product in list:
            if product["nome"] == key_to_update:
                print(f"O produto {key_to_update} tem atualmente o preço de R${product["preco"]:.2f} e quantidade de {product["quantidade"]}")
                value_to_update = float(input(f"Digite o novo valor que deseja para o produto {key_to_update}: \n"))
                product["preco"] = value_to_update
                quant_to_update = int(input(f"Digite a nova quantidade para o produto: \n"))
                product["quantidade"] = quant_to_update
    elif update_menu == "n":
        print("Você não deseja alterar nenhum valor, voltando para o menu principal...")
    else:
        print("Opção inválida...")

def calculate_total_prices(result):
    name_product = input("Digite o nome do produto que deseja somar o total: \n").capitalize()
    for product in products:
        if product["nome"] == name_product:
            price = product["preco"]
            quant = product["quantidade"]
            result = price * float(quant)
            print(f"O preço total do produto é de {result:.2f}")

while MENU != 5:
    MENU = int(input("Loja: \n1 - Adicionar produtos: \n2 - Listar produtos \n3 - Atualizar estoque \n4 - Calcular total produto em stock \n5 - Sair \n"))
    if MENU == 1:
        add_product()
    elif MENU == 2:
        show_products(products)
    elif MENU == 3:
        update_products(products)
    elif MENU == 4:
        calculate_total_prices(result)
    elif MENU == 5:
        print("Saindo...")
    else:
        print("Opção inválida, tente novamente")