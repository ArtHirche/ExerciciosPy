listaNum = []
maior = 0
menor = 0
for c in range(0, 5):
    listaNum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = listaNum[c]
    else:
        if listaNum[c] > maior:
            maior = listaNum[c]
        if listaNum[c] < menor:
            menor = listaNum[c]
print(f'Você digitou os valores {listaNum}')
print(f'O maior valor foi {maior} na(s) posição(ões): ', end='')
for i, v in enumerate(listaNum):
    if v == maior:
        print(f'{i}... ', end=' ')
print(f'O menor valor foi {menor} na(s) posição(ões): ', end='')
for i, v in enumerate(listaNum):
    if v == menor:
        print(f'{i}... ', end='')