total18 = totalHomens = totalMulheres20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalHomens += 1
    if sexo == 'F' and idade < 20:
        totalMulheres20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resposta == 'N':
        break
print(
    f'Total de pessoas com mais de 18 anos: {total18}\nAo todo temos {totalHomens} homens cadastrados.\nE temos {totalMulheres20} mulheres com menos de 20 anos.'
)
