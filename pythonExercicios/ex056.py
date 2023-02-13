somaIdade = 0
maiorIdadedeHomem = 0
nomeMaisVelho = ''
totalMulherMenos20 = 0
for p in range(0, 4):
    print(f'-=-=- {p+1}ª PESSOA =-=-=')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    somaIdade += 1
    if p == 1 and sexo in 'M':
        maiorIdadedeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'M' and idade > maiorIdadedeHomem:
        maiorIdadedeHomem = idade
        nomeMaisVelho = nome
    if sexo in 'F' and idade < 20:
        totalMulherMenos20 += 1
print(f'O homem mais velho tem {maiorIdadedeHomem} anos e se chama {nomeMaisVelho}.')
print(f'Ao todo são {totalMulherMenos20} mulheres com menos de 20 anos.')
