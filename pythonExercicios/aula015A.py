#PRÁTICA:
num = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
print(f'A soma é {soma}')

"""
TEORIA:
while não maçã:
    if bloco:
        anda()
    if abismo:
        pule()
    if moeda:
        pegue()
pegue()

Podemos fazer:
while True:
    if bloco:
        anda()
    if abismo:
        pule()
    if moeda:
        pega()
    if troféu:
        pule()
        break()
pega()
O break interrompe o While True
"""