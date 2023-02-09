valorCasa = float(input('Qual é o valor da casa? '))
salario = float(input('Quanto você ganha? R$ '))
pagarAnos = int(input('Em quantos anos você irá pagar? '))
prestação = valorCasa/(pagarAnos*12)
minimo = salario * (30/100)
print('-'*30)
print(f'Você irá pagar R$ {prestação:.2f} por mês.')
if prestação > minimo:
    print('\033[1;31mInfelizmente você não conseguirá financiar essa casa.\033[m')
else:
    print('\033[1;32mVocê conseguirá financiar essa casa!\033[m')
print('\033[4mFim da simulação.\033[m')
print('-'*30)
#Correto!