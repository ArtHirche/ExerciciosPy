from time import sleep

print('-==-'*20)
print('Programa de Sequência de Fibonacci')
print('-==-'*20)
termo = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('-'*30)
print(f'{t1} -> {t2}', end=' ')
contador = 3
while contador <= termo:
    t3 = t1 + t2
    print(f'-> {t3}', end=' ')
    t1 = t2
    t2 = t3
    contador += 1
sleep(1)
print('\nFIM DO PROGRAMA')
print('-'*30)