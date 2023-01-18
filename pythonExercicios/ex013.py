salário = float(input('Qual o seu salário? R$ '))
aumento = salário*(15/100)
total = salário+aumento
print(f'Seu reajuste será de $ {aumento:.2f}, logo, passará a ganhar $ {total:.2f}!')
