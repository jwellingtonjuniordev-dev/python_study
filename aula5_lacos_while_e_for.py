# Laços de repetição While e for 
# while (enquanto a condição for verdadeira execute o código)
# for (percorre sequencias dentro de um range)

# Exercício 5.1
# Crie um contador que:
# comece em 1;
# vá até 10;
# mostre os números.

counter = 1

while counter <= 10:
    print(counter)
    counter += 1

# Exercício 5.2

# Mostre:
# números de 0 até 20;
# apenas os pares.
# Dica: if numero % 2 == 0

for numero in range(21):
    if numero % 2 == 0:
        print(numero)

# mini desafio 5

# Crie um sistema de senha:
# Enquanto a senha estiver errada:
# continue pedindo.
# Senha correta: python123
# Quando acertar: mostrar "Acesso liberado".

correct_pass = 'python123'
is_correct_pass = True

while is_correct_pass:
    request_pass = input('Digite a senha: ')
    if request_pass == correct_pass:
        is_correct_pass = False
        print(f'Acesso liberado')

# Desafio extra 5
# Crie um mini menu interativo:
# 1 - Ver saldo
# 2 - Depositar
# 3 - Sair
# O sistema deve repetir até o usuário escolher sair.

menu = 0
saldo = 0
deposito = 0

print('Bem vindo ao sistema Wellbank, por favor selecione a opção desejada: ')

while menu != 3:
    menu = int(input('\n1 - Ver saldo \n2 - Depositar \n3 - Sair \n\n'))
    if menu == 1:
        print(f'Seu saldo atual é de {saldo:.2f}R$')
    elif menu == 2:
        deposito = float(input('Digite o valor a ser depositado: '))
        print(f'O valor depositado foi de {deposito:.2f}R$')
        saldo += deposito
    elif menu == 3:
        print('Volte sempre!')
    else:
        print(f'Você digitou {menu}, essa opção não existe, tente novamente!')