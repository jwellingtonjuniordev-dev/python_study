# Dicionarios DICT

# Criando dicionário: 
usuario = {
    "nome": "Wellington",
    "idade": 33,
    "admin": True
}

#Acessando valores
print(usuario["nome"])

#Adicionando novos valores
usuario["email"] = "well@email.com"

# Alterando valores
usuario["idade"] = 34

# Percorrendo dicionário
for chave, valor in usuario.items():
    print(chave, valor)

# Exercício 8.1
# Crie um dicionário chamado: produto
# Com: nome; preço; estoque.
# Depois mostre todos os valores.

produto = {
    "nome":"Computador",
    "preco": 1299.98,
    "estoque": True
}

for key, value in produto.items():
    print(key, value)

# Exercício 8.2
# Crie um dicionário de usuário: usuario
# Com: nome; email; idade.
# Depois: altere a idade; adicione telefone.

usuario = {
    "nome": "João",
    "email": "joao@email.com",
    "idade": 25
}

usuario["idade"] = 22
usuario["telefone"] = 913913913
print(usuario)

# Mini desafio 8
# Crie um sistema de cadastro de usuários.
# Cada usuário deve ter: nome; email; idade.
# Armazene vários usuários em uma lista.

MENU = 0 # declaração constante MENU
list_users = [] # declaração lista usu
users = {} # declaração DICT usuarios
name_usr = ''
email_usr = ''
age_usr = 0
have_at = ''
ends_with = ''

def add_users(list_users):

    name = input('Digite o nome do usuario: \n').lower() # var nome recebe uma entrada com o nome do usuario
    email = input('Digite o email pretendido: \n').lower() # var email recebe uma entrada com o email do usuario
    age = int(input('Digite a idade do usuario \n')) # var age recebe uma entrada com o idade tipo INT do usuario

    have_at = "@" in email # verifica se tem o caractere no email recebido e guarda na var
    ends_with = email.endswith(".com") # verifica se o final do email termina com .com

    if have_at and ends_with and age > 12 and len(name) > 2: # verifica se dentro das strings recebidas tem mais de 2 caracteres, e idade é maior que 12
        user = {"name": name, "email": email, "age": age} # DICT recebe os valores recebidos nos inputs
        list_users.append(user.copy()) # adiciona o usuario com os dados registados na lista
    else:
        print("Você precisa digitar um nome válido e um email válido, a idade também precisa estar correta")

def listing_users(list_users):
    for user in list_users:
        print(
            f"Nome: {user['name']} | "
            f"Email: {user['email']} | "
            f"Idade: {user['age']}"
        )

while MENU < 3: # enquanto o numero digitado para MENU for menor que 3 o programa anda
    MENU = int(input('Cadastro de usuarios, escolha uma opção: \n1 - Adicionar usuário \n2 - Listar usuários \n3 - Sair \n')) # MENU recebe um valor
    if MENU == 1: # opção de adicionar um usuario
        add_users(list_users) # chamada função add_usrs
    elif MENU == 2: # Opção de listar usuarios cadastrados
        listing_users(list_users)
    elif MENU == 3: # Opção de Sair
        print('Saindo...')
        
# Desafio extra 8
# Crie um sistema de login com dicionários.
#usuarios = {
    #"admin": "123456",
    #"wellington": "python123"
# O sistema deve: 
# pedir login;
# pedir senha;
# validar acesso.

loged = False # variavel vai mudar conforme as verificações estiverem certas
login = '' # variavem que recebe input de login
password = '' #variavel que recebe input de password

users = { # DICT com informações de chave / valor 
    "admin": "123456",
    "wellington": "python123",
    "zildenir": "ana1234"
}

def req_login(login): # função que verifica se login tem mais que 3 caracteres e está inserido no dicionário 
    if len(login) > 3 and login in users:
        return login # retorno do valor se estiver correto
    
def req_password(password):# função que verifica se password tem mais que 4 caracteres e está inserido no dicionário users
    exists = password in " ".join(map(str, users.values())) # verifica se existe alguma coisa nesse sentido dentro do dicionario
    if len(password) > 4 and exists:
        return password # retorna o valor de password se estiver tudo OK

while not loged: # laço que vai parar se estiver um usuario logado
    login = input('Digite o login: \n').lower() # input do login
    password = input('Digite a sua senha \n').lower() # input do password
    if users.get(login) == password: # Verifica se o retorno de login é verdadeiro e se a senha é a mesma que está associada a KEY certa no dicionário
        req_login(login) # chamada da função de login
        req_password(password) # chamada da função de password
        print(f"Bem vindo(a) {login}.") # imprime a mensagem de bem vindo
        loged = True # muda o valor da variável do laço while
    else:
        print('Usuário ou senha inválido, por favor, tente novamente!') # retorna essa mensagem se um dos valores digitados estiver errado.