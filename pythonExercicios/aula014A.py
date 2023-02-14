#PRÁTICA:
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares!')

"""
TEORIA:
Imagine no exemplo dos passos que você não saiba o quanto que você andará:
Era:
for c in range(1, 10):
    passo()
pega()
Ficará:
while not maçã:
    passo()
pega()

Exemplos:
1)
while not maçã:
    if chão:
        passo()
    if buraco:
        pule()
    if moeda:
        pega()
pega()
"""