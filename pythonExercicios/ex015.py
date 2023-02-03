dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias*60)+(km*0.15)
print(f'O total a pagar é de $ \033[1;31m{pago:.2f}\033[m')
