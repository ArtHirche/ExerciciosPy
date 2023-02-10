from time import sleep
from datetime import date
soma = 0
maioridade = 0
menoridade = 0
atual = date.today()year
for c in range(0,7):
    ano = int(input('Digite o ano de nascimento: '))
    idade = atual - ano
    soma += idade
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
    sleep(0,5)
    print(f'A soma das idades é igual a {soma}')
