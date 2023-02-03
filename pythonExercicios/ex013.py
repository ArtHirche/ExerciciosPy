salário = float(input('Qual o seu salário? R$ '))
aumento = salário*(15/100)
total = salário+aumento
print(f'Seu reajuste será de $ \033[1;34m{aumento:.2f}\033[m, logo, passará a ganhar $ \033[1;4;32m{total:.2f}\033[m!')
#Correto!