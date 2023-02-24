print('~==~' * 12)
print('{:^25}'.format('BANCO HIRCHE'))
print('~==~' * 12)
saque = int(input('Quanto deseja sacar: '))
total = saque
cedulas = 50
totalCedulas = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cédulas de R$ {cedulas:.2f}')
        if cedulas == 50:
            cedulas == 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totalCedulas = 0
        if total == 0:
            break
print('~==~' * 12)
print('Volte sempre ao BANCO HIRCHE! Tenha um bom dia!')