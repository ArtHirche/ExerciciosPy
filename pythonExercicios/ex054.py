from datetime import date

atual = date.today().year
totalMaior = 0
totalMenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        totalMaior += 1
    else:
        totalMenor += 1
print(
    f'Ao todo tivemos {totalMaior} pessoas maiores de idade.\nE tivemos {totalMenor} pessoas menores de idade.'
)