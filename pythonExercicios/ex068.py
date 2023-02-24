from random import randint

print('~' * 20)
print('VAMOS JOGAR PAR OU IMPAR!')
print('~' * 20)
vitorias = 0
while True:
    valor = int(input('Digite um valor: '))
    maquina = randint(0, 10)
    total = valor + maquina
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()
        print(
            f'Você jogou {valor} e o computador {maquina}. Total de {valor+maquina}'
        )
        print(f'DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitorias} vezes')