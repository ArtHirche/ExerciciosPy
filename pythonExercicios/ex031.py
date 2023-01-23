viagem = float(input('Quantos quilômetros terá a viagem? '))
cobrança1 = viagem*0.50
cobrança2 = viagem*0.45
if viagem <= 200:
    print(f'A passagem tem {viagem}Km, logo, custará: R$ {cobrança1:.2f}')
else:
    print(f'A passagem tem {viagem}Km, logo, custará: R$ {cobrança2}')
