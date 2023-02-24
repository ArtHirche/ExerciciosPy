while True:
    numero = int(input('Qual valor deseja ver a tabuada? '))
    print('-' * 20)
    if numero < 0:
        break
    for c in range(1, 11):
        print(f'{numero} x {c} = {numero*c}')
    print('-' * 20)
print('TABUADA ENCERRADA. Volte sempre!')