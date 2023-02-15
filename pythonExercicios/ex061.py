termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão da Progressão Aritmética: '))
termo = termo1
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('Fim.')