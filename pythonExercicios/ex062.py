from time import sleep
from os import system

print('Gerador de Progressão Aritmética')
print('-==-'*20)
primeiroT = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiroT
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} ->', end='')
        termo += razao
        contador += 1
    print('Programa suspenso.')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    system('cls')
print('Finalizando...')
sleep(1)
print(f'Programa finalizado com {total} termos.')