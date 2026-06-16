# Condicionais if, elif, else
# operadores de comparação == (igual), != (diferente), > (maior que), < (menor que), >= (maior ou igual), <= (menor ou igual)
# depois de montar a estrutura basica de uma condicional (if condição: TAB codigo) os : são obrigatórios e identação também

# Exercício 1
# Crie um programa que: peça a idade; informe se a pessoa é:
# menor de idade; maior de idade.

idade = int(input('Informe a idade: '))
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

# Exercício 2
#Crie um sistema de notas:
#Nota	Resultado
#9 ou mais	Excelente
#7 até 8.9	Bom
#abaixo de 7	Reprovado


nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
nota3 = float(input('Terceira nota:'))

media = (nota1 + nota2 + nota3) / 3

if media >= 9:
    print(f'Sua nota foi de {media:.1f}, Excelente!!!')
elif media >= 7 and media <= 8.9:
    print(f'Sua nota foi de {media:.1f}, Bom!!!')
else:
    print(f'Sua nota foi {media:.1f} infelizmente você foi Reprovado')

# Mini desafio
# Crie um sistema de login simples:
''' 
O programa deve:
pedir usuário;
pedir senha;
mostrar:
"Login realizado"
ou "Usuário ou senha incorretos"
'''

login = input('Digite o seu usuario: ').lower()
senha = input('Digite a senha: ').lower()

login_admin = 'admin'
senha_admin = '123456'

if login == login_admin and senha == senha_admin:
    print(f'''Login Realizado.\nBem vindo(a) ao sistema!''')
else:
    print(f'Usuario ou senha incorretos!')
    print(f'Sua senha possui apenas {len(senha)} caracteres')