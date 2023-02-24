from os import system

total = totalMil = menor = contador = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))
    contador += 1
    total += preco
    if preco > 1000:
        totalMil += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resposta == 'S':
        system('cls')
    if resposta == 'N':
        break
print('{:~^40}'.format(' FIM DO PROGRAMA '))
print(
    f'O total de compra foi R$ {total:.2f}\nTemos {totalMil} produtos custando mais de R$ 1000.00.\nO produto mais barato foi {barato} que custa R$ {menor:.2f}'
)
