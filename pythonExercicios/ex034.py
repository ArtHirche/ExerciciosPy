salário = float(input('Quanto você ganha? '))
aumento_caso1 = (10/100)*salário
total_caso1 = salário+aumento_caso1
aumento_caso2 = (15/100)*salário
total_caso2 = salário+aumento_caso2
if salário > 1250:
    print(f'Seu aumento será de 10% no salário atual. Totalizando: R$ {total_caso1:.2f}!')
else:
    print(f'Seu aumento será de 15% no salário atual. Totalizando: R$ {total_caso2:.2f}!')
