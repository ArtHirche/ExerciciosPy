viagem = float(input('Quantos quilômetros terá a viagem? '))
cobrança1 = viagem*0.50
cobrança2 = viagem*0.45
if viagem <= 200:
    print(f'A passagem tem \033[1;34m{viagem}\033[mKm, logo, custará: R$ \033[1;4;31m{cobrança1:.2f}\033[m')
else:
    print(f'A passagem tem \033[1;34m{viagem}\033[mKm, logo, custará: R$ \033[1;4;31m{cobrança2:.2f}\033[m')
