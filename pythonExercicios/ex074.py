from random import choices

tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
sorteio = choices(tupla, k=5)
print(f'Os valores sorteados foram: {sorteio}')
print(f'O maior valor é {max(sorteio)}')
print(f'O menor valor é {min(sorteio)}')