# Operadores lógicos e validações reais
# AND (duas condições precisam ser verdadeiras), OR (apenas uma precisa ser verdadeira), NOT (Inverte o valor logico)

# Exercício 4.1

#Crie um sistema que:
#peça idade;
#pergunte se possui carteira (s ou n);

#Regras:

#pode dirigir se:
#idade >= 18
#E possuir carteira.

idade = int(input('Digite sua idade: '))
carteira = input('Tem carteira (s ou n): ').lower()

if idade >= 18 and carteira == 's':
    print(f'Pode dirigir')
elif idade >= 18 and carteira == 'n':
    print(f'Você ainda não tem carteira, pode tentar tirar, depois pode dirigir.')
else:
    print(f'Você não tem idade suficiente para dirigir!')

# Exercício 4.2

#Crie um sistema de desconto:
#O usuário terá desconto se:
#for cliente VIP
#OU
#compra acima de 100 reais.

valor_aporte = float(input('Digite o valor que deseja aportar: '))
usuario_vip = input('Deseja se tornar VIP (s ou n)').lower()
desconto = 37.7
total_compra = 0

if usuario_vip == 's' or valor_aporte >= 100:
    total_compra = valor_aporte - (desconto / 100 * valor_aporte)
    print(f'Recebe desconto de {desconto:.2f}%')
    print(f'O valor total aportado foi de {valor_aporte:.2f}$, o valor total a ser pago será de {total_compra:.2f}$')
else:
    total_compra = valor_aporte
    print(f'Não recebe desconto')
    print(f'O valor total aportado foi de {valor_aporte:.2f}$, o valor total a ser pago será de {total_compra:.2f}$')

# Mini desafio

#Crie um sistema de acesso:
#Regras:

#usuário precisa:
#estar logado;
#e ser administrador.

user_admin = True
logado = True
login = input('Digite o seu usuario: ').lower()
senha = input('Digite sua senha: ')
check_senha = len(senha)

if login == 'admin' and senha == '123456' and user_admin and logado:
    print('Acesso Permitido')
else:
    print('Acesso Negado')

# Desafio extra
# Crie um sistema de validação de senha.
# A senha deve possuir:
# pelo menos 8 caracteres;
# pelo menos 1 número.
# Dica: any(char.isdigit() for char in senha) Essa linha verifica se existe algum número na senha.

senha = input('Crie sua senha, ela deve ter pelo menos 8 caracteres, pelo menos 1 número: ')
verifica_numero = any(char.isdigit() for char in senha)

if len(senha) >= 8 and verifica_numero:
    print(f'Senha cadastrada\nEla tem {len(senha)} caracteres.')
else:
    print(f'Senha não registrada\nEla tem {len(senha)} caracteres.')